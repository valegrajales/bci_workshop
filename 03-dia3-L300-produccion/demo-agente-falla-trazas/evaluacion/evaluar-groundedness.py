"""Evalua groundedness de normativa-falla vs normativa-corregido con el mismo dataset.

Requisitos: pip install azure-ai-projects azure-identity ; az login
No modifica los agentes: solo los usa como target de la evaluacion.
"""
import json
import os
import sys
import time

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

ENDPOINT = "https://bci-demo.services.ai.azure.com/api/projects/bci-workshop"
JUDGE = "gpt-6.1-sol"
AGENTS = ["normativa-falla", "normativa-corregido"]
DATASET_NAME = "normativa-groundedness-eval"
DATASET_VERSION = os.environ.get("DATASET_VERSION", "1")
HERE = os.path.dirname(os.path.abspath(__file__))

client = AIProjectClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
openai = client.get_openai_client()

ds = client.datasets.upload_file(
    name=DATASET_NAME,
    version=DATASET_VERSION,
    file_path=os.path.join(HERE, "dataset-groundedness.jsonl"),
)
print("Dataset:", ds.id)

evaluation = openai.evals.create(
    name="normativa-groundedness",
    data_source_config={
        "type": "custom",
        "item_schema": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "tema": {"type": "string"},
                "control": {"type": "boolean"},
                "query": {"type": "string"},
                "ground_truth": {"type": "string"},
            },
            "required": ["query"],
        },
        "include_sample_schema": True,
    },
    testing_criteria=[
        {
            "type": "azure_ai_evaluator",
            "name": "groundedness",
            "evaluator_name": "builtin.groundedness",
            "initialization_parameters": {"deployment_name": JUDGE},
            "data_mapping": {
                "query": "{{item.query}}",
                "response": "{{sample.output_items}}",
            },
        }
    ],
)
print("Eval:", evaluation.id)

runs = {}
for agent in AGENTS:
    run = openai.evals.runs.create(
        eval_id=evaluation.id,
        name=f"groundedness-{agent}",
        data_source={
            "type": "azure_ai_target_completions",
            "source": {"type": "file_id", "id": ds.id},
            "input_messages": {
                "type": "template",
                "template": [
                    {
                        "type": "message",
                        "role": "user",
                        "content": {"type": "input_text", "text": "{{item.query}}"},
                    }
                ],
            },
            "target": {"type": "azure_ai_agent", "name": agent},
        },
    )
    runs[agent] = run.id
    print("Run", agent, run.id)

results = {}
for agent, run_id in runs.items():
    while True:
        r = openai.evals.runs.retrieve(run_id=run_id, eval_id=evaluation.id)
        if r.status in ("completed", "failed", "canceled"):
            break
        time.sleep(15)
    print(agent, r.status, getattr(r, "report_url", ""))
    items = list(openai.evals.runs.output_items.list(run_id=run_id, eval_id=evaluation.id))
    results[agent] = {"run": r.model_dump(), "items": [i.model_dump() for i in items]}

out = os.path.join(HERE, "resultados-raw.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump({"eval_id": evaluation.id, "runs": runs, "results": results}, f, ensure_ascii=False, indent=2, default=str)
print("Guardado", out)

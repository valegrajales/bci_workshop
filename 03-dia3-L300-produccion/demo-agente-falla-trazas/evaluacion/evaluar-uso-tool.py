"""Evalua el uso de la tool (builtin.tool_call_accuracy y builtin.tool_selection) en ambos agentes.

Crea una evaluacion NUEVA; no toca la de groundedness ni los agentes.
Reutiliza el dataset ya subido (normativa-groundedness-eval v2).
"""
import json
import os
import time

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

ENDPOINT = "https://bci-demo.services.ai.azure.com/api/projects/bci-workshop"
JUDGE = "gpt-6.1-sol"
AGENTS = ["normativa-falla", "normativa-corregido"]
HERE = os.path.dirname(os.path.abspath(__file__))

client = AIProjectClient(endpoint=ENDPOINT, credential=DefaultAzureCredential())
openai = client.get_openai_client()
ds = client.datasets.get(name="normativa-groundedness-eval", version="2")
print("Dataset:", ds.id)

mapping = {
    "query": "{{item.query}}",
    "response": "{{sample.output_items}}",
    "tool_definitions": "{{sample.tool_definitions}}",
}
criteria = [
    {
        "type": "azure_ai_evaluator",
        "name": name,
        "evaluator_name": ev,
        "initialization_parameters": {"deployment_name": JUDGE},
        "data_mapping": mapping,
    }
    for name, ev in [
        ("tool_call_accuracy", "builtin.tool_call_accuracy"),
        ("tool_selection", "builtin.tool_selection"),
    ]
]

evaluation = openai.evals.create(
    name="normativa-uso-de-tool",
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
    testing_criteria=criteria,
)
print("Eval:", evaluation.id)

runs = {}
for agent in AGENTS:
    run = openai.evals.runs.create(
        eval_id=evaluation.id,
        name=f"uso-tool-{agent}",
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

results = {}
for agent, run_id in runs.items():
    while True:
        r = openai.evals.runs.retrieve(run_id=run_id, eval_id=evaluation.id)
        if r.status in ("completed", "failed", "canceled"):
            break
        time.sleep(15)
    print(agent, r.status, r.result_counts, getattr(r, "report_url", ""))
    items = list(openai.evals.runs.output_items.list(run_id=run_id, eval_id=evaluation.id))
    results[agent] = {"run": r.model_dump(), "items": [i.model_dump() for i in items]}

out = os.environ.get("RAW_OUT", os.path.join(HERE, "resultados-uso-tool-raw.json"))
with open(out, "w", encoding="utf-8") as f:
    json.dump({"eval_id": evaluation.id, "runs": runs, "results": results}, f, ensure_ascii=False, indent=2, default=str)
print("Guardado", out)

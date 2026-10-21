r"""EXTENSIÓN (opcional, para quien termine antes): evaluación por lotes del agente.

Ejecuta:  python solutions\extensiones\ext_evaluar.py            (usa data\preguntas_evaluacion.jsonl)
Respeta LAB_NIVEL_USUARIO: con `interno`, las preguntas P05 y P06 (restringidas) deben ser rechazadas.
Genera salidas\evaluacion.jsonl. Reglas en src\evaluacion.py (ver ai-rag-chat-evaluator para evaluación con LLM).
"""
import asyncio
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(RAIZ / "src"))

from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential

import busqueda
import registro_herramientas as reg
from agente_lab import crear_agente
from config import cargar_settings, exigir
from evaluacion import cargar_preguntas, evaluar_respuesta, resumir
from normativa import cargar_corpus


async def main() -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    corpus, preguntas, filas = cargar_corpus(), cargar_preguntas(), []
    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        agent = crear_agente(client)
        try:
            for p in preguntas:
                reg.limpiar()
                respuesta = (await agent.run(p["question"])).text
                m = evaluar_respuesta(p, respuesta, reg.usadas(), s.nivel_usuario, corpus)
                print(f"{p['id']} {'✔' if m['aprobada'] else '✘'} {m}")
                filas.append({"id": p["id"], "respuesta": respuesta, "tools": reg.usadas(), **m})
        finally:
            await busqueda.cerrar()
    salida = RAIZ / "salidas" / "evaluacion.jsonl"
    salida.parent.mkdir(exist_ok=True)
    salida.write_text("\n".join(json.dumps(f, ensure_ascii=False) for f in filas), encoding="utf-8")
    print(f"\nNivel de usuario: {s.nivel_usuario} · Resumen (% aprobado): {resumir(filas)}")
    print(f"Detalle en {salida}")


if __name__ == "__main__":
    asyncio.run(main())

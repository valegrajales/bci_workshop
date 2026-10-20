r"""SOLUCIÓN Tarea 4 — Trazas con OpenTelemetry y checklist de éxito.

Ejecuta:  python solutions\05_trazas.py
Cada pregunta genera una traza: invoke_agent > chat + execute_tool.
Búscala en el portal de Foundry (Observability > Traces) o en Application Insights (Investigar >
Búsqueda de transacciones) con el Trace ID impreso; puede demorar 2-5 minutos en aparecer. Con ENABLE_CONSOLE_EXPORTERS=true se imprime en la consola.
Fuentes: agent-framework/python/samples/02-agents/observability/foundry_tracing.py
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential

import busqueda
import registro_herramientas as reg
from agente_lab import CASOS, crear_agente, reportar
from config import cargar_settings, exigir
from normativa import cargar_corpus
from trazas import configurar_trazas, traza_con_nombre, vaciar_trazas


async def main() -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    corpus = cargar_corpus()
    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        destino = await configurar_trazas(client)  # 4.1: activar OpenTelemetry (antes de ejecutar el agente)
        print(f"Trazas activadas -> {destino}")
        agent = crear_agente(client)
        aprobados = 0
        try:
            for caso in CASOS:
                reg.limpiar()
                with traza_con_nombre(f"lab-{caso['id']}") as trace_id:  # 4.2: un span por pregunta
                    respuesta = await agent.run(caso["pregunta"])
                aprobados += reportar(caso, trace_id, respuesta.text, corpus)
        finally:
            await busqueda.cerrar()
            vaciar_trazas()
    print(f"\nCasos aprobados: {aprobados}/{len(CASOS)}")
    print("Siguiente paso: abre el portal de Foundry (Observability > Traces) o Application Insights y busca los Trace ID (espera 2-5 min).")


if __name__ == "__main__":
    asyncio.run(main())

r"""Tarea 4 — Activa las trazas y ejecuta los 3 casos de referencia con su checklist de éxito.

Completa los TODO 4.1 y 4.2 y ejecuta:  python src\05_trazas.py
Luego busca los Trace ID impresos en el portal de Foundry (Observability > Traces) o en Application
Insights (Investigar > Búsqueda de transacciones); tarda 2-5 min. Si no tienes Application Insights: ENABLE_CONSOLE_EXPORTERS=true en tu .env.
Después diagnostica el caso fallido de los instructores:  python src\05_caso_fallido.py
Pista: solutions\05_trazas.py (solo si te atascas).
"""
import asyncio

from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential

import busqueda
import registro_herramientas as reg
from agente_lab import CASOS, crear_agente, reportar
from config import cargar_settings, completar_todos, exigir
from normativa import cargar_corpus
from trazas import configurar_trazas, traza_con_nombre, vaciar_trazas  # noqa: F401 - los usarás en 4.1 y 4.2


async def main() -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    corpus = cargar_corpus()
    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        # TODO 4.1: activa las trazas ANTES de ejecutar el agente -> destino = await configurar_trazas(client)
        destino = None
        completar_todos(destino=destino)
        print(f"Trazas activadas -> {destino}")
        agent = crear_agente(client)
        aprobados = 0
        try:
            for caso in CASOS:
                reg.limpiar()
                # TODO 4.2: ejecuta el caso dentro de un span con nombre para obtener su Trace ID:
                #   with traza_con_nombre(f"lab-{caso['id']}") as trace_id:
                #       respuesta = await agent.run(caso["pregunta"])
                trace_id = None
                respuesta = None
                completar_todos(trace_id=trace_id, respuesta=respuesta)
                aprobados += reportar(caso, trace_id, respuesta.text, corpus)
        finally:
            await busqueda.cerrar()
            vaciar_trazas()
    print(f"\nCasos aprobados: {aprobados}/{len(CASOS)}")
    print("Siguiente paso: abre el portal de Foundry (Observability > Traces) o Application Insights y busca los Trace ID (espera 2-5 min).")


if __name__ == "__main__":
    asyncio.run(main())

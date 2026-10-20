r"""SOLUCIÓN Tarea 4 — El mismo caso fallido, ya corregido.

Ejecuta:  python instructores\05_caso_fallido_corregido.py --caso 1      (o --caso 2)
Usa las herramientas correctas de src\agente_lab.py (filtro por nivel del usuario y descripción de la
herramienta de estado con el formato completo SOL-AAAA-NNNN). Compara su traza con la del caso fallido.
"""
import argparse
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

CASO_POR_NUMERO = {1: CASOS[0], 2: CASOS[1]}


async def main(numero_caso: int) -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    caso = CASO_POR_NUMERO[numero_caso]
    corpus = cargar_corpus()
    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        destino = await configurar_trazas(client)
        print(f"Trazas activadas -> {destino}")
        agent = crear_agente(client)
        try:
            reg.limpiar()
            with traza_con_nombre(f"caso-corregido-{numero_caso}") as trace_id:
                respuesta = await agent.run(caso["pregunta"])
            reportar(caso, trace_id, respuesta.text, corpus)
        finally:
            await busqueda.cerrar()
            vaciar_trazas()


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Caso fallido con las herramientas corregidas.")
    ap.add_argument("--caso", type=int, choices=sorted(CASO_POR_NUMERO), default=1)
    asyncio.run(main(ap.parse_args().caso))

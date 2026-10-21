r"""SOLUCIÓN Tarea 3 — Herramienta personalizada `consultar_estado_solicitud`.

Ejecuta:  python solutions\04_herramienta_estado.py   (o con --solo-tool para probar solo la herramienta)
Una buena herramienta = nombre claro + descripción de CUÁNDO usarla (y cuándo no) + parámetros con
formato explícito + resultado estructurado que también explique los errores.
Fuentes: agent-framework/python/samples/01-get-started/02_add_tools.py, 02-agents/tools.
"""
import asyncio
import json
import sys
from pathlib import Path
from typing import Annotated

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from agent_framework import Agent, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential
from pydantic import Field

import busqueda
import registro_herramientas as reg
from agente_lab import INSTRUCCIONES, buscar_normativa  # buscar_normativa: versión de referencia de la Tarea 2
from config import cargar_settings, exigir
from solicitudes import consultar_estado

PREGUNTAS = [
    "¿En qué estado está la solicitud SOL-2026-0003?",  # debe usar consultar_estado_solicitud
    "¿Cuál es el plazo de revisión de una solicitud interna?",  # NO debe usarla: es una norma
    "¿En qué estado está la solicitud SOL-2026-0006 y cuánto suele demorar ese estado?",  # usa las dos
    "Consulta el estado de la solicitud 12345.",  # identificador inválido
]


@tool(approval_mode="never_require")
async def consultar_estado_solicitud(
    id_solicitud: Annotated[
        str, Field(description="Identificador completo con formato SOL-AAAA-NNNN, p. ej. SOL-2026-0003.")
    ],
) -> str:
    """Consulta el estado actual de UNA solicitud interna de Austral Bank (estado, fecha y responsable).
    Úsala solo si el usuario menciona un identificador de solicitud; no sirve para preguntas sobre normas."""
    resultado = consultar_estado(id_solicitud)  # lógica pura y probada con pytest (src\solicitudes.py)
    reg.registrar("consultar_estado_solicitud", {"id_solicitud": id_solicitud}, ok=resultado["encontrada"])
    return json.dumps(resultado, ensure_ascii=False)  # texto legible también en la traza


async def main(solo_tool: bool) -> None:
    if solo_tool:  # Checkpoint: probar la tool sin modelo de lenguaje (no necesita Azure)
        for id_ in ("SOL-2026-0003", "12345"):
            print(id_, "->", (await consultar_estado_solicitud.invoke(id_solicitud=id_))[0].text)
        return
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        agent = Agent(
            client=client,
            name="asistente-normativa",
            instructions=INSTRUCCIONES,
            tools=[buscar_normativa, consultar_estado_solicitud],
        )
        try:
            for pregunta in PREGUNTAS:
                reg.limpiar()
                print(f"\n> {pregunta}")
                respuesta = await agent.run(pregunta)
                print(respuesta.text)
                print(f"   · tools usadas: {reg.usadas() or 'ninguna'}")
        finally:
            await busqueda.cerrar()


if __name__ == "__main__":
    asyncio.run(main("--solo-tool" in sys.argv))

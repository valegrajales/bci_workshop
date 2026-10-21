r"""Tarea 3 — Implementa y prueba una herramienta personalizada: `consultar_estado_solicitud`.

Objetivo: el agente consulta el estado de una solicitud ficticia (data\solicitudes.json) cuando el
usuario da un identificador SOL-AAAA-NNNN, y NO la usa para preguntas sobre normas.
Completa los TODO 3.1 y 3.2. Prueba primero la herramienta sola:  python src\04_herramienta_estado.py --solo-tool
Luego con el agente:  python src\04_herramienta_estado.py
Pista: solutions\04_herramienta_estado.py (solo si te atascas).
"""
import asyncio
import json
import sys
from typing import Annotated

from agent_framework import Agent, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential
from pydantic import Field

import busqueda
import registro_herramientas as reg
from agente_lab import INSTRUCCIONES, buscar_normativa  # buscar_normativa: versión de referencia de la Tarea 2
from config import cargar_settings, completar_todos, exigir
from solicitudes import consultar_estado  # noqa: F401 - la usarás en el TODO 3.1c

PREGUNTAS = [
    "¿En qué estado está la solicitud SOL-2026-0003?",  # debe usar consultar_estado_solicitud
    "¿Cuál es el plazo de revisión de una solicitud interna?",  # NO debe usarla: es una norma
    "¿En qué estado está la solicitud SOL-2026-0006 y cuánto suele demorar ese estado?",  # usa las dos
    "Consulta el estado de la solicitud 12345.",  # identificador inválido
]


# TODO 3.1: completa la herramienta. El modelo SOLO ve el nombre, la descripción y los parámetros:
# de ellos depende que la use bien.
@tool(approval_mode="never_require")
async def consultar_estado_solicitud(
    # 3.1a: describe el parámetro y su formato exacto, con un ejemplo (Field(description="..."))
    id_solicitud: Annotated[str, Field(description="TODO 3.1a")],
) -> str:
    """TODO 3.1b: qué hace (estado, fecha y responsable de UNA solicitud), cuándo usarla y cuándo NO."""
    # 3.1c: resultado = consultar_estado(id_solicitud); registra con
    #       reg.registrar("consultar_estado_solicitud", {"id_solicitud": id_solicitud}, ok=resultado["encontrada"])
    #       y devuelve json.dumps(resultado, ensure_ascii=False). Luego borra la línea siguiente:
    raise NotImplementedError("Completa consultar_estado_solicitud (TODO 3.1c)")


async def main(solo_tool: bool) -> None:
    pendiente = "TODO" in (consultar_estado_solicitud.description or "") or "TODO" in str(
        consultar_estado_solicitud.parameters()
    )
    completar_todos(descripcion_de_la_tool=None if pendiente else "ok")
    if solo_tool:  # Checkpoint: probar la tool sin modelo de lenguaje (no necesita Azure)
        for id_ in ("SOL-2026-0003", "12345"):
            print(id_, "->", (await consultar_estado_solicitud.invoke(id_solicitud=id_))[0].text)
        return
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        # TODO 3.2: entrega ambas herramientas al agente: [buscar_normativa, consultar_estado_solicitud]
        TOOLS = None
        completar_todos(TOOLS=TOOLS)
        agent = Agent(client=client, name="asistente-normativa", instructions=INSTRUCCIONES, tools=TOOLS)
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

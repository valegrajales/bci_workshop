"""[DEMO] Cliente de Agent Framework que usa el servidor MCP LOCAL.

Requiere que `mcp_server_local.py` esté corriendo en otra terminal (puerto 8900).
Muestra lo mismo que la Tarea 3 (consultar_estado_solicitud), pero la tool ahora
vive en un servidor MCP separado en vez de ser una function tool en el mismo proceso.

Uso:
    # Terminal 1
    python mcp_server_local.py

    # Terminal 2
    python mcp_demo_cliente_local.py
"""
from __future__ import annotations

import asyncio
import sys

sys.path.insert(0, "src")  # reutiliza config.py del lab
from config import cargar_settings, exigir  # noqa: E402

from agent_framework import Agent, MCPStreamableHTTPTool  # noqa: E402
from agent_framework.foundry import FoundryChatClient  # noqa: E402
from azure.identity.aio import DefaultAzureCredential  # noqa: E402

INSTRUCCIONES = (
    "Eres el asistente interno de Austral Bank (banco ficticio). "
    "Para consultar el estado de una solicitud, usa SIEMPRE la herramienta MCP "
    "consultar_estado_solicitud con el formato SOL-AAAA-NNNN. "
    "Responde en español, breve."
)

PREGUNTAS = [
    "¿Cuál es el estado de la solicitud SOL-2026-0003?",
    "¿Y la SOL-2026-0007?",
]


async def main() -> None:
    settings = exigir(cargar_settings(), "project_endpoint", "model")

    # El servidor MCP local no tiene autenticación (solo para prototipar, ver slide
    # "Servidor MCP local vs. remoto"): cualquier cliente que llegue al puerto lo usa.
    mcp_tool = MCPStreamableHTTPTool(
        name="normativa-austral-local",
        description="Servidor MCP local de solicitudes internas (demo, sin autenticación)",
        url="http://127.0.0.1:8901/mcp",
    )

    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(
            project_endpoint=settings.project_endpoint,
            model=settings.model,
            credential=credential,
        )
        async with Agent(
            client=client,
            name="asistente-austral-mcp-local",
            instructions=INSTRUCCIONES,
            tools=[mcp_tool],
        ) as agent:
            for pregunta in PREGUNTAS:
                print(f"\n> {pregunta}")
                resultado = await agent.run(pregunta)
                print(resultado.text)


if __name__ == "__main__":
    asyncio.run(main())

r"""SOLUCIÓN Tarea 1 — Agente base (sin herramientas) con Microsoft Agent Framework.

Ejecuta:  python solutions\02_agente_base.py
Patrón: agent-framework/python/samples/01-get-started (FoundryChatClient + Agent + sesión).
"""
import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential

from config import cargar_settings, exigir

INSTRUCCIONES = (
    "Eres el asistente de normativa interna de Austral Bank (banco ficticio). "
    "Responde en español, de forma breve y clara. Si no conoces un dato, dilo."
)

PREGUNTAS = [
    "¿Qué es el KYC en un banco?",
    "¿Cuál es el límite mensual de gasto con tarjeta corporativa para el nivel Jefatura de Austral Bank?",
    "¿Y para el nivel Gerencia?",  # la sesión recuerda la pregunta anterior
]


async def main() -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model")
    async with DefaultAzureCredential() as credential:  # Microsoft Entra ID, tu `az login`
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        agent = Agent(client=client, name="asistente-normativa", instructions=INSTRUCCIONES)
        session = agent.create_session()  # conserva el historial entre preguntas
        for pregunta in PREGUNTAS:
            print(f"\n> {pregunta}")
            respuesta = await agent.run(pregunta, session=session)
            print(respuesta.text)


if __name__ == "__main__":
    asyncio.run(main())

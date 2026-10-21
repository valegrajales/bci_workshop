r"""Tarea 1 — Agente base (sin herramientas) con Microsoft Agent Framework.

Objetivo: un agente en Python que responda con un modelo de tu proyecto de Foundry.
Completa los TODO 1.1 a 1.3 y ejecuta:  python src\02_agente_base.py
Pista: la solución está en solutions\02_agente_base.py (úsala solo si te atascas).
"""
import asyncio

from agent_framework import Agent
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential

from config import cargar_settings, completar_todos, exigir

# TODO 1.2: escribe las instrucciones (system prompt) del agente: rol (asistente de normativa
# interna de Austral Bank, banco ficticio), idioma (español), tono breve y "si no sabes, dilo".
INSTRUCCIONES = None

PREGUNTAS = [
    "¿Qué es el KYC en un banco?",
    "¿Cuál es el límite mensual de gasto con tarjeta corporativa para el nivel Jefatura de Austral Bank?",
    "¿Y para el nivel Gerencia?",  # la sesión recuerda la pregunta anterior
]


async def main() -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model")
    async with DefaultAzureCredential() as credential:  # Microsoft Entra ID, tu `az login`
        # TODO 1.1: crea el cliente -> FoundryChatClient(project_endpoint=..., model=..., credential=...)
        client = None

        # TODO 1.3: crea el agente -> Agent(client=..., name="asistente-normativa", instructions=...)
        agent = None

        completar_todos(INSTRUCCIONES=INSTRUCCIONES, client=client, agent=agent)
        session = agent.create_session()  # conserva el historial entre preguntas
        for pregunta in PREGUNTAS:
            print(f"\n> {pregunta}")
            respuesta = await agent.run(pregunta, session=session)
            print(respuesta.text)


if __name__ == "__main__":
    asyncio.run(main())

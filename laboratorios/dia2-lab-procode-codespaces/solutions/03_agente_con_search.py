r"""SOLUCIÓN Tarea 2 — Grounding empresarial con Azure AI Search (herramienta `buscar_normativa`).

Ejecuta:  python solutions\03_agente_con_search.py   (o con --solo-tool para probar solo la herramienta)
Patrón: búsqueda híbrida (BM25 + vectores) + ranker semántico, con filtro por nivel_acceso.
La recuperación se expone como una herramienta, por eso aparecerá como `execute_tool` en la traza.
Fuentes: azure-search-python-samples/Quickstart-Vector-Search; agent-framework/.../02-agents/tools.
"""
import asyncio
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
from config import cargar_settings, exigir
from normativa import construir_filtro_acceso, formatear_resultados

INSTRUCCIONES = """Eres el asistente de normativa interna de Austral Bank (banco ficticio).
Reglas:
1. Para cualquier pregunta sobre normas, políticas, límites o plazos usa SIEMPRE la herramienta
   buscar_normativa antes de responder. Si la pregunta tiene varias partes, haz una búsqueda por cada parte.
2. Responde en español, de forma breve, y cita cada dato con el id del fragmento entre corchetes,
   por ejemplo [NOR-001-02]. Cita solo ids que aparezcan en los resultados.
3. Si no hay información suficiente responde: "No tengo información en la normativa disponible para tu
   nivel de acceso". No inventes cifras ni plazos.
"""

PREGUNTAS = [
    "¿Cuál es el límite mensual de gasto con tarjeta corporativa para el nivel Jefatura?",
    "¿Cuál es el límite de gasto por noche en un viaje nacional y por cuántos años debo conservar los comprobantes de la rendición?",
    "¿Quién aprueba un crédito a una empresa por 3.000.000 USD?",  # documento restringido
    "¿Cuántos días de vacaciones legales tengo al año?",  # fuera del corpus
]


@tool(approval_mode="never_require")
async def buscar_normativa(
    consulta: Annotated[
        str,
        Field(description="Consulta autocontenida en español, p. ej. 'límite mensual tarjeta corporativa Jefatura'."),
    ],
) -> str:
    """Busca en la normativa interna de Austral Bank (gastos, viajes, KYC, retención de documentos,
    IA generativa, incidentes, crédito, continuidad, conducta) y devuelve fragmentos con su id citable."""
    # El nivel de acceso sale de tu sesión (LAB_NIVEL_USUARIO), nunca de un parámetro que decida el modelo.
    filtro = construir_filtro_acceso(cargar_settings().nivel_usuario)
    fragmentos = await busqueda.buscar(consulta, filtro)
    reg.registrar("buscar_normativa", {"consulta": consulta})
    return formatear_resultados(fragmentos)


async def main(solo_tool: bool) -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    print(f"Nivel de acceso simulado del usuario: {s.nivel_usuario}")
    async with DefaultAzureCredential() as credential:
        try:
            if solo_tool:  # Checkpoint: la tool funciona sin modelo de lenguaje
                resultado = await buscar_normativa.invoke(consulta="límite mensual tarjeta corporativa Jefatura")
                print(resultado[0].text)
                return

            client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
            agent = Agent(client=client, name="asistente-normativa", instructions=INSTRUCCIONES, tools=[buscar_normativa])
            for pregunta in PREGUNTAS:
                reg.limpiar()
                print(f"\n> {pregunta}")
                respuesta = await agent.run(pregunta)
                print(respuesta.text)
                for llamada in reg.LLAMADAS:
                    print(f"   · búsqueda realizada: {llamada.argumentos['consulta']}")
        finally:
            await busqueda.cerrar()


if __name__ == "__main__":
    asyncio.run(main("--solo-tool" in sys.argv))

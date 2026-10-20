r"""Tarea 2 — Grounding con Azure AI Search: la herramienta `buscar_normativa`.

Objetivo: que el agente responda SOLO con la normativa del índice y cite la fuente.
Completa los TODO 2.1 a 2.4 y ejecuta:  python src\03_agente_con_search.py
Antes de probar con el agente, puedes probar la tool sola:  python src\03_agente_con_search.py --solo-tool
Pista: solutions\03_agente_con_search.py (solo si te atascas).
"""
import asyncio
import sys
from typing import Annotated

from agent_framework import Agent, tool
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential
from pydantic import Field

import busqueda
import registro_herramientas as reg
from config import cargar_settings, completar_todos, exigir
from normativa import construir_filtro_acceso, formatear_resultados  # noqa: F401 - los usarás en 2.1 y 2.2

# TODO 2.3: instrucciones con 3 reglas: (1) usar SIEMPRE buscar_normativa para normas, límites y plazos
# (una búsqueda por cada parte de la pregunta), (2) citar cada dato como [NOR-001-02] usando solo ids
# devueltos por la tool, (3) si no hay evidencia responder "No tengo información en la normativa
# disponible para tu nivel de acceso" sin inventar.
INSTRUCCIONES = None

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
    # TODO 2.1: arma el filtro de acceso con el nivel del usuario: construir_filtro_acceso(cargar_settings().nivel_usuario)
    #           (el nivel sale de tu sesión, NUNCA de un parámetro que decida el modelo)
    # TODO 2.2: llama a `await busqueda.buscar(consulta, filtro)`, registra la llamada con
    #           reg.registrar("buscar_normativa", {"consulta": consulta}) y devuelve formatear_resultados(fragmentos)
    # Cuando termines, borra la línea siguiente:
    raise NotImplementedError("Completa buscar_normativa (TODO 2.1 y 2.2)")


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
            # TODO 2.4: pasa la herramienta al agente: tools=[buscar_normativa]
            TOOLS = None
            completar_todos(INSTRUCCIONES=INSTRUCCIONES, TOOLS=TOOLS)
            agent = Agent(client=client, name="asistente-normativa", instructions=INSTRUCCIONES, tools=TOOLS)
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

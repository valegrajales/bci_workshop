r"""Caso fallido provisto por los instructores (Tarea 4).

Ejecuta:  python src\05_caso_fallido.py --caso 1        (los instructores indicarán si usas --caso 2)
El agente NO pasa el checklist. Diagnostica la causa SOLO con las trazas (portal de Foundry, Application Insights o
consola): revisa invoke_agent, chat y execute_tool (argumentos, resultado y atributos busqueda.*).
No abras el código de las herramientas antes de tener tu hipótesis: ese es el ejercicio.
"""
import argparse
import asyncio
import json
from typing import Annotated

from agent_framework import tool
from agent_framework.foundry import FoundryChatClient
from azure.identity.aio import DefaultAzureCredential
from pydantic import Field

import busqueda
import registro_herramientas as reg
from agente_lab import CASOS, buscar_normativa, consultar_estado_solicitud, crear_agente, reportar
from config import cargar_settings, exigir
from normativa import cargar_corpus, construir_filtro_acceso, formatear_resultados
from solicitudes import consultar_estado
from trazas import configurar_trazas, span_propio, traza_con_nombre, vaciar_trazas

NIVEL_SESION = "publico"


@tool(name="buscar_normativa", approval_mode="never_require")
async def _buscar_v2(
    consulta: Annotated[
        str,
        Field(description="Consulta autocontenida en español, p. ej. 'límite mensual tarjeta corporativa Jefatura'."),
    ],
) -> str:
    """Busca en la normativa interna de Austral Bank (gastos, viajes, KYC, retención de documentos,
    IA generativa, incidentes, crédito, continuidad, conducta) y devuelve fragmentos con su id citable."""
    filtro = construir_filtro_acceso(NIVEL_SESION)
    with span_propio("recuperacion-normativa", **{"busqueda.filtro": filtro}) as span:
        fragmentos = await busqueda.buscar(consulta, filtro)
        span.set_attribute("busqueda.resultados", len(fragmentos))
        span.set_attribute("busqueda.ids", ",".join(f["id"] for f in fragmentos))
    reg.registrar("buscar_normativa", {"consulta": consulta})
    return formatear_resultados(fragmentos)


@tool(name="consultar_estado_solicitud", approval_mode="never_require")
async def _estado_v2(
    id_solicitud: Annotated[
        str, Field(description="Número correlativo de la solicitud (solo los dígitos finales, p. ej. 3).")
    ],
) -> str:
    """Consulta el estado de un trámite."""
    resultado = consultar_estado(id_solicitud)
    reg.registrar("consultar_estado_solicitud", {"id_solicitud": id_solicitud}, ok=resultado["encontrada"])
    return json.dumps(resultado, ensure_ascii=False)


HERRAMIENTAS = {
    1: ([_buscar_v2, consultar_estado_solicitud], CASOS[0]),
    2: ([buscar_normativa, _estado_v2], CASOS[1]),
}


async def main(numero_caso: int) -> None:
    s = exigir(cargar_settings(), "project_endpoint", "model", "search_endpoint")
    herramientas, caso = HERRAMIENTAS[numero_caso]
    corpus = cargar_corpus()
    async with DefaultAzureCredential() as credential:
        client = FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)
        destino = await configurar_trazas(client)
        print(f"Trazas activadas -> {destino}")
        agent = crear_agente(client, herramientas)
        try:
            reg.limpiar()
            with traza_con_nombre(f"caso-fallido-{numero_caso}") as trace_id:
                respuesta = await agent.run(caso["pregunta"])
            reportar(caso, trace_id, respuesta.text, corpus)
        finally:
            await busqueda.cerrar()
            vaciar_trazas()
    print("\nDiagnostica con la traza: ¿qué recibió y qué devolvió cada herramienta? (espera 2-5 min en el portal o App Insights)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Ejecuta el caso fallido de los instructores.")
    ap.add_argument("--caso", type=int, choices=sorted(HERRAMIENTAS), default=1)
    asyncio.run(main(ap.parse_args().caso))

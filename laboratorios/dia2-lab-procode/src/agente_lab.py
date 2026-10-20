"""Agente de referencia del laboratorio (Tarea 4): instrucciones + 2 herramientas + casos de prueba.

Es la versión final de lo que construyes en las Tareas 1-3. Se usa en 05_trazas.py y
en 05_caso_fallido.py para que la Tarea 4 no dependa de haber terminado las anteriores.
"""
from __future__ import annotations

import json
from typing import Annotated

from agent_framework import Agent, tool
from pydantic import Field

import busqueda
from config import cargar_settings
from normativa import construir_filtro_acceso, formatear_resultados
from registro_herramientas import registrar
from solicitudes import consultar_estado
from trazas import span_propio

NOMBRE_AGENTE = "asistente-normativa"

INSTRUCCIONES = """Eres el asistente de normativa interna de Austral Bank (banco ficticio).
Reglas:
1. Para preguntas sobre normas, políticas, límites o plazos usa SIEMPRE la herramienta buscar_normativa
   antes de responder. Si la pregunta tiene varias partes, haz una búsqueda por cada parte.
2. Para conocer el estado de una solicitud (identificador tipo SOL-2026-0003) usa consultar_estado_solicitud.
3. Responde en español, de forma breve, y cita la fuente de cada dato con el id del fragmento entre
   corchetes, por ejemplo [NOR-001-02]. Cita solo ids que aparezcan en los resultados de las herramientas.
4. Si las herramientas no entregan información suficiente, responde: "No tengo información en la
   normativa disponible para tu nivel de acceso" y sugiere contactar al área responsable. No inventes
   cifras, plazos ni estados.
"""

CASOS = [
    {
        "id": "C1",
        "pregunta": "¿Cuál es el límite mensual de gasto con tarjeta corporativa para el nivel Jefatura?",
        "tool": "buscar_normativa",
        "esperado": ("2.500",),
    },
    {
        "id": "C2",
        "pregunta": "¿En qué estado está la solicitud SOL-2026-0003 y quién la está revisando?",
        "tool": "consultar_estado_solicitud",
        "esperado": ("en revisión", "área legal"),
    },
    {
        "id": "C3",
        "pregunta": (
            "¿Cuál es el límite de gasto por noche en un viaje nacional y por cuántos años "
            "debo conservar los comprobantes de la rendición?"
        ),
        "tool": "buscar_normativa",
        "esperado": ("350", "6 años|seis años"),
    },
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
    filtro = construir_filtro_acceso(cargar_settings().nivel_usuario)  # el nivel sale del código, no del modelo
    with span_propio("recuperacion-normativa", **{"busqueda.filtro": filtro}) as span:
        fragmentos = await busqueda.buscar(consulta, filtro)
        span.set_attribute("busqueda.resultados", len(fragmentos))
        span.set_attribute("busqueda.ids", ",".join(f["id"] for f in fragmentos))
    registrar("buscar_normativa", {"consulta": consulta})
    return formatear_resultados(fragmentos)


@tool(approval_mode="never_require")
async def consultar_estado_solicitud(
    id_solicitud: Annotated[
        str, Field(description="Identificador completo con formato SOL-AAAA-NNNN, p. ej. SOL-2026-0003.")
    ],
) -> str:
    """Consulta el estado actual de UNA solicitud interna de Austral Bank (estado, fecha y responsable).
    Úsala solo si el usuario menciona un identificador de solicitud; no sirve para preguntas sobre normas."""
    resultado = consultar_estado(id_solicitud)
    registrar("consultar_estado_solicitud", {"id_solicitud": id_solicitud}, ok=resultado["encontrada"])
    return json.dumps(resultado, ensure_ascii=False)  # texto legible también en la traza


def crear_agente(client, tools=None) -> Agent:
    """Agente final. `tools` permite cambiar las herramientas (lo usa el caso fallido)."""
    return Agent(
        client=client,
        name=NOMBRE_AGENTE,
        instructions=INSTRUCCIONES,
        tools=tools if tools is not None else [buscar_normativa, consultar_estado_solicitud],
    )


def reportar(caso: dict, trace_id: str, respuesta: str, corpus: list[dict]) -> bool:
    """Imprime respuesta + checklist de éxito. Devuelve True si pasa los 4 criterios."""
    import checklist
    import registro_herramientas as reg

    resultado = checklist.evaluar(respuesta, reg.LLAMADAS, caso["tool"], corpus, caso.get("esperado", ()))
    print(f"\n=== {caso['id']} · {caso['pregunta']}")
    print(f"Respuesta: {respuesta}")
    print(f"Tools llamadas: {reg.usadas() or 'ninguna'}")
    print(f"Trace ID: {trace_id}")
    print(checklist.formatear(resultado))
    return resultado.aprobado

"""Evaluación por lotes (extensión opcional): preguntas con respuesta esperada y reglas deterministas.

Al estilo de ai-rag-chat-evaluator (repos/publico-samples/ai-rag-chat-evaluator): un archivo .jsonl con
`question` + `truth` y un resumen de métricas. Aquí las métricas son reglas locales, sin modelo evaluador:
  - negativa_correcta: si el usuario no debe obtener la respuesta (documento restringido o fuera del corpus),
    el agente debe decir que no tiene información.
  - cita_esperada: cita un fragmento de cada documento en `fuentes`.
  - tool_correcta: usó consultar_estado_solicitud si y solo si la pregunta lo requería.
Este módulo no usa Azure; lo ejecuta solutions/extensiones/ext_evaluar.py.
"""
from __future__ import annotations

import json
from pathlib import Path

from checklist import SIN_INFORMACION
from config import DATA_DIR
from normativa import citas_validas, extraer_citas, niveles_permitidos

TOOL_ESTADO = "consultar_estado_solicitud"


def cargar_preguntas(ruta: Path | None = None) -> list[dict]:
    ruta = ruta or DATA_DIR / "preguntas_evaluacion.jsonl"
    lineas = ruta.read_text(encoding="utf-8").splitlines()
    return [json.loads(linea) for linea in lineas if linea.strip()]


def debe_negarse(pregunta: dict, nivel_usuario: str) -> bool:
    """True si la respuesta correcta es "no tengo información" (sin acceso o fuera del corpus)."""
    sin_acceso = pregunta["nivel_minimo"] not in niveles_permitidos(nivel_usuario)
    return sin_acceso or (not pregunta["fuentes"] and not pregunta["usa_tool"])


def evaluar_respuesta(
    pregunta: dict, respuesta: str, herramientas: list[str], nivel_usuario: str, corpus: list[dict]
) -> dict:
    """Devuelve las métricas de una respuesta; `None` = no aplica."""
    texto = (respuesta or "").lower()
    negada = any(f in texto for f in SIN_INFORMACION)
    negarse = debe_negarse(pregunta, nivel_usuario)
    citas = citas_validas(extraer_citas(respuesta), corpus)
    cita = None
    if not negarse and pregunta["fuentes"]:
        cita = all(any(c.startswith(doc) for c in citas) for doc in pregunta["fuentes"])
    metricas = {
        "negativa_correcta": negada if negarse else (not negada),
        "cita_esperada": cita,
        "tool_correcta": (TOOL_ESTADO in herramientas) == pregunta["usa_tool"],
    }
    metricas["aprobada"] = all(v is not False for v in metricas.values())
    return metricas


def resumir(resultados: list[dict]) -> dict:
    """Porcentaje de aprobación por métrica (ignora los `None`)."""
    resumen = {}
    for nombre in ("negativa_correcta", "cita_esperada", "tool_correcta", "aprobada"):
        valores = [r[nombre] for r in resultados if r[nombre] is not None]
        resumen[nombre] = round(100 * sum(valores) / len(valores)) if valores else None
    return resumen

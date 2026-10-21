"""Lógica de la herramienta de solicitudes (datos ficticios en data/solicitudes.json).

`consultar_estado(id)` es una función pura: la herramienta del agente
(04_herramienta_estado.py) solo la envuelve con @tool. Así se prueba sin Azure.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from config import DATA_DIR

PATRON_ID = re.compile(r"^SOL-\d{4}-\d{4}$")


def cargar_solicitudes(ruta: Path | None = None) -> dict[str, dict]:
    """Lee solicitudes.json y devuelve {id: solicitud}."""
    ruta = ruta or DATA_DIR / "solicitudes.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    return {s["id"]: s for s in datos}


def normalizar_id(id_solicitud: str) -> str:
    """Tolera espacios y minúsculas: ' sol-2026-0003 ' -> 'SOL-2026-0003'."""
    return (id_solicitud or "").strip().upper()


def consultar_estado(id_solicitud: str, solicitudes: dict[str, dict] | None = None) -> dict:
    """Busca una solicitud. Siempre devuelve un dict serializable (nunca lanza al modelo)."""
    sol_id = normalizar_id(id_solicitud)
    if not PATRON_ID.match(sol_id):
        return {
            "encontrada": False,
            "error": "formato_invalido",
            "mensaje": f"'{id_solicitud}' no tiene el formato SOL-AAAA-NNNN (ej.: SOL-2026-0003).",
        }
    solicitudes = solicitudes if solicitudes is not None else cargar_solicitudes()
    solicitud = solicitudes.get(sol_id)
    if solicitud is None:
        return {
            "encontrada": False,
            "error": "no_encontrada",
            "mensaje": f"No existe la solicitud {sol_id}.",
        }
    return {"encontrada": True, **solicitud}

"""[DEMO] Servidor MCP local — expone `consultar_estado_solicitud` como tool MCP.

Reutiliza los mismos datos ficticios del laboratorio (data/solicitudes.json) para
mostrar la MISMA funcionalidad de la Tarea 3 (ahí era una function tool local),
pero ahora servida por un servidor MCP independiente, en streamable-http.

Para la demo del Día 2 (slide "Servidor MCP local vs. remoto"):
  - Corre en tu máquina (localhost), sin autenticación: solo para prototipar.
  - El mismo servidor podría servir a Foundry, Agent Framework o cualquier
    cliente MCP compatible (acá lo probamos con un cliente Agent Framework local).

Cómo correrlo:
    python mcp_server_local.py
Queda escuchando en http://127.0.0.1:8900/mcp
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from mcp.server.fastmcp import FastMCP

DATA_DIR = Path(__file__).parent / "data"
PATRON_ID = re.compile(r"^SOL-\d{4}-\d{4}$")

mcp = FastMCP("normativa-austral-mcp-local", host="127.0.0.1", port=8901)


def _cargar_solicitudes() -> dict[str, dict]:
    ruta = DATA_DIR / "solicitudes.json"
    datos = json.loads(ruta.read_text(encoding="utf-8"))
    return {s["id"]: s for s in datos}


@mcp.tool()
def consultar_estado_solicitud(id_solicitud: str) -> dict:
    """Consulta el estado actual de UNA solicitud interna de Austral Bank (banco ficticio).

    Usa el identificador completo con formato SOL-AAAA-NNNN, por ejemplo SOL-2026-0003.
    Devuelve estado, fecha y responsable, o un error si el formato es inválido o no existe.
    """
    sol_id = (id_solicitud or "").strip().upper()
    if not PATRON_ID.match(sol_id):
        return {
            "encontrada": False,
            "error": "formato_invalido",
            "mensaje": f"'{id_solicitud}' no tiene el formato SOL-AAAA-NNNN (ej.: SOL-2026-0003).",
        }
    solicitudes = _cargar_solicitudes()
    solicitud = solicitudes.get(sol_id)
    if solicitud is None:
        return {"encontrada": False, "error": "no_encontrada", "mensaje": f"No existe la solicitud {sol_id}."}
    return {"encontrada": True, **solicitud}


if __name__ == "__main__":
    print("Servidor MCP local escuchando en http://127.0.0.1:8901/mcp (Ctrl+C para detener)")
    mcp.run(transport="streamable-http")

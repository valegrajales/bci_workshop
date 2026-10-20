"""Registro de llamadas a herramientas (para el checklist automático de la Tarea 4).

Las herramientas llaman a `registrar(...)`; 05_trazas.py lee `LLAMADAS` y verifica
que el agente realmente usó la tool (además de verlo en la traza).
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field


@dataclass
class Llamada:
    herramienta: str
    argumentos: dict
    ok: bool
    ts: float = field(default_factory=time.time)


LLAMADAS: list[Llamada] = []


def registrar(herramienta: str, argumentos: dict, ok: bool = True) -> None:
    LLAMADAS.append(Llamada(herramienta, dict(argumentos), ok))


def limpiar() -> None:
    LLAMADAS.clear()


def usadas() -> list[str]:
    """Nombres de herramientas llamadas, en orden."""
    return [c.herramienta for c in LLAMADAS]

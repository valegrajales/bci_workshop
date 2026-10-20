"""Checklist de éxito de la Tarea 4 (lógica local, sin Azure).

Los 4 criterios son los de la diapositiva del laboratorio:
responde · cita fuente · usa la tool · sin errores en la traza.
"""
from __future__ import annotations

from dataclasses import dataclass

from normativa import citas_validas, extraer_citas
from registro_herramientas import Llamada

SIN_INFORMACION = ("no tengo información", "no encontré", "no cuento con", "no puedo confirmar")


@dataclass
class Resultado:
    responde: bool
    cita_fuente: bool | None  # None = no aplica (el caso no usa normativa)
    usa_tool: bool
    sin_errores: bool

    def items(self) -> list[tuple[str, bool | None]]:
        return [
            ("Responde con el dato correcto", self.responde),
            ("Cita una fuente válida [NOR-xxx-xx]", self.cita_fuente),
            ("Usa la tool esperada", self.usa_tool),
            ("Sin errores en las llamadas a tools", self.sin_errores),
        ]

    @property
    def aprobado(self) -> bool:
        return all(v is not False for _, v in self.items())


def contiene_esperados(texto: str, esperado: tuple[str, ...]) -> bool:
    """Cada elemento de `esperado` admite alternativas: "6 años|seis años"."""
    bajo = texto.lower()
    return all(any(alt.strip().lower() in bajo for alt in e.split("|")) for e in esperado)


def evaluar(
    respuesta: str,
    llamadas: list[Llamada],
    tool_esperada: str,
    corpus: list[dict],
    esperado: tuple[str, ...] = (),
) -> Resultado:
    """Evalúa una ejecución. `llamadas` viene de registro_herramientas.LLAMADAS."""
    texto = (respuesta or "").strip()
    responde = (
        len(texto) > 20
        and not any(f in texto.lower() for f in SIN_INFORMACION)
        and contiene_esperados(texto, esperado)
    )
    exige_cita = tool_esperada == "buscar_normativa"
    cita = bool(citas_validas(extraer_citas(texto), corpus)) if exige_cita else None
    usa_tool = any(c.herramienta == tool_esperada for c in llamadas)
    sin_errores = all(c.ok for c in llamadas)
    return Resultado(responde, cita, usa_tool, sin_errores)


def formatear(resultado: Resultado) -> str:
    marca = {True: "✔", False: "✘", None: "–"}
    lineas = [f"  {marca[v]} {nombre}" for nombre, v in resultado.items()]
    lineas.append("  => " + ("APROBADO" if resultado.aprobado else "REVISAR LA TRAZA"))
    return "\n".join(lineas)

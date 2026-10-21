"""Datos ficticios y lógica pura de la tool `consultar_limite_gastos`.

Los topes replican la sección 3 de la política ficticia POL-GV-001 v2.1 de Austral Bank
(laboratorios/dia1-lab-guiado/datos/politicas-internas/politica-gastos-de-viaje.md).
No depende de Azure ni de Agent Framework, así que se puede probar sin credenciales.
"""
import unicodedata

FUENTE = "POL-GV-001 v2.1 (Política de Gastos de Viaje, Austral Bank), sección 3 - Topes de gasto"
VIGENTE_DESDE = "2026-03-01"

CONCEPTOS = ("alojamiento", "alimentacion")
AMBITOS = ("nacional", "internacional")

# Ciudades de categoría A: tope de alojamiento internacional de USD 250 por noche.
CIUDADES_CATEGORIA_A = ("nueva york", "londres", "tokio")

# Variantes en inglés y sin espacios que el modelo puede enviar en el parámetro libre `ciudad`.
_ALIAS_CIUDAD = {"new york": "nueva york", "nyc": "nueva york", "london": "londres", "tokyo": "tokio"}

_ALIAS_CONCEPTO = {"alimentacion": "alimentacion", "alojamiento": "alojamiento", "hotel": "alojamiento"}

_TOPES = {
    ("alojamiento", "nacional"): (90_000, "CLP", "por noche"),
    ("alojamiento", "internacional"): (180, "USD", "por noche"),
    ("alimentacion", "nacional"): (35_000, "CLP", "por día"),
    ("alimentacion", "internacional"): (70, "USD", "por día"),
}
_TOPE_CATEGORIA_A = (250, "USD", "por noche")


def _normalizar(texto: str | None) -> str:
    sin_tildes = unicodedata.normalize("NFKD", (texto or "").strip().lower())
    return "".join(c for c in sin_tildes if not unicodedata.combining(c))


def consultar_limite(concepto: str, ambito: str, ciudad: str | None = None) -> dict:
    """Devuelve el tope vigente o un error explícito; nunca inventa valores."""
    c = _ALIAS_CONCEPTO.get(_normalizar(concepto))
    a = _normalizar(ambito)
    if c is None:
        return {"encontrado": False, "error": f"concepto '{concepto}' no válido; usa uno de {list(CONCEPTOS)}"}
    if a not in AMBITOS:
        return {"encontrado": False, "error": f"ámbito '{ambito}' no válido; usa uno de {list(AMBITOS)}"}

    valor, moneda, unidad = _TOPES[(c, a)]
    ciudad_norm = _normalizar(ciudad)
    categoria_a = _ALIAS_CIUDAD.get(ciudad_norm, ciudad_norm) in CIUDADES_CATEGORIA_A
    if c == "alojamiento" and a == "internacional" and categoria_a:
        valor, moneda, unidad = _TOPE_CATEGORIA_A

    resultado = {
        "encontrado": True,
        "concepto": c,
        "ambito": a,
        "limite": valor,
        "moneda": moneda,
        "unidad": unidad,
        "vigente_desde": VIGENTE_DESDE,
        "fuente": FUENTE,
    }
    if ciudad_norm:
        resultado["ciudad"] = ciudad.strip()
        resultado["ciudad_categoria_a"] = categoria_a
    return resultado

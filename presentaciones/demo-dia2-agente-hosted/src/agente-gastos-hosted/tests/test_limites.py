import asyncio
import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from limites import FUENTE, consultar_limite  # noqa: E402


@pytest.mark.parametrize(
    "concepto, ambito, ciudad, limite, moneda",
    [
        ("alojamiento", "nacional", None, 90_000, "CLP"),
        ("alimentacion", "nacional", None, 35_000, "CLP"),
        ("alojamiento", "internacional", None, 180, "USD"),
        ("alimentacion", "internacional", None, 70, "USD"),
        ("alojamiento", "internacional", "Tokio", 250, "USD"),
        ("Alojamiento", "Internacional", "nueva york", 250, "USD"),
        ("alojamiento", "internacional", "Tokyo", 250, "USD"),
        ("alojamiento", "internacional", "New York", 250, "USD"),
        ("alojamiento", "internacional", "London", 250, "USD"),
        ("alojamiento", "internacional", "Santiago", 180, "USD"),
        ("alimentacion", "internacional", "Londres", 70, "USD"),  # categoría A solo aplica a alojamiento
        ("alojamiento", "nacional", "Tokio", 90_000, "CLP"),
    ],
)
def test_topes_segun_politica(concepto, ambito, ciudad, limite, moneda):
    r = consultar_limite(concepto, ambito, ciudad)
    assert r["encontrado"] is True
    assert (r["limite"], r["moneda"]) == (limite, moneda)
    assert r["fuente"] == FUENTE and "POL-GV-001" in r["fuente"]


def test_normaliza_tildes_y_alias():
    assert consultar_limite("alimentación", "nacional")["limite"] == 35_000
    assert consultar_limite("hotel", "nacional")["concepto"] == "alojamiento"


@pytest.mark.parametrize("concepto, ambito", [("transporte", "nacional"), ("alojamiento", "regional"), ("", ""), (None, None)])
def test_entradas_invalidas_no_inventan_datos(concepto, ambito):
    r = consultar_limite(concepto, ambito)
    assert r["encontrado"] is False and "limite" not in r and r["error"]


def test_contrato_de_la_tool():
    pytest.importorskip("agent_framework")
    from main import consultar_limite_gastos

    assert consultar_limite_gastos.name == "consultar_limite_gastos"
    esquema = consultar_limite_gastos.parameters()
    assert set(esquema["required"]) == {"concepto", "ambito"}
    assert set(esquema["properties"]) == {"concepto", "ambito", "ciudad"}
    salida = asyncio.run(consultar_limite_gastos.invoke(concepto="alojamiento", ambito="internacional", ciudad="Tokio"))
    datos = json.loads(salida[0].text)
    assert datos["limite"] == 250 and "POL-GV-001" in datos["fuente"]

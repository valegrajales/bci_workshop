"""Pruebas de la lógica de la herramienta consultar_estado_solicitud (sin Azure)."""
import json

import pytest

import registro_herramientas as reg
import solicitudes as s


def test_hay_diez_solicitudes_con_campos_completos():
    sols = s.cargar_solicitudes()
    assert len(sols) == 10
    for sol_id, sol in sols.items():
        assert s.PATRON_ID.match(sol_id)
        assert set(sol) >= {"id", "estado", "fecha", "responsable"}
        assert all(str(sol[c]).strip() for c in ("id", "estado", "fecha", "responsable"))


def test_los_estados_son_los_de_la_norma_nor_011():
    estados = {sol["estado"] for sol in s.cargar_solicitudes().values()}
    permitidos = {
        "Recibida",
        "En revisión",
        "Pendiente de información",
        "Aprobada",
        "Rechazada",
        "Cerrada",
    }
    assert estados <= permitidos
    assert len(estados) >= 4  # variedad suficiente para las demos


def test_consulta_existente():
    r = s.consultar_estado("SOL-2026-0003")
    assert r["encontrada"] is True
    assert r["estado"] == "En revisión" and r["responsable"] == "Área Legal"


@pytest.mark.parametrize("entrada", [" sol-2026-0003 ", "Sol-2026-0003", "SOL-2026-0003\n"])
def test_normaliza_mayusculas_y_espacios(entrada):
    assert s.consultar_estado(entrada)["id"] == "SOL-2026-0003"


@pytest.mark.parametrize("entrada", ["12345", "", "SOL-26-3", "SOL-2026-00033", "REQ-2026-0001", None])
def test_formato_invalido_no_lanza_y_explica(entrada):
    r = s.consultar_estado(entrada)
    assert r["encontrada"] is False and r["error"] == "formato_invalido"
    assert "SOL-AAAA-NNNN" in r["mensaje"]


def test_id_con_formato_valido_pero_inexistente():
    r = s.consultar_estado("SOL-2026-9999")
    assert r == {
        "encontrada": False,
        "error": "no_encontrada",
        "mensaje": "No existe la solicitud SOL-2026-9999.",
    }


def test_resultado_es_serializable_a_json():
    assert json.loads(json.dumps(s.consultar_estado("SOL-2026-0001")))["encontrada"] is True


def test_acepta_diccionario_inyectado():
    falsa = {"SOL-2026-0001": {"id": "SOL-2026-0001", "estado": "Cerrada", "fecha": "2026-01-01", "responsable": "X"}}
    assert s.consultar_estado("SOL-2026-0001", falsa)["estado"] == "Cerrada"
    assert s.consultar_estado("SOL-2026-0002", falsa)["error"] == "no_encontrada"


def test_registro_de_herramientas():
    reg.limpiar()
    reg.registrar("buscar_normativa", {"consulta": "x"})
    reg.registrar("consultar_estado_solicitud", {"id_solicitud": "SOL-2026-0001"}, ok=False)
    assert reg.usadas() == ["buscar_normativa", "consultar_estado_solicitud"]
    assert reg.LLAMADAS[-1].ok is False
    reg.limpiar()
    assert reg.usadas() == []

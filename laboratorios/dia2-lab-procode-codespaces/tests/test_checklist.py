"""Pruebas del checklist de éxito de la Tarea 4 (sin Azure)."""
import checklist as ck
import normativa as n
from registro_herramientas import Llamada

CORPUS = n.cargar_corpus()
RESP_OK = "El límite mensual para Jefatura es de 2.500 USD por mes [NOR-001-01]."


def test_caso_normativa_aprobado():
    r = ck.evaluar(RESP_OK, [Llamada("buscar_normativa", {"consulta": "x"}, True)], "buscar_normativa", CORPUS)
    assert (r.responde, r.cita_fuente, r.usa_tool, r.sin_errores) == (True, True, True, True)
    assert r.aprobado


def test_sin_tool_ni_cita_no_aprueba():
    r = ck.evaluar(RESP_OK.replace("[NOR-001-01]", ""), [], "buscar_normativa", CORPUS)
    assert r.cita_fuente is False and r.usa_tool is False and not r.aprobado


def test_cita_inventada_no_cuenta():
    r = ck.evaluar("Son 900 USD [NOR-777-01] según la norma.", [Llamada("buscar_normativa", {}, True)], "buscar_normativa", CORPUS)
    assert r.cita_fuente is False


def test_caso_estado_no_exige_cita():
    llamadas = [Llamada("consultar_estado_solicitud", {"id_solicitud": "SOL-2026-0003"}, True)]
    r = ck.evaluar("La solicitud SOL-2026-0003 está En revisión con el Área Legal.", llamadas, "consultar_estado_solicitud", CORPUS)
    assert r.cita_fuente is None and r.aprobado


def test_error_en_tool_se_detecta():
    llamadas = [Llamada("consultar_estado_solicitud", {"id_solicitud": "3"}, False)]
    r = ck.evaluar("Parece que no existe esa solicitud en el sistema.", llamadas, "consultar_estado_solicitud", CORPUS)
    assert r.usa_tool and r.sin_errores is False and not r.aprobado


def test_respuesta_vacia_o_evasiva():
    assert ck.evaluar("", [], "buscar_normativa", CORPUS).responde is False
    assert ck.evaluar("No tengo información sobre eso, lo siento mucho.", [], "buscar_normativa", CORPUS).responde is False


def test_formatear_muestra_cuatro_criterios():
    r = ck.evaluar(RESP_OK, [Llamada("buscar_normativa", {}, True)], "buscar_normativa", CORPUS)
    salida = ck.formatear(r)
    assert salida.count("✔") == 4 and "APROBADO" in salida


def test_dato_esperado_con_alternativas():
    llamadas = [Llamada("buscar_normativa", {}, True)]
    ok = "El alojamiento cuesta 350 USD y los comprobantes se conservan seis años [NOR-002-01] [NOR-004-01]."
    mal = "Los comprobantes se conservan 2 años [NOR-004-01] y el alojamiento cuesta 100 USD."
    esperado = ("350", "6 años|seis años")
    assert ck.evaluar(ok, llamadas, "buscar_normativa", CORPUS, esperado).responde is True
    assert ck.evaluar(mal, llamadas, "buscar_normativa", CORPUS, esperado).responde is False

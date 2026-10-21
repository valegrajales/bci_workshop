"""Pruebas de la evaluación por lotes (reglas locales, sin Azure)."""
import evaluacion as ev
from normativa import cargar_corpus

CORPUS = cargar_corpus()
P = {p["id"]: p for p in ev.cargar_preguntas()}


def test_carga_las_preguntas_con_los_campos_esperados():
    assert len(P) >= 10
    for p in P.values():
        assert {"id", "question", "truth", "fuentes", "usa_tool", "nivel_minimo"} <= set(p)


def test_debe_negarse_por_nivel_o_por_estar_fuera_del_corpus():
    assert ev.debe_negarse(P["P05"], "interno") and not ev.debe_negarse(P["P05"], "restringido")
    assert ev.debe_negarse(P["P07"], "restringido")  # vacaciones: no está en el corpus
    assert ev.debe_negarse(P["P01"], "publico")  # nivel público no alcanza para documentos internos
    assert not ev.debe_negarse(P["P08"], "interno")  # usa la tool de estado


def test_respuesta_correcta_con_cita_y_tool():
    m = ev.evaluar_respuesta(P["P01"], "El límite es 2.500 USD [NOR-001-02].", ["buscar_normativa"], "interno", CORPUS)
    assert m == {"negativa_correcta": True, "cita_esperada": True, "tool_correcta": True, "aprobada": True}


def test_respuesta_sin_cita_falla():
    m = ev.evaluar_respuesta(P["P01"], "El límite es 2.500 USD.", ["buscar_normativa"], "interno", CORPUS)
    assert m["cita_esperada"] is False and not m["aprobada"]


def test_pregunta_restringida_debe_ser_rechazada_para_nivel_interno():
    rechazo = "No tengo información en la normativa disponible para tu nivel de acceso."
    ok = ev.evaluar_respuesta(P["P06"], rechazo, ["buscar_normativa"], "interno", CORPUS)
    assert ok["negativa_correcta"] and ok["aprobada"]
    filtrado = ev.evaluar_respuesta(P["P06"], "Lo aprueba el Comité de Crédito Central [NOR-007-01].", [], "interno", CORPUS)
    assert not filtrado["negativa_correcta"] and not filtrado["aprobada"]


def test_tool_de_estado_solo_cuando_corresponde():
    sin_tool = ev.evaluar_respuesta(P["P08"], "Está En revisión.", [], "interno", CORPUS)
    assert sin_tool["tool_correcta"] is False
    de_mas = ev.evaluar_respuesta(P["P10"], "3 días hábiles [NOR-011-02].", ["consultar_estado_solicitud"], "interno", CORPUS)
    assert de_mas["tool_correcta"] is False


def test_resumen_ignora_metricas_que_no_aplican():
    r = ev.resumir([
        {"negativa_correcta": True, "cita_esperada": None, "tool_correcta": True, "aprobada": True},
        {"negativa_correcta": True, "cita_esperada": False, "tool_correcta": True, "aprobada": False},
    ])
    assert r == {"negativa_correcta": 100, "cita_esperada": 0, "tool_correcta": 100, "aprobada": 50}

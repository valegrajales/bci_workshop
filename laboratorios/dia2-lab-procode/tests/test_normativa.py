"""Pruebas de metadatos, chunking y filtros de acceso (todo local, sin Azure)."""
import pytest

import normativa as n

DOC = """---
id: NOR-099
titulo: Documento de prueba
area: Pruebas
nivel_acceso: Público
---

# Documento de prueba

## Sección A

Primer párrafo de la sección A.

## Sección B

Texto de B.
"""


def test_parsear_documento_normaliza_nivel_con_acento():
    meta, cuerpo = n.parsear_documento(DOC)
    assert meta["id"] == "NOR-099"
    assert meta["nivel_acceso"] == "publico"
    assert cuerpo.startswith("# Documento de prueba")


@pytest.mark.parametrize(
    "texto",
    [
        "sin encabezado",
        "---\nid: X\ntitulo: T\n",  # no se cierra
        "---\nid: X\ntitulo: T\narea: A\n---\ncuerpo",  # falta nivel_acceso
        "---\nid: X\ntitulo: T\narea: A\nnivel_acceso: secreto\n---\ncuerpo",  # nivel inválido
    ],
)
def test_parsear_documento_rechaza_encabezados_invalidos(texto):
    with pytest.raises(ValueError):
        n.parsear_documento(texto)


def test_fragmentos_por_seccion_con_ids_estables():
    meta, cuerpo = n.parsear_documento(DOC)
    frags = n.crear_fragmentos(meta, cuerpo)
    assert [f["id"] for f in frags] == ["NOR-099-01", "NOR-099-02"]
    assert frags[0]["seccion"] == "Sección A"
    assert frags[1]["contenido"] == "Texto de B."
    assert all(f["nivel_acceso"] == "publico" and f["doc_id"] == "NOR-099" for f in frags)


def test_seccion_larga_se_parte_sin_cortar_parrafos():
    parrafos = [f"Párrafo {i} " + "x" * 90 for i in range(10)]
    meta = {"id": "NOR-098", "titulo": "T", "area": "A", "nivel_acceso": "interno"}
    cuerpo = "## Larga\n\n" + "\n\n".join(parrafos)
    frags = n.crear_fragmentos(meta, cuerpo, max_caracteres=300)
    assert len(frags) > 1
    assert all(len(f["contenido"]) <= 300 for f in frags)
    assert "\n\n".join(f["contenido"] for f in frags).split("\n\n") == parrafos


def test_corpus_real_cumple_el_contrato():
    corpus = n.cargar_corpus()
    docs = {f["doc_id"] for f in corpus}
    assert 10 <= len(docs) <= 14
    assert {f["nivel_acceso"] for f in corpus} == {"publico", "interno", "restringido"}
    assert all(f["contenido"].strip() and f["seccion"] for f in corpus)
    assert len({f["id"] for f in corpus}) == len(corpus)
    assert max(len(f["contenido"]) for f in corpus) <= n.MAX_CARACTERES


def test_corpus_contiene_los_hechos_que_usan_las_preguntas():
    texto = " ".join(f["contenido"] for f in n.cargar_corpus())
    for hecho in ("2.500", "350", "6 años", "36 meses", "250.000"):
        assert hecho in texto


def test_niveles_permitidos_y_filtro():
    assert n.niveles_permitidos("publico") == ("publico",)
    assert n.niveles_permitidos("Interno") == ("publico", "interno")
    assert n.niveles_permitidos("restringido") == ("publico", "interno", "restringido")
    assert n.construir_filtro_acceso("interno") == "search.in(nivel_acceso, 'publico,interno', ',')"
    with pytest.raises(ValueError):
        n.construir_filtro_acceso("admin")


def test_el_nivel_interno_no_alcanza_documentos_restringidos():
    permitidos = n.niveles_permitidos("interno")
    visibles = [f for f in n.cargar_corpus() if f["nivel_acceso"] in permitidos]
    assert visibles and all(f["doc_id"] not in ("NOR-006", "NOR-007") for f in visibles)


def test_formatear_resultados_incluye_id_citable_y_maneja_vacio():
    frag = n.cargar_corpus()[0]
    salida = n.formatear_resultados([frag])
    assert f"[{frag['id']}]" in salida and frag["contenido"] in salida
    assert n.formatear_resultados([]).startswith("SIN_RESULTADOS")


def test_extraer_y_validar_citas():
    texto = "El límite es 2.500 USD [NOR-001-02]. Ver también [NOR-004] y [NOR-001-02] y [NOR-999-01]."
    citas = n.extraer_citas(texto)
    assert citas == ["NOR-001-02", "NOR-004", "NOR-999-01"]
    validas = n.citas_validas(citas, n.cargar_corpus())
    assert "NOR-999-01" not in validas and "NOR-004" in validas
    assert n.extraer_citas("") == [] and n.extraer_citas(None) == []


def test_texto_para_embedding_incluye_titulo_y_seccion():
    frag = n.cargar_corpus()[0]
    t = n.texto_para_embedding(frag)
    assert frag["titulo"] in t and frag["seccion"] in t and frag["contenido"] in t

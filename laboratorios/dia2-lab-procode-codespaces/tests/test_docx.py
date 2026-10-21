"""Prueba local del conversor README -> Word (herramientas\\md_a_docx.py). Se omite si no está python-docx."""
import importlib.util
import re
from pathlib import Path

import pytest

docx = pytest.importorskip("docx")

RAIZ = Path(__file__).resolve().parent.parent


def _cargar_conversor():
    spec = importlib.util.spec_from_file_location("md_a_docx", RAIZ / "herramientas" / "md_a_docx.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def test_separar_celdas_respeta_pipes_escapados_y_codigo():
    conv = _cargar_conversor()
    fila = r"| `a \| b` | texto `x | y` | c |"
    assert conv.separar_celdas(fila) == ["`a | b`", "texto `x | y`", "c"]


def test_readme_se_convierte_sin_marcas_markdown(tmp_path):
    conv = _cargar_conversor()
    destino = tmp_path / "guia.docx"
    conv.convertir(RAIZ / "README.md", destino)
    doc = docx.Document(str(destino))
    md = (RAIZ / "README.md").read_text(encoding="utf-8")

    titulos = [p.text for p in doc.paragraphs if p.style.name.startswith(("Heading", "Title"))]
    assert len(titulos) == len(re.findall(r"^#{1,4} ", md, re.M))
    assert len(doc.tables) == len(re.findall(r"^\|[\s:|-]+\|?$", md, re.M))

    mono = {id(p) for p in doc.paragraphs if p.runs and p.runs[0].font.name == "Consolas"}
    texto = "\n".join(p.text for p in doc.paragraphs if id(p) not in mono)
    texto += "\n".join(c.text for t in doc.tables for f in t.rows for c in f.cells)
    for resto in ("**", "`", "](", "<details", "<summary", "- [ ]"):
        assert resto not in texto, resto
    assert "Preparación del entorno" in texto and "Austral Bank" in texto

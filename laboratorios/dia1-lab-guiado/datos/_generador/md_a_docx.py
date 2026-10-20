"""Convierte un archivo Markdown simple a .docx con python-docx.

Soporta: encabezados (#..####), párrafos, negrita, cursiva, `código` en línea,
enlaces [texto](url), listas con viñetas (incluye "- [ ]" como casilla) y numeradas,
listas anidadas, citas (>), bloques de código (```), tablas con "|" y reglas (---).

Uso:
    python md_a_docx.py ENTRADA.md SALIDA.docx
"""
import re
import sys
from pathlib import Path

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

FUENTE_TEXTO = "Calibri"
FUENTE_CODIGO = "Consolas"
COLOR_ENLACE = RGBColor(0x05, 0x63, 0xC1)
COLOR_ENCABEZADO = RGBColor(0x1F, 0x3A, 0x5F)

RE_ENCABEZADO = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RE_TABLA_SEP = re.compile(r"^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
RE_LISTA = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+(.*)$")
RE_CASILLA = re.compile(r"^\[( |x|X)\]\s+(.*)$")
RE_REGLA = re.compile(r"^\s*([-*_])(\s*\1){2,}\s*$")

PATRONES_INLINE = [
    ("code", re.compile(r"`([^`]+)`")),
    ("link", re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")),
    ("bold", re.compile(r"\*\*(.+?)\*\*")),
    ("italic", re.compile(r"(?<![\w*])\*(?!\s)([^*]+?)(?<!\s)\*(?![\w*])")),
]


def sombrear(elemento_pr, color_hex):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), color_hex)
    elemento_pr.append(shd)


def fuente_run(run, nombre, tam=None):
    run.font.name = nombre
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for atributo in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(atributo), nombre)
    if tam:
        run.font.size = Pt(tam)


def agregar_enlace(parrafo, texto, url, tam=None):
    rid = parrafo.part.relate_to(
        url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink", is_external=True
    )
    h = OxmlElement("w:hyperlink")
    h.set(qn("r:id"), rid)
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    estilo = OxmlElement("w:color")
    estilo.set(qn("w:val"), "0563C1")
    rpr.append(estilo)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    if tam:
        sz = OxmlElement("w:sz")
        sz.set(qn("w:val"), str(int(tam * 2)))
        rpr.append(sz)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.text = texto
    t.set(qn("xml:space"), "preserve")
    r.append(t)
    h.append(r)
    parrafo._p.append(h)


def agregar_inline(parrafo, texto, negrita=False, cursiva=False, tam=None):
    texto = texto.replace("\\|", "|")
    while texto:
        mejor = None
        for tipo, patron in PATRONES_INLINE:
            m = patron.search(texto)
            if m and (mejor is None or m.start() < mejor[1].start()):
                mejor = (tipo, m)
        if mejor is None:
            agregar_run(parrafo, texto, negrita, cursiva, tam)
            return
        tipo, m = mejor
        if m.start() > 0:
            agregar_run(parrafo, texto[: m.start()], negrita, cursiva, tam)
        if tipo == "code":
            run = parrafo.add_run(m.group(1))
            fuente_run(run, FUENTE_CODIGO, (tam or 11) - 1)
            run.bold = negrita
            sombrear(run._element.get_or_add_rPr(), "EFEFEF")
        elif tipo == "link":
            agregar_enlace(parrafo, m.group(1), m.group(2), tam)
            agregar_run(parrafo, f" ({m.group(2)})", negrita, cursiva, (tam or 11) - 2, gris=True)
        elif tipo == "bold":
            agregar_inline(parrafo, m.group(1), True, cursiva, tam)
        else:
            agregar_inline(parrafo, m.group(1), negrita, True, tam)
        texto = texto[m.end():]


def agregar_run(parrafo, texto, negrita=False, cursiva=False, tam=None, gris=False):
    partes = texto.split("<br>")
    for i, parte in enumerate(partes):
        if i > 0:
            parrafo.add_run().add_break(WD_BREAK.LINE)
        if not parte:
            continue
        run = parrafo.add_run(parte)
        run.bold = negrita or None
        run.italic = cursiva or None
        if tam:
            run.font.size = Pt(tam)
        if gris:
            run.font.color.rgb = RGBColor(0x59, 0x59, 0x59)


def borde_izquierdo(parrafo, color="2F6EBA", ancho=18):
    ppr = parrafo._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    izq = OxmlElement("w:left")
    izq.set(qn("w:val"), "single")
    izq.set(qn("w:sz"), str(ancho))
    izq.set(qn("w:space"), "8")
    izq.set(qn("w:color"), color)
    bdr.append(izq)
    ppr.append(bdr)
    sombrear(ppr, "EEF4FB")


def partir_fila(linea):
    linea = linea.strip()
    if linea.startswith("|"):
        linea = linea[1:]
    if linea.endswith("|") and not linea.endswith("\\|"):
        linea = linea[:-1]
    celdas, actual = [], ""
    i = 0
    while i < len(linea):
        if linea[i] == "\\" and i + 1 < len(linea) and linea[i + 1] == "|":
            actual += "\\|"
            i += 2
            continue
        if linea[i] == "|":
            celdas.append(actual.strip())
            actual = ""
        else:
            actual += linea[i]
        i += 1
    celdas.append(actual.strip())
    return celdas


def agregar_tabla(doc, filas):
    n = max(len(f) for f in filas)
    tabla = doc.add_table(rows=0, cols=n)
    tabla.style = "Table Grid"
    tabla.alignment = WD_TABLE_ALIGNMENT.CENTER
    for idx, fila in enumerate(filas):
        celdas = tabla.add_row().cells
        trpr = tabla.rows[-1]._tr.get_or_add_trPr()
        trpr.append(OxmlElement("w:cantSplit"))
        if idx == 0:
            trpr.append(OxmlElement("w:tblHeader"))
        for j in range(n):
            texto = fila[j] if j < len(fila) else ""
            celda = celdas[j]
            p = celda.paragraphs[0]
            p.paragraph_format.space_after = Pt(2)
            p.paragraph_format.space_before = Pt(2)
            agregar_inline(p, texto, negrita=(idx == 0), tam=9.5)
            if idx == 0:
                sombrear(celda._tc.get_or_add_tcPr(), "DCE6F2")
    ajustar_tabla(tabla, filas, n)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def ajustar_tabla(tabla, filas, n):
    """Anchos proporcionales al contenido y cabecera pegada a la tabla (sin filas huérfanas)."""
    pesos = []
    for j in range(n):
        largos = [len(f[j]) for f in filas if j < len(f)]
        promedio = sum(largos) / max(len(largos), 1)
        pesos.append(min(max(promedio, 9), 55))
    total_cm = 17.2
    tabla.autofit = False
    for fila in tabla.rows:
        for j, celda in enumerate(fila.cells):
            celda.width = Cm(total_cm * pesos[j] / sum(pesos))
    pegar = len(filas) - 1 if len(filas) <= 9 else 2
    for fila in tabla.rows[:pegar]:
        for celda in fila.cells:
            for p in celda.paragraphs:
                p.paragraph_format.keep_with_next = True


def agregar_codigo(doc, lineas):
    for linea in lineas or [""]:
        p = doc.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.left_indent = Cm(0.5)
        run = p.add_run(linea if linea else " ")
        fuente_run(run, FUENTE_CODIGO, 9)
        sombrear(p._p.get_or_add_pPr(), "F3F3F3")
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def pie_con_pagina(doc, texto):
    sec = doc.sections[0]
    doc.styles["Footer"].font.size = Pt(8)
    p = sec.footer.paragraphs[0]
    p.text = ""
    run = p.add_run(texto + " · Página ")
    run.font.size = Pt(8)
    run.font.color.rgb = RGBColor(0x59, 0x59, 0x59)
    campo = OxmlElement("w:fldSimple")
    campo.set(qn("w:instr"), "PAGE")
    r = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    sz = OxmlElement("w:sz")
    sz.set(qn("w:val"), "16")
    rpr.append(sz)
    r.append(rpr)
    t = OxmlElement("w:t")
    t.text = "1"
    r.append(t)
    campo.append(r)
    p._p.append(campo)


def configurar_estilos(doc):
    normal = doc.styles["Normal"]
    normal.font.name = FUENTE_TEXTO
    normal.font.size = Pt(11)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FUENTE_TEXTO)
    normal.paragraph_format.space_after = Pt(6)
    for nombre, tam in (("Title", 24), ("Heading 1", 18), ("Heading 2", 14), ("Heading 3", 12), ("Heading 4", 11)):
        est = doc.styles[nombre]
        est.font.name = FUENTE_TEXTO
        est.font.size = Pt(tam)
        est.font.bold = True
        est.font.color.rgb = COLOR_ENCABEZADO
        est.element.rPr.rFonts.set(qn("w:eastAsia"), FUENTE_TEXTO)
        est.element.rPr.rFonts.set(qn("w:ascii"), FUENTE_TEXTO)
        est.element.rPr.rFonts.set(qn("w:hAnsi"), FUENTE_TEXTO)
    sec = doc.sections[0]
    sec.page_width, sec.page_height = Cm(21.59), Cm(27.94)
    sec.left_margin = sec.right_margin = Cm(2.2)
    sec.top_margin = sec.bottom_margin = Cm(2.0)


def convertir(ruta_md, ruta_docx, titulo_pie):
    lineas = Path(ruta_md).read_text(encoding="utf-8").splitlines()
    doc = Document()
    configurar_estilos(doc)
    pie_con_pagina(doc, titulo_pie)

    i = 0
    titulo_usado = False
    ultimo_item = None
    while i < len(lineas):
        linea = lineas[i]
        if not linea.strip():
            ultimo_item = None
            i += 1
            continue

        if linea.strip().startswith("```"):
            i += 1
            bloque = []
            while i < len(lineas) and not lineas[i].strip().startswith("```"):
                bloque.append(lineas[i])
                i += 1
            i += 1
            agregar_codigo(doc, bloque)
            ultimo_item = None
            continue

        if RE_REGLA.match(linea):
            i += 1
            continue

        m = RE_ENCABEZADO.match(linea)
        if m:
            nivel, texto = len(m.group(1)), m.group(2)
            if nivel == 1 and not titulo_usado:
                p = doc.add_paragraph(style="Title")
                titulo_usado = True
            else:
                p = doc.add_paragraph(style=f"Heading {min(max(nivel - 1, 1), 4)}")
            agregar_inline(p, texto)
            ultimo_item = None
            i += 1
            continue

        if "|" in linea and i + 1 < len(lineas) and RE_TABLA_SEP.match(lineas[i + 1]):
            filas = [partir_fila(linea)]
            i += 2
            while i < len(lineas) and "|" in lineas[i] and lineas[i].strip():
                filas.append(partir_fila(lineas[i]))
                i += 1
            agregar_tabla(doc, filas)
            ultimo_item = None
            continue

        if linea.lstrip().startswith(">"):
            partes = []
            while i < len(lineas) and lineas[i].lstrip().startswith(">"):
                partes.append(re.sub(r"^\s*>\s?", "", lineas[i]))
                i += 1
            parrafos, actual = [], []
            for parte in partes:
                if parte.strip():
                    actual.append(parte.strip())
                elif actual:
                    parrafos.append(" ".join(actual))
                    actual = []
            if actual:
                parrafos.append(" ".join(actual))
            for texto in parrafos:
                p = doc.add_paragraph()
                p.paragraph_format.left_indent = Cm(0.6)
                p.paragraph_format.space_after = Pt(4)
                borde_izquierdo(p)
                agregar_inline(p, texto)
            ultimo_item = None
            continue

        m = RE_LISTA.match(linea)
        if m:
            sangria = len(m.group(1).replace("\t", "    "))
            marcador, texto = m.group(2), m.group(3)
            nivel = 0 if sangria < 2 else 1 if sangria < 6 else 2
            numerada = marcador[0].isdigit()
            casilla = RE_CASILLA.match(texto)
            if numerada:
                p = doc.add_paragraph()
                sangria_cm = 0.9 + 0.8 * nivel
                p.paragraph_format.left_indent = Cm(sangria_cm)
                p.paragraph_format.first_line_indent = Cm(-0.7)
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.tab_stops.add_tab_stop(Cm(sangria_cm))
                agregar_run(p, marcador + "\t")
                agregar_inline(p, texto)
            elif casilla:
                p = doc.add_paragraph()
                sangria_cm = 0.9 + 0.8 * nivel
                p.paragraph_format.left_indent = Cm(sangria_cm)
                p.paragraph_format.first_line_indent = Cm(-0.7)
                p.paragraph_format.space_after = Pt(3)
                p.paragraph_format.tab_stops.add_tab_stop(Cm(sangria_cm))
                marca = "☑" if casilla.group(1).lower() == "x" else "☐"
                run = p.add_run(marca + "\t")
                fuente_run(run, "Segoe UI Symbol")
                agregar_inline(p, casilla.group(2))
            else:
                estilo = "List Bullet" if nivel == 0 else "List Bullet 2"
                p = doc.add_paragraph(style=estilo)
                p.paragraph_format.space_after = Pt(3)
                agregar_inline(p, texto)
            ultimo_item = (p, nivel)
            i += 1
            continue

        # Línea de texto: continuación de un ítem de lista o párrafo normal
        if ultimo_item and linea.startswith((" ", "\t")):
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(0.9 + 0.8 * ultimo_item[1])
            p.paragraph_format.space_after = Pt(3)
            agregar_inline(p, linea.strip())
            i += 1
            continue

        partes = [linea.strip()]
        i += 1
        while (
            i < len(lineas)
            and lineas[i].strip()
            and not RE_ENCABEZADO.match(lineas[i])
            and not RE_LISTA.match(lineas[i])
            and not lineas[i].lstrip().startswith((">", "```"))
            and "|" not in lineas[i][:1]
            and not RE_REGLA.match(lineas[i])
        ):
            partes.append(lineas[i].strip())
            i += 1
        p = doc.add_paragraph()
        agregar_inline(p, " ".join(partes))
        ultimo_item = None

    doc.core_properties.title = "Guía del participante — Día 1: Del catálogo de modelos a una experiencia de agente"
    doc.core_properties.subject = "Microsoft AI Foundry BCI Training Day — Laboratorio guiado Día 1"
    doc.core_properties.author = "Equipo del taller (Microsoft Chile)"
    doc.core_properties.language = "es-CL"
    doc.save(ruta_docx)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    convertir(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3] if len(sys.argv) > 3 else "Austral Bank — material ficticio de capacitación",
    )
    print(f"OK: {sys.argv[2]}")

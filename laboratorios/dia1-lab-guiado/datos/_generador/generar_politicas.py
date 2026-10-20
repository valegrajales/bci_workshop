# -*- coding: utf-8 -*-
"""Genera las 4 políticas internas ficticias de Austral Bank (.md y .pdf).

Uso:  python generar_politicas.py
Requiere: pip install reportlab
Todo el contenido es ficticio y existe solo para el laboratorio del Día 1.
"""
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (KeepTogether, ListFlowable, ListItem, Paragraph,
                                SimpleDocTemplate, Spacer, Table, TableStyle)

OUT = Path(__file__).resolve().parent.parent / "politicas-internas"
OUT.mkdir(parents=True, exist_ok=True)

FONTS = Path("C:/Windows/Fonts")
pdfmetrics.registerFont(TTFont("Arial", str(FONTS / "arial.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Bold", str(FONTS / "arialbd.ttf")))
pdfmetrics.registerFont(TTFont("Arial-Italic", str(FONTS / "ariali.ttf")))
pdfmetrics.registerFontFamily("Arial", normal="Arial", bold="Arial-Bold",
                              italic="Arial-Italic", boldItalic="Arial-Bold")

AVISO = "Documento ficticio para capacitación — Austral Bank"

DOCS = [
    {
        "file": "politica-gastos-de-viaje",
        "title": "Política de Gastos de Viaje",
        "code": "POL-GV-001",
        "version": "2.1",
        "vigencia": "01-03-2026",
        "area": "Administración y Finanzas Corporativas",
        "sections": [
            ("1. Objetivo y alcance", [
                ("p", "Esta política define cómo se solicitan, aprueban y rinden los gastos de viaje de las y los colaboradores de Austral Bank. Aplica a viajes nacionales e internacionales realizados por motivos de trabajo."),
            ]),
            ("2. Solicitud y anticipación mínima", [
                ("table", ["Tipo de viaje", "Anticipación mínima de la solicitud"], [
                    ["Nacional", "5 días hábiles"],
                    ["Internacional", "15 días hábiles"],
                ]),
                ("p", "Las solicitudes con menos anticipación requieren una excepción aprobada por la Gerencia de Administración y Finanzas Corporativas."),
            ]),
            ("3. Topes de gasto", [
                ("table", ["Concepto", "Viaje nacional", "Viaje internacional"], [
                    ["Alojamiento por noche", "$90.000 CLP", "USD 180"],
                    ["Alimentación diaria", "$35.000 CLP", "USD 70"],
                ]),
                ("p", "En ciudades de categoría A (Nueva York, Londres y Tokio) el tope de alojamiento internacional es de USD 250 por noche."),
            ]),
            ("4. Transporte aéreo", [
                ("ul", [
                    "Vuelos de menos de 6 horas: clase económica.",
                    "Vuelos de 6 horas o más: clase premium economy, con aprobación del gerente de área.",
                    "Clase ejecutiva: solo con aprobación del Gerente General.",
                ]),
            ]),
            ("5. Niveles de aprobación", [
                ("table", ["Monto total estimado del viaje", "Quién aprueba"], [
                    ["Hasta $500.000", "Jefatura directa"],
                    ["Desde $500.001 hasta $3.000.000", "Gerente de área"],
                    ["Más de $3.000.000", "Comité de Gastos Corporativos"],
                ]),
            ]),
            ("6. Rendición de gastos y reembolso", [
                ("ul", [
                    "La rendición se presenta dentro de los 7 días corridos posteriores al regreso.",
                    "Cada gasto debe tener boleta o factura; las facturas se emiten a nombre de Austral Bank.",
                    "Sin comprobante no hay reembolso.",
                    "El reembolso se paga dentro de 10 días hábiles desde que la rendición queda aprobada.",
                ]),
            ]),
            ("7. Gastos no reembolsables", [
                ("ul", [
                    "Minibar y servicios de entretenimiento del hotel.",
                    "Multas de tránsito.",
                    "Mejoras de categoría (upgrades) de carácter personal.",
                    "Gastos de acompañantes.",
                ]),
            ]),
            ("8. Qué no cubre este documento", [
                ("p", "Esta política no regula vacaciones, licencias médicas, teletrabajo ni capacitaciones externas. Para esos temas, consulta con Gestión de Personas."),
            ]),
        ],
    },
    {
        "file": "politica-uso-ia-generativa",
        "title": "Política de Uso de IA Generativa",
        "code": "POL-TI-007",
        "version": "1.3",
        "vigencia": "15-04-2026",
        "area": "Seguridad de la Información y Gobierno de Datos",
        "sections": [
            ("1. Objetivo y alcance", [
                ("p", "Esta política establece cómo las y los colaboradores de Austral Bank pueden usar herramientas de IA generativa para su trabajo, protegiendo la información de la institución y de sus clientes."),
            ]),
            ("2. Clasificación de la información", [
                ("table", ["Nivel", "Descripción", "Ejemplos"], [
                    ["Público", "Autorizada para difusión externa", "Comunicados de prensa, tasas publicadas"],
                    ["Interno", "Uso interno general", "Circulares, organigramas"],
                    ["Confidencial", "Su filtración puede dañar a Austral Bank", "Planes estratégicos, informes financieros previos a su publicación"],
                    ["Restringido", "Datos personales y financieros de clientes", "RUT, números de cuenta, saldos, claves, datos biométricos"],
                ]),
            ]),
            ("3. Herramientas aprobadas y nivel de información permitido", [
                ("table", ["Herramienta", "Niveles permitidos"], [
                    ["Austral Copilot Interno (herramienta corporativa con protección de datos)", "Público, Interno y Confidencial"],
                    ["Chatbots y asistentes de IA públicos (cuentas personales)", "Solo Público"],
                ]),
                ("p", "La información Restringida no puede ingresarse en ninguna herramienta de IA generativa, salvo en una solución aprobada explícitamente por el Comité de IA Responsable para ese caso de uso."),
            ]),
            ("4. Reglas de uso", [
                ("ul", [
                    "Anonimiza los datos antes de usarlos en cualquier herramienta de IA generativa (por ejemplo, reemplaza nombres, RUT y números de cuenta por marcadores).",
                    "Toda respuesta que se use en una comunicación a clientes o en una decisión sobre un cliente debe ser revisada por una persona antes de usarse.",
                    "Está prohibido tomar decisiones de crédito, bloqueo o cierre de productos basadas únicamente en IA generativa.",
                    "El contenido enviado a clientes externos que se haya preparado con IA debe incluir la etiqueta \"Generado con apoyo de IA\".",
                ]),
            ]),
            ("5. Nuevos casos de uso", [
                ("p", "Antes de iniciar un piloto, registra el caso de uso en el Registro de Casos de Uso de IA. El Comité de IA Responsable entrega la evaluación de riesgo en 10 días hábiles."),
            ]),
            ("6. Incidentes", [
                ("p", "Si detectas que se ingresó información Restringida o Confidencial en una herramienta no autorizada, repórtalo de inmediato y a más tardar dentro de 2 horas desde que lo detectes, al canal seguridad-informacion@austral-bank.example."),
            ]),
            ("7. Retención de historiales", [
                ("p", "Los historiales de conversación de Austral Copilot Interno se conservan por 90 días."),
            ]),
            ("8. Qué no cubre este documento", [
                ("p", "Esta política no regula la selección de proveedores de IA ni el desarrollo de modelos propios. Para esos temas, consulta con Gobierno de Datos."),
            ]),
        ],
    },
    {
        "file": "protocolo-atencion-reclamos",
        "title": "Protocolo de Atención de Reclamos",
        "code": "PRO-CL-003",
        "version": "3.0",
        "vigencia": "02-01-2026",
        "area": "Experiencia de Cliente",
        "sections": [
            ("1. Objetivo y alcance", [
                ("p", "Este protocolo define cómo se reciben, clasifican, resuelven y escalan los reclamos de clientes de Banca Personas de Austral Bank."),
            ]),
            ("2. Canales de recepción", [
                ("ul", [
                    "Sucursales.",
                    "Banca en línea.",
                    "App móvil.",
                    "Centro de Atención Telefónica: 600 000 0000 (número ficticio).",
                ]),
            ]),
            ("3. Registro y folio", [
                ("p", "Todo reclamo se registra en el momento del contacto y se entrega al cliente un folio con el formato REC-AAAA-NNNNNN."),
                ("p", "Nunca le pidas al cliente su clave, token ni sus coordenadas completas."),
            ]),
            ("4. Clasificación", [
                ("table", ["Nivel", "Tipo", "Ejemplo"], [
                    ["1", "Consulta", "Cómo descargar una cartola"],
                    ["2", "Reclamo", "Cobro de una comisión que el cliente no esperaba"],
                    ["3", "Fraude o riesgo reputacional", "Cargos no reconocidos, suplantación de identidad"],
                ]),
            ]),
            ("5. Plazos", [
                ("table", ["Nivel", "Acuse de recibo", "Respuesta"], [
                    ["1 - Consulta", "Inmediato", "En la misma atención o dentro de 2 días hábiles"],
                    ["2 - Reclamo", "1 día hábil", "Respuesta definitiva en 10 días hábiles"],
                    ["3 - Fraude", "Inmediato", "Evaluación inicial en 5 días hábiles"],
                ]),
                ("p", "En los casos de fraude se bloquea de inmediato el producto afectado. Para montos de hasta $300.000 se realiza un abono provisorio dentro de 3 días hábiles, mientras dura la investigación."),
            ]),
            ("6. Escalamiento", [
                ("ul", [
                    "Si vence el plazo sin resolución, el reclamo escala a la Jefatura de Experiencia de Cliente.",
                    "Si pasan más de 15 días hábiles, escala a la Gerencia de Experiencia de Cliente.",
                    "Los casos de Nivel 3 se derivan el mismo día a la Unidad de Prevención de Fraude, por el canal interno fraude@austral-bank.example.",
                ]),
            ]),
            ("7. Cierre y reapertura", [
                ("p", "La respuesta se entrega por el canal que el cliente eligió. El cliente puede reabrir el reclamo dentro de 30 días corridos desde el cierre."),
            ]),
            ("8. Qué no cubre este documento", [
                ("p", "Este protocolo no cubre reclamos de proveedores, temas laborales ni disputas legales."),
            ]),
        ],
    },
    {
        "file": "manual-onboarding-clientes",
        "title": "Manual de Onboarding de Clientes",
        "code": "MAN-ON-002",
        "version": "1.5",
        "vigencia": "01-02-2026",
        "area": "Banca Personas",
        "sections": [
            ("1. Objetivo y alcance", [
                ("p", "Este manual describe cómo se abre la relación con un cliente persona natural mayor de 18 años en Banca Personas de Austral Bank."),
            ]),
            ("2. Documentos requeridos", [
                ("table", ["Tipo de cliente", "Documentos"], [
                    ["Dependiente", "Cédula de identidad vigente (original); comprobante de domicilio con antigüedad máxima de 90 días; 3 últimas liquidaciones de sueldo"],
                    ["Independiente", "Cédula de identidad vigente (original); comprobante de domicilio con antigüedad máxima de 90 días; declaración anual de impuestos de los últimos 2 años"],
                ]),
            ]),
            ("3. Proceso de apertura en 5 pasos", [
                ("ol", [
                    "Validación de identidad con biometría.",
                    "Verificación en listas de control (sanciones y personas expuestas políticamente).",
                    "Perfil de riesgo y de necesidades del cliente.",
                    "Firma digital del contrato.",
                    "Activación de la Cuenta Austral Vista dentro de 24 horas hábiles.",
                ]),
            ]),
            ("4. Personas expuestas políticamente (PEP)", [
                ("p", "Si el cliente es una persona expuesta políticamente, se requiere la aprobación previa de Cumplimiento antes de abrir la cuenta. Mientras no exista esa aprobación, no se abre la cuenta."),
            ]),
            ("5. Productos iniciales", [
                ("ul", [
                    "Cuenta Austral Vista.",
                    "Tarjeta de débito.",
                    "Línea de crédito: disponible solo después de 90 días de antigüedad como cliente.",
                ]),
            ]),
            ("6. Tiempos de atención de referencia", [
                ("table", ["Modalidad", "Tiempo de referencia"], [
                    ["Digital", "15 minutos"],
                    ["Presencial", "40 minutos"],
                ]),
            ]),
            ("7. Qué no cubre este documento", [
                ("p", "Este manual no cubre cuentas para menores de edad, empresas ni personas no residentes."),
            ]),
        ],
    },
]


def md_table(header, rows):
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    lines += ["| " + " | ".join(r) + " |" for r in rows]
    return "\n".join(lines)


def render_md(doc):
    out = [f"# {doc['title']}", "",
           f"> {AVISO}.", "",
           "| Campo | Valor |", "|---|---|",
           f"| Código | {doc['code']} |",
           f"| Versión | {doc['version']} |",
           f"| Vigente desde | {doc['vigencia']} |",
           f"| Área responsable | {doc['area']} |",
           "| Clasificación | Interno |", ""]
    for heading, blocks in doc["sections"]:
        out += [f"## {heading}", ""]
        for b in blocks:
            if b[0] == "p":
                out += [b[1], ""]
            elif b[0] == "ul":
                out += [f"- {i}" for i in b[1]] + [""]
            elif b[0] == "ol":
                out += [f"{n}. {i}" for n, i in enumerate(b[1], 1)] + [""]
            elif b[0] == "table":
                out += [md_table(b[1], b[2]), ""]
    out += ["---", f"*{AVISO}.*", ""]
    return "\n".join(out)


def render_pdf(doc, path):
    navy = colors.HexColor("#0B2545")
    teal = colors.HexColor("#13808C")
    body = ParagraphStyle("body", fontName="Arial", fontSize=10, leading=14, spaceAfter=6)
    h1 = ParagraphStyle("h1", fontName="Arial-Bold", fontSize=18, leading=22, textColor=navy, spaceAfter=4)
    h2 = ParagraphStyle("h2", fontName="Arial-Bold", fontSize=12, leading=16, textColor=teal,
                        spaceBefore=10, spaceAfter=4, keepWithNext=1)
    cell = ParagraphStyle("cell", fontName="Arial", fontSize=9, leading=12)
    cellb = ParagraphStyle("cellb", fontName="Arial-Bold", fontSize=9, leading=12, textColor=colors.white)

    def footer(canvas, d):
        canvas.saveState()
        canvas.setFillColor(navy)
        canvas.rect(0, A4[1] - 1.2 * cm, A4[0], 1.2 * cm, stroke=0, fill=1)
        canvas.setFillColor(colors.white)
        canvas.setFont("Arial-Bold", 9)
        canvas.drawString(2 * cm, A4[1] - 0.8 * cm, "AUSTRAL BANK")
        canvas.setFont("Arial", 8)
        canvas.drawRightString(A4[0] - 2 * cm, A4[1] - 0.8 * cm, f"{doc['code']} · v{doc['version']}")
        canvas.setFillColor(colors.grey)
        canvas.setFont("Arial-Italic", 8)
        canvas.drawString(2 * cm, 1.1 * cm, AVISO)
        canvas.drawRightString(A4[0] - 2 * cm, 1.1 * cm, f"Página {d.page}")
        canvas.restoreState()

    story = [Paragraph(doc["title"], h1), Spacer(1, 4)]
    meta = [["Código", doc["code"], "Versión", doc["version"]],
            ["Vigente desde", doc["vigencia"], "Clasificación", "Interno"],
            ["Área responsable", doc["area"], "", ""]]
    mt = Table([[Paragraph(str(c), cell) for c in r] for r in meta],
               colWidths=[3.2 * cm, 6 * cm, 3 * cm, 4.8 * cm])
    mt.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.4, colors.lightgrey),
                            ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#EEF3F7")),
                            ("BACKGROUND", (2, 0), (2, 1), colors.HexColor("#EEF3F7")),
                            ("SPAN", (1, 2), (3, 2))]))
    story += [mt, Spacer(1, 6)]
    for heading, blocks in doc["sections"]:
        start = len(story)
        story.append(Paragraph(heading, h2))
        for b in blocks:
            if b[0] == "p":
                story.append(Paragraph(b[1], body))
            elif b[0] in ("ul", "ol"):
                items = [ListItem(Paragraph(i, body), leftIndent=14) for i in b[1]]
                story.append(ListFlowable(items, bulletType="bullet" if b[0] == "ul" else "1",
                                          start="•" if b[0] == "ul" else 1, leftIndent=14,
                                          bulletFontName="Arial", bulletFontSize=9))
            elif b[0] == "table":
                data = [[Paragraph(h, cellb) for h in b[1]]] + [[Paragraph(c, cell) for c in r] for r in b[2]]
                n = len(b[1])
                t = Table(data, colWidths=[17 * cm / n] * n, repeatRows=1)
                t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), teal),
                                       ("GRID", (0, 0), (-1, -1), 0.4, colors.lightgrey),
                                       ("VALIGN", (0, 0), (-1, -1), "TOP"),
                                       ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F8FA")])]))
                story += [t, Spacer(1, 6)]
        if len(story) >= start + 2:
            story[start:start + 2] = [KeepTogether(story[start:start + 2])]
    SimpleDocTemplate(str(path), pagesize=A4, leftMargin=2 * cm, rightMargin=2 * cm,
                      topMargin=2 * cm, bottomMargin=2 * cm, title=doc["title"],
                      author="Austral Bank (ficticio)", subject=AVISO).build(
        story, onFirstPage=footer, onLaterPages=footer)


if __name__ == "__main__":
    for d in DOCS:
        (OUT / f"{d['file']}.md").write_text(render_md(d), encoding="utf-8")
        render_pdf(d, OUT / f"{d['file']}.pdf")
        print("OK", d["file"])



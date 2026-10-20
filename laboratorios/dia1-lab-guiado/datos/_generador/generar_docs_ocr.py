# -*- coding: utf-8 -*-
"""Genera los 3 documentos ficticios para el Bloque C (Document Intelligence) y la demo en vivo.

Para cada documento produce:
  - NN-nombre.png               imagen con aspecto de escaneo
  - NN-nombre.pdf               PDF de solo imagen (escaneado)
  - pdf-texto-nativo/NN-nombre.pdf   PDF con capa de texto (para comparar)
y los archivos campos-esperados.csv y campos-esperados.md.

Uso:  python generar_docs_ocr.py
Requiere: pip install reportlab pymupdf pillow numpy
Todos los datos son ficticios. No incluyen datos reales de ninguna persona ni empresa.
"""
import csv
import random
from pathlib import Path

import numpy as np
import pymupdf
from PIL import Image, ImageFilter
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

OUT = Path(__file__).resolve().parent.parent / "documentos-ocr"
NATIVO = OUT / "pdf-texto-nativo"
NATIVO.mkdir(parents=True, exist_ok=True)

FONTS = Path("C:/Windows/Fonts")
for name, file in [("Arial", "arial.ttf"), ("Arial-Bold", "arialbd.ttf"),
                   ("Courier", "cour.ttf"), ("Courier-Bold", "courbd.ttf")]:
    pdfmetrics.registerFont(TTFont(name, str(FONTS / file)))

AVISO = "Documento ficticio para capacitación — Austral Bank"
W, H = A4
NAVY = colors.HexColor("#0B2545")
RED = colors.HexColor("#B3261E")


def watermark(c, w, h, size=54, angle=35):
    c.saveState()
    c.setFillColor(colors.Color(0.45, 0.45, 0.45))
    c.setFillAlpha(0.14)
    c.translate(w / 2, h / 2)
    c.rotate(angle)
    c.setFont("Arial-Bold", size)
    c.drawCentredString(0, 0, "DOCUMENTO FICTICIO")
    c.restoreState()


def txt(c, x, y, s, font="Arial", size=9, color=colors.black, align="l"):
    c.setFillColor(color)
    c.setFont(font, size)
    {"l": c.drawString, "r": c.drawRightString, "c": c.drawCentredString}[align](x, y, s)


# ---------------------------------------------------------------- 01 FACTURA
FACTURA = {
    "proveedor": "SUMINISTROS PACÍFICO SpA",
    "rut_prov": "76.111.222-3",
    "dir_prov": "Calle Ficticia 123, Oficina 4, Santiago, Chile",
    "numero": "F-000458",
    "emision": "05-10-2026",
    "vence": "04-11-2026",
    "pago": "30 días",
    "oc": "OC-2026-0731",
    "cliente": "AUSTRAL BANK S.A.",
    "rut_cli": "99.888.777-6",
    "dir_cli": "Avenida Ficticia 1000, Santiago",
    "items": [
        ("PAP-001", "Papel bond carta, resma 500 hojas", 40, 4500),
        ("TON-014", "Tóner láser negro compatible", 6, 38000),
        ("ARC-120", "Archivador de palanca, tamaño oficio", 50, 3200),
        ("SIL-300", "Silla ergonómica de oficina", 4, 98000),
        ("SRV-001", "Servicio de despacho e instalación", 1, 40000),
    ],
}


def clp(n):
    return "$" + f"{n:,}".replace(",", ".")


def dibujar_factura(c):
    f = FACTURA
    watermark(c, W, H)
    txt(c, 40, H - 58, f["proveedor"], "Arial-Bold", 15, NAVY)
    txt(c, 40, H - 74, "Venta al por mayor de artículos de oficina", "Arial", 8.5)
    txt(c, 40, H - 87, f["dir_prov"], "Arial", 8.5)
    txt(c, 40, H - 100, "Teléfono: +56 2 0000 0000 · ventas@suministros-pacifico.example", "Arial", 8.5)
    c.setStrokeColor(RED)
    c.setLineWidth(1.6)
    c.rect(375, H - 112, 180, 78)
    txt(c, 465, H - 56, f"R.U.T.: {f['rut_prov']}", "Arial-Bold", 11, RED, "c")
    txt(c, 465, H - 77, "FACTURA", "Arial-Bold", 15, RED, "c")
    txt(c, 465, H - 98, f"N° {f['numero']}", "Arial-Bold", 12, RED, "c")

    c.setStrokeColor(colors.black)
    c.setLineWidth(0.6)
    c.rect(40, H - 205, 515, 70)
    filas = [("Fecha de emisión:", f["emision"]), ("Fecha de vencimiento:", f["vence"]),
             ("Condición de pago:", f["pago"]), ("Orden de compra:", f["oc"])]
    for i, (k, v) in enumerate(filas):
        txt(c, 50, H - 152 - i * 15, k, "Arial-Bold", 9)
        txt(c, 160, H - 152 - i * 15, v, "Arial", 9)
    txt(c, 330, H - 152, "Moneda:", "Arial-Bold", 9)
    txt(c, 380, H - 152, "Peso chileno (CLP)", "Arial", 9)

    c.rect(40, H - 285, 515, 65)
    for i, (k, v) in enumerate([("Señor(es):", f["cliente"]), ("R.U.T.:", f["rut_cli"]),
                                ("Dirección:", f["dir_cli"]), ("Giro:", "Servicios financieros")]):
        txt(c, 50, H - 236 - i * 14, k, "Arial-Bold", 9)
        txt(c, 120, H - 236 - i * 14, v, "Arial", 9)

    y = H - 315
    c.setFillColor(NAVY)
    c.rect(40, y - 6, 515, 20, stroke=0, fill=1)
    for x, s, a in [(46, "Código", "l"), (110, "Descripción", "l"), (385, "Cant.", "r"),
                    (470, "P. Unitario", "r"), (550, "Total", "r")]:
        txt(c, x, y, s, "Arial-Bold", 9, colors.white, a)
    neto = 0
    y -= 22
    for cod, desc, cant, pu in f["items"]:
        total = cant * pu
        neto += total
        txt(c, 46, y, cod, "Arial", 9)
        txt(c, 110, y, desc, "Arial", 9)
        txt(c, 385, y, str(cant), "Arial", 9, align="r")
        txt(c, 470, y, clp(pu), "Arial", 9, align="r")
        txt(c, 550, y, clp(total), "Arial", 9, align="r")
        c.setStrokeColor(colors.Color(0.75, 0.75, 0.75))
        c.line(40, y - 6, 555, y - 6)
        y -= 20
    iva = round(neto * 0.19)
    c.setStrokeColor(colors.black)
    ty = y - 20
    c.rect(360, ty - 52, 195, 62)
    txt(c, 370, ty - 4, "Monto neto", "Arial", 9.5)
    txt(c, 545, ty - 4, clp(neto), "Arial", 9.5, align="r")
    txt(c, 370, ty - 20, "IVA (19%)", "Arial", 9.5)
    txt(c, 545, ty - 20, clp(iva), "Arial", 9.5, align="r")
    txt(c, 370, ty - 42, "TOTAL", "Arial-Bold", 11)
    txt(c, 545, ty - 42, clp(neto + iva), "Arial-Bold", 11, align="r")

    txt(c, 40, ty - 4, "Forma de pago: Transferencia bancaria", "Arial", 9)
    txt(c, 40, ty - 18, "Cuenta de destino: 000-000000-00 (ficticia)", "Arial", 9)
    txt(c, 40, ty - 32, "Observaciones: Entrega en bodega central.", "Arial", 9)

    rnd = random.Random(7)
    bx, by = 40, 70
    c.setFillColor(colors.black)
    x = bx
    while x < bx + 200:
        wbar = rnd.choice([0.8, 1.2, 1.8])
        c.rect(x, by, wbar, 38, stroke=0, fill=1)
        x += wbar + rnd.choice([0.8, 1.2, 1.8])
    txt(c, bx, by - 11, "TIMBRE ELECTRÓNICO (FICTICIO)", "Arial", 7)
    txt(c, W / 2, 28, AVISO, "Arial", 8, colors.grey, "c")
    return neto, iva


# ----------------------------------------------------------- 02 SOLICITUD
SOLICITUD = {
    "numero": "SOL-2026-004512",
    "fecha": "15-10-2026",
    "sucursal": "Sucursal Ficticia Centro",
    "nombre": "Camila Andrea Ejemplo Prueba",
    "rut": "12.345.678-5",
    "nacimiento": "14-03-1988",
    "estado_civil": "Soltera",
    "nacionalidad": "Chilena",
    "direccion": "Calle Ficticia 456, Depto 78, Comuna de Ejemplo",
    "telefono": "+56 9 0000 0000",
    "correo": "camila.ejemplo@correo.example",
    "empleador": "Servicios Demo Ltda.",
    "cargo": "Analista de Operaciones",
    "antiguedad": "4 años",
    "renta": "$1.450.000",
    "monto": "$6.000.000",
    "plazo": "36 meses",
    "destino": "Remodelación de vivienda",
    "cuota": "$198.000",
    "obligaciones": [
        ("Banco Demo", "Tarjeta de crédito", "$350.000", "$45.000"),
        ("Financiera Ejemplo", "Crédito automotriz", "$4.800.000", "$160.000"),
    ],
}


def campo(c, x, ytop, w, label, valor, h=30):
    c.setStrokeColor(colors.Color(0.35, 0.35, 0.35))
    c.setLineWidth(0.6)
    c.rect(x, H - ytop - h, w, h)
    txt(c, x + 4, H - ytop - 9, label, "Arial", 6.8, colors.Color(0.35, 0.35, 0.35))
    txt(c, x + 4, H - ytop - h + 7, valor, "Courier-Bold", 10)


def casilla(c, x, ytop, marcada, etiqueta):
    c.setStrokeColor(colors.black)
    c.setLineWidth(0.8)
    c.rect(x, H - ytop - 9, 9, 9)
    if marcada:
        c.setLineWidth(1.4)
        c.line(x + 1.5, H - ytop - 7.5, x + 7.5, H - ytop - 1.5)
        c.line(x + 1.5, H - ytop - 1.5, x + 7.5, H - ytop - 7.5)
    txt(c, x + 14, H - ytop - 8, etiqueta, "Arial", 8.5)


def seccion(c, ytop, titulo):
    c.setFillColor(colors.HexColor("#E3EAF2"))
    c.rect(40, H - ytop - 15, 515, 15, stroke=0, fill=1)
    txt(c, 46, H - ytop - 11, titulo, "Arial-Bold", 9, NAVY)


def dibujar_solicitud(c):
    s = SOLICITUD
    watermark(c, W, H, 54, 38)
    c.setFillColor(NAVY)
    c.rect(0, H - 62, W, 62, stroke=0, fill=1)
    txt(c, 40, H - 32, "AUSTRAL BANK", "Arial-Bold", 17, colors.white)
    txt(c, 555, H - 28, "SOLICITUD DE CRÉDITO DE CONSUMO", "Arial-Bold", 12, colors.white, "r")
    txt(c, 555, H - 44, "Formulario SCC-01 · Banca Personas", "Arial", 8.5, colors.white, "r")
    campo(c, 40, 72, 150, "N° de solicitud", s["numero"], 28)
    campo(c, 195, 72, 120, "Fecha de solicitud", s["fecha"], 28)
    campo(c, 320, 72, 235, "Sucursal", s["sucursal"], 28)

    seccion(c, 110, "1. DATOS DEL SOLICITANTE")
    campo(c, 40, 129, 345, "Nombre completo", s["nombre"])
    campo(c, 390, 129, 165, "RUT", s["rut"])
    campo(c, 40, 163, 150, "Fecha de nacimiento", s["nacimiento"])
    campo(c, 195, 163, 150, "Estado civil", s["estado_civil"])
    campo(c, 350, 163, 205, "Nacionalidad", s["nacionalidad"])
    campo(c, 40, 197, 345, "Dirección", s["direccion"])
    campo(c, 390, 197, 165, "Teléfono", s["telefono"])
    campo(c, 40, 231, 515, "Correo electrónico", s["correo"])

    seccion(c, 272, "2. DATOS LABORALES")
    campo(c, 40, 291, 270, "Empleador", s["empleador"])
    campo(c, 315, 291, 240, "Cargo", s["cargo"])
    campo(c, 40, 325, 120, "Antigüedad laboral", s["antiguedad"])
    campo(c, 165, 325, 160, "Renta líquida mensual", s["renta"])
    txt(c, 335, H - 335, "Tipo de contrato", "Arial", 6.8, colors.Color(0.35, 0.35, 0.35))
    casilla(c, 335, 342, True, "Indefinido")
    casilla(c, 405, 342, False, "Plazo fijo")
    casilla(c, 478, 342, False, "Honorarios")

    seccion(c, 366, "3. CRÉDITO SOLICITADO")
    campo(c, 40, 385, 150, "Monto solicitado", s["monto"])
    campo(c, 195, 385, 110, "Plazo", s["plazo"])
    campo(c, 310, 385, 245, "Destino del crédito", s["destino"])
    campo(c, 40, 419, 150, "Cuota mensual estimada", s["cuota"])

    seccion(c, 458, "4. OBLIGACIONES VIGENTES")
    cols = [(40, 160, "Institución"), (200, 140, "Tipo de obligación"), (340, 110, "Saldo"), (450, 105, "Cuota mensual")]
    y = 478
    for x, w, t in cols:
        c.setStrokeColor(colors.Color(0.35, 0.35, 0.35))
        c.rect(x, H - y - 16, w, 16)
        txt(c, x + 4, H - y - 11, t, "Arial-Bold", 8)
    filas = list(s["obligaciones"]) + [("", "", "", "")]
    for i, fila in enumerate(filas):
        yy = y + 16 + i * 20
        for (x, w, _), v in zip(cols, fila):
            c.rect(x, H - yy - 20, w, 20)
            txt(c, x + 4, H - yy - 14, v, "Courier-Bold", 9.5)

    seccion(c, 575, "5. DECLARACIONES")
    casilla(c, 46, 598, True, "Declaro que la información entregada en esta solicitud es verídica.")
    casilla(c, 46, 616, True, "Autorizo la consulta de mis antecedentes comerciales.")
    casilla(c, 46, 634, False, "Deseo recibir ofertas comerciales por correo electrónico.")

    c.setStrokeColor(colors.black)
    c.setLineWidth(0.7)
    c.line(60, H - 722, 280, H - 722)
    p = c.beginPath()
    p.moveTo(75, H - 712)
    for dx, dy in [(95, 690), (112, 716), (130, 686), (150, 718), (172, 690), (195, 712), (225, 698), (252, 708)]:
        p.lineTo(dx, H - dy)
    c.setLineWidth(1.3)
    c.drawPath(p, stroke=1, fill=0)
    txt(c, 60, H - 734, "Firma del solicitante (firma ficticia)", "Arial", 8)
    txt(c, 340, H - 716, "Fecha de firma:", "Arial", 8.5)
    txt(c, 420, H - 716, s["fecha"], "Courier-Bold", 10)
    txt(c, W / 2, 28, AVISO, "Arial", 8, colors.grey, "c")


# -------------------------------------------------------- 03 COMPROBANTE
RW, RH = 226, 402
BOLETA = {
    "comercio": "CAFÉ AUSTRAL EXPRESS",
    "razon": "Comercial Demo SpA",
    "rut": "76.555.444-3",
    "direccion": "Av. Ficticia 321, Local 2",
    "ciudad": "Santiago",
    "numero": "004871",
    "fecha": "17-10-2026",
    "hora": "12:42",
    "items": [(2, "Café americano grande", 5600), (1, "Sándwich ave palta", 5900),
              (1, "Jugo natural naranja", 3200)],
}


def dibujar_boleta(c):
    b = BOLETA
    watermark(c, RW, RH, 27, 55)
    y = RH - 28

    def linea(s, font="Courier", size=8.5, align="c", x=None):
        nonlocal y
        xx = x if x is not None else (RW / 2 if align == "c" else 12)
        txt(c, xx, y, s, font, size, align=align)
        y -= size + 4

    def sep():
        linea("-" * 34, size=8)

    linea(b["comercio"], "Courier-Bold", 11)
    linea(b["razon"])
    linea(f"RUT {b['rut']} (ficticio)")
    linea(b["direccion"])
    linea(f"{b['ciudad']} · Tel. +56 2 0000 0000")
    sep()
    linea("COMPROBANTE DE COMPRA", "Courier-Bold", 9)
    linea(f"N° {b['numero']}", "Courier-Bold", 9)
    linea(f"Fecha: {b['fecha']}   Hora: {b['hora']}")
    linea("Caja: 02    Atendió: Cajero 03")
    sep()
    txt(c, 12, y, "CANT DESCRIPCIÓN", "Courier", 8)
    txt(c, RW - 12, y, "TOTAL", "Courier", 8, align="r")
    y -= 12
    total = 0
    for cant, desc, monto in b["items"]:
        total += monto
        txt(c, 12, y, f"{cant:<3}{desc[:21]:<22}", "Courier", 8)
        txt(c, RW - 12, y, clp(monto), "Courier", 8, align="r")
        y -= 12
    sep()
    neto = round(total / 1.19)
    iva = total - neto
    for k, v, bold in [("SUBTOTAL (neto)", neto, False), ("IVA 19% incluido", iva, False), ("TOTAL", total, True)]:
        font = "Courier-Bold" if bold else "Courier"
        txt(c, 12, y, k, font, 9 if bold else 8.5)
        txt(c, RW - 12, y, clp(v), font, 9 if bold else 8.5, align="r")
        y -= 13
    sep()
    linea("Pago: Tarjeta de crédito")
    linea("Tarjeta: **** **** **** 0000")
    linea("Aprobación: 000000")
    y -= 6
    linea("¡Gracias por tu compra!", "Courier-Bold", 9)
    linea("Propina no incluida")
    y -= 4
    linea("DOCUMENTO FICTICIO", "Courier-Bold", 8)
    linea("PARA CAPACITACIÓN", "Courier-Bold", 8)
    return total, neto, iva


# ----------------------------------------------------------------- SCAN
def scanify(img, angle, seed, sombra=0.10, ruido=7.0, desenfoque=0.55):
    rnd = np.random.default_rng(seed)
    g = img.convert("L")
    g = g.rotate(angle, resample=Image.BICUBIC, expand=True, fillcolor=250)
    g = g.filter(ImageFilter.GaussianBlur(desenfoque))
    a = np.asarray(g, dtype=np.float32)
    h, w = a.shape
    a = 18 + a * (0.93 - 0.0)  # papel levemente gris, texto no totalmente negro
    grad = np.linspace(1 - sombra, 1.0, w, dtype=np.float32)[None, :]
    a = a * grad
    a += rnd.normal(0, ruido, a.shape).astype(np.float32)
    for _ in range(45):
        x, y = rnd.integers(0, w), rnd.integers(0, h)
        r = int(rnd.integers(1, 3))
        a[max(0, y - r):y + r, max(0, x - r):x + r] -= rnd.uniform(25, 70)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "L")


def exportar(nombre, dibujar, size, dpi, angle, seed, **kw):
    nativo = NATIVO / f"{nombre}.pdf"
    c = canvas.Canvas(str(nativo), pagesize=size)
    c.setTitle(nombre)
    c.setAuthor("Austral Bank (ficticio)")
    c.setSubject(AVISO)
    res = dibujar(c)
    c.showPage()
    c.save()
    pix = pymupdf.open(str(nativo))[0].get_pixmap(dpi=dpi, alpha=False)
    base = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    scan = scanify(base, angle, seed, **kw)
    scan.save(OUT / f"{nombre}.png", optimize=True)
    scan.save(OUT / f"{nombre}.pdf", "PDF", resolution=dpi, quality=85)
    return res


def csv_y_md(neto, iva, total_f, total_b, neto_b, iva_b):
    f, s, b = FACTURA, SOLICITUD, BOLETA
    inv = "prebuilt-invoice"
    rows = [
        # (doc, modelo, campo DI / clave, etiqueta en el documento, valor esperado, nota)
        ("01-factura", inv, "VendorName", "Encabezado", "Suministros Pacífico SpA", "Puede devolverse en mayúsculas, como en el documento"),
        ("01-factura", inv, "VendorTaxId", "R.U.T. (recuadro)", f["rut_prov"], "RUT ficticio"),
        ("01-factura", inv, "VendorAddress", "Dirección del proveedor", f["dir_prov"], "Revisar separación en calle / comuna"),
        ("01-factura", inv, "InvoiceId", "N°", f["numero"], ""),
        ("01-factura", inv, "InvoiceDate", "Fecha de emisión", "2026-10-05", "El formato del documento es dd-mm-aaaa; la API devuelve fecha ISO. Verifica que no invierta día y mes"),
        ("01-factura", inv, "DueDate", "Fecha de vencimiento", "2026-11-04", "Ídem"),
        ("01-factura", inv, "PaymentTerm", "Condición de pago", f["pago"], "Puede no extraerse (campo opcional)"),
        ("01-factura", inv, "PurchaseOrder", "Orden de compra", f["oc"], ""),
        ("01-factura", inv, "CustomerName", "Señor(es)", f["cliente"], ""),
        ("01-factura", inv, "CustomerTaxId", "R.U.T. del cliente", f["rut_cli"], "RUT ficticio"),
        ("01-factura", inv, "CustomerAddress", "Dirección del cliente", f["dir_cli"], ""),
        ("01-factura", inv, "SubTotal", "Monto neto", clp(neto), "Verifica cómo representa la API los montos en CLP (separador de miles con punto, sin decimales)"),
        ("01-factura", inv, "TotalTax", "IVA (19%)", clp(iva), "Ídem"),
        ("01-factura", inv, "InvoiceTotal", "TOTAL", clp(total_f), "Debe cumplir: SubTotal + TotalTax = InvoiceTotal"),
        ("01-factura", inv, "Items (cantidad de líneas)", "Tabla de detalle", str(len(f["items"])), "Revisa descripción, cantidad, precio unitario y monto por línea"),
    ]
    for i, (cod, desc, cant, pu) in enumerate(f["items"], 1):
        rows.append(("01-factura", inv, f"Items[{i}]", f"{cod} · {desc}", f"{cant} × {clp(pu)} = {clp(cant * pu)}", ""))
    lay = "Layout + keyValuePairs"
    pares = [
        ("N° de solicitud", s["numero"]), ("Fecha de solicitud", s["fecha"]), ("Sucursal", s["sucursal"]),
        ("Nombre completo", s["nombre"]), ("RUT", s["rut"]), ("Fecha de nacimiento", s["nacimiento"]),
        ("Estado civil", s["estado_civil"]), ("Nacionalidad", s["nacionalidad"]), ("Dirección", s["direccion"]),
        ("Teléfono", s["telefono"]), ("Correo electrónico", s["correo"]), ("Empleador", s["empleador"]),
        ("Cargo", s["cargo"]), ("Antigüedad laboral", s["antiguedad"]), ("Renta líquida mensual", s["renta"]),
        ("Monto solicitado", s["monto"]), ("Plazo", s["plazo"]), ("Destino del crédito", s["destino"]),
        ("Cuota mensual estimada", s["cuota"]),
    ]
    for k, v in pares:
        rows.append(("02-solicitud-credito", lay, "Par clave-valor", k, v, "Se espera detectar la mayoría; no necesariamente todos"))
    rows += [
        ("02-solicitud-credito", lay, "Selection mark", "Tipo de contrato: Indefinido", "selected", "Layout detecta casillas (selected / unselected)"),
        ("02-solicitud-credito", lay, "Selection mark", "Tipo de contrato: Plazo fijo / Honorarios", "unselected", ""),
        ("02-solicitud-credito", lay, "Selection mark", "Declaro que la información ... es verídica", "selected", ""),
        ("02-solicitud-credito", lay, "Selection mark", "Autorizo la consulta de mis antecedentes comerciales", "selected", ""),
        ("02-solicitud-credito", lay, "Selection mark", "Deseo recibir ofertas comerciales ...", "unselected", ""),
        ("02-solicitud-credito", lay, "Tabla", "Obligaciones vigentes (4 columnas)", "2 filas con datos + 1 fila vacía", "Revisa que la tabla se reconozca como tabla"),
    ]
    for ins, tipo, saldo, cuota in s["obligaciones"]:
        rows.append(("02-solicitud-credito", lay, "Tabla: fila", "Obligaciones vigentes", f"{ins} | {tipo} | {saldo} | {cuota}", ""))
    rc = "prebuilt-receipt"
    rows += [
        ("03-comprobante-compra", rc, "MerchantName", "Encabezado", "Café Austral Express", "Puede devolverse en mayúsculas"),
        ("03-comprobante-compra", rc, "MerchantAddress", "Dirección", "Av. Ficticia 321, Local 2, Santiago", ""),
        ("03-comprobante-compra", rc, "TransactionDate", "Fecha", "2026-10-17", ""),
        ("03-comprobante-compra", rc, "TransactionTime", "Hora", "12:42:00", ""),
        ("03-comprobante-compra", rc, "Subtotal", "SUBTOTAL (neto)", clp(neto_b), "Puede no extraerse"),
        ("03-comprobante-compra", rc, "TotalTax", "IVA 19% incluido", clp(iva_b), ""),
        ("03-comprobante-compra", rc, "Total", "TOTAL", clp(total_b), "Campo clave; debe cumplir: suma de ítems = Total"),
    ]
    for cant, desc, monto in b["items"]:
        rows.append(("03-comprobante-compra", rc, "Items", f"{cant} × {desc}", clp(monto), ""))

    cab = ["documento", "modelo_recomendado", "campo_o_clave", "etiqueta_en_documento", "valor_esperado", "nota"]
    with open(OUT / "campos-esperados.csv", "w", newline="", encoding="utf-8-sig") as fh:
        w = csv.writer(fh)
        w.writerow(cab)
        w.writerows(rows)

    md = ["# Campos esperados — Documentos ficticios del Bloque C y de la demo en vivo", "",
          "> Documentos y datos **ficticios**. Sirven para que el equipo facilitador verifique los resultados de Document Intelligence. "
          "Los valores esperados son los que están impresos en el documento; la API puede normalizarlos "
          "(fechas en formato ISO, montos como número + moneda). **Compara el significado, no el formato exacto.**", "",
          "**Criterio de aceptación sugerido:** campos clave de la factura (VendorName, InvoiceId, InvoiceDate, InvoiceTotal) correctos y con confianza ≥ 0,80; "
          "en la solicitud, al menos ~80 % de los pares clave-valor detectados; en el comprobante, Total y fecha correctos.", ""]
    docs = [("01-factura", "01 · Factura (modelo `prebuilt-invoice`, locale `es-CL`)", "Archivos: `01-factura.png`, `01-factura.pdf` (escaneado) y `pdf-texto-nativo/01-factura.pdf`."),
            ("02-solicitud-credito", "02 · Solicitud de crédito de consumo (modelo **Layout** con la opción `keyValuePairs`)", "Archivos: `02-solicitud-credito.png`, `02-solicitud-credito.pdf` y `pdf-texto-nativo/02-solicitud-credito.pdf`. En Document Intelligence Studio, activa los pares clave-valor desde *Analyze options* del modelo Layout (el nombre exacto puede variar)."),
            ("03-comprobante-compra", "03 · Comprobante de compra (modelo `prebuilt-receipt`) — demo en vivo de los facilitadores y extensión del Bloque C", "Archivos: `03-comprobante-compra.png`, `03-comprobante-compra.pdf` y `pdf-texto-nativo/03-comprobante-compra.pdf`.")]
    for key, titulo, nota in docs:
        md += [f"## {titulo}", "", nota, "", "| Campo / clave | Etiqueta en el documento | Valor esperado | Nota |", "|---|---|---|---|"]
        for r in rows:
            if r[0] == key:
                md.append(f"| {r[2]} | {r[3]} | {r[4]} | {r[5]} |")
        md.append("")
    md += ["## Observaciones para el equipo facilitador", "",
           "- Los tres documentos llevan la marca de agua diagonal **DOCUMENTO FICTICIO**. Es normal que aparezca como texto en la pestaña *Content*; no es un campo del documento.",
           "- `prebuilt-invoice` lista monedas como USD, EUR, BRL, etc.; **CLP no figura entre los códigos documentados**. Verifica en vivo cómo devuelve los montos en pesos (valor, símbolo y código de moneda). Es un buen punto de discusión con el grupo.",
           "- Los PDF de `pdf-texto-nativo` tienen capa de texto; los PDF/PNG principales son solo imagen. Comparar ambos muestra el valor del OCR.",
           "- Un cheque no se incluyó a propósito: el modelo `prebuilt-check.us` solo admite documentos de EE. UU. (en-US).",
           "- Todos los datos (RUT, direcciones, teléfonos, cuentas) son inventados. No contienen información real de personas, empresas ni de BCI.", ""]
    (OUT / "campos-esperados.md").write_text("\n".join(md), encoding="utf-8")
    return len(rows)


if __name__ == "__main__":
    neto, iva = exportar("01-factura", dibujar_factura, A4, 150, 0.7, 11)
    exportar("02-solicitud-credito", dibujar_solicitud, A4, 150, -0.9, 12)
    total_b, neto_b, iva_b = exportar("03-comprobante-compra", dibujar_boleta, (RW, RH), 220, 1.6, 13,
                                      sombra=0.06, ruido=6.0, desenfoque=0.5)
    n = csv_y_md(neto, iva, neto + iva, total_b, neto_b, iva_b)
    print("OK. Campos esperados:", n, "| neto", neto, "iva", iva, "total", neto + iva)

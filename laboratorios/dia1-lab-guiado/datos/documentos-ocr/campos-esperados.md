# Campos esperados — Documentos ficticios del Bloque C y de la demo en vivo

> Documentos y datos **ficticios**. Sirven para que el equipo facilitador verifique los resultados de Document Intelligence. Los valores esperados son los que están impresos en el documento; la API puede normalizarlos (fechas en formato ISO, montos como número + moneda). **Compara el significado, no el formato exacto.**

**Criterio de aceptación sugerido:** campos clave de la factura (VendorName, InvoiceId, InvoiceDate, InvoiceTotal) correctos y con confianza ≥ 0,80; en la solicitud, al menos ~80 % de los pares clave-valor detectados; en el comprobante, Total y fecha correctos.

## 01 · Factura (modelo `prebuilt-invoice`, locale `es-CL`)

Archivos: `01-factura.png`, `01-factura.pdf` (escaneado) y `pdf-texto-nativo/01-factura.pdf`.

| Campo / clave | Etiqueta en el documento | Valor esperado | Nota |
|---|---|---|---|
| VendorName | Encabezado | Suministros Pacífico SpA | Puede devolverse en mayúsculas, como en el documento |
| VendorTaxId | R.U.T. (recuadro) | 76.111.222-3 | RUT ficticio |
| VendorAddress | Dirección del proveedor | Calle Ficticia 123, Oficina 4, Santiago, Chile | Revisar separación en calle / comuna |
| InvoiceId | N° | F-000458 |  |
| InvoiceDate | Fecha de emisión | 2026-10-05 | El formato del documento es dd-mm-aaaa; la API devuelve fecha ISO. Verifica que no invierta día y mes |
| DueDate | Fecha de vencimiento | 2026-11-04 | Ídem |
| PaymentTerm | Condición de pago | 30 días | Puede no extraerse (campo opcional) |
| PurchaseOrder | Orden de compra | OC-2026-0731 |  |
| CustomerName | Señor(es) | AUSTRAL BANK S.A. |  |
| CustomerTaxId | R.U.T. del cliente | 99.888.777-6 | RUT ficticio |
| CustomerAddress | Dirección del cliente | Avenida Ficticia 1000, Santiago |  |
| SubTotal | Monto neto | $1.000.000 | Verifica cómo representa la API los montos en CLP (separador de miles con punto, sin decimales) |
| TotalTax | IVA (19%) | $190.000 | Ídem |
| InvoiceTotal | TOTAL | $1.190.000 | Debe cumplir: SubTotal + TotalTax = InvoiceTotal |
| Items (cantidad de líneas) | Tabla de detalle | 5 | Revisa descripción, cantidad, precio unitario y monto por línea |
| Items[1] | PAP-001 · Papel bond carta, resma 500 hojas | 40 × $4.500 = $180.000 |  |
| Items[2] | TON-014 · Tóner láser negro compatible | 6 × $38.000 = $228.000 |  |
| Items[3] | ARC-120 · Archivador de palanca, tamaño oficio | 50 × $3.200 = $160.000 |  |
| Items[4] | SIL-300 · Silla ergonómica de oficina | 4 × $98.000 = $392.000 |  |
| Items[5] | SRV-001 · Servicio de despacho e instalación | 1 × $40.000 = $40.000 |  |

## 02 · Solicitud de crédito de consumo (modelo **Layout** con la opción `keyValuePairs`)

Archivos: `02-solicitud-credito.png`, `02-solicitud-credito.pdf` y `pdf-texto-nativo/02-solicitud-credito.pdf`. En Document Intelligence Studio, activa los pares clave-valor desde *Analyze options* del modelo Layout (el nombre exacto puede variar).

| Campo / clave | Etiqueta en el documento | Valor esperado | Nota |
|---|---|---|---|
| Par clave-valor | N° de solicitud | SOL-2026-004512 | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Fecha de solicitud | 15-10-2026 | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Sucursal | Sucursal Ficticia Centro | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Nombre completo | Camila Andrea Ejemplo Prueba | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | RUT | 12.345.678-5 | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Fecha de nacimiento | 14-03-1988 | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Estado civil | Soltera | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Nacionalidad | Chilena | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Dirección | Calle Ficticia 456, Depto 78, Comuna de Ejemplo | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Teléfono | +56 9 0000 0000 | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Correo electrónico | camila.ejemplo@correo.example | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Empleador | Servicios Demo Ltda. | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Cargo | Analista de Operaciones | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Antigüedad laboral | 4 años | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Renta líquida mensual | $1.450.000 | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Monto solicitado | $6.000.000 | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Plazo | 36 meses | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Destino del crédito | Remodelación de vivienda | Se espera detectar la mayoría; no necesariamente todos |
| Par clave-valor | Cuota mensual estimada | $198.000 | Se espera detectar la mayoría; no necesariamente todos |
| Selection mark | Tipo de contrato: Indefinido | selected | Layout detecta casillas (selected / unselected) |
| Selection mark | Tipo de contrato: Plazo fijo / Honorarios | unselected |  |
| Selection mark | Declaro que la información ... es verídica | selected |  |
| Selection mark | Autorizo la consulta de mis antecedentes comerciales | selected |  |
| Selection mark | Deseo recibir ofertas comerciales ... | unselected |  |
| Tabla | Obligaciones vigentes (4 columnas) | 2 filas con datos + 1 fila vacía | Revisa que la tabla se reconozca como tabla |
| Tabla: fila | Obligaciones vigentes | Banco Demo | Tarjeta de crédito | $350.000 | $45.000 |  |
| Tabla: fila | Obligaciones vigentes | Financiera Ejemplo | Crédito automotriz | $4.800.000 | $160.000 |  |

## 03 · Comprobante de compra (modelo `prebuilt-receipt`) — demo en vivo de los facilitadores y extensión del Bloque C

Archivos: `03-comprobante-compra.png`, `03-comprobante-compra.pdf` y `pdf-texto-nativo/03-comprobante-compra.pdf`.

| Campo / clave | Etiqueta en el documento | Valor esperado | Nota |
|---|---|---|---|
| MerchantName | Encabezado | Café Austral Express | Puede devolverse en mayúsculas |
| MerchantAddress | Dirección | Av. Ficticia 321, Local 2, Santiago |  |
| TransactionDate | Fecha | 2026-10-17 |  |
| TransactionTime | Hora | 12:42:00 |  |
| Subtotal | SUBTOTAL (neto) | $12.353 | Puede no extraerse |
| TotalTax | IVA 19% incluido | $2.347 |  |
| Total | TOTAL | $14.700 | Campo clave; debe cumplir: suma de ítems = Total |
| Items | 2 × Café americano grande | $5.600 |  |
| Items | 1 × Sándwich ave palta | $5.900 |  |
| Items | 1 × Jugo natural naranja | $3.200 |  |

## Observaciones para el equipo facilitador

- Los tres documentos llevan la marca de agua diagonal **DOCUMENTO FICTICIO**. Es normal que aparezca como texto en la pestaña *Content*; no es un campo del documento.
- `prebuilt-invoice` lista monedas como USD, EUR, BRL, etc.; **CLP no figura entre los códigos documentados**. Verifica en vivo cómo devuelve los montos en pesos (valor, símbolo y código de moneda). Es un buen punto de discusión con el grupo.
- Los PDF de `pdf-texto-nativo` tienen capa de texto; los PDF/PNG principales son solo imagen. Comparar ambos muestra el valor del OCR.
- Un cheque no se incluyó a propósito: el modelo `prebuilt-check.us` solo admite documentos de EE. UU. (en-US).
- Todos los datos (RUT, direcciones, teléfonos, cuentas) son inventados. No contienen información real de personas, empresas ni de BCI.

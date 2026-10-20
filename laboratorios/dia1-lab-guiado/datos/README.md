# datos\ — Material ficticio del laboratorio Día 1

Todo el contenido es **ficticio** (Austral Bank). No incluye datos reales de ninguna institución, personas reales, claves ni endpoints.

| Carpeta / archivo | Para qué sirve | Bloque |
|---|---|---|
| `prompts.md` | Texto de las instrucciones del agente, preguntas de prueba con el comportamiento esperado y prompts de comparación | B, C |
| `politicas-internas\` | 4 documentos de política (`.md` y `.pdf`, mismo contenido) para subir a **file search**. Sube un solo formato | B |
| `documentos-ocr\` | 3 documentos con aspecto de escaneo (`.png` y `.pdf` de solo imagen) con la marca de agua **DOCUMENTO FICTICIO** | C (y demo en vivo) |
| `documentos-ocr\pdf-texto-nativo\` | Los mismos 3 documentos como PDF con capa de texto (para comparar con el escaneo) | C (extensión) |
| `documentos-ocr\campos-esperados.md` / `.csv` | Valores correctos de cada campo, para validar el resultado de Document Intelligence | C (y demo en vivo) |
| `_generador\` | Scripts de Python que generan los documentos (para facilitadores; no son parte del laboratorio) | — |

## Políticas internas (carpeta `politicas-internas\`)

| Archivo | Código | Tema |
|---|---|---|
| `politica-gastos-de-viaje` | POL-GV-001 | Anticipación, topes, aprobaciones y rendición de viajes |
| `politica-uso-ia-generativa` | POL-TI-007 | Uso permitido de IA generativa según nivel de clasificación |
| `protocolo-atencion-reclamos` | PRO-CL-003 | Niveles, plazos y escalamiento de reclamos y fraude |
| `manual-onboarding-clientes` | MAN-ON-002 | Documentos y pasos para abrir una cuenta |

Los documentos **no cubren** las vacaciones ni otros temas de personas: se usa a propósito para comprobar que el agente dice "no encuentro esa información" y no inventa.

## Documentos para OCR (carpeta `documentos-ocr\`)

| Archivo | Documento | Modelo sugerido |
|---|---|---|
| `01-factura` | Factura F-000458 de un proveedor ficticio a Austral Bank | Invoice |
| `02-solicitud-credito` | Solicitud de crédito de consumo SOL-2026-004512 (formulario) | Layout con pares clave-valor |
| `03-comprobante-compra` | Comprobante de una cafetería ficticia (demo en vivo de los facilitadores; extensión del Bloque C) | Receipt |

Todos pesan menos de 2 MB y tienen 1 página (cumplen los límites del nivel gratuito F0: 4 MB y 2 páginas).

## Regenerar los archivos (opcional)

Requiere Python 3.10+ y los paquetes `reportlab`, `pymupdf`, `pillow` y `numpy`:

```
python datos\_generador\generar_politicas.py
python datos\_generador\generar_docs_ocr.py
```

Los scripts usan fuentes del sistema Windows y semillas fijas, por lo que el resultado es repetible.

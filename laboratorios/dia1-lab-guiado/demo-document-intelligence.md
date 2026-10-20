# Demo en vivo de Document Intelligence (≈10 min) — Guion del facilitador

**Microsoft AI Foundry BCI Training Day** · Día 1 · Miércoles 21 de octubre de 2026 · módulo **Azure AI Services** (10:15–10:55, hora de Chile)

> Todo el material usa la institución **ficticia Austral Bank**. El documento de la demo es un comprobante inventado. No muestres claves, TAP, endpoints ni tu correo en pantalla.

---

## 1. Propósito

Mostrar en vivo, con un documento real de solo imagen (escaneo), la diferencia entre:

1. **OCR / lectura** (Read o Layout): devuelve texto, líneas, tablas y estructura, pero no sabe qué significa cada dato.
2. **Extracción estructurada** (modelo prebuilt **Receipt**): devuelve campos con nombre, tipo, valor y **confianza** (confidence).

La demo prepara a los participantes para el **Bloque C** del laboratorio (donde ellos mismos hacen OCR con **Invoice** y **Layout**) y deja la semilla para el Día 2: un agente puede usar **tools** para actuar sobre estos datos.

**Por qué este documento:** el laboratorio de los participantes usa `01-factura` (modelo **Invoice**) y `02-solicitud-credito` (modelo **Layout**) (README del Día 1, sección 8). El archivo `03-comprobante-compra` solo aparece allí como extensión opcional. La demo usa el 03 para que nadie haya visto el resultado antes del Bloque C.

## 2. Tiempo y roles

| Dato | Valor |
|---|---|
| Momento | Dentro del módulo **Azure AI Services**, ≈**10:40–10:50** (módulo: 10:15–10:55) |
| Duración | ≈10 min (8 min de demo + 2 min de puente al laboratorio) |
| Presenta | La persona que dicta el módulo Azure AI Services (en el runbook: Valentina; **por confirmar**) |
| Apoyo | Segundo facilitador: monitorea el chat de Teams y tiene abierto el Plan B (sección 7) |
| Cuenta de demo | Una cuenta de instructor `instNN` con su TAP (cuál: **por confirmar**) |

## 3. Prerrequisitos (verifícalos en el pre-flight T-30, y deja todo abierto antes de las 10:15)

| # | Requisito | Detalle |
|---|---|---|
| 1 | Document Intelligence Studio | `https://documentintelligence.ai.azure.com` (el laboratorio oficial usa `https://contentunderstanding.ai.azure.com/documentintelligence/studio`: es el mismo servicio con otra dirección). Ten **ambas pestañas probadas** |
| 2 | Recurso seleccionado en Studio | **Settings** (engranaje) > pestaña **Resource**. Autenticación con **Microsoft Entra ID**. Qué recurso de Document Intelligence/Foundry usa la cuenta de demo: **por confirmar** |
| 3 | Rol | **Cognitive Services User** sobre ese recurso. El aprovisionamiento actual solo asigna Foundry User + Reader: **por confirmar** en la prueba de humo (ver `checklist-validacion.md`) |
| 4 | Cookies de terceros permitidas | Si no, aparece el error **AADSTS50058** al abrir Studio |
| 5 | Sesión iniciada con TAP | El TAP del día solo es válido el 21 de octubre de 06:30 a 14:30 (hora de Chile). Si aparece **AADSTS50079/50076**, no estás usando el TAP: elige **Use a Temporary Access Pass instead** |
| 6 | Archivo de la demo | `datos\documentos-ocr\03-comprobante-compra.pdf` (210 KB; solo imagen) en una carpeta fácil de abrir. Respaldo: el `.png` de la misma carpeta |
| 7 | Valores esperados | `datos\documentos-ocr\campos-esperados.md`, sección **03**, abierto en otra ventana (no la compartas en pantalla) |
| 8 | Ensayo previo | Ejecuta **Receipt** y **Layout** sobre el 03 antes del módulo y guarda las capturas y los JSON del Plan B (sección 7) |
| 9 | Pantalla limpia | Navegador al 110 %, modo claro, sin marcadores ni correos visibles, notificaciones desactivadas |

## 4. Guion minuto a minuto

| Min | Reloj | Qué haces (clics) | Qué dices | Qué esperas ver |
|---|---|---|---|---|
| 0–1 | 10:40 | Muestra la página de inicio de Studio con los modelos agrupados (lectura y análisis de documentos, modelos prebuilt) | «Hasta aquí vimos Azure AI Services. Ahora miremos uno en vivo: Document Intelligence convierte documentos en datos. Usaremos un comprobante ficticio de una cafetería» | Inicio de Studio con el recurso seleccionado |
| 1–2 | 10:41 | Abre el modelo **Receipt** (en los modelos prebuilt; puede decir **Receipts**). Arrastra o usa **Browse for a file** y selecciona `03-comprobante-compra.pdf`. Si aparece la opción de idioma o configuración regional (locale), deja la detección automática o elige `es-CL`. Selecciona **Run analysis** | «Este PDF es un escaneo: no tiene texto seleccionable. Todo lo que verán sale del OCR» | El documento a la izquierda; análisis en pocos segundos |
| 2–5 | 10:42 | Recorre los campos de la derecha, uno por uno, y compara con `campos-esperados.md` sección 03 (tabla de la sección 5 de este guion). Detente en **Total** y en los **Items** | «Fíjense que no es solo texto: cada dato tiene nombre, tipo y confianza. `MerchantName`, la fecha como fecha, el total como moneda» | Campos extraídos: `MerchantName`, `MerchantAddress`, `TransactionDate`, `TransactionTime`, `TotalTax`, `Total` y `Items` (`Subtotal` puede no extraerse) |
| 5–6 | 10:45 | Verifica la aritmética en voz alta: 5.600 + 5.900 + 3.200 = 14.700. Abre la pestaña **Result** y muestra el JSON (campos tipados, `confidence`, ubicación en el documento) | «Esto es lo que consumiría una aplicación o un agente: un JSON, no una imagen» | JSON con campos, valores y confianza; la suma de los ítems coincide con `Total` |
| 6–8 | 10:46 | Vuelve a la página de inicio, abre **Layout** (o **Read**) y analiza **el mismo archivo**. Muestra la pestaña **Content** | «Mismo documento, otro modelo. Layout lee texto, líneas, tablas y casillas, pero no sabe que `14.700` es el total. Eso lo decide quien use el resultado» | Texto reconocido sin campos semánticos. La marca de agua **DOCUMENTO FICTICIO** puede aparecer como texto: es normal, no es un campo del documento |
| 8–9 | 10:48 | Vuelve unos segundos a **Receipt** y señala la **confianza** de `Total`, `TransactionDate` y de cualquier campo más bajo (puede no extraerse `Subtotal`) | Usa los puntos de la sección 6 | Confianza por campo; en el laboratorio se revisa manualmente lo que queda bajo 0,80 |
| 9–10 | 10:49 | Cierra la ventana de Studio (sin abrir otras pestañas ni cuentas) y vuelve a la presentación | Puente (sección 8): «En el laboratorio, Bloque C, harán esto ustedes con una factura y una solicitud de crédito» | — |

> Si vas retrasado: omite el paso de las 10:46 (Layout) o hazlo en 1 minuto; el mensaje clave (OCR vs extracción estructurada) se puede dar con la pestaña **Content** de Receipt.

## 5. Campos esperados del comprobante (de `campos-esperados.md`, sección 03)

Los valores son los impresos en el documento; la API puede normalizarlos (fechas en formato ISO, montos como número + moneda). **Compara el significado, no el formato exacto.**

| Campo | Etiqueta en el documento | Valor esperado | Nota |
|---|---|---|---|
| `MerchantName` | Encabezado | Café Austral Express | Puede devolverse en mayúsculas |
| `MerchantAddress` | Dirección | Av. Ficticia 321, Local 2, Santiago | |
| `TransactionDate` | Fecha | 2026-10-17 | |
| `TransactionTime` | Hora | 12:42:00 | |
| `Subtotal` | SUBTOTAL (neto) | $12.353 | Puede no extraerse |
| `TotalTax` | IVA 19% incluido | $2.347 | |
| `Total` | TOTAL | $14.700 | Campo clave; la suma de los ítems debe dar el `Total` |
| `Items` | 2 × Café americano grande | $5.600 | |
| `Items` | 1 × Sándwich ave palta | $5.900 | |
| `Items` | 1 × Jugo natural naranja | $3.200 | |

**Criterio de aceptación para la demo:** `Total` y fecha correctos (criterio sugerido en `campos-esperados.md` para el comprobante). No prometas que todos los campos salgan perfectos: si uno falla, úsalo como ejemplo (sección 6).

## 6. Puntos de conversación sobre la confianza (confidence)

- Cada campo trae un valor de **confianza**; no es una garantía de que el dato sea correcto, sino qué tan seguro está el modelo.
- En el laboratorio del Día 1 se usa **0,80** como umbral de revisión: lo que queda por debajo se revisa manualmente. El umbral real de un proceso del banco lo define el negocio según el riesgo (**por definir con el equipo de negocio**, no es una regla de la plataforma).
- Un campo que **no se extrae** (por ejemplo `Subtotal`) también es un resultado válido: se completa o se revisa a mano.
- Los valores se **normalizan** (fechas ISO, montos como número + moneda): por eso se compara el significado, no el texto exacto.
- La suma de ítems = `Total` es una **validación de negocio** que se hace después de la extracción; Document Intelligence extrae, la regla la aplica quien consume los datos.
- Todos los datos son ficticios; en un caso real hay que cuidar los datos personales y las políticas de retención (tema de gobierno del Día 3).

## 7. Plan B (prepáralo en el pre-flight)

**Qué guardar antes de las 10:15** (en `laboratorios\entorno-y-facilitacion\plan-b\D1\`, con la convención de nombres de `plan-b-demos.md`; corresponde al elemento **PB-D1-01**):

- `D1_01_demo-doc-intelligence_IMG_v01_01.png` a `_04.png`: capturas de Receipt (campos), pestaña **Result**, Layout (**Content**) y la lista de confianza.
- `D1_01_resultado-receipt_DATA_v01.json` y `D1_01_resultado-layout_DATA_v01.json`: JSON de la pestaña **Result** de cada análisis.
- Opcional: `D1_01_demo-doc-intelligence_VID_v01.mp4` (2–4 minutos, sin narración).
- Copia local fuera de OneDrive en el equipo del presentador y en el del segundo facilitador. Sin claves, TAP, ids de suscripción ni correos en las capturas.

**Cuándo activarlo:**

| Situación | Acción |
|---|---|
| Studio no carga, pide un recurso que no existe o da 403 / `PermissionDenied` | Pasa a las capturas y al JSON guardados; cuenta el mismo guion («esto es lo que obtuve en el ensayo») y avisa al segundo facilitador para revisar el rol más tarde |
| El análisis tarda más de lo razonable (por ejemplo, más de ~30 segundos; **umbral propuesto**) | Muestra la captura de la pestaña **Result** del ensayo y sigue; no esperes en silencio |
| Error AADSTS50079/50076 o TAP rechazado | Usa el Plan B; el segundo facilitador resuelve la sesión en paralelo |
| Error AADSTS50058 | Permite las cookies de terceros en otra ventana; si no se resuelve en 1 minuto, usa el Plan B |
| Fallo de red general | Usa el video o las capturas locales |

Nunca pidas disculpas largas: «Para no gastar su tiempo, les muestro el resultado que obtuve en el ensayo» y continúa.

## 8. Puentes

**Hacia el Bloque C (11:40 en adelante; Bloque C: 12:20–12:45):** «Lo que acaban de ver con un comprobante lo harán ustedes con una **factura** (modelo Invoice) y una **solicitud de crédito** (modelo Layout), y luego compararán qué entrega Document Intelligence frente a lo que hace un modelo o agente con esos datos. Si terminan antes, pueden repetir mi demo con `03-comprobante-compra`».

**Hacia agentes y tools (Día 2):** «Document Intelligence **extrae**; un modelo o agente **razona y decide**. En la práctica se combinan. El Día 2 (Tarea 3 del laboratorio pro-code) implementarán una **herramienta propia** para un agente: extraer campos de un documento es el tipo de capacidad que se expone como tool».

## 9. Qué no hacer

- No uses `01-factura` ni `02-solicitud-credito` en la demo: son del laboratorio.
- No muestres claves, endpoints, TAP ni tu cuenta completa. No pegues credenciales en el chat.
- No crees recursos nuevos ni cambies configuraciones del recurso en vivo.
- No prometas que la extracción es perfecta ni uses datos reales de BCI o de clientes.

## 10. Fuentes

- `datos\documentos-ocr\campos-esperados.md` (sección 03) y `datos\documentos-ocr\03-comprobante-compra.pdf` / `.png`.
- `README.md` del Día 1, sección 8 (Bloque C) para los documentos del laboratorio.
- Laboratorio oficial `03-document-intelligence.md` de `mslearn-ai-information-extraction` y la guía [Primeros pasos con Document Intelligence Studio](https://learn.microsoft.com/azure/ai-services/document-intelligence/quickstarts/get-started-studio).
- [Visión general de Document Intelligence](https://learn.microsoft.com/azure/ai-services/document-intelligence/overview) y [Elegir un modelo](https://learn.microsoft.com/azure/ai-services/document-intelligence/concept/choose-model-feature).
- `guia-facilitador.md` (sección 4.2, demo en vivo) y `checklist-validacion.md` (ítem de la demo).

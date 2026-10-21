# Plan B: demos grabadas, capturas y artefactos sin conexión (preparar HOY)

**Objetivo:** que ninguna demo ni laboratorio dependa de que Azure, una función en *preview*, la red o el audio funcionen en vivo. Cada elemento de esta lista reemplaza (o respalda) un momento concreto de las diapositivas de `presentaciones\content\day1.json`, `day2.json` y `day3.json`. Hoy es **T-1**: la lista está ordenada por **riesgo** (P1 = si falla, se rompe el bloque; P2 = se degrada; P3 = comodidad).
**Regla de oro:** todo con **datos ficticios**; nada con claves, ids de suscripción, correos reales ni nombres de clientes (ver sección 2).

---

## 1. Presupuesto de tiempo y reparto sugerido

| Prioridad | Elementos | Tiempo estimado (suma) | Reparto sugerido |
|---|---|---|---|
| **P1** | PB-D1-01, 02, 03 · PB-D2-01, 02, 03, 04 · PB-D3-01 | ≈ 4 h 20 min | Pablo: D2-01, D2-02, D2-03, D2-04 · Valentina: D1-01, D1-02, D1-03, D3-01 |
| **P2** | PB-D1-04, 05, 06 · PB-D2-05, 06, 07 · PB-D3-03 | ≈ 1 h 50 min | Reparto según disponibilidad; Robert: transversales y empaquetado |
| **P3** | PB-D1-07 · PB-D3-04 · PB-X-01 a 03 | ≈ 55 min | Robert |

> **Si hoy solo hay ≈ 3 horas-persona en total**, graba en este orden: PB-D2-02 (trazas) → PB-D1-01 (demo en vivo de Document Intelligence) → PB-D2-03 (retrieval agéntico) → PB-D1-02 (agente en portal) → PB-D3-01 (AI Gateway) (≈ 2 h 20 min) → PB-X-02 (copia local sin conexión, 10 min). El ensayo completo PB-D2-01 es el siguiente en la lista. Los tiempos son **estimaciones**: aumentan si el entorno todavía no está listo; las demos que dependen del entorno se graban **cuando el validador (`scripts\02_validar_entorno.py`) esté en PASS**.

---

## 2. Convención de almacenamiento, nombres y calidad

**Carpeta:** `laboratorios\entorno-y-facilitacion\plan-b\` con subcarpetas `D1\`, `D2\`, `D3\`, `X\` (transversal). Además, una **copia local fuera de OneDrive** en cada equipo de los instructores (y en un pendrive) para usar sin conexión. Para crear la estructura:

```powershell
$raiz = ".\laboratorios\entorno-y-facilitacion\plan-b"
"D1","D2","D3","X" | ForEach-Object { New-Item -ItemType Directory -Force -Path (Join-Path $raiz $_) | Out-Null }
```

**Convención de nombres:** `D{día}_{nn}_{tema-en-minusculas}_{TIPO}_v{NN}[_{k}].{ext}`

| Campo | Valores |
|---|---|
| `TIPO` | `VID` (video), `IMG` (captura), `DOC` (PDF/documento), `DATA` (JSON/CSV de ejemplo), `COD` (código) |
| Ejemplos | `D1_01_demo-doc-intelligence_IMG_v01_01.png` · `D1_03_doc-intelligence_IMG_v01_03.png` · `D2_02_traza-fallida_VID_v02.mp4` |

**Calidad de captura**
- Resolución 1080p; navegador al 100 % o 110 % de zoom; modo claro; idioma de la interfaz en español o inglés, pero **el mismo en todas las tomas**.
- Videos de **2 a 4 minutos** como máximo, **sin narración** (el instructor narra en vivo) y con una pausa de 1 s entre pasos. Herramientas: Herramienta Recortes de Windows (modo video), Barra de juegos (Win+G) o una reunión de Teams a solas con grabación.
- Cursor visible; clics lentos; **un solo escenario por clip**.
- **Oculta o difumina:** id de suscripción, correos, tokens, cadenas de conexión, claves, nombres de clientes. Usa una cuenta/proyecto de prueba.
- Cada clip incluye, en una captura `..._IMG_v01_00` o en el nombre, **qué proyecto/modelo/región** se usó (para reproducir y para auditar versiones de preview).
- Revisa cada archivo en **reproducción completa** antes de marcarlo como listo (estado en la sección 6).

---

## 3. Mapa de reemplazo y prioridad

| ID | Elemento | Reemplaza / respalda | Prio. | Qué lo hace riesgoso | Tiempo est. |
|---|---|---|---|---|---|
| PB-D1-01 | Demo en vivo de Document Intelligence (Receipt sobre `03-comprobante-compra` + Layout) | Día 1, módulo Azure AI Services, ≈10:40–10:50 (guion: `dia1-lab-guiado\demo-document-intelligence.md`) | **P1** | Acceso a Studio y rol sobre el recurso (*por confirmar*), cookies de terceros, Studio lento | 20 min |
| PB-D1-02 | Crear prompt agent + file search | Día 1, demo 26 y Bloque B | **P1** | Permisos del proyecto, modelo (`gpt-5.6-luna` + Agent Service + file search aún no probado), vector store | 25 min |
| PB-D1-03 | OCR con Document Intelligence | Día 1, Bloque C | **P1** | Acceso a Studio/región; F0 vs S0 (límite de 1 TPS en F0 según la guía) | 20 min |
| PB-D2-01 | Ensayo completo del laboratorio y solución | Día 2, diapositivas 35–39 | **P1** | Variables de entorno, roles, Search, tool, trazas | 60 min |
| PB-D2-02 | Traza fallida y diagnóstico | Día 3, módulo "Observabilidad y ciclo de vida" (ejercicio de trazas; antes era la demo 30 y la Tarea 4 del laboratorio del Día 2) | **P1** | Trazas en *preview* según tipo de agente; retraso de ingestión | 25 min |
| PB-D2-03 | Retrieval agéntico con 2 usuarios simulados | Día 2, demo 26 | **P1** | Funciones en *preview*; región de Search; modelo para planificación | 30 min |
| PB-D2-04 | Agente hospedado con tool propia | Día 2, demo 10 (y logs de demo 30) | **P1** | Requiere ACR, roles de MI y despliegue | 40 min |
| PB-D3-01 | AI Gateway / APIM (4 escenas) | Día 3, demo 21 | **P1** | Artefacto externo ilustrativo; red privada; sin entorno propio | 40 min |
| PB-D1-04 | Recorrido por el portal | Día 1, demo 11 | P2 | Cambios de interfaz del portal | 10 min |
| PB-D1-05 | Catálogo → deployment → playground | Día 1, demo 14 | P2 | Cuota/capacidad al crear el deployment | 10 min |
| PB-D1-06 | Hoja «errores frecuentes y qué hacer» | Bloques de laboratorio | P2 | Bloqueos de acceso y 429 | 20 min |
| PB-D2-05 | Capturas del índice de normativa | Día 2, demo 26 y T1–T2 | P2 | Índice sin datos/permisos | 10 min |
| PB-D2-06 | `.env` de ejemplo y errores de conexión | Día 2, preparación (diapositiva 36) | P2 | Variables mal configuradas (la causa de bloqueo más frecuente según las notas del orador) | 10 min |
| PB-D2-07 | Prueba de Codespaces / dev container | Alternativa para equipos restringidos | P2 | Política de GitHub de BCI | 20 min |
| PB-D3-03 | Canvas de ejemplo «Austral Bank» completado | Día 3, workshop (diapositivas 34–40) | P2 | Formato ambiguo para los grupos | 30 min |
| PB-D1-07 | PDF de las 3 presentaciones + notas | Todos los días | P3 | Fallo del equipo de presentación | 10 min |
| PB-D3-04 | Diagramas de arquitectura exportados (PNG/PDF) | Día 3, módulo de arquitectura | P3 | Fallo de PowerPoint | 15 min |
| PB-X-01 | Mensajes pre-escritos del chat (modo demo, modo pareja) | Todos los días | P3 | Comunicación lenta bajo presión | 10 min |
| PB-X-02 | Copia local de `plan-b\` + pendrive | Todos los días | P3 | Sin red / OneDrive bloqueado | 10 min |
| PB-X-03 | Reunión de prueba de Teams con grabación | Todos los días | P3 | Políticas del tenant | 10 min |

---

## 4. Detalle por día (pasos exactos)

> Los nombres exactos de menús del portal cambian; si un paso no coincide con tu pantalla, anótalo en el clip (captura de la pantalla real) y **verificar**. Usa **siempre** la misma cuenta de prueba, miembro **solo** del grupo de participantes, para que lo grabado represente lo que verán los participantes.

### Día 1 — L100

**PB-D1-01 · Demo en vivo de Document Intelligence (≈ 20 min) → `D1\D1_01_demo-doc-intelligence_IMG_v01_01–04.png` + `D1_01_resultado-receipt_DATA_v01.json` + `D1_01_resultado-layout_DATA_v01.json` (opcional: `D1_01_demo-doc-intelligence_VID_v01.mp4`)**
1. Abre Document Intelligence Studio (`https://documentintelligence.ai.azure.com`) con la cuenta de prueba (con TAP) y selecciona el recurso.
2. Modelo prebuilt **Receipt** → carga `laboratorios\dia1-lab-guiado\datos\documentos-ocr\03-comprobante-compra.pdf` → **Run analysis** → captura los campos con su confianza y guarda el JSON de la pestaña **Result** (`D1_01_resultado-receipt_DATA_v01.json`).
3. Repite sobre el mismo archivo con **Layout** (o **Read**) y guarda la captura de **Content** y el JSON (`D1_01_resultado-layout_DATA_v01.json`).
4. Compara con la sección 03 de `datos\documentos-ocr\campos-esperados.md` y anota las diferencias en la captura o en el nombre del archivo.
5. Nota en `D1_01_..._IMG_v01_00` qué recurso/región/cuenta usaste. Cronometra: la demo en vivo dura ≈ 10 min.
*Referencias:* `dia1-lab-guiado\demo-document-intelligence.md` (guion y Plan B); guía, sección 8.1.

**PB-D1-02 · Crear un prompt agent con file search (≈ 25 min) → `D1\D1_02_agente-portal_VID_v01.mp4` + `IMG_v01_01–08.png` + `D1_02_instrucciones_DOC_v01.txt`**
1. Documento ficticio de política interna (2–3 páginas; el del laboratorio o uno propio sin datos reales) listo para subir.
2. En el portal: crea un agente → elige `gpt-5.6-luna` (respaldo: `gpt-5-mini`; ambos ya desplegados en la cuenta de prueba) → pega las instrucciones de «asistente de políticas internas ficticio» → agrega la herramienta de búsqueda en archivos y sube el documento → guarda. **`gpt-5.6-luna` con Agent Service + file search aún no se probó**: si falla, graba con `gpt-5-mini` y anótalo en la captura.
3. En el *playground* de agentes: 3 preguntas (una respuesta directa, una que requiere citar el documento y una fuera del documento para mostrar el rechazo).
4. Captura: lista de agentes, configuración, resultado con cita.
5. Guarda el texto de instrucciones y las 3 preguntas en `D1_02_instrucciones_DOC_v01.txt` (se pega en el chat si el portal falla).
*Referencias:* `repos\microsoftlearning-labs\mslearn-agent-quickstart\Instructions\Labs\01b-create-first-agent.md` (verificar pasos).

**PB-D1-03 · Document Intelligence (≈ 20 min) → `D1\D1_03_doc-intelligence_VID_v01.mp4` + `IMG_v01_01–04.png` + `D1_03_resultado_DATA_v01.json`**
1. Abre el estudio de Document Intelligence (la URL del laboratorio `03-document-intelligence.md` es `https://contentunderstanding.ai.azure.com/documentintelligence/studio`; la demo en vivo usa `https://documentintelligence.ai.azure.com`; verificar vigencia de ambas).
2. Carga el documento ficticio (solicitud de crédito de ejemplo) → ejecuta un modelo *prebuilt* → revisa campos y confianza por campo.
3. Exporta el JSON del resultado y captura la vista de campos.
4. Esos archivos sirven de **resultado pre-extraído** si el Bloque C pasa a demo guiada.
*Referencias:* `repos\microsoftlearning-labs\mslearn-ai-information-extraction\Instructions\Exercises\03-document-intelligence.md`; usar el recurso **S0** (F0 limita a 1 TPS; guía, sección 8.1).

**PB-D1-04 · Recorrido por el portal (≈ 10 min) → `D1\D1_04_portal_VID_v01.mp4`.** Inicia sesión → abre el proyecto → muestra Modelos, Agentes, Conocimiento, Observabilidad y la configuración de RBAC/red (diapositiva 11).

**PB-D1-05 · Catálogo → deployment → playground (≈ 10 min) → `D1\D1_05_catalogo-deployment_VID_v01.mp4`.** Busca un modelo → ficha → crea un deployment de prueba **Global Standard** (bórralo después) → *playground* con un prompt bancario ficticio.

**PB-D1-06 · Hoja de errores frecuentes (≈ 20 min) → `D1\D1_06_errores-frecuentes_DOC_v01.pdf`.** Una página con: «no veo mi proyecto» (rol/propagación), 401/403, 429 (esperar ≈10 s, acortar el prompt o cambiar al respaldo `gpt-5-mini`), no puedo iniciar sesión (AADSTS50079/50076 = no estás usando el TAP; TAP no válido o expirado; acceso condicional/MFA), Document Intelligence 403/1 TPS. Incluye mensajes reales capturados durante los ensayos.

**PB-D1-07 · PDF de los decks (≈ 10 min) → `D1\D1_07_decks-pdf_DOC_v01.zip`.** Exporta los 3 `.pptx` de `presentaciones\` a PDF con las notas del orador.

### Día 2 — L200

**PB-D2-01 · Ensayo completo del laboratorio + solución (≈ 60 min) → `D2\D2_01_lab-solucion_VID_v01.mp4` + carpeta `D2\solucion\` (COD)**
1. Con la cuenta de participante de prueba: `git clone` del starter → entorno virtual → instalar dependencias → completar `.env` → `python src\00_verificar_entorno.py --probar-modelo` → agente base.
2. Tareas 1–2: conectar el índice y probar 2 preguntas (simple y de dos subconsultas).
3. Tarea 3: implementar la function tool «consultar estado de solicitud» ficticia y verificar que se invoca (y que no se invoca en una pregunta no relacionada). Hazlo con `FOUNDRY_MODEL=gpt-5-mini`; si la herramienta falla, repite con `gpt-4.1-mini` y anota la diferencia en `D2_01_versiones_DOC_v01.txt` (guía, sección 5.2).
4. (Preparación para el ejercicio del Día 3) abre la traza en el portal (ver PB-D2-02).
5. Guarda **cada punto de control** en `D2\solucion\` (por ejemplo, ramas `t1-t2`, `t3`, `t4`) y registra cuánto demoró cada paso (sirve para ajustar el reloj del runbook).
6. Anota la versión de Python y de los paquetes (`pip freeze` sin secretos) en `D2_01_versiones_DOC_v01.txt`.

**PB-D2-02 · Traza fallida y diagnóstico (≈ 25 min) → `D2\D2_02_traza-fallida_VID_v01.mp4` + `IMG_v01_01–06.png`** — *se usa el Día 3, en el módulo "Observabilidad y ciclo de vida" (11:05–11:35): los participantes retoman su propio proyecto `dia2-lab-procode\` del Día 2 (mismo entorno, mismo agente, mismo índice) para diagnosticar con su propia traza; esta grabación es el plan B si algo falla en vivo.*
1. Ejecuta el **caso fallido** diseñado para el ejercicio de trazas (pregunta fuera del índice o tool con parámetro mal formado).
2. Abre la traza en el portal de Foundry: ubica el *span* de retrieval y el `execute_tool`; muestra argumentos y resultado.
3. Muestra dónde se identifica la causa (retrieval vs tool vs modelo).
4. Espera unos minutos si las trazas no aparecen (retraso de ingestión) y anota el tiempo real.
5. Captura también la vista de la traza **sana** para comparar.
*Referencias:* `docs-oficiales\foundry\observability\how-to\trace-agent-setup.md` (rastreo GA para agentes de prompt y hospedados; flujo de trabajo y externos en preview; verificar qué categoría aplica al agente del starter).

**PB-D2-03 · Retrieval agéntico con 2 usuarios simulados (≈ 30 min) → `D2\D2_03_retrieval-agentico_VID_v01.mp4` + `IMG_v01_01–05.png`**
1. Pregunta ambigua que requiere dos subconsultas contra el índice de normativa ficticia.
2. Muestra el plan de subconsultas y las citas devueltas (fragmento exacto).
3. Repite con un segundo usuario simulado con permisos distintos y muestra la diferencia (recorte por permisos).
4. Si la planificación/síntesis (preview) no está disponible: graba el flujo clásico híbrido y captura el mensaje de error o limitación.
*Referencias:* `docs-oficiales\foundry\agents\how-to\foundry-iq-connect.md`; `docs-oficiales\azure-ai-search\get-started-portal-agentic-retrieval.md`; guía, sección 7.

**PB-D2-04 · Agente hospedado con tool propia (≈ 40 min) → `D2\D2_04_agente-hospedado_VID_v01.mp4` + `IMG_v01_01–04.png`**
1. Despliega el agente hospedado de ejemplo (función `consultar_limite_gastos` ficticia).
2. Pregunta por el límite de gastos de viaje → muestra la llamada a la tool y la respuesta con su fuente.
3. Muestra los registros del agente y la traza asociada.
4. Si el despliegue falla (ACR/permisos): graba lo que llegues a mostrar y anota el error en `D2_04_error_DOC_v01.txt` (útil para el riesgo R15).
*Referencias:* `docs-oficiales\foundry\agents\how-to\test-hosted-agent.md`; `docs-oficiales\foundry\agents\concepts\hosted-agent-permissions.md`; guía, sección 6.4.

**PB-D2-05 · Índice de normativa (≈ 10 min) → `D2\D2_05_indice-search_IMG_v01_01–03.png`.** Campos (texto, vector, metadatos de seguridad), conteo de documentos y una consulta de ejemplo.

**PB-D2-06 · `.env` y errores de conexión (≈ 10 min) → `D2\D2_06_env-ejemplo_DOC_v01.md`.** `.env` con **placeholders** (nunca claves): `FOUNDRY_PROJECT_ENDPOINT`, `FOUNDRY_MODEL` (ejemplo: `gpt-5-mini`; es el nombre del deployment), `FOUNDRY_EMBEDDING_MODEL` (ejemplo: `text-embedding-3-small`; vacío = plan B sin vectores), `AZURE_SEARCH_ENDPOINT`, `AZURE_SEARCH_INDEX_NAME` (`normativa-austral`), `APPLICATIONINSIGHTS_CONNECTION_STRING` (nombres de `laboratorios\dia2-lab-procode\.env.example`); con la tabla «síntoma → causa → solución» (401/403, 404, deployment inexistente, índice inexistente).

**PB-D2-07 · Codespaces / dev container (≈ 20 min) → `D2\D2_07_codespaces_DOC_v01.md` + `IMG`.** Abre `<LINK-REPO>` en Codespaces con una cuenta de prueba, ejecuta el validador y confirma que funciona; anota las restricciones (política de GitHub, Actions deshabilitado, etc.; verificar).

### Día 3 — L300 (sin laboratorio en la nube)

**PB-D3-01 · AI Gateway / APIM (≈ 40 min) → `D3\D3_01_ai-gateway_VID_v01.mp4` + `IMG_v01_01–04.png`**
Las 4 escenas de la demo 21: (1) un consumidor sin permiso intenta un modelo no autorizado → 403; (2) supera su cuota de tokens por minuto → rechazo por tasa; (3) el presupuesto diario se agota y el gateway degrada a un modelo más económico; (4) el tablero muestra tokens por consumidor y por modelo.
- **Definir hoy cuál es el artefacto de origen** (probable: `repos\publico-samples\apim-foundry-governance\` con su interfaz de administración y las imágenes de `docs\images\`; *verificar* que corresponde al panel de la diapositiva). Si no hay entorno desplegado, arma el clip con **capturas de la documentación del repositorio** y marca el clip como «ilustrativo».

**PB-D3-03 · Canvas de ejemplo «Austral Bank» (≈ 30 min) → `D3\D3_03_canvas-ejemplo_DOC_v01.pdf` + plantilla `D3_03_canvas-plantilla_DOC_v01.pptx/xlsx`**
Completa un canvas de ejemplo con el caso ficticio (canal → identidad → sesión → agente → modelo → tools → datos), 3 amenazas con su control y 2 SLO; los grupos lo usan como referencia de formato. Fuente de la plantilla: `<LINK-CANVAS>` (el kit de arquitectura de `MATERIALS_INDEX.md`, §3; verificar disponibilidad).

**PB-D3-04 · Diagramas exportados (≈ 15 min) → `D3\D3_04_diagramas_IMG_v01.zip`.** PNG/PDF de los diagramas de arquitectura de las diapositivas 17–19 y 24.

### Transversal

- **PB-X-01 · Mensajes pre-escritos (≈ 10 min) → `X\X_01_mensajes-chat_DOC_v01.md`:** aviso de «modo demo guiada», «modo pareja», recordatorio de convenciones del chat (`[P]`, `[LAB]`, `[PARK]`), enlace al autochequeo.
- **PB-X-02 · Copia local (≈ 10 min):** copia de `plan-b\` en cada equipo de instructores y en un pendrive; verifica que los videos se reproducen sin conexión.
- **PB-X-03 · Reunión de prueba de Teams (≈ 10 min):** valida grabación, transcripción, Q&A y salas con Robert (ver `runbook-facilitacion-3-dias.md`, sección 3).

---

## 5. Cuándo se activa el Plan B (resumen)

| Situación | Activa | Quién decide |
|---|---|---|
| Falla el entorno en el pre-flight (T-30) | Modo demo guiada: PB-D1-02/03 o PB-D2-01/02 | Pablo |
| Una demo falla en vivo > 1 minuto | Reproduce el clip PB correspondiente (sin disculpas largas) y continúa | Presentador |
| Un bloque de laboratorio se atrasa > 5 min | Reglas de recorte del runbook; el resultado pre-extraído/solución se comparte | Robert (tiempo) + presentador |
| Alguien no puede iniciar sesión | Modo pareja + PB-D1-06 | Instructor de soporte |

---

## 6. Seguimiento de preparación (marcar al terminar)

| ID | Responsable | Grabado | Revisado en reproducción completa | Copiado a pendrive |
|---|---|:---:|:---:|:---:|
| PB-D1-01 | Valentina | ☐ | ☐ | ☐ |
| PB-D1-02 | Valentina | ☐ | ☐ | ☐ |
| PB-D1-03 | Valentina | ☐ | ☐ | ☐ |
| PB-D2-01 | Pablo | ☐ | ☐ | ☐ |
| PB-D2-02 | Pablo | ☐ | ☐ | ☐ |
| PB-D2-03 | Pablo | ☐ | ☐ | ☐ |
| PB-D2-04 | Pablo | ☐ | ☐ | ☐ |
| PB-D3-01 | Valentina | ☐ | ☐ | ☐ |
| Resto (P2/P3) | Según disponibilidad | ☐ | ☐ | ☐ |

---

## Fuentes
- Demos, laboratorios y números de diapositiva: `presentaciones\content\day1.json` (diapositivas 11, 14, 26, 33–36), `day2.json` (10, 26, 30, 35–39), `day3.json` (21, 34–40); `MATERIALS_INDEX.md` (§1–§3). La numeración de diapositivas de los tres días puede haber cambiado tras los últimos ajustes de agenda: *por confirmar* con el deck vigente.
- Demo en vivo de Document Intelligence y laboratorio del Día 1: `laboratorios\dia1-lab-guiado\demo-document-intelligence.md` y `guia-facilitador.md`. F0 de Document Intelligence: guía, sección 8.1 (fuente: `docs-oficiales\ai-services-document-intelligence\service-limits.md`).
- Trazas, agentes hospedados y evaluación: `docs-oficiales\foundry\observability\how-to\trace-agent-setup.md`; `docs-oficiales\foundry\observability\how-to\azure-developer-cli-evaluation.md`; `docs-oficiales\foundry\agents\how-to\test-hosted-agent.md`; `docs-oficiales\foundry\agents\concepts\hosted-agent-permissions.md`; `docs-oficiales\foundry\agents\how-to\set-up-ci-cd-cli.md`.
- Search y retrieval agéntico: `docs-oficiales\foundry\agents\how-to\foundry-iq-connect.md`; `docs-oficiales\azure-ai-search\get-started-portal-agentic-retrieval.md`.
- Laboratorios de origen: `repos\microsoftlearning-labs\mslearn-agent-quickstart\Instructions\Labs\01b-create-first-agent.md`; `repos\microsoftlearning-labs\mslearn-ai-information-extraction\Instructions\Exercises\03-document-intelligence.md`; `repos\publico-workshops\foundry-hosted-agents-workshop\`; `repos\publico-samples\apim-foundry-governance\` (README).
- Tiempos estimados de captura: estimación del autor (sin datos medidos).

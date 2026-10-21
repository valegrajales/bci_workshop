# Guía del facilitador — Laboratorio Día 2: Agente pro-code con grounding y herramientas

**Evento:** Microsoft AI Foundry BCI Training Day (híbrido) · Día 2, jueves 22 de octubre de 2026 · L200
**Bloque:** laboratorio de 85 min, 11:15 – 12:40 (hora de Chile); el cierre del día va de 12:40 a 13:00 · ~48 participantes (desarrolladores, ingenieros de IA/datos, arquitectos, DevOps)
**Instructores:** Pablo Braconi y Valentina Grajales · **Idioma:** español (neutro LatAm)

> **Estado de validación:** el kit se verificó localmente (compilación y 100+ pruebas con `pytest` de las partes que no usan Azure; firmas de API contrastadas con
> los SDKs instalados). **No se ejecutó contra recursos reales de Azure.** Antes de la sesión corre el smoke test de `checklist-validacion.md` en una
> suscripción real y revisa la sección [11](#11-supuestos-de-api-que-debes-verificar-en-vivo).

---

## 0. Ficha rápida

| Tema | Detalle |
|---|---|
| Escenario | Asistente de normativa interna de **Austral Bank** (banco ficticio) + herramienta `consultar_estado_solicitud`. El diagnóstico de un caso fallido con trazas y el checklist de éxito **ya no se practican con código**: el Día 3 los presenta de forma conceptual |
| Lenguaje | Python 3.10+ (probado en 3.13). Agent Framework (`agent-framework-foundry`), `azure-search-documents`, `azure-monitor-opentelemetry` |
| Autenticación | Sin llaves: Microsoft Entra ID (`az login` + `DefaultAzureCredential`) |
| Materiales para participantes | Carpeta `dia2-lab-procode\` **sin** `instructores\`, `herramientas\` ni los scripts de observabilidad (`src\05_*`, `solutions\05_trazas.py`), que no se usan en el laboratorio; conserva `src\trazas.py` y `src\checklist.py`, que `agente_lab.py` y `evaluacion.py` importan (+ `README.md` y `Guia_del_participante_Dia2.docx`). `solutions\` se comparte durante la sesión. Si editas el README, regenera el Word: `python herramientas\md_a_docx.py README.md Guia_del_participante_Dia2.docx` (necesita `python-docx`, incluido en `requirements-dev.txt`) |
| Lo que se prepara antes | Servicio de Search + índice `normativa-austral` (lo crean los instructores), deployments y roles. Application Insights solo es necesario si quieres ensayar el material opcional de trazas |
| Tiempos | Preparación 10 · Tareas 1-2 30 · Tarea 3 25 · Revisión en parejas y preguntas 20 (total 85, 11:15–12:40; el tiempo liberado por la Tarea 4 se reparte entre las Tareas 1-3) |
| Criterios de éxito | Responde · cita fuente · usa la tool correcta según el tipo de pregunta (checklist de diseño del README §7) |

**Reparto sugerido (ajústalo entre ustedes):**
- **Instructor A (Pablo)** — presenta y comparte pantalla; conduce las Tareas 1-3 y la revisión en parejas final.
- **Instructor B (Valentina)** — soporte activo: sala presencial o chat de Teams (según quién esté en sitio), desbloquea entornos y permisos.
- Si hay otra persona del equipo en la sala: un tercer "pasillo" para el soporte presencial.

---

## 1. Checklist de preparación previa

### 1.1 T-7 días — recursos y permisos

| # | Qué | Detalle / cómo verificar |
|---|---|---|
| 1 | Proyecto de Foundry (nuevo portal) | Un proyecto compartido (o uno por grupo de ~12 si hay límites de cuota). Anota **Project endpoint** (Overview) |
| 2 | Deployment de **chat** con *function calling* | Anota el **nombre del deployment** (`FOUNDRY_MODEL`). Cuota: estimación ≈ 6–7 M tokens en total durante el lab; pico 250–350 K TPM con 48 personas → subir TPM o repartir en 2–4 deployments/proyectos |
| 3 | Deployment de **embeddings** (p. ej. `text-embedding-3-small`, 1536 dimensiones) | Nombre → `FOUNDRY_EMBEDDING_MODEL`. Si no hay cuota: `01_crear_indice.py --sin-vectores` y deja la variable vacía |
| 4 | Azure AI Search (Basic o superior) | **Ranker semántico habilitado** (portal: Search service → *Semantic ranker*). **Control de acceso:** *Role-based access control* o *Both* (si solo admite llaves de API, la autenticación con Entra ID devolverá 403). Región cercana al proyecto |
| 5 | *(Opcional)* Application Insights **conectado al proyecto** | Solo para ensayar el material de trazas (`src\05_trazas.py`), que ya no forma parte del laboratorio. Foundry portal → proyecto → *Observability/Traces* → *Connect*. Anota si tiene la **autenticación local deshabilitada**: ver fila de roles "Monitoring Metrics Publisher" |
| 6 | Grupo de Entra ID para participantes | Ej.: `grp-lab-dia2-participantes` (nombre ficticio). Más fácil que asignar roles uno a uno |

### 1.2 Roles (los roles pueden tardar hasta 10 min en propagarse)

| Identidad | Alcance | Rol | Para qué |
|---|---|---|---|
| Participantes | Recurso de Foundry / proyecto | **Foundry User** (antes *Azure AI User*) | Llamar al modelo y a embeddings desde el código |
| Participantes | Servicio de Azure AI Search | **Search Index Data Reader** | Consultar el índice (Tareas 2-3) |
| Participantes *(opcional)* | Application Insights / workspace conectado | **Log Analytics Reader** (+ *Privileged Monitoring Data Reader* si las tablas están protegidas) | Solo para el material opcional de trazas: no se necesita en el laboratorio |
| Participantes *(opcional)* | Application Insights conectado | **Monitoring Metrics Publisher** | Solo para el material opcional de trazas, y **solo si** la autenticación local está deshabilitada (`LAB_APPINSIGHTS_ENTRA=true`) |
| Instructores | Servicio de Search | **Search Service Contributor** + **Search Index Data Contributor** | Crear el índice y cargar documentos (`01_crear_indice.py`) |
| Instructores | Proyecto de Foundry | **Foundry User** (o *Contributor* para crear deployments) | Embeddings al cargar el índice y pruebas |
| Instructores (extensión *hosted agent*) | Grupo de recursos / ACR / proyecto | *Contributor* + permiso para asignar roles | `azd`/despliegue; la identidad del agente necesita *Search Index Data Reader* |

### 1.3 T-3 días — índice y ensayo completo

Desde `laboratorios\dia2-lab-procode\` con el `.env` de instructor completado y el venv activo:

```powershell
python src\01_crear_indice.py --dry-run          # sin Azure: debe decir "12 documentos, 46 fragmentos"
python src\01_crear_indice.py                    # crea normativa-austral (texto + vector + semántico) y carga los 46 fragmentos
python src\00_verificar_entorno.py --probar-modelo
```

Verifica en el portal de Azure (Search service → *Indexes* → `normativa-austral` → *Search explorer*): 46 documentos; una consulta `límite Jefatura` con filtro
`search.in(nivel_acceso, 'publico,interno', ',')` devuelve `NOR-001-02`, y con `'publico'` **no** lo devuelve.

Si cambias el modelo de embeddings (dimensiones distintas): `python src\01_crear_indice.py --recrear`.

Ejecuta **todo el flujo con las soluciones**, en este orden, y captura las salidas del Plan B (sección 7):

```powershell
python solutions\02_agente_base.py
python solutions\03_agente_con_search.py
python solutions\04_herramienta_estado.py
```

*(Opcional)* El diagnóstico con trazas y el caso fallido ya no se practican con código: el Día 3 los presenta de forma
conceptual. El código sigue en el kit como material de instructor; si quieres ensayarlo con Application Insights
conectado, ejecuta `python solutions\05_trazas.py`, `python src\05_caso_fallido.py --caso 1|2` y
`python instructores\05_caso_fallido_corregido.py --caso 1`, y anota en `instructores\README.md` lo que viste.

### 1.4 T-1 día / T-1 hora

- [ ] Envía a los participantes el prerrequisito: Python 3.10+, Azure CLI, VS Code, acceso a PyPI y los permisos de la sección 1.2 ya asignados.
- [ ] Prepara el **paquete de entrega** (`dia2-lab-procode` sin `instructores\` ni `salidas\`, con `.env.example` y sin `.env`; omite también `src\05_*` y `solutions\05_trazas.py` si no quieres que aparezcan; **conserva** `src\trazas.py` y `src\checklist.py`, porque `agente_lab.py` y `evaluacion.py` los importan). Compártelo por SharePoint/Teams o repo privado.
- [ ] Publica en el chat de Teams los **valores del `.env`** (endpoint de Foundry, deployment, endpoint de Search, índice). No hay secretos: son nombres y URL.
- [ ] 60 min antes: `python src\00_verificar_entorno.py --probar-modelo` con una **cuenta de prueba de participante** (no la de instructor) para validar roles reales.
- [ ] Confirma cuota del deployment (sin throttling 429) y que el índice responde.
- [ ] Deja abiertas la terminal con el kit y las capturas del Plan B.

---

## 2. Minuto a minuto

| Hora | Min | Bloque | Qué haces tú | Señal de que va bien | Si vas atrasado |
|---|---|---|---|---|---|
| 11:15 | 0-2 | Apertura (parte de la Preparación) | Explica qué construirán (diagrama del README §1), dónde está el kit, canal de ayuda (chat de Teams) y los 3 entregables de hoy. Recuerda: datos 100 % ficticios | Todos abren la carpeta del kit | — |
| 11:17 | 2-10 | **Preparación del entorno** | Circula; resuelve primero `az login` y `.env`. A los 11:23 pide un ✔ en el chat a quien tenga `Entorno listo ✔`. Ejecuta `--probar-modelo` en pantalla | ≥ 80 % con ✔ a las 11:25 | Quien no esté listo trabaja **en pareja** con un vecino o sigue tu pantalla; un instructor lo atiende en paralelo |
| 11:25 | 10-20 | **Tarea 1** (≈10) | Muestra en 1 min la forma `Agent(client, instructions)` y `agent.run`. Deja trabajar. Pregunta: "¿inventó el límite de Austral Bank?" | Respuesta en español; el límite **no** se inventa | Comparte `solutions\02_agente_base.py` a los 7 min |
| 11:35 | 20-40 | **Tarea 2** (≈20) | A los 11:40: checkpoint `--solo-tool`. A los 11:47 corre la pregunta compuesta (dos búsquedas). A los 11:50: **security trimming** en vivo (nivel `restringido`, 3 min) | Cita `[NOR-001-02]`; pregunta compuesta = 2 búsquedas | Cambia 2.3 por las instrucciones de la solución; omite la prueba `restringido` si no alcanza el tiempo (se muestra en pantalla) |
| 11:55 | 40-65 | **Tarea 3** (25) | 1 min: "el modelo solo ve nombre + descripción + parámetros". A los 12:03 checkpoint `--solo-tool`. A los 12:10 compara **descripciones** entre 2-3 equipos (¿cuál se llama de más/de menos?) y lanza el **experimento de contraste** (descripción vaga, ≈5 min) | Línea `tools usadas: ['consultar_estado_solicitud']`; la pregunta de normas **no** la usa; con la descripción vaga la elección de tool cambia | Entrega `solutions\04_herramienta_estado.py` a los 12:08 y que solo la ejecuten; omite el experimento de contraste y muéstralo tú en pantalla |
| 12:20 | 65-80 | **Revisión en parejas y preguntas técnicas** | Forma parejas; que cada una compare su agente/tool con la del compañero (3-4 min) y anote 1 diferencia de diseño. Abre turno de preguntas técnicas | Al menos una pareja comparte una diferencia en el chat | Si faltan parejas, hazlo como pregunta abierta al grupo completo |
| 12:35 | 80-85 | **Cierre del laboratorio** | Resume: agente con grounding (T1-2) + tool funcionando (T3). Anticipa que el Día 3 (módulo "Observabilidad y ciclo de vida") presenta de forma **conceptual** cómo leer trazas, diagnosticar un caso fallido y aplicar un checklist de éxito | Todos saben qué verán el Día 3 | — |

**Regla de oro del tiempo:** a los 11:55 todos deben tener un agente que responde con cita. Quien llegue sin eso, usa la solución y se concentra en la Tarea 3. Después de las 12:40 sigue el cierre del día (12:40–13:00).

---

## 3. Solución del defecto plantado (material opcional de instructor)

> **Ya no se practica con código en el laboratorio del Día 2 ni del Día 3**: el Día 3 presenta el diagnóstico de un caso
> fallido y el checklist de éxito de forma conceptual. Esta sección se conserva como referencia por si un participante
> pregunta o quieres mostrar un ejemplo real. Los diffs y las pistas siguen siendo válidos, porque usan los mismos
> archivos de este proyecto (`src\05_caso_fallido.py`, `instructores\`).

Detalle completo, pistas y *diffs* en `instructores\README.md`. Resumen:

| Caso | Defecto | Dónde se ve en la traza | Corrección |
|---|---|---|---|
| **1** (principal, determinista) | `NIVEL_SESION = "publico"`: el filtro de seguridad solo permite documentos públicos, así que NOR-001 (interno) nunca se recupera | Span `recuperacion-normativa`: `busqueda.filtro = search.in(nivel_acceso, 'publico', ',')`, `busqueda.ids = NOR-009-…,NOR-010-…`; el resultado de `execute_tool buscar_normativa` no contiene la respuesta | El nivel sale de la sesión/identidad (`cargar_settings().nivel_usuario`), no de una constante |
| **2** (variante) | Descripción de la tool vaga + parámetro descrito como "solo los dígitos finales" → `id_solicitud="3"` → `formato_invalido` | `execute_tool consultar_estado_solicitud`: argumentos `{"id_solicitud": "3"}` y resultado con `formato_invalido`; `gen_ai.tool.definitions` muestra la descripción errónea | Describir el formato completo `SOL-AAAA-NNNN` y cuándo usar la tool |

Mensaje de cierre: *"el checklist marcó ✔ usa la tool y ✔ sin errores en el caso 1: el problema era de datos (recuperación), invisible si solo miras el texto final. La traza lo muestra."*

---

## 4. Extensiones para quienes terminan antes (fast-finishers)

| # | Extensión | Tiempo | Cómo |
|---|---|---|---|
| 1 | **Fuera de alcance y nivel de acceso** | 3-5 min | Preguntas P05-P07 de `data\preguntas_evaluacion.jsonl` con `LAB_NIVEL_USUARIO=interno` y luego `restringido` |
| 2 | **Validación y errores de la tool** | 5 min | En `consultar_estado_solicitud`, rechazar años distintos de 2026 o devolver un error estructurado (`error`, `mensaje`); observar cómo el modelo explica el error en su respuesta |
| 3 | **Evaluación por lotes** (estilo *ai-rag-chat-evaluator*) | 10 min | `python solutions\extensiones\ext_evaluar.py` ejecuta las 11 preguntas (`question`/`truth`) y calcula negativa correcta, cita esperada y tool correcta. Para métricas con LLM (groundedness, relevancia, *citation matching*) ver `repos\publico-samples\ai-rag-chat-evaluator`; el SDK trae `LocalEvaluator`, `evaluate_agent`, `tool_calls_present` (`agent-framework\python\samples\02-agents\evaluation\evaluate_with_expected.py`) |
| 4 | **Recuperación con *context provider*** | 10-15 min | `pip install agent-framework-azure-ai-search` (beta) y, en lugar de la tool, `from agent_framework.azure import AzureAISearchContextProvider`; `AzureAISearchContextProvider(source_id=..., endpoint=..., index_name=..., credential=<aio>, mode="semantic", top_k=3)` y `Agent(..., context_providers=[provider])` dentro de `async with`. Muestra cómo cambia el flujo (no hay llamada a tool de búsqueda: el contexto se inyecta antes del modelo). Modo `agentic` con *knowledge base*: **(preview)**, requiere crear la knowledge base en Search (`search-get-started-agentic-retrieval`) |
| 5 | **Herramienta MCP** | 10 min | `from agent_framework import MCPStreamableHTTPTool`; `tools=MCPStreamableHTTPTool(name=..., description=..., url="<url del servidor MCP>")` dentro de `async with Agent(...)` (ver `02-agents\mcp\mcp_api_key_auth.py`). Usa un servidor MCP público/inofensivo (sin datos del banco) |
| 6 | **Desplegar como hosted agent** | 20+ min (demo del instructor) | Patrón de `foundry-samples\samples\python\hosted-agents\agent-framework\responses\02-tools` (tools) y `11-azure-search-rag` (RAG): `agent-framework-foundry-hosting`, `ResponsesHostServer`, `azd`. Requiere Python ≥ 3.13 y permisos de despliegue. La identidad del agente necesita *Search Index Data Reader*; y *Monitoring Metrics Publisher* si App Insights exige Entra ID. Ver también `repos\publico-workshops\foundry-hosted-agents-workshop` |
| 7 | **Trazas propias** (opcional, requiere Application Insights) | 5 min | Agregar atributos a `span_propio(...)` (p. ej. `busqueda.top`) y filtrarlos en KQL |

---

## 5. Alternativa .NET (solo para quien la pida)

El laboratorio está pensado y soportado en vivo **solo en Python**. Quien prefiera .NET puede seguir el mismo flujo (agente → grounding → tool) con:

- Workshop `repos\publico-workshops\Hosted_Agents_Workshop_dotNET` (hosted agents con Agent Framework en C#).
- Samples de Agent Framework para .NET: `repos\publico-samples\agent-framework\dotnet\samples\01-get-started`.
- Samples de Foundry en C#: `repos\publico-samples\foundry-samples\samples\csharp`.

Los datos (`data\`) y el índice son los mismos; no hay un starter .NET en este kit. Menciónalo brevemente y no dediques tiempo del lab.

---

## 6. Facilitación híbrida

- **Canal único de ayuda:** chat de Teams del evento. Pide que escriban el **mensaje de error exacto** (o captura) y su paso (Prep, T1…T3).
- **Reacciones como semáforo:** ✔ = listo, ✋ = necesito ayuda; al final de cada bloque pide un ✔.
- **Un instructor "pasillo" y otro "chat":** cada pregunta del chat con respuesta reutilizable se copia a un mensaje fijado (troubleshooting del README §8).
- **Pantalla compartida con fuente grande** y la terminal a ancho completo; evita abrir `.env` con valores en pantalla.
- **Participantes remotos:** misma carpeta de kit y mismas instrucciones; si no tienen permisos aún, que sigan tu pantalla y ejecuten `--solo-tool` (no requiere Azure) en las Tareas 2-3.
- **Parejas:** un participante con el entorno listo + uno sin entorno (pair programming) para no frenar el bloque.
- **Ritmo:** marca los checkpoints en voz alta ("a los 12:03 todos con `--solo-tool` ✔").

---

## 7. Plan B (si algo falla en vivo)

**Capturas y salidas para dejar listas (ensayo T-3 días), guardadas fuera del kit de participantes:**

| # | Qué capturar | Para qué |
|---|---|---|
| 1 | `00_verificar_entorno.py --probar-modelo` completo en verde | Comparar con quien falla |
| 2 | Salidas de `solutions\02_agente_base.py`, `03_agente_con_search.py` y `04_herramienta_estado.py` | Si el modelo o Search no responden |
| 3 | Captura del *Search explorer* con el filtro por `nivel_acceso` | Explicar security trimming |
| 4 | Salida de `ext_evaluar.py` (resumen % aprobado) | Extensión sin cuota |
| 5 | Video corto (≤ 2 min) del flujo completo | Falla general |

**Árbol de decisión:**

| Falla | Acción inmediata |
|---|---|
| Un participante sin entorno | Pareja con un vecino o sigue tu pantalla; `--solo-tool` en Tareas 2-3 no usa Azure |
| Permisos faltantes (403) en varios | Asigna el rol al grupo y espera ≤ 10 min; mientras tanto demo tuya y `--solo-tool` |
| 429 / cuota del modelo | Reparte entre deployments/proyectos o pide ejecutar de a uno por equipo; usa las salidas pre-capturadas |
| Embeddings o vectores fallan | Deja `FOUNDRY_EMBEDDING_MODEL=` vacío: la consulta usa texto + semántico (válido aunque el índice tenga campo vectorial) |
| Ranker semántico no disponible | `LAB_SIN_SEMANTICO=true` en el `.env` |
| Search no responde | Muestra salidas pre-capturadas; la Tarea 3 puede seguir con la tool de estado (no depende de Search) |

---

## 8. Preguntas frecuentes esperadas

| Pregunta | Respuesta corta |
|---|---|
| ¿Por qué el grounding es una *tool* y no un *context provider*? | Para que cada recuperación sea una llamada a tool explícita y visible (`búsqueda realizada`) y el modelo decida cuántas búsquedas hacer. El *context provider* (`AzureAISearchContextProvider`) inyecta contexto antes del modelo: es la extensión 4 |
| ¿Cómo pasaría esto a producción? | Identidad administrada, nivel de acceso desde los claims/grupos del usuario (o ACL por documento: `Quickstart-Document-Permissions-Push-API`), contenido de trazas desactivado (`enable_sensitive_data=False`), evaluación continua, red privada |
| ¿Qué es la recuperación agéntica de Azure AI Search? | *Knowledge base* que descompone la consulta en subconsultas y sintetiza (**preview**). En el lab, "agéntico" es el propio agente haciendo una búsqueda por subpregunta |
| ¿Dónde están los datos de BCI? | No hay: todo es ficticio (Austral Bank) |
| ¿Por qué no usamos llaves? | Microsoft Entra ID: `az login` local y identidad administrada en producción |

---

## 9. Referencias del material

- Código base: `repos\publico-workshops\foundry-hosted-agents-workshop` (`travel_assistant`), `repos\publico-samples\foundry-samples\samples\python\{quickstart,hosted-agents\agent-framework,prompt-agents,enterprise-agent-tutorial}`, `repos\publico-samples\agent-framework\python\samples`.
- Estructura de tareas: `repos\microsoftlearning-labs\mslearn-ai-agents` (C0-C4, D1 *Trace your agent*) y `repos\internal\agent-framework-workshop` (referencia interna, solo notas).
- Search: `repos\publico-samples\azure-search-python-samples`, `azure-search-openai-demo` (`docs\login_and_acl.md`), `docs-oficiales\azure-ai-search\`.
- Observabilidad: `docs-oficiales\foundry\observability\` (`trace-agent-setup`, `trace-agent-framework`, `trace-ingestion-entra-authentication`, `troubleshooting`), `docs-oficiales\foundry\agents\how-to\{configure-hosted-agent-telemetry,debug-hosted-agent}.md`.
- Láminas: `presentaciones\content\day2.json` (35-39 lab; 10, 26 y 30 demos).

---

## 10. Cierre post-sesión

- [ ] Reúne el feedback (qué tarea fue más difícil, tiempos reales) y ajusta `README.md`/tiempos.
- [ ] Comparte `solutions\` completo con todos.
- [ ] Revoca los roles temporales del grupo de participantes y elimina o desactiva el índice y los deployments de la sesión si no se reutilizan.
- [ ] Registra lo verificado en vivo contra la sección 11 y actualiza el kit.

## 11. Supuestos de API que debes verificar en vivo

Se contrastaron con los SDKs instalados (introspección sin llamar a Azure), pero **no** contra recursos reales:

| # | Supuesto | Dónde se usa | Si falla |
|---|---|---|---|
| 1 | `FoundryChatClient` funciona con la credencial **asíncrona** `azure.identity.aio.DefaultAzureCredential` (los samples usan `AzureCliCredential` síncrono) | Todos los scripts | Cambiar a `azure.identity.AzureCliCredential()` sin `async with` (como en los samples oficiales) |
| 2 | `agent.run(texto)` sin sesión y `agent.run(texto, session=session)` devuelven un objeto con `.text` | Tareas 1-3 | Revisar la salida real (`print(respuesta)`) |
| 3 | *(Opcional, material de trazas)* `await client.configure_azure_monitor(enable_sensitive_data=True)` toma la conexión del proyecto y los spans llegan a Application Insights con Entra ID del usuario | `trazas.py` | `APPLICATIONINSIGHTS_CONNECTION_STRING` en `.env`; `LAB_APPINSIGHTS_ENTRA=true`; consola |
| 4 | *(Opcional, material de trazas)* Un agente **local** (sin registrar) aparece en *Observability → Traces* del portal de Foundry | `05_trazas.py` | Usar Application Insights (Transaction search/KQL); según el sample, puede requerir registrar el agente con el mismo ID |
| 5 | *(Opcional, material de trazas)* KQL `union dependencies, requests \| where operation_Id == "<TRACE_ID>"` muestra los spans (`gen_ai.*` en `customDimensions`) | `instructores\README.md` | Ajustar tabla/columnas según el esquema real |
| 6 | *(Opcional, material de trazas)* El span propio `recuperacion-normativa` se anida bajo `execute_tool` y sus atributos `busqueda.*` son visibles | `05_caso_fallido.py` | Mostrarlos desde `gen_ai.tool.call.arguments/result` |
| 7 | Consulta semántica con `query_type="semantic"` + `semantic_configuration_name`, analizador `es.microsoft` y vector `k_nearest_neighbors = top*3` válidos en la región/SKU | `busqueda.py`, `01_crear_indice.py` | `LAB_SIN_SEMANTICO=true`; `--sin-vectores`; ajustar analizador |
| 8 | `FoundryEmbeddingClient.get_embeddings` + rol *Foundry User* alcanzan para embeddings; dimensiones coinciden con el deployment | `01_crear_indice.py` | `--recrear` con las dimensiones correctas |
| 9 | Versiones: `requirements.txt` (rangos) resuelve a versiones compatibles | Instalación | `pip install -r requirements-probado.txt` |
| 10 | *(Opcional, material de trazas)* El caso fallido 2 puede **autocorregirse**; el caso 1 falla siempre | `05_caso_fallido.py` | Ver `instructores\README.md` |
| 11 | Límites de índices por SKU si los participantes crean el suyo (opcional) | README Tarea 2 (recuadro) | Mantener un solo índice compartido |
| 12 | *(Opcional, material de trazas)* Nombres de spans/atributos (`invoke_agent`, `chat`, `execute_tool`, `gen_ai.tool.*`) coinciden con la versión instalada | `src\trazas.py` | Actualizar las referencias en `instructores\README.md` |

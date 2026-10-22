# Demo (Día 2) — Retrieval agéntico sobre un índice de normativa

Demo en vivo de la lámina **«Demo: retrieval sobre un índice de normativa»** (`presentaciones\content\day2.json`, Día 2). Un índice de Azure AI Search con la normativa ficticia de Austral Bank, un *knowledge base* que planifica **subconsultas en paralelo** y una respuesta con **citas verificables** que respeta el permiso del usuario simulado (*security trimming*).

> Todos los datos son ficticios. No hay llaves ni secretos: todo usa Microsoft Entra ID (`az login`); el servicio de Search tiene la autenticación por llave deshabilitada.

## Qué hay en esta carpeta

| Archivo | Para qué sirve |
|---|---|
| `scripts\mostrar-indice.ps1` | Paso 1: esquema del índice (texto, vector, metadatos de seguridad) y fragmentos por nivel de acceso. |
| `scripts\crear-knowledge-base.ps1` | Crea/actualiza (idempotente) el knowledge source `normativa-ks` y el knowledge base `normativa-kb`. |
| `scripts\consultar.ps1` | Pasos 2–4: pregunta al knowledge base como un usuario de nivel `publico`, `interno` o `restringido`; muestra subconsultas, respuesta, citas y fragmentos exactos. |
| `tests\validar-local.ps1` | Regresiones sin Azure: filtros con mayúsculas, rechazo antes de imprimir, citas, UTF-8 y errores de autenticación; simula todas las llamadas externas. |

El índice se crea con el código del laboratorio del Día 2 (`laboratorios\dia2-lab-procode`), que incorpora la configuración del vectorizador.

**Con los recursos ya preparados, no repitas el aprovisionamiento:** desde la raíz, ejecuta `cd presentaciones\demo-dia2-retrieval-normativa` y sigue directamente el guion. `mostrar-indice.ps1` y `consultar.ps1` solo leen/consultan; `crear-knowledge-base.ps1` modifica recursos.

## Recursos de esta demo

| Recurso | Valor |
|---|---|
| Suscripción | `Valentina-Subscription` (`0f90da9c-b7e8-4535-8394-777ee2651022`) |
| Resource group | `bci-workshop` |
| Azure AI Search | `bci-workshop-srch-fjdb` (`https://bci-workshop-srch-fjdb.search.windows.net`, SKU serverless, semantic ranker disponible) |
| Cuenta / proyecto Foundry | `bci-demo` / `bci-workshop` (`https://bci-demo.services.ai.azure.com/api/projects/bci-workshop`) |
| Despliegue de embeddings | `text-embedding-3-large` (3072 dimensiones) |
| Despliegue de chat (planificación y síntesis) | `gpt-5-mini-013161` (modelo `gpt-5-mini`) |
| Índice / knowledge source / knowledge base | `normativa-austral` (46 fragmentos de 12 documentos) / `normativa-ks` / `normativa-kb` |

El índice admite búsqueda **híbrida**: texto (BM25, analizador `es.microsoft`) + vectores (`vector`, 3072 dimensiones, `text-embedding-3-large`) + ranker semántico. El perfil vectorial lleva un **vectorizador** (`vectorizador-openai`, mismo despliegue de embeddings) que permite convertir texto en vectores; la identidad administrada de Search lo invoca (rol `Cognitive Services OpenAI User` sobre `bci-demo`). Para que el knowledge base use ese campo, su knowledge source también debe incluirlo entre los campos de búsqueda. El campo `vector` es `retrievable: false` a propósito (evita devolver 3072 números por fragmento): **no se devuelve en los documentos de Search explorer**, pero su definición sí aparece en el esquema. `mostrar-indice.ps1` comprueba el tamaño del índice vectorial y ejecuta una consulta vectorial pura; esto demuestra la capacidad del **índice**, no el uso de vectores por el KB.

### Evidencia y límite de la validación (22 de octubre de 2026, UTC)

- **Comprobado en Azure:** perfil `perfil-hnsw` → `vectorizador-openai`, modelo/deployment `text-embedding-3-large`, 46 fragmentos y ~1664 KiB de índice vectorial. Una consulta `vectorQueries` con `kind: text`, sin `search` ni ranker semántico, recupera `NOR-002-*`.
- **KB comprobado:** la pregunta interna de viajes y retención devuelve 350 USD por noche, 45 USD diarios y 6 años, con citas a `NOR-002-01` y `NOR-004-01`. La pregunta del SOC no revela su plazo a `interno`; `restringido` obtiene 15 minutos con `NOR-006-02`. Los filtros y niveles de referencias pasan las comprobaciones del script.
- **Hallazgo pendiente en Azure:** `normativa-ks` aún tiene `searchFields` limitados a `titulo`, `seccion` y `contenido`, excluyendo `vector`. Con la consulta exacta `lodging reimbursement ceiling`, texto devuelve 0 documentos y la búsqueda vectorial pura recupera viajes. El retrieve con `intents` (sin planificación), esfuerzo `minimal`, salida `extractiveData`, filtro interno y `resultsProcessing: none` devuelve 0 documentos. Esto apunta a la exclusión del vector en el KB actual; **no se ha demostrado que su retrieve use búsqueda vectorial**. Una buena respuesta a una paráfrasis con planificación tampoco lo probaría, porque el modelo puede reescribirla.
- La definición **local** de `crear-knowledge-base.ps1` ya omite `searchFields`, para incluir por defecto todos los campos `searchable`, también `vector`. **No se ha aplicado al servicio durante esta revisión de solo lectura.** Una actualización autorizada del knowledge source y una nueva prueba quedan pendientes; no hay que borrar ni recrear el índice.

Microsoft Learn documenta que el retrieval agéntico combina texto y vectores cuando el campo vectorial es `searchable` y tiene vectorizador, y que la fuente puede restringir los campos: [índice para retrieval agéntico](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-how-to-create-index) y [SearchFields](https://learn.microsoft.com/en-us/dotnet/api/azure.search.documents.indexes.models.searchindexknowledgesourceparameters.searchfields?view=azure-dotnet-preview). La respuesta cruda observada expone `search`, filtros, configuración semántica y `searchFields`, pero no un detalle `vectorQueries` ni trazas de invocación del vectorizador. La ausencia de ese detalle por sí sola no demuestra ausencia de búsqueda vectorial.

## Requisitos

- Azure CLI con sesión iniciada (`az login`) en la suscripción anterior, Python 3.10+ y PowerShell 7.
- Roles del usuario que ejecuta la demo (Owner en la suscripción **no** da acceso a datos de Search):

| Rol | Ámbito | Para qué |
|---|---|---|
| Search Service Contributor | servicio de Search | crear índice, knowledge source y knowledge base; leer el esquema con `mostrar-indice.ps1` |
| Search Index Data Contributor | servicio de Search | cargar y consultar documentos; para solo consultar basta Search Index Data Reader |
| Foundry User | proyecto `bci-workshop` (o ámbito superior heredado) | acceder al proyecto mediante `FoundryEmbeddingClient` del laboratorio |
| Cognitive Services OpenAI User | cuenta `bci-demo` | invocar el modelo de embeddings al indexar |

- El servicio de Search usa su **identidad administrada SystemAssigned**, con *Cognitive Services User* sobre `bci-demo` para la llamada del knowledge base al modelo. En este entorno también tiene *Cognitive Services OpenAI User*; la presencia de ambos no demuestra que ambos sean el mínimo necesario.
- **Validado en Azure:** llaves deshabilitadas, semantic search `standard`; el usuario tiene los roles de la tabla (Foundry User heredado de la suscripción) y la identidad de Search tiene los dos roles anteriores. No hace falta reasignarlos para ejecutar el guion.

## Preparación (hacer antes de la sesión)

Desde la raíz del repositorio, en PowerShell.

### 1. Roles e identidad administrada

Solo para preparar un entorno al que le falten permisos. Asignar roles requiere permisos de administración de RBAC (p. ej., Owner o Role Based Access Control Administrator al ámbito correspondiente); Search Service Contributor no permite asignarlos.

```powershell
az login
$sub = "0f90da9c-b7e8-4535-8394-777ee2651022"
az account set --subscription $sub
$yo  = az ad signed-in-user show --query id -o tsv
$search = "/subscriptions/$sub/resourceGroups/bci-workshop/providers/Microsoft.Search/searchServices/bci-workshop-srch-fjdb"
$foundry = "/subscriptions/$sub/resourceGroups/bci-workshop/providers/Microsoft.CognitiveServices/accounts/bci-demo"
$proyecto = "$foundry/projects/bci-workshop"

az role assignment create --assignee-object-id $yo --assignee-principal-type User --role "Search Service Contributor" --scope $search
az role assignment create --assignee-object-id $yo --assignee-principal-type User --role "Search Index Data Contributor" --scope $search
az role assignment create --assignee-object-id $yo --assignee-principal-type User --role "Cognitive Services OpenAI User" --scope $foundry
az role assignment create --assignee-object-id $yo --assignee-principal-type User --role "Foundry User" --scope $proyecto

# Identidad administrada del servicio de Search y sus permisos sobre Foundry
$mi = az search service update --name bci-workshop-srch-fjdb --resource-group bci-workshop --identity-type SystemAssigned --query identity.principalId -o tsv
az role assignment create --assignee-object-id $mi --assignee-principal-type ServicePrincipal --role "Cognitive Services OpenAI User" --scope $foundry
az role assignment create --assignee-object-id $mi --assignee-principal-type ServicePrincipal --role "Cognitive Services User" --scope $foundry
```

La propagación de roles puede tardar varios minutos; no reasignes permisos repetidamente si todavía no surten efecto.

Comprobación **solo lectura** (también sirve para verificar el entorno existente):

```powershell
az search service show -g bci-workshop -n bci-workshop-srch-fjdb --query "{sku:sku.name,disableLocalAuth:disableLocalAuth,semanticSearch:semanticSearch,identity:identity}" -o json
$search = az search service show -g bci-workshop -n bci-workshop-srch-fjdb --query id -o tsv
$mi = az search service show -g bci-workshop -n bci-workshop-srch-fjdb --query identity.principalId -o tsv
$yo = az ad signed-in-user show --query id -o tsv
$foundry = $search -replace "Microsoft.Search/searchServices/bci-workshop-srch-fjdb$", "Microsoft.CognitiveServices/accounts/bci-demo"
az role assignment list --assignee-object-id $yo --scope $search --include-inherited --query "[].{rol:roleDefinitionName,ambito:scope}" -o table
az role assignment list --assignee-object-id $yo --scope $foundry --include-inherited --query "[].{rol:roleDefinitionName,ambito:scope}" -o table
az role assignment list --assignee-object-id $yo --scope "$foundry/projects/bci-workshop" --include-inherited --query "[].{rol:roleDefinitionName,ambito:scope}" -o table
az role assignment list --assignee-object-id $mi --scope $foundry --include-inherited --query "[].{rol:roleDefinitionName,ambito:scope}" -o table
```

### 2. Entorno Python del laboratorio

```powershell
cd laboratorios\dia2-lab-procode
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 3. Crear el índice `normativa-austral`

Las variables de entorno solo viven en esta sesión de PowerShell (no se guardan en ningún archivo). **Antes de continuar, revisa si el laboratorio ya tiene `.env`: `src\config.py` lo carga con `override=True`, por lo que sus valores pisan los `$env:` siguientes.** Si existe, debe contener estos mismos valores (o apartarse antes de ejecutar). `.env.example` define los nombres correctos; no necesitas copiarlo para usar estas variables.

`FOUNDRY_EMBEDDING_MODEL` debe ser el nombre del **despliegue** de embeddings; en este proyecto es `text-embedding-3-large` (la documentación del laboratorio menciona `text-embedding-3-small`, que aquí no está desplegado). Si el despliegue tiene un alias, define además `FOUNDRY_EMBEDDING_MODEL_NAME` con el modelo real: el vectorizador requiere ambos datos. `FOUNDRY_MODEL` no es necesario para crear el índice; la planificación usa `DeploymentChat` del script de knowledge base.

```powershell
$env:FOUNDRY_PROJECT_ENDPOINT = "https://bci-demo.services.ai.azure.com/api/projects/bci-workshop"
$env:AZURE_SEARCH_ENDPOINT    = "https://bci-workshop-srch-fjdb.search.windows.net"
$env:AZURE_SEARCH_INDEX_NAME  = "normativa-austral"
$env:FOUNDRY_EMBEDDING_MODEL  = "text-embedding-3-large"

python src\01_crear_indice.py --dry-run     # valida los documentos sin llamar a Azure
python src\01_crear_indice.py               # crea/actualiza (con vectorizador), calcula embeddings y carga los fragmentos
cd ..\..
```

Salida esperada: `Índice 'normativa-austral' listo (vectores: 3072; vectorizador: text-embedding-3-large; ...)`, configuración semántica `normativa-semantica` y `46/46 fragmentos` cargados (niveles: `interno` 30, `restringido` 8, `publico` 8). El vectorizador se deriva del endpoint del proyecto (`https://bci-demo.openai.azure.com`). Agregar un vectorizador a un índice existente no requiere borrar sus documentos; se puede actualizar su configuración. Reserva `--recrear` para cambios de esquema incompatibles, como dimensiones distintas: **borra el índice si ya existe**, y nunca es una comprobación previa de la demo.

### 4. Crear knowledge source y knowledge base

```powershell
cd presentaciones\demo-dia2-retrieval-normativa
.\scripts\crear-knowledge-base.ps1
```

Salida esperada: `Knowledge source 'normativa-ks' listo` y `Knowledge base 'normativa-kb' listo`. El script usa la API `2026-08-01-preview` (el LLM del knowledge base requiere la versión preview).

### 5. Prueba previa

```powershell
.\scripts\mostrar-indice.ps1
.\scripts\consultar.ps1
```

## Guion de la demo (pasos de la lámina)

Ejecutar desde `presentaciones\demo-dia2-retrieval-normativa`.

| # | Paso de la lámina | Qué hacer | Resultado esperado |
|---|---|---|---|
| 1 | Mostrar el índice con campos de texto, vector y metadatos de seguridad | `.\scripts\mostrar-indice.ps1` | Campos `titulo`, `seccion`, `contenido`, `area` (texto, analizador `es.microsoft`), `vector` (3072 dimensiones, no recuperable) y `nivel_acceso` (filtrable, metadato de seguridad); vectorizador `vectorizador-openai` → `text-embedding-3-large`; índice vectorial de ~1,7 MB para 46 documentos; 46 fragmentos: interno 30, publico 8, restringido 8. La **prueba vectorial pura** (paráfrasis sobre viajes) devuelve `NOR-002-*` (Reglamento de viajes y viáticos). No prueba el uso vectorial del KB. |
| 2 | Hacer una pregunta ambigua que requiere dos subconsultas | `.\scripts\consultar.ps1 -Nivel interno` (pregunta por defecto: límite de gasto por noche en viaje nacional **y** años de conservación de comprobantes) | Una sola pregunta mezcla dos temas (NOR-002 y NOR-004). |
| 3 | Ver cómo el retrieval agéntico genera subconsultas en paralelo | Mismo comando: sección «Subconsultas ejecutadas» | Habitualmente **2 o más subconsultas**, con sus filtros reales y los intervalos UTC de `activity`. `Paralelismo ...: True` confirma intervalos solapados; inicios cercanos por sí solos no lo prueban. |
| 4 | Revisar las citas devueltas y el fragmento exacto usado | Mismo comando: sección «Citas devueltas» | **350 USD por noche de alojamiento + viático diario de 45 USD**, fuente `NOR-002-01`, y **6 años**, fuente `NOR-004-01`. Los marcadores reales son `[ref_id:N]` (N varía), asociados al `docKey`, texto exacto, sección, nivel y score de cada referencia. |

La redacción y el número de subconsultas pueden variar entre ejecuciones (el planificador es un LLM); contrasta siempre los datos con los fragmentos, no con una redacción memorizada. En las pruebas se recuperaron los dos temas y hubo dos subconsultas, aunque sus textos mezclaban ambos asuntos: no prometas una división limpia de una consulta por tema. Si no hay solapamiento, no afirmes que esa ejecución fue paralela; repite o muestra la captura preparada.

### Mostrar el control de permisos (security trimming)

Pregunta con respuesta **solo** en un documento restringido (NOR-006, respuesta a incidentes):

```powershell
$p = "En cuanto tiempo debe confirmar el SOC un incidente de severidad 1?"
.\scripts\consultar.ps1 -Pregunta $p -Nivel interno        # usuario sin permiso
.\scripts\consultar.ps1 -Pregunta $p -Nivel restringido    # usuario con permiso
```

| Usuario simulado | Filtro aplicado a cada subconsulta | Resultado |
|---|---|---|
| `interno` | `search.in(nivel_acceso, 'publico,interno', ',')` | «No encontré … un plazo explícito»; ninguna referencia con nivel `restringido`. |
| `restringido` | `search.in(nivel_acceso, 'publico,interno,restringido', ',')` | **15 minutos** (documento NOR-006). |

**Diferencia observada al repetir la prueba:** la salida completa de `interno` puede contener «15 minutos» en una referencia **autorizada** (`NOR-008-01`, RPO de continuidad, no plazo del SOC). Por eso buscar esa cadena en toda la salida no prueba una fuga. Comprueba que la respuesta no atribuya ese plazo al SOC y que ninguna referencia sea restringida ni proceda de NOR-006; con `restringido`, la evidencia correcta es `NOR-006-02`. No ocultes un fragmento autorizado para aparentar que la cadena nunca aparece.

Mensaje clave: aquí **`-Nivel` es una simulación controlada por el instructor, no una identidad autenticada ni una ACL nativa de Search**. El script construye `filterAddOn`, comprueba el filtro real de cada subconsulta y verifica todos los niveles de las referencias **antes** de mostrar la respuesta, incluso con `-Crudo`. Si faltan metadatos o hay una referencia fuera de permiso, se detiene sin imprimirla. La última línea confirma `con nivel fuera del permiso del usuario: 0`.

En producción el backend debe obtener el nivel de una identidad autenticada, no aceptar libremente `-Nivel` del cliente, y evitar que este consulte Search directamente con una credencial de lectura global. El filtro limita los documentos recuperados; no demuestra por sí solo que toda afirmación del LLM esté fundamentada.

### Preguntas de apoyo

Más preguntas en `laboratorios\dia2-lab-procode\data\preguntas_evaluacion.jsonl`. Dos útiles:

```powershell
# Sin respuesta en el corpus: debe decir que no lo encuentra, sin inventar
.\scripts\consultar.ps1 -Pregunta "Cual es la politica de teletrabajo para empleados en el extranjero?" -Nivel restringido
# Respuesta cruda (JSON con activity, references y sourceData) por si preguntan cómo se ve la API
.\scripts\consultar.ps1 -Crudo
```

## Problemas frecuentes

Pruebas de regresión locales, desde esta carpeta: `pwsh -NoProfile -File .\tests\validar-local.ps1`. No necesitan Azure ni modifican recursos.

| Síntoma | Causa y solución |
|---|---|
| `403 Forbidden` al crear/consultar | Faltan roles o no se han propagado. Verifica los roles de la sección *Requisitos* y espera unos minutos; ejecuta `az login` otra vez para renovar el token. |
| `crear-knowledge-base.ps1` funciona pero `consultar.ps1` falla con error del modelo (401/403) | La identidad administrada de Search no tiene `Cognitive Services User` sobre `bci-demo` (ver paso 1). |
| `DeploymentNotFound` al indexar | El despliegue de embeddings no existe con ese nombre: define `$env:FOUNDRY_EMBEDDING_MODEL` con un despliegue real (`az cognitiveservices account deployment list -g bci-workshop -n bci-demo -o table`). Si cambias de modelo cambian las dimensiones: recrea el índice con `--recrear`. |
| Aparece un error de ranker semántico | El servicio no tiene semantic search habilitado; usa el plan B. |
| La respuesta no trae marcadores `[ref_id:N]` | El script advierte y muestra hasta 3 referencias de apoyo, **no citas ni fragmentos cuyo uso esté verificado**. Repite la pregunta; esa ejecución no cumple el paso 4. Una cita a un ID inexistente detiene la presentación. |
| El script se detiene porque no puede verificar el recorte de seguridad | No muestres el resultado como si fuera correcto. Revisa sourceData, la fuente configurada y los filtros de activity; no desactives la comprobación. |
| `403`/`401` desde el vectorizador (consultas con `vectorQueries` o retrieve) | La identidad administrada de Search necesita `Cognitive Services OpenAI User` sobre `bci-demo` (paso 1). |
| Número de subconsultas distinto al de la lámina | Es normal (2 o 3). Si solo sale 1, reformula la pregunta para que mezcle dos temas. |

## Plan B

- **Sin semantic ranker:** el knowledge source de esta demo depende de él. `LAB_SIN_SEMANTICO=true` solo afecta al retrieval clásico del laboratorio, **no** a estos scripts ni al knowledge base. Usa ese flujo clásico o el respaldo grabado y explica la diferencia; no recrees el índice en vivo.
- **Sin vectores:** `python src\01_crear_indice.py --sin-vectores --recrear` crea un índice solo texto + semántico (sin vectorizador); el knowledge base sigue funcionando, pero sin búsqueda vectorial. No lo hagas en vivo.
- **Sin red o sin Foundry:** `consultar.ps1 -Crudo` **también llama a Azure**, no reproduce archivos. Sigue **PB-D2-03** (retrieval con dos usuarios) y **PB-D2-05** (esquema y conteos) de `laboratorios\entorno-y-facilitacion\plan-b-demos.md`. El catálogo es una lista de preparación: no garantiza que los videos/capturas ya existan.

Para preparar un respaldo JSON, **con conexión y antes de la sesión**, desde esta carpeta:

```powershell
.\scripts\consultar.ps1 -Nivel interno -Crudo | Set-Content -Encoding utf8 .\respaldo-interno.json
$p = "En cuanto tiempo debe confirmar el SOC un incidente de severidad 1?"
.\scripts\consultar.ps1 -Pregunta $p -Nivel interno -Crudo | Set-Content -Encoding utf8 .\respaldo-soc-interno.json
.\scripts\consultar.ps1 -Pregunta $p -Nivel restringido -Crudo | Set-Content -Encoding utf8 .\respaldo-soc-restringido.json
```

Revisa que los tres archivos sean JSON completos y respeten los niveles simulados; oculta identificadores del entorno en capturas compartidas según el catálogo y no subas estos respaldos al repositorio. Graba además la salida de `mostrar-indice.ps1` para PB-D2-05.

Para reproducir **sin ninguna llamada de red**, por ejemplo:

```powershell
$r = Get-Content -Raw -Encoding utf8 .\respaldo-interno.json | ConvertFrom-Json
$r.response.content.text
$r.activity | Where-Object type -eq searchIndex | Select-Object id, startedAt, completedAt, searchIndexArguments
$r.references | Select-Object id, docKey, sourceData | ConvertTo-Json -Depth 10
```

Aclara que es una respuesta guardada, no una consulta en vivo. Los archivos anteriores deben prepararse: no vienen incluidos en esta carpeta.

## Limpieza

**Opcional y destructiva; no forma parte del guion ni de la validación.** Elimina solo los objetos de esta demo:

```powershell
$token = az account get-access-token --resource https://search.azure.com --query accessToken -o tsv
$h = @{ Authorization = "Bearer $token" }
$base = "https://bci-workshop-srch-fjdb.search.windows.net"; $v = "api-version=2026-08-01-preview"
Invoke-RestMethod -Method Delete -Headers $h -Uri "$base/knowledgebases/normativa-kb?$v"
Invoke-RestMethod -Method Delete -Headers $h -Uri "$base/knowledgesources/normativa-ks?$v"
Invoke-RestMethod -Method Delete -Headers $h -Uri "$base/indexes/normativa-austral?$v"
```

Esto no elimina el servicio de Search, la cuenta Foundry, los despliegues ni sus asignaciones RBAC. Revísalos aparte con el administrador y comprueba la facturación de los recursos que sigan aprovisionados.

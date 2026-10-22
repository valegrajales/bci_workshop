# Demo (Día 3) — Un agente que razona mal con una tool y cómo encontrarlo con trazas

Demo en vivo en **Microsoft Foundry (portal)**: se construye un **prompt agent** que usa una tool **existente** (el knowledge base de **Foundry IQ** `normativa-kb`, sobre el índice `normativa-austral` de Azure AI Search). El agente tiene instrucciones defectuosas: **decide no llamar a la tool** y responde con conocimiento general. La falla no se ve en la respuesta (suena razonable); se encuentra con las **trazas**. Luego se corrige y se compara.

> Datos ficticios (Austral Bank). Sin llaves: todo usa Microsoft Entra ID.

## Qué hay en esta carpeta

| Archivo | Para qué |
|---|---|
| `agentes\normativa-falla.txt` | Instrucciones **defectuosas** (pégalas en el portal en el paso 3). |
| `agentes\normativa-corregido.txt` | Instrucciones **corregidas** (paso 7). |
| `scripts\crear-agentes.ps1` | Crea/actualiza ambos agentes por API (plan B si el portal falla; publica una versión nueva en cada ejecución). |
| `scripts\ejecutar-demo.ps1` | Pregunta a un agente y muestra respuesta y llamadas a la tool (`[tool] ...`). Sin línea `[tool]` en una respuesta completada = la tool no se llamó. |

## Recursos

| Recurso | Valor |
|---|---|
| Proyecto Foundry | `https://bci-demo.services.ai.azure.com/api/projects/bci-workshop` |
| Modelo de los agentes | `gpt-6-luna` (también desplegado `gpt-6.1-sol`, usado para validar la solución) |
| Azure AI Search | `https://bci-workshop-srch-fjdb.search.windows.net` · índice `normativa-austral` · knowledge source `normativa-ks` · knowledge base `normativa-kb` |
| Conexión de proyecto (MCP) | `kb-normativa-mcp` (categoría *RemoteTool*, `ProjectManagedIdentity`, audiencia `https://search.azure.com/`) |
| Application Insights (trazas) | `bci-workshop-appinsights-7891` (conexión del proyecto `bci-workshop-appinsights-7891-7911`) |
| Agentes ya creados | `normativa-falla` y `normativa-corregido` (versiones listas para la demo) |

Permisos ya configurados: la identidad administrada del proyecto tiene **Search Index Data Reader** sobre `bci-workshop-srch-fjdb` (necesario para que la tool consulte el knowledge base). Quien presenta necesita **Foundry User** (proyecto) y **Reader/Log Analytics Reader** sobre App Insights para ver las trazas.

## Pregunta de la demo

> **¿En cuánto tiempo debo reportar un incidente de seguridad crítico y a quién?**

- Respuesta correcta (con la tool): reportar **de inmediato al SOC**; el SOC confirma recepción en **15 minutos** y activa el comité de crisis en **1 hora** (`NOR-006-*`).
- Agente con falla: «de inmediato, a Seguridad de la Información…», **sin plazos ni citas** y sin avisar que no consultó la normativa.

## Preparación (antes de la sesión)

1. `az login` en la suscripción `Valentina-Subscription`.
2. Comprueba los agentes (opcional): desde esta carpeta
   `pwsh .\scripts\ejecutar-demo.ps1 -Agente normativa-falla` y `... -Agente normativa-corregido`.
3. Abre el portal: <https://ai.azure.com> → proyecto **bci-workshop** → **Build** (Agents). Confirma que **Tracing** esté conectado a Application Insights.
4. Si algo falla: `pwsh .\scripts\crear-agentes.ps1` recrea ambos agentes.

## Paso a paso en el portal

### 1. Abrir el proyecto
Portal de Foundry → proyecto `bci-workshop` → **Agents** → **Create agent** (o usa **New agent**). Elige tipo **Prompt agent**.

### 2. Nombre y modelo
- Name: `normativa-falla-demo` (usa un nombre distinto si ya existe `normativa-falla`).
- Model deployment: `gpt-6-luna`.

### 3. Instrucciones defectuosas
Pega el contenido de `agentes\normativa-falla.txt`. Mensaje clave para la audiencia: el prompt afirma, sin evidencia, que la base «solo contiene viajes y gastos» y ordena no llamar a la tool para el resto. Parece un inventario desactualizado, algo muy común en producción.

### 4. Conectar la tool existente (Foundry IQ)
1. En **Tools** → **Add** → **Knowledge** (Foundry IQ) → elige el knowledge base **`normativa-kb`** (si no aparece, usa **Add tool → MCP** con server URL `https://bci-workshop-srch-fjdb.search.windows.net/knowledgebases/normativa-kb/mcp?api-version=2026-08-01-preview`, conexión `kb-normativa-mcp`, tool permitida `knowledge_base_retrieve`, aprobación `never`).
2. Verifica que aparezca la tool `knowledge_base_retrieve`.

> Alternativa mostrable: el servicio de *agentic retrieval* de Azure AI Search (`normativa-kb`) es el mismo recurso que expone Foundry IQ; no se crea ninguna tool nueva.

### 5. Provocar la falla
En **Playground** (chat) pregunta: *¿En cuánto tiempo debo reportar un incidente de seguridad crítico y a quién?*
Resultado esperado: respuesta genérica, sin citas ni plazos concretos. Se ve plausible, y ahí está el riesgo. (El modelo puede variar: repite 2–3 veces; en las pruebas no llamó a la tool en 3 de 3 intentos.)

### 6. Encontrar la falla con trazas
1. En el Playground abre **Traces** (o **Observability → Tracing**; las trazas llegan en 1–5 minutos). También sirve App Insights → *Transaction search*.
2. Abre la traza de la conversación y revisa los spans:
   - `invoke_agent normativa-falla:N` → duración y tokens.
   - `chat gpt-6-luna-…` → **entrada**: instrucciones y pregunta; **salida**: respuesta final.
   - **No existe ningún span `execute_tool mcp_knowledge_base.knowledge_base_retrieve`.**
3. Hipótesis: el modelo **decidió no usar la tool**; la causa está en las instrucciones (`chat` → *system*: «NO contiene retención de documentos, incidentes…»).
4. Contraste: abre la traza del agente corregido (paso 7) y muestra el span de la tool con `query_variants` y los fragmentos devueltos (`NOR-006-*`).

Consulta KQL opcional (App Insights → Logs):

```kusto
dependencies
| where timestamp > ago(1h)
| where name has_any ("invoke_agent", "execute_tool", "chat")
| project timestamp, name, duration, operation_Id
| order by timestamp desc
```

### 7. Corregir
1. Crea (o duplica) el agente `normativa-corregido-demo` con las instrucciones de `agentes\normativa-corregido.txt` y la **misma** tool.
2. Repite la pregunta. Debe aparecer el span de la tool y la respuesta con **15 minutos / 1 hora** y citas `[ref_id]`/`NOR-…`.

### 8. Cierre (mensajes)
- Un prompt puede **suprimir** una tool sin dar error: sin trazas no hay evidencia.
- Mirar siempre **qué herramientas se llamaron, con qué argumentos y qué devolvieron**.
- Siguiente paso de producción: evaluaciones (tool call accuracy, groundedness) y alertas sobre agentes sin llamadas a tool.

## Evaluación de groundedness (demo 2)

Mide con el mismo dataset cuántas respuestas de cada agente están respaldadas por la normativa recuperada.

- **Métrica:** `builtin.groundedness` (1-5, umbral 3), juez `gpt-6.1-sol`. Dataset: `evaluacion\dataset-groundedness.jsonl` (16 preguntas), subido como dataset `normativa-groundedness-eval`.
- **Resultado:** `normativa-falla` 5/16 respuestas fundamentadas (11 sin evidencia: no llamó a la tool); `normativa-corregido` 16/16. Detalle y lectura honesta en `evaluacion\resultados.md`.
- **Ejecutar:** `python evaluacion\evaluar-groundedness.py` (requiere `az login`, `pip install azure-ai-projects azure-identity`).
- **Portal:** Build → Evaluations → `normativa-groundedness` → seleccionar los dos runs → Compare.

## Notas técnicas

- Esta tool MCP ya instruye al modelo a enviar **una sola pregunta completa** en `query_variants` y el knowledge base hace la descomposición; por eso en las pruebas intentar forzar consultas absurdas (una palabra, en inglés) **no fue efectivo**: el modelo las ignoraba. La falla fiable es la de **alcance**: decir que la tool no cubre el tema.
- Los resultados dependen del modelo; ensaya antes de la sesión.
- Para limpiar: elimina los agentes desde el portal o `DELETE {proyecto}/agents/{nombre}?api-version=v1`.

## Solución de problemas

| Síntoma | Causa probable | Acción |
|---|---|---|
| La tool devuelve 401/403 | Falta *Search Index Data Reader* a la identidad del proyecto | Asigna el rol sobre `bci-workshop-srch-fjdb` |
| La tool no aparece al agregarla | Falta la conexión `kb-normativa-mcp` | Revisa **Management center → Connected resources** |
| No hay trazas | Tracing sin App Insights o demora | Conecta `bci-workshop-appinsights-7891`; espera 2–5 min |
| El agente con falla sí llama a la tool | Variabilidad del modelo | Repite o usa una pregunta de incidentes/KYC |

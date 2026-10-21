# Instructores — Caso fallido de observabilidad (material opcional de instructor) (NO distribuir esta carpeta)

Esta carpeta es solo para Pablo Braconi y Valentina Grajales. Explica los dos defectos plantados en
`src\05_caso_fallido.py`, cómo se ven en la traza y cómo corregirlos. Los participantes reciben el script
**sin** esta guía y deben diagnosticar mirando solo las trazas.

> Este ejercicio (antes la "Tarea 4" del laboratorio pro-code del Día 2) **ya no se practica con código**: el
> módulo "Observabilidad y ciclo de vida" del Día 3 presenta el diagnóstico de un caso fallido y el checklist de éxito
> de forma conceptual. Este material se conserva como referencia del instructor y para quien quiera ensayarlo de
> forma opcional (mismo entorno, mismo agente, mismo índice de `dia2-lab-procode/`); el contenido técnico no cambia.

> Aún no se ha validado contra recursos reales de Azure: si decides ensayarlo, ejecuta ambos casos en la suscripción
> de prueba (ver `checklist-validacion.md`, puntos opcionales 12–15) y ajusta los textos de "qué debería verse".

## Cómo ejecutar

```bash
python src/05_caso_fallido.py --caso 1      # defecto de recuperación (determinista)  <- caso para todos
python src/05_caso_fallido.py --caso 2      # defecto de descripción de la herramienta (variante, para quienes terminen antes)
python instructores/05_caso_fallido_corregido.py --caso 1    # mismo caso con las herramientas correctas
```

Pregunta del caso 1 (la misma que C1 de `src\agente_lab.py`): *"¿Cuál es el límite mensual de gasto con
tarjeta corporativa para el nivel Jefatura?"* — respuesta correcta: **2.500 USD/mes** `[NOR-001-xx]`.

## Defecto 1 — filtro de seguridad demasiado estricto (`NIVEL_SESION = "publico"`)

| Qué | Detalle |
|---|---|
| Dónde | `src\05_caso_fallido.py`, constante `NIVEL_SESION = "publico"` usada por `_buscar_v2` |
| Código sano | `agente_lab.buscar_normativa` toma el nivel de `LAB_NIVEL_USUARIO` (por defecto `interno`) |
| Efecto | El filtro OData queda `search.in(nivel_acceso, 'publico', ',')`: solo se pueden recuperar NOR-009 (conducta) y NOR-010 (denuncias). El límite de gasto está en NOR-001 (`interno`) y nunca se recupera |
| Síntoma visible | El agente responde "No tengo información en la normativa disponible para tu nivel de acceso" o, peor, improvisa una cifra. El checklist marca ✘ **cita fuente**/**responde** (la respuesta no contiene "2.500") |
| Ojo | El modelo **sí** llamó a la herramienta (✔ usa la tool) y **no hay excepciones** (✔ sin errores). Por eso hay que leer la traza: el problema es de datos, no de ejecución |

**Dónde verlo en la traza (qué buscar, en este orden):**

1. `invoke_agent asistente-normativa` → duración total y número de `chat` hijos (normalmente 2: uno con `finish_reason = tool_calls` y otro con `stop`).
2. `execute_tool buscar_normativa` → `gen_ai.tool.call.arguments` (la consulta que armó el modelo es razonable) y `gen_ai.tool.call.result` (empieza con fragmentos de NOR-009/NOR-010 o con `SIN_RESULTADOS…`: **el resultado no responde la pregunta**).
3. Span hijo `recuperacion-normativa` (atributos propios): `busqueda.filtro = search.in(nivel_acceso, 'publico', ',')`, `busqueda.resultados`, `busqueda.ids = NOR-009-…,NOR-010-…`. **Aquí está la causa raíz.**
4. `chat` final → la respuesta del modelo se basa en lo que recibió; el modelo no "alucinó" sin motivo.

Conclusión que esperamos del participante: *"la consulta es buena pero el filtro `nivel_acceso` excluye NOR-001; el
problema está en la recuperación, no en el modelo ni en el prompt"*. Si propone cambiar el prompt o subir el
modelo, guíalo a abrir el span `recuperacion-normativa`.

**Corrección:** que el nivel salga de la identidad/sesión real (aquí `LAB_NIVEL_USUARIO`, por defecto `interno`) y no
de una constante fija:

```diff
-    filtro = construir_filtro_acceso(NIVEL_SESION)
+    filtro = construir_filtro_acceso(cargar_settings().nivel_usuario)
```

Comprobación: `python instructores/05_caso_fallido_corregido.py --caso 1` → 4 de 4 ✔ y `busqueda.ids` contiene `NOR-001-…`.

Conversación de cierre (security trimming): el nivel **nunca** es un parámetro que decida el modelo; en producción
sale del token del usuario (grupos/oid → filtro `search.in(...)` o ACL de documento). Referencia:
`azure-search-openai-demo` (document-level access control).

## Defecto 2 — descripción de la herramienta que induce un argumento inválido (variante)

| Qué | Detalle |
|---|---|
| Dónde | `_estado_v2` en `src\05_caso_fallido.py` |
| Código sano | `agente_lab.consultar_estado_solicitud`: docstring "Consulta el estado actual de UNA solicitud…" y parámetro "Identificador completo con formato SOL-AAAA-NNNN" |
| Defecto | Descripción vaga ("Consulta el estado de un trámite.") y parámetro descrito como "solo los dígitos finales, p. ej. 3" |
| Efecto | El modelo llama `consultar_estado_solicitud(id_solicitud="3")` → la función devuelve `{"encontrada": false, "error": "formato_invalido", …}` |
| Comportamiento esperado | Puede **auto-corregirse**: el mensaje de error incluye el formato correcto y el modelo reintenta con `SOL-2026-0003`. **Verifícalo en vivo**: si se auto-corrige, la traza igual muestra 2 `execute_tool` (el primero con error) y el checklist marca ✘ "sin errores" porque `registrar(... ok=False)` quedó en el registro |

**Dónde verlo:** `execute_tool consultar_estado_solicitud` (primer span): `gen_ai.tool.call.arguments = {"id_solicitud": "3"}`,
`gen_ai.tool.call.result` con `formato_invalido`; y en `invoke_agent` → `gen_ai.tool.definitions` aparece la descripción
errónea que causó el argumento.

**Corrección:** describir la herramienta con el formato completo y cuándo usarla:

```diff
-    id_solicitud: Annotated[str, Field(description="Número correlativo de la solicitud (solo los dígitos finales, p. ej. 3).")],
+    id_solicitud: Annotated[str, Field(description="Identificador completo con formato SOL-AAAA-NNNN, p. ej. SOL-2026-0003.")],
 ...
-    """Consulta el estado de un trámite."""
+    """Consulta el estado actual de UNA solicitud interna de Austral Bank (estado, fecha y responsable).
+    Úsala solo si el usuario menciona un identificador de solicitud; no sirve para preguntas sobre normas."""
```

Si el caso 2 no falla de forma visible en tu ensayo (el modelo infiere el formato), úsalo igual como ejemplo de
"los errores recuperables también aparecen en la traza" y vuelve al caso 1 como ejercicio principal.

## Pistas escalonadas (si un equipo se atasca > 3 min)

1. "¿Llamó a alguna herramienta? ¿Cuál? Abre el span `execute_tool` y compara argumentos con resultado."
2. "El resultado de la herramienta, ¿contiene la respuesta a la pregunta?"
3. "Abre el span `recuperacion-normativa` y mira `busqueda.filtro` y `busqueda.ids`."
4. "Compara el filtro con el `nivel_acceso` de NOR-001 (en `data\normativa\NOR-001-limites-de-gasto.md`)."

## Dónde abrir la traza (portal y KQL)

| Dónde | Cómo |
|---|---|
| **Portal de Foundry** | [ai.azure.com](https://ai.azure.com) → proyecto → **Observability** → **Traces** → abre la traza más reciente (o filtra por el Trace ID). Si un agente local no aparece, usa Application Insights: es la misma telemetría |
| **Application Insights** | Portal de Azure → el Application Insights conectado al proyecto → **Investigate → Search → Transaction search** → pega el Trace ID → *View all telemetry* |
| **Logs (KQL)** | `union dependencies, requests \| where operation_Id == "<TRACE_ID>" \| order by timestamp asc` *(verifica los nombres de tabla en tu entorno)*; los atributos `gen_ai.*` están en `customDimensions` |
| **Consola** (plan B) | En el `.env`: `ENABLE_CONSOLE_EXPORTERS=true` y vuelve a ejecutar: los spans se imprimen como JSON |

## Si la traza no aparece en el portal / Application Insights (plan B)

- Pasa `ENABLE_CONSOLE_EXPORTERS=true` en el `.env` del participante: los spans se imprimen en la consola
  (busca `name`, `attributes` → `gen_ai.tool.call.arguments`, `busqueda.filtro`).
- Entrega la **traza pre-capturada** (screenshots/JSON de tu ensayo opcional; ya no forma parte de la lista de capturas del Plan B de `guia-facilitador.md`).
- El script imprime el `Trace ID` para buscarlo; la ingestión puede demorar 2-5 minutos.

## Restablecer

No hay estado que limpiar: el caso fallido no modifica el índice ni los datos. Solo hay que volver a ejecutar el
script. `registro_herramientas.limpiar()` se llama al inicio de cada caso.

## Reglas para no revelar el defecto

- No compartas `instructores\` (excluirla de la copia que se entrega a participantes). `solutions\` sí se puede compartir durante la sesión (no contiene la corrección del caso fallido).
- Tras la sesión, muestra el diff de arriba en pantalla y lo que cambió en la traza (antes/después).

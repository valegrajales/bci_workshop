# Checklist de validación — Smoke test previo a la sesión (Día 2, laboratorio pro-code)

**Cuándo:** 2-3 días antes del 22 de octubre de 2026 (y 1 hora antes, solo los puntos 3 y 4).
**Dónde:** en la **suscripción real** del taller, con una **cuenta de prueba de participante** (sin roles de instructor) para validar permisos.
**Por qué:** el kit se validó localmente (`py_compile` + `pytest`), pero **nunca contra recursos reales de Azure**. Anota cada resultado y las desviaciones.
Detalle de los supuestos de API en `guia-facilitador.md` §11. Ejecuta desde `laboratorios/dia2-lab-procode-codespaces/` dentro de un Codespace (Python 3.12 ya configurado).
**Alcance del laboratorio (85 min, Tareas 1-3):** los puntos 1-11 y 17-20 son obligatorios. Los puntos 12-16 (trazas y caso fallido) son **opcionales**: ese contenido ya no se practica con código, el Día 3 lo presenta de forma conceptual.

| # | Verificación (comando / acción) | Resultado esperado | ✔ / notas |
|---|---|---|---|
| 1 | Codespace nuevo (Python 3.12, desde una cuenta distinta a la del instructor): el `postCreateCommand` instala `requirements-dev.txt`; anota versiones con `pip list` (`agent-framework-foundry`, `azure-search-documents`, `azure-monitor-opentelemetry`) | Instala sin conflictos; versiones compatibles con `requirements-probado.txt` (si no, usar ese archivo) | ☐ |
| 2 | `python -m pytest` (instala `requirements-dev.txt`) | 107 pruebas en verde (no usan Azure) | ☐ |
| 3 | `az login` con la cuenta de prueba; completar `.env` con endpoint/deployments reales | `az account show` correcto; `.env` sin valores `<...>` | ☐ |
| 4 | `python src/00_verificar_entorno.py --probar-modelo` | Todo ✔: tokens de `ai.azure.com` y `search.azure.com`, índice con fragmentos, deployment responde `OK` | ☐ |
| 5 | Roles de la cuenta de prueba (Foundry User, Search Index Data Reader; Log Analytics Reader solo si harás los puntos opcionales 12-16) | Sin 401/403 en los puntos 4, 8 y 11; propagación ≤ 10 min | ☐ |
| 6 | Instructor: `python src/01_crear_indice.py --dry-run` y luego `python src/01_crear_indice.py` | `12 documentos, 46 fragmentos`; índice `normativa-austral` con 46 documentos (Search explorer) | ☐ |
| 7 | Search explorer: filtro `search.in(nivel_acceso, 'publico', ',')` vs `'publico,interno'` con la consulta `límite Jefatura` | Con `publico` **no** aparece NOR-001-02; con `publico,interno` sí | ☐ |
| 8 | `python solutions/02_agente_base.py` | Responde en español, mantiene la sesión y **no inventa** el límite de Austral Bank | ☐ |
| 9 | `python solutions/03_agente_con_search.py --solo-tool` y luego sin flag | Fragmentos `[NOR-001-02]`; respuesta con cita; pregunta compuesta = 2 búsquedas; fuera del corpus se niega | ☐ |
| 10 | Mismo script con `LAB_NIVEL_USUARIO=interno` y luego `restringido` (pregunta del crédito de 3.000.000 USD) | `interno`: "No tengo información…"; `restringido`: Comité de Crédito Central `[NOR-007-xx]` | ☐ |
| 11 | `python solutions/04_herramienta_estado.py --solo-tool` y luego sin flag | Usa la tool con `SOL-2026-0003` (En revisión, Área Legal); **no** la usa para normas; `12345` devuelve `formato_invalido` explicado | ☐ |
| 12 | *(Opcional)* `python solutions/05_trazas.py` | `Trazas activadas -> app-insights`, Trace IDs impresos, `Casos aprobados: 3/3` | ☐ |
| 13 | *(Opcional)* Esperar 2-5 min; abrir la traza en Foundry (*Observability → Traces*) **y** en Application Insights (Transaction search / KQL, sección "Dónde abrir la traza" de `instructores\README.md`) | Spans `invoke_agent`, `chat`, `execute_tool`, `recuperacion-normativa` con `gen_ai.tool.call.*` y `busqueda.*`. **Anota si el agente local aparece en el portal de Foundry** | ☐ |
| 14 | *(Opcional)* `python src/05_caso_fallido.py --caso 1` y luego `python instructores/05_caso_fallido_corregido.py --caso 1` | Fallido: ✘ responde/cita y traza con `busqueda.filtro = …'publico'…`; corregido: 4/4 ✔ con ids `NOR-001-…` | ☐ |
| 15 | *(Opcional)* `python src/05_caso_fallido.py --caso 2` | Anota si el modelo se **autocorrige**; la traza muestra `formato_invalido`; ajusta `instructores\README.md` | ☐ |
| 16 | *(Opcional)* ¿Application Insights tiene la autenticación local deshabilitada? Si sí: `LAB_APPINSIGHTS_ENTRA=true` + rol *Monitoring Metrics Publisher* | Las trazas llegan con Entra ID | ☐ |
| 17 | Planes B: `LAB_SIN_SEMANTICO=true`; `FOUNDRY_EMBEDDING_MODEL=` vacío (y, si hiciste los puntos opcionales, `ENABLE_CONSOLE_EXPORTERS=true`) | Cada uno funciona por separado (consulta sin ranker; consulta sin vectores; spans en consola) | ☐ |
| 18 | Carga: 5 personas (o 10 ejecuciones seguidas) en paralelo con `03_agente_con_search.py` | Sin 429; si hay, subir TPM o repartir deployments/proyectos | ☐ |
| 19 | Extensión: `python solutions/extensiones/ext_evaluar.py` con nivel `interno` | Genera `salidas/evaluacion.jsonl`; P05 y P06 rechazadas; resumen % aprobado razonable | ☐ |
| 20 | Guardar capturas/salidas del Plan B (`guia-facilitador.md` §7), y registrar fecha, versiones, responsable y desviaciones | Carpeta del Plan B lista; kit ajustado si hubo diferencias | ☐ |

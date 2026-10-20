# Ejemplo resuelto · Austral Bank (Asistente de Tesorería)

> **Ejemplo, no prescriptivo.** Es una respuesta plausible para que los trainers calibren el ejercicio y las preguntas de facilitación. No es «la solución correcta»: otro grupo puede decidir distinto con otros supuestos y estar igual de bien si explica criterio, supuesto y primer experimento. **No lo compartas con los grupos antes del cierre.** Las cifras son hipótesis ilustrativas del caso ficticio.

Archivos relacionados en esta carpeta: `arquitectura-objetivo.md` (diagrama y lectura), `Workshop_BCI_Ejemplo_Resuelto.xlsx` (las mismas cinco plantillas completas, con el mismo contenido que este documento).

## 0. Cómo usarlo para calibrar

| Paso | Mínimo aceptable | Bueno | Sobresaliente |
|---|---|---|---|
| Canvas | Las 5 dimensiones con una decisión cada una | Cada decisión con criterio y supuesto explícito | Además marcan qué decisión merece ADR y qué cambia si cae un supuesto |
| Amenazas | 3 amenazas con control | Cada una con punto de aplicación y dueño; incluyen una amenaza de herramientas/MCP | Distinguen control preventivo y detectivo, y reconocen límites de la plataforma (qué guardrails no cubren MCP) |
| SLOs y evaluación | Una métrica por dimensión | Objetivo numérico marcado como hipótesis y fuente de datos | Evaluador con umbral, alerta con dueño y gate en CI/CD |
| Backlog | 3 ítems con dueño | Criterio de éxito verificable y dependencia | Primer experimento claro, pequeño y de bajo costo que valida el supuesto más riesgoso |

## 1. Canvas de arquitectura y decisiones (paso 2)

| Dimensión | Decisión | Opciones | Criterio | Supuesto | Riesgo asociado | Estado ADR |
|---|---|---|---|---|---|---|
| Canal | Web y app entran por un backend intermedio (Session Gateway) detrás de APIM. El contact center usa la misma API con la identidad del ejecutivo y el caso del cliente en llamada. Teams queda fuera de la v1. | Web, app móvil, contact center, Teams | Volumen y SLA por canal: web/app tienen alta concurrencia y primer texto ≤ 3 s; contact center tiene baja concurrencia pero ≤ 5 s. | Los tres canales comparten API, gobierno y observabilidad; solo cambian identidad y estrategia de sesión. | Un canal ruidoso agota la cuota de los demás si comparten límite. | No requiere ADR |
| Identidad | Identidad delegada del usuario hasta la API de core (el backend intermedio hace el intercambio de token; la plataforma no lo hace por él). Identidad propia del agente solo para políticas y precios FX. En contact center se propaga ejecutivo + cliente atendido y la API valida ambos. | OBO delegado · client-credentials | Sensibilidad del dato accedido: saldos, posiciones y comex son datos por cliente. | El IdP de clientes soporta token delegado con audience propio; el ejecutivo solo puede actuar sobre clientes de su cartera. | Confused deputy; encabezado de identidad tomado del cliente en lugar del contexto validado. | Propuesta |
| Sesión | Multiplexado con Session Gateway para web/app (pool acotado, mapeo sticky usuario→sesión, identidad por request). Sesión 1:1 por (ejecutivo, caso) en contact center. | Hosted Agent dedicado · Session Gateway | Concurrencia esperada y costo: ~1.500 usuarios con conversación abierta en 15 min frente al límite por defecto de 1.000 sesiones concurrentes por suscripción y región. | Con idle timeout de 15 min (por defecto) las sesiones siguen con cómputo activo; bajarlo o pedir aumento de cuota son alternativas. | Datos propios del contenedor sin partición (sesión, usuario) → fuga entre clientes. | En validación (PoC) |
| Agente / modelo | Un solo Hosted Agent con 4 grupos de herramientas. Escalar a orquestador + especialista de Comex solo si hay sobrecarga de herramientas o una frontera de seguridad distinta. Modelo elegido por evaluación (calidad en español, latencia, disponibilidad regional). | Single agent, sequential, handoff, group chat | Complejidad real de la tarea: un dominio, 4 capacidades. Usar el nivel de complejidad más bajo que cumpla. | Las 4 capacidades comparten permisos y caben en un conjunto de herramientas manejable. | Selección errónea de herramienta; costo por iteraciones del agente. | Propuesta |
| Tools / datos | MCP de Tesorería, FX y Comex publicados vía APIM (catálogo, validación de audience, límites, logs). AI Search con filtros de seguridad por segmento y permiso. Sin caché semántico para datos por cliente; solo para preguntas normativas. | MCP directo vs vía AI Gateway | Gobierno y auditoría requerida (RD-2) y red privada (RD-5). | Los 3 MCP se pueden poner detrás de APIM sin cambiar sus contratos. | Tool poisoning o shadowing en un MCP; el guardrail de respuesta de herramienta no cubre todos los tipos de herramienta. | Propuesta |
| Datos / retrieval (extra) | AI Search con recorte de seguridad (security trimming) por segmento y permiso; el filtro se arma con la identidad del usuario, nunca con texto del prompt. | Índice único con filtros · índice por segmento | Permission-aware retrieval y calidad medible (groundedness). | Las etiquetas de acceso de los 12.000 documentos son confiables. | Etiquetas desactualizadas; un filtro puntual sobrescribe el filtro global de seguridad. | Por redactar |

## 2. Amenazas y controles (paso 3)

| Amenaza | Activo afectado | Vector | Control propuesto | Punto de aplicación | Dueño |
|---|---|---|---|---|---|
| T1 · Prompt injection indirecto vía adjuntos de comex | Comportamiento del agente; datos del cliente | PDF de carta de crédito con instrucciones ocultas. | Prompt Shields (ataques de documento) sobre cada adjunto antes de entregarlo al agente; guardrail de respuesta de herramienta en las herramientas que lo soportan (preview); revisión humana si el adjunto activa señal; validación de salida. | Contenido recuperado / adjunto | Seguridad |
| T2 · Agente con permisos excesivos | Saldos, posiciones, operaciones | Identidad del agente con alcance mayor al del usuario; herramienta que permite escritura. | Identidad delegada + RBAC de mínimo privilegio; lista de herramientas permitidas; v1 solo lectura; aprobación humana y doble control para cualquier acción futura. | Identidad / RBAC | Arquitectura |
| T3 · Fuga de datos de clientes en logs y trazas | Prompts, respuestas y argumentos de herramientas en telemetría | Application Insights guarda contenido sensible legible por muchos roles. | Enmascarado en origen; contenido sensible a una tabla protegida con lectura solo para un rol privilegiado; retención mínima; sin secretos en trazas. | Telemetría y logs | GenAIOps |
| T4 · Suplantación entre agentes o llamadas laterales (A2A) | Confianza entre agentes | Un agente (o un cliente) invoca a otro sin validar quién es; token con audience equivocado. | Entra Agent ID por agente; validar audience en cada token; lista de agentes invocables; sin llamadas laterales entre especialistas; v1 sin A2A. | Identidad / RBAC | Arquitectura |
| T5 · Tool poisoning / shadowing en un servidor MCP | Cadena de herramientas | La descripción o respuesta de una herramienta contiene instrucciones que redirigen al agente. | Catálogo de MCP aprobados vía APIM; revisar y fijar versión de descripciones; validar esquema de salida; egress controls del Hosted Agent (preview); evaluador de ataque indirecto en CI/CD. | Gateway (APIM) | Plataforma |
| T6 · Acceso cruzado entre clientes por sesión compartida o caché | Aislamiento entre clientes | Datos del contenedor sin partición por usuario; caché semántico compartido entre clientes. | Partición por (sesión, usuario) en todo dato propio; sin caché semántico para datos por cliente; prueba A-A-B en el pipeline. | Pipeline CI/CD | Plataforma |

## 3. Mapa de riesgos (cierre del paso 3)

| Riesgo | Probabilidad | Impacto | Mitigación | Dueño | Fecha de revisión | Nivel |
|---|---|---|---|---|---|---|
| Prompt injection vía documento adjunto | Media | Alto | Prompt Shields + revisión humana de adjuntos; pruebas con documentos en español | Seguridad | 23-11-2026 | Alto |
| Agente con permisos excesivos | Baja | Alto | Identidad delegada, RBAC mínimo privilegio, v1 solo lectura, aprobación por monto | Arquitectura | 23-11-2026 | Medio |
| Acceso cruzado entre clientes en sesión multiplexada | Baja | Alto | Partición (sesión, usuario), prueba A-A-B en CI/CD, revisión de código del Session Gateway | Plataforma | 07-12-2026 | Medio |
| Degradación silenciosa del retrieval | Media | Medio | Evaluación continua de groundedness y revisión de etiquetas de acceso | GenAIOps | 21-12-2026 | Medio |
| Costo fuera de rango por mal dimensionamiento | Media | Medio | Límites y alertas en el AI Gateway; presupuesto por proyecto; dimensionar sandbox con carga real | Plataforma | 21-12-2026 | Medio |
| Superar el límite de sesiones concurrentes en pico | Media | Alto | Multiplexar, ajustar idle timeout, test de carga, solicitar aumento de cuota con antelación | Plataforma | 07-12-2026 | Alto |
| Dependencia de funciones en preview (guardrails de agentes, memoria, monitoreo) | Media | Medio | Lista de funciones permitidas solo GA en producción; excepciones aprobadas; plan B por función | Gobierno | 21-01-2027 | Medio |
| Prompt Shields menos efectivo en español | Media | Medio | Evaluar con ataques y documentos en español; controles complementarios de validación | Seguridad | 07-12-2026 | Medio |

*Nivel = probabilidad × impacto (Baja/Bajo = 1, Media/Medio = 2, Alta/Alto = 3): Alto si ≥ 6, Medio si 3 a 5, Bajo si ≤ 2.*

## 4. SLOs, evaluaciones y observabilidad (paso 4)

| Dimensión | Métrica | Objetivo | Fuente de datos | Evaluador / umbral | Alerta |
|---|---|---|---|---|---|
| Disponibilidad | Éxito de sesión del Hosted Agent | ≥ 99,5 % mensual (hipótesis) | Trazas OpenTelemetry (Application Insights) | n/a (indicador de plataforma) | Consumo de presupuesto de error > 50 % en 7 días → Plataforma/SRE |
| Latencia | Primer texto visible y respuesta completa con consulta a core | Web/app p95 ≤ 3 s y ≤ 8 s; contact center ≤ 5 s (hipótesis) | Trazas OTel y logs de APIM | n/a | p95 > objetivo por 15 min → SRE |
| Calidad: retrieval | Groundedness de respuestas basadas en políticas | ≥ 90 % de casos del golden set sobre el umbral | Evaluación en CI/CD + evaluación continua sobre tráfico | Groundedness (escala 1–5), umbral ≥ 4 a calibrar | Caída > 5 pp vs línea base → bloquea release |
| Calidad: herramientas | Precisión de uso de herramientas (selección y parámetros) | ≥ 95 % de llamadas correctas en el golden set | Evaluación en CI/CD | Tool Call Accuracy; Tool Input Accuracy (umbral a calibrar) | Regresión vs versión anterior → bloquea release |
| Seguridad | Tasa de éxito de ataque (ASR) en red teaming y tasa de bloqueo de Prompt Shields | 0 éxitos críticos en fuga de datos; ASR total bajo el umbral acordado con Riesgos | Escaneos del AI Red Teaming Agent y logs de guardrails | Indirect Attack, Prohibited Actions, Sensitive Data Leakage | Éxito crítico → incidente; cambio brusco en bloqueos → revisión |
| Aislamiento | Prueba A-A-B entre usuarios en sesión compartida | 100 % superada en cada release | Pruebas automatizadas | Fuga de datos sensibles = 0 en set adversarial | Cualquier fallo bloquea el despliegue |
| Fidelidad FX | Cotizaciones con hora, vigencia y etiqueta 'indicativa' | 100 % de respuestas con cotización cumplen el formato | Evaluador personalizado sobre el golden set y muestreo de producción | Rúbrica propia (grader) ≥ umbral | Una cotización sin etiqueta → alerta a Producto |
| Costo | Tokens por conversación y CPU/memoria por sesión activa | ≤ presupuesto mensual aprobado (hipótesis); alerta al 80 % | AI Gateway + panel de costos del proyecto | n/a | 80 % del presupuesto → FinOps; 100 % → degradar a modelo más económico |
| Capacidad | Sesiones concurrentes con cómputo activo vs límite de la región | ≤ 70 % del límite en pico | Métricas del proyecto y trazas | n/a | 70 % → pedir aumento de cuota / ajustar idle timeout |

*Todos los objetivos numéricos son hipótesis a validar con tráfico piloto. Los evaluadores nombrados (Groundedness, Tool Call Accuracy, Tool Input Accuracy, Indirect Attack, Prohibited Actions, Sensitive Data Leakage) están en la lista de evaluadores integrados de la documentación; confirma el estado (GA o preview) de cada uno antes de usarlo como gate.*

## 5. Backlog (paso 5)

| Ítem | Tipo | Prioridad | Dueño | Esfuerzo | Criterio de éxito | Dependencia |
|---|---|---|---|---|---|---|
| ADR-001: patrón de sesión (multiplexado vs 1:1) por canal | Decisión (ADR) | Alta | Arquitectura | S (≤ 1 semana) | ADR aceptada por Arquitectura, Seguridad y Riesgos con criterios y supuestos explícitos. | Resultado del PoC de sesión |
| PoC Session Gateway con 50 usuarios sintéticos | PoC / experimento | Alta | Plataforma | M (≤ 1 mes) | Prueba A-A-B superada; p95 ≤ 8 s; pool dimensionado con datos de carga. | Permiso de suplantación de usuario concedido solo al backend |
| ADR-002: identidad delegada hasta el MCP/API de core | Decisión (ADR) | Alta | Seguridad | S (≤ 1 semana) | Flujo de token documentado y validado con el IdP de clientes. | Confirmación del IdP de clientes |
| Test de carga de sesiones concurrentes vs cuota regional | Test | Alta | Plataforma | S (≤ 1 semana) | Curva de sesiones activas en pico vs límite; decisión sobre idle timeout y solicitud de cuota. | PoC Session Gateway |
| Políticas de Content Safety y Prompt Shields para adjuntos de comex | Habilitador | Media | Seguridad | M (≤ 1 mes) | Dataset de adjuntos benignos y maliciosos en español evaluado; umbrales acordados. | Dataset de adjuntos sintéticos |
| Golden dataset y gate de evaluación en CI/CD | Habilitador | Media | GenAIOps | M (≤ 1 mes) | Pipeline bloquea la promoción bajo umbral; resultados por versión. | Casos representativos aprobados por negocio |
| Escaneo de red teaming base sobre el agente en entorno acotado | Test | Media | Seguridad | M (≤ 1 mes) | ASR base documentado y plan de mitigación. | Agente desplegado en entorno de pruebas |
| Catálogo de MCP aprobados vía APIM | Habilitador | Media | Plataforma | M (≤ 1 mes) | Los 3 MCP publicados con validación de audience, límites y logs. | ADR-002 |

**Primer experimento sugerido:** PoC del Session Gateway con 50 usuarios sintéticos y prueba A-A-B, porque valida a la vez los dos supuestos más riesgosos (concurrencia y aislamiento entre usuarios).

## 6. Dos ADR de ejemplo

### ADR-001 · Patrón de sesión por canal (multiplexado vs 1:1)

| Campo | Contenido |
|---|---|
| **Estado** | En validación (PoC) |
| **Fecha / dueño** | 23-10-2026 (ejemplo) · Arquitectura |
| **Dimensión del canvas** | Sesión |
| **Revisores** | Seguridad, Riesgos, Plataforma |

**Contexto.** Web y app tendrían unos 1.500 usuarios con conversación abierta en una ventana de 15 minutos. Un Hosted Agent asigna una sesión aislada, con su propio cómputo, a cada conversación, y existe un límite por defecto de sesiones concurrentes por suscripción y región (1.000 según la documentación; confírmalo en tu región). Aplican RD-1 (aislamiento) y RD-2 (auditoría).

**Decisión.** Usaremos **sesión multiplexada con Session Gateway** en web y app, y **sesión 1:1 por (ejecutivo, caso)** en contact center, porque la concurrencia de web/app excede el límite sin multiplexar, mientras que el contact center tiene baja concurrencia y mayor necesidad de aislamiento por caso.

| Opción | A favor | En contra | ¿Cumple el criterio? |
|---|---|---|---|
| A. Sesión 1:1 en todos los canales | Aislamiento por diseño; fácil de razonar | El pico supera el límite por defecto; costo por sesión activa; depende de aumentar la cuota | Parcial |
| B. Multiplexado en web/app + 1:1 en contact center | Cabe en el límite; menor costo por usuario; aislamiento fuerte donde más importa | El aislamiento entre usuarios depende de tu código; hay que construir y operar el Session Gateway; requiere un permiso especial de suplantación de usuario | Sí, con controles |
| C. 1:1 en todo + idle timeout corto + aumento de cuota | Sin componente nuevo | Peor experiencia al reanudar; depende de aprobar la cuota | Parcial |

**Criterios (en orden):** 1) concurrencia frente al límite, 2) aislamiento entre clientes, 3) costo.

**Consecuencias.** *Positivas:* dentro del límite y con menor costo. *Negativas:* asumimos la partición de datos por (sesión, usuario) y la operación de la capa intermedia; pruebas A-A-B obligatorias. *Abierto:* estrategia de mapeo (sticky, hash, round-robin) y tamaño del pool.

| Supuesto | Si es falso | Experimento o prueba | Dueño / fecha |
|---|---|---|---|
| Pico de ~1.500 usuarios con conversación abierta en 15 min | Con 400 bastaría la opción A | Test de carga con tráfico sintético | Plataforma · 4 semanas |
| El contenedor puede particionar todo dato propio por (sesión, usuario) | Fuga entre clientes | Prueba A-A-B en el pipeline | Seguridad · 4 semanas |
| El permiso de suplantación se concede solo al Session Gateway | Se reabre la opción A o C | Revisión con Seguridad e IAM | Seguridad · 2 semanas |

**Riesgos y controles:** amenaza T6 y riesgos «Acceso cruzado entre clientes en sesión multiplexada» y «Superar el límite de sesiones concurrentes en pico».
**Métrica y revisión:** 0 fugas en la prueba A-A-B; ≤ 70 % del límite en pico; p95 ≤ 8 s. Revisar a los 60 días o si el pico supera el 70 % del límite.
**Referencias:** [Multiplexar sesiones de usuarios](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/multiplex-session-users), [Aislar sesiones por usuario](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/isolate-sessions-per-user), [Permisos de Hosted Agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agent-permissions), [Límites y cuotas](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions).

### ADR-002 · Identidad delegada hasta las herramientas de datos por cliente

| Campo | Contenido |
|---|---|
| **Estado** | Propuesta |
| **Fecha / dueño** | 23-10-2026 (ejemplo) · Seguridad |
| **Dimensión del canvas** | Identidad |
| **Revisores** | Arquitectura, Riesgos, Dueño de datos |

**Contexto.** Saldos, posiciones y operaciones de comex son datos por cliente (RD-1) y el core necesita saber quién consulta (RD-2). La plataforma no hace el intercambio de token delegado (OBO) por la aplicación: lo hace el backend. En contact center, el ejecutivo actúa sobre el cliente que atiende en la llamada.

**Decisión.** Usaremos **identidad delegada del usuario** (OBO realizado por el Session Gateway) hasta las herramientas que acceden a datos por cliente, y la **identidad propia del agente** solo para recursos que no son por cliente (políticas y precios FX), porque la sensibilidad del dato exige que el core autorice con el usuario real.

| Opción | A favor | En contra | ¿Cumple el criterio? |
|---|---|---|---|
| A. Identidad del agente (client-credentials) para todo | Simple; sin dependencia del IdP | El core no sabe quién pregunta; permisos amplios; riesgo de confused deputy | No (RD-1) |
| B. OBO donde el dato es por cliente + identidad propia en recursos compartidos | Auditable; mínimo privilegio | Depende del IdP de clientes; manejo y expiración de tokens | Sí |
| C. OAuth identity passthrough vía Toolbox donde aplique | Autenticación de herramientas centralizada | Depende del soporte de cada herramienta o MCP | A evaluar en el PoC |

**Criterio principal:** sensibilidad del dato accedido.

**Consecuencias.** *Positivas:* trazabilidad por usuario real. *Negativas:* complejidad de tokens y dependencia del IdP de clientes. *Abierto:* tratamiento de sesiones largas y expiración de tokens.

| Supuesto | Si es falso | Experimento o prueba | Dueño / fecha |
|---|---|---|---|
| El IdP de clientes emite token delegado con audience propio | Opción A con controles compensatorios o alcance reducido | PoC con el IdP | Seguridad · 3 semanas |
| La identidad del usuario se deriva del token validado, nunca de un encabezado del cliente | Suplantación | Prueba negativa con encabezado manipulado | Seguridad · 3 semanas |
| El ejecutivo solo puede actuar sobre clientes de su cartera | Acceso indebido | Validación en la API de core con el par (ejecutivo, cliente) | Dueño de datos · 4 semanas |

**Riesgos y controles:** amenazas T2 y T4; riesgo «Agente con permisos excesivos».
**Métrica y revisión:** 100 % de las llamadas a core con la identidad del usuario en el log de auditoría y 0 accesos permitidos en las pruebas negativas. Revisar a los 60 días.
**Referencias:** [Flujo on-behalf-of](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/use-on-behalf-of-flow), [Permisos de Hosted Agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agent-permissions).

## 7. Puesta en común de ejemplo (3 minutos)

- **Decisión principal:** «Multiplexamos sesiones en web y app con un Session Gateway, y mantenemos 1:1 en contact center.»
- **Supuesto crítico:** «El pico real es de unos 1.500 usuarios con conversación abierta; si fuera menor, bastaría 1:1.»
- **Primer experimento:** «PoC con 50 usuarios sintéticos y prueba A-A-B: cero fugas y p95 ≤ 8 s en cuatro semanas.»
- **Amenaza que más nos preocupa:** «Prompt injection en los adjuntos de comex, porque el guardrail de respuesta de herramienta no cubre todos los tipos de herramienta.»

## 8. Variantes legítimas (para no esperar «la» respuesta)

- **Sesión 1:1 en todo** si el grupo estima que el pico real es menor al límite, o si decide bajar el idle timeout y solicitar aumento de cuota.
- **Orquestador con especialista de Comex (A2A)** si el grupo argumenta una frontera de seguridad distinta para comex (permisos, equipo dueño) y acepta la complejidad extra.
- **Identidad solo del agente en la v1** si el core ofrece autorización por llamada con contexto de cliente y el grupo declara ese supuesto y su control compensatorio.
- **Sin caché semántico** o **con caché solo para normativa**: ambas son defendibles; lo inaceptable es cachear datos por cliente sin aislamiento.
- **Más de un proyecto Foundry** (por segmento o por ambiente) si Riesgos pide separación de datos más fuerte.

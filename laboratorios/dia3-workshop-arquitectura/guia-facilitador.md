# Guía del facilitador · Workshop BCI: Architecture Decision Workshop

**Día 3 · viernes 23-oct-2026 · 12:05–12:40 (35 min) + puestas en común y cierre ejecutivo 12:40–13:00 · híbrido (Microsoft Chile + Teams)**
Trainers: Pablo Braconi · Valentina Grajales · Caso ficticio «Austral Bank» (Asistente de Tesorería) · Todo en español neutro, tú.

> Esta guía acompaña a `caso-austral-bank.md`, a las plantillas (`plantillas\Workshop_BCI_Plantillas.xlsx`, `Plantillas_Workshop_BCI.docx`, `ADR-plantilla`) y al `ejemplo-resuelto\` (solo para trainers: no lo compartas con los grupos antes del cierre). Material de apoyo: `matriz-referencia-decisiones.md` (criterios) y `checklist-produccion-seguridad-genaiops.md/.docx` (entregable del Día 3 que se comparte al cierre).

## 0. Qué debes llevar de este ejercicio

- **Objetivo del slot:** que cada grupo salga con una arquitectura objetivo y decisiones por validar (ADR), un mapa de riesgos y un backlog de PoC, pruebas y habilitadores, sobre un caso ficticio y reutilizable para sus casos reales.
- **Entregable mínimo por grupo (según las diapositivas):** 5 decisiones del canvas, 3 a 5 amenazas con control y dueño, métricas/SLO por dimensión, 3 a 5 ítems de backlog, y una puesta en común de 3 min (decisión principal, supuesto crítico, primer experimento).
- **Tu rol:** no resuelves; haces preguntas. Una buena intervención dura 30 segundos y termina en una pregunta.

## 1. Preparación (antes del 23-oct)

| Cuándo | Qué | Quién (propuesta) |
|---|---|---|
| T-7 días | Confirmar con la organización que **ambos trainers serán coorganizadores** de la reunión de Teams (sin ese permiso no podrás abrir ni moverte entre salas) y que las salas de grupo se crean antes de la sesión. | Pablo |
| T-3 días | Crear la carpeta compartida `Workshop-BCI/Dia3/` (Teams o OneDrive) con una subcarpeta por grupo y una copia de `Workshop_BCI_Plantillas.xlsx` por grupo (ver §6). | Valentina |
| T-1 día | Imprimir `Plantillas_Workshop_BCI.docx` (1 juego por mesa) y el caso (1 copia por persona), pliegos de papel, marcadores y cronómetro visible. | Equipo en sala |
| Día D, 10:45–10:55 (break) | Publicar la lista de grupos (ver §2) y abrir salas Teams. | Ambos |
| 12:00 | Mensaje en el chat con enlace a la carpeta, el caso y las plantillas; probar que se puede editar el archivo. | Valentina |

## 2. Formación de grupos (híbrido)

Con unas 48 personas (según el índice de materiales: 21 en sala y 27 por Teams; confirma el número final al abrir la sesión):

- **Grupos homogéneos por modalidad.** No mezcles personas en sala y remotas en un mismo grupo: el audio y la pizarra lo vuelven injusto. Referencia: **4 mesas en sala (5, 5, 5, 6)** y **5 salas Teams (5, 5, 5, 6, 6)**, es decir, 9 grupos de 4 a 6 personas.
- **Mezcla de perfiles dentro del grupo.** Intenta que cada grupo tenga al menos una persona de arquitectura, una de seguridad o plataforma, y una de datos o IA. Usa el perfil declarado en la inscripción y una pregunta rápida en el chat en la mañana.
- **Asigna roles antes de empezar** (en la lista de grupos puedes proponer relator y escriba):

| Rol | Qué hace | Señal de que funciona |
|---|---|---|
| **Relator** | Presenta los 3 minutos finales y cuida el reloj de cada paso. | Avisa «quedan 2 min» sin que lo pida el trainer. |
| **Escriba** | Es la única persona que escribe en el archivo del grupo; el resto habla. | El archivo refleja lo discutido, no lo que dijo el más veloz. |
| **Retador de seguridad** | Hace la pregunta incómoda en cada decisión («¿qué pasa si…?»). | Al menos una decisión cambia o gana un control por su pregunta. |
| **Dueño de datos** | Defiende la sensibilidad y quién puede ver qué (clientes, ejecutivos, trazas). | Ninguna decisión asume acceso amplio por comodidad. |

Con 4 personas, el relator cumple también el rol de dueño de datos; con 6, suma un **cronometrista/SRE** (vigila el tiempo y pregunta por SLO y alertas) y una **voz de negocio** (qué pasa con el cliente).

- **Reparto de trainers (decisión pendiente):** una propuesta es que Pablo siga las mesas en sala más 2 salas Teams (arquitectura y plataforma) y Valentina 3 salas Teams (seguridad y gobierno), cruzándose a mitad del ejercicio. Confirmen el reparto en el ensayo.
- **Cómo moverte por Teams:** entra a cada sala 1 a 2 minutos por paso, haz 2 preguntas y sal. Usa el chat de cada sala para mandar un aviso de tiempo («Quedan 2 min en Canvas») y el mensaje general para todos los grupos.

## 3. Minuto a minuto (35 min)

| Hora | Min | Paso | Qué ocurre | Qué dices o haces tú |
|---|---|---|---|---|
| 12:00–12:05 | 5 | Preparación | Grupos en mesas o salas, archivo abierto, roles asignados. | Muestra la diapositiva de reglas; confirma que cada escriba tiene el archivo abierto. |
| **12:05–12:10** | **5** | **Contexto** | Lectura del caso (3 min), acuerdo de alcance y 2 supuestos que cambiarían (2 min). | 12:05 «Tienen 35 minutos y 5 pasos; la prioridad es criterio y supuesto, no un diagrama bonito». 12:08 «Marquen los 2 supuestos que cambiarían». |
| **12:10–12:20** | **10** | **Canvas de arquitectura y decisiones** | Completan Canal, Identidad, Sesión, Agente/modelo y Tools/datos con decisión, opciones, criterio y supuesto. Marcan Estado ADR. | Reloj sugerido: Canal 1,5 · Identidad 2,5 · Sesión 2,5 · Agente 1,5 · Tools/datos 2 min. 12:17 «Quedan 3 min: todas las filas con criterio». |
| **12:20–12:28** | **8** | **Amenazas** (y mapa de riesgos) | Dibujan el flujo (2 min), enumeran 3 a 5 amenazas con control, punto y dueño (4 min), priorizan y pasan a la hoja de riesgos (2 min). | 12:20 «Miren los cuatro puntos: entrada, herramienta, salida, memoria». 12:26 «¿Cuál amenaza es la más cara si ocurre?». |
| **12:28–12:35** | **7** | **SLOs y evaluación** | Una métrica por dimensión (Disponibilidad, Calidad, Seguridad, Costo), objetivo marcado como hipótesis, fuente, evaluador/umbral y alerta. | 12:28 «Una métrica por dimensión; si no hay datos, escríbanlo como hipótesis». 12:33 «Elijan qué evaluación bloquea un release». |
| **12:35–12:40** | **5** | **Backlog** | 3 a 5 ítems con tipo, prioridad, dueño y criterio de éxito; marcan el primer experimento; el relator ensaya su frase. | 12:35 «Empiecen por el supuesto más riesgoso». 12:38 «Elijan el primer experimento y su criterio de éxito». |
| 12:40–13:00 | 20 | Puesta en común y cierre | Ver §8. | Ver §8. |

**Avisos de tiempo (di en voz alta y escribe en el chat):** cada paso a 3 min del final y a 1 min del final. Si tienes dos salas Teams, el aviso lo mandas por el chat general.

## 4. Preguntas de facilitación por paso

Elige 2 o 3 por grupo y por paso; no las leas como lista. Las primeras de cada lista son las que más rinden.

### Paso 1 · Contexto (5 min)

1. ¿Quién es el usuario real de la v1 y qué decisión toma con la respuesta del asistente?
2. ¿Cuál es el peor daño razonable si el asistente se equivoca en una cotización FX o en el estado de una carta de crédito?
3. ¿Qué requisito duro del caso limita más la arquitectura: aislamiento (RD-1), residencia (RD-4) o red privada (RD-5)?
4. ¿Qué supuesto del caso cambiarían primero y qué mueve en cascada?
5. ¿Qué parte de la v1 no necesita un agente (una consulta directa a una API, un buscador o una llamada al modelo bastan)?
6. ¿Qué canal tiene el SLA más exigente y cuál el riesgo más alto? ¿Son el mismo?
7. ¿Qué datos son por cliente y cuáles son compartidos (políticas, precios)?
8. ¿Qué significa «solo lectura» para el banco: ¿incluye enviar un correo o crear un ticket?
9. ¿Qué dato no debería entrar nunca en un prompt ni en una traza?
10. ¿Quién sería la persona dueña del producto y quién firma el riesgo?
11. ¿Cómo se mide el éxito a los 90 días: menos llamadas, menos tiempo por consulta, menos incidentes?
12. ¿Qué parte de este caso se parece a tu caso real y qué parte es distinta?

### Paso 2 · Canvas de arquitectura y decisiones (10 min)

1. ¿Qué canal define el SLA más duro y qué cambia en la arquitectura por ese canal?
2. ¿Dónde vive la identidad del usuario final y quién puede afirmar «este es el usuario» ante el agente?
3. ¿OBO delegado o identidad propia del agente? ¿Qué dato obliga a usar la identidad delegada?
4. ¿Qué pasa si un encabezado de identidad lo manda el cliente en lugar del backend?
5. ¿Cuántos usuarios con conversación abierta hay en el pico y cuántas sesiones concurrentes soporta tu región? ¿Qué cuenta como sesión activa?
6. Si multiplexas sesiones: ¿quién garantiza que el usuario A no vea datos del usuario B y dónde particionas?
7. ¿Qué pasa con el estado de la conversación cuando vence el tiempo de inactividad o el usuario cambia de dispositivo?
8. ¿Qué te obligaría de verdad a dividir en varios agentes: sobrecarga de herramientas, una frontera de seguridad distinta, equipos dueños distintos?
9. ¿Con qué criterio eligen el modelo (calidad en español financiero, latencia, disponibilidad regional, costo) y cómo lo medirían?
10. ¿Qué pasa si el servidor MCP devuelve instrucciones maliciosas? ¿Dónde lo detectan?
11. ¿MCP directo o vía gateway? ¿Qué ganan en gobierno y qué pierden en latencia y punto único de falla?
12. ¿Qué ve cada usuario en AI Search y quién filtra: el prompt o el sistema? ¿Qué cachearían y qué nunca?

### Paso 3 · Amenazas (8 min, incluye mapa de riesgos)

1. ¿Qué pasa si el servidor MCP devuelve instrucciones maliciosas en la descripción de una herramienta o en su respuesta?
2. ¿Qué pasa si un PDF adjunto de comex trae instrucciones ocultas, también en español? ¿Dónde lo inspeccionan: antes del agente, al recuperar o en la salida?
3. Dibujen el peor camino: ¿qué podría hacer hoy el agente si lo engañan?
4. ¿Qué control es preventivo y cuál detectivo? ¿Cuál puede fallar en silencio?
5. De los cuatro puntos de intervención (entrada, llamada a herramienta, respuesta de herramienta, salida), ¿cuáles cubre el guardrail para tus herramientas y qué cae fuera? ¿Cómo lo compensan?
6. ¿Qué datos terminan en trazas y logs y quién los puede leer?
7. ¿Cómo prueban el aislamiento entre clientes en la caché, la memoria y el retrieval?
8. ¿Cómo evitan que un agente invoque a otro sin saber quién es (validación del audience, lista de agentes permitidos)?
9. Si roban el token de un ejecutivo del contact center, ¿qué alcance tiene el atacante?
10. ¿Qué amenaza es de abuso de costo y cómo la limitan (TPM, cuotas por canal)?
11. ¿Qué control depende de una función en preview y cuál es el plan B?
12. ¿Quién es dueño de cada control y cómo se entera si deja de funcionar?

### Paso 4 · SLOs y evaluación (7 min)

1. ¿Qué significa «disponible» para este asistente: que responda, que responda bien o que respete permisos?
2. ¿Cuál es el indicador de éxito de sesión y cómo lo medirían con trazas?
3. ¿Qué latencia siente cada usuario: primer texto o respuesta completa? ¿Y el ejecutivo en una llamada?
4. ¿Cómo detectan una degradación silenciosa del retrieval (mismas preguntas, respuestas más pobres)?
5. ¿Qué evaluadores usarían (groundedness, uso de herramientas, ataque indirecto, fuga de datos) y con qué umbral inicial? ¿Cómo lo calibran?
6. ¿De dónde sale el golden dataset, quién lo aprueba y tiene casos en español y casos adversariales?
7. ¿Qué evaluación corre en CI/CD y cuál sobre tráfico real? ¿Qué bloquea un release?
8. ¿Qué miden en seguridad: bloqueos, tasa de éxito de ataques en red teaming, fugas? ¿Cuántos éxitos críticos toleran?
9. ¿Qué métrica de costo siguen: tokens por conversación, CPU y memoria por sesión activa, o ambas?
10. ¿A quién despierta cada alerta y qué hace esa persona en sus primeros 15 minutos?
11. ¿Qué indicador les avisa que se acerca el límite de sesiones concurrentes?
12. ¿Cómo apagan el asistente en 5 minutos si hay un incidente (terminar sesiones, deshabilitar herramientas, volver a la versión anterior)?

### Paso 5 · Backlog (5 min)

1. ¿Qué supuesto es el más riesgoso si cae y cuál es el experimento más barato para saberlo?
2. ¿Qué decisión necesita ADR antes de construir y cuál puede esperar?
3. ¿Qué diferencia hay entre este PoC y este test? ¿Cómo sabes que están terminados?
4. ¿Qué habilitador de plataforma (red, gateway, catálogo MCP, pipeline de evaluación) bloquea todo lo demás?
5. ¿Cuál es el criterio de éxito verificable (número, prueba, fecha) de cada ítem?
6. ¿Quién es el dueño (rol o nombre) y tiene capacidad real para entregarlo en 30 días?
7. ¿Qué dependencias hay entre ítems (por ejemplo, identidad antes del PoC de sesiones)? ¿Cuál es la ruta crítica?
8. ¿Qué pasa si el PoC falla: cuál es el plan B de la decisión?
9. ¿Qué entra en los primeros 30 días y qué queda para 60 o 90?
10. ¿Qué ítems dependen de funciones en preview y qué aprobación necesitan del comité de riesgo?
11. ¿Qué evidencia le darían al comité de riesgo para pasar de piloto a producción?
12. ¿Cuál presentarían como primer experimento y por qué ese?

## 5. Cómo se ve un buen resultado y errores frecuentes

| Paso | Señales de un buen resultado | Errores frecuentes |
|---|---|---|
| Contexto | Alcance acordado en una frase y 2 supuestos escritos. | Releer el caso sin tomar decisiones; olvidar los requisitos duros. |
| Canvas | Cada decisión con **criterio y supuesto**; saben qué decisión merece ADR; usan las opciones como punto de partida, no como lista cerrada. | Dibujar el diagrama antes de decidir; decidir por tecnología favorita; llenar «Opciones» y dejar «Criterio» vacío; ignorar la concurrencia real. |
| Amenazas | 3 a 5 amenazas distintas (entrada, herramientas, datos, identidad, telemetría) con control, punto y dueño; reconocen un límite de la plataforma (por ejemplo, un guardrail que no cubre su herramienta). | Lista de 15 amenazas sin priorizar; «Content Safety» como único control; controles sin dueño; olvidar el MCP y los logs. |
| SLOs y evaluación | Una métrica por dimensión, objetivos como hipótesis, evaluador con umbral y alerta con responsable; un gate en CI/CD. | Métricas de vanidad; números sin fuente; confundir SLO con evaluación; no definir qué bloquea un release. |
| Backlog | Ítems pequeños y verificables, con dueño y dependencia; primer experimento claro que ataca el supuesto más riesgoso. | «Hacer el agente» como único ítem; sin criterio de éxito; todo prioridad alta; backlog sin habilitadores. |

## 6. Cómo capturar los resultados

1. **Antes de la sesión:** crea `Workshop-BCI/Dia3/Grupo-01 … Grupo-09` y copia `Workshop_BCI_Plantillas.xlsx` como `Grupo-XX_Workshop_BCI.xlsx` en cada carpeta. Un ejemplo de script (ajusta las rutas):

```powershell
$origen = "C:\ruta\plantillas\Workshop_BCI_Plantillas.xlsx"
$destino = "C:\ruta\OneDrive\Workshop-BCI\Dia3"
1..9 | ForEach-Object {
  $g = "Grupo-{0:00}" -f $_
  New-Item -ItemType Directory -Force -Path "$destino\$g" | Out-Null
  Copy-Item $origen "$destino\$g\${g}_Workshop_BCI.xlsx"
}
```

2. **Durante la sesión:** solo el escriba edita; los demás ven el archivo. Si la co-edición falla, el escriba trabaja en una copia local y la sube al final.
3. **Plan de respaldo en sala:** plantillas impresas y foto de las hojas completas subida al chat de Teams («Workshop BCI · capturas»).
4. **Después:** dentro de las 24 horas, enviar a los grupos su archivo y la síntesis consolidada. Recuerda que el caso es ficticio: recomienda no pegar datos reales en carpetas compartidas.

## 7. Consolidar para el cierre ejecutivo

Mientras los grupos presentan, un trainer anota la tabla de recuento y el otro prepara la diapositiva de síntesis.

**Tabla de recuento (lápiz o pantalla compartida):**

| Dimensión | Opción A | Opción B | Otra | Supuesto más repetido |
|---|---|---|---|---|
| Canal | | | | |
| Identidad (OBO vs propia) | | | | |
| Sesión (1:1 vs multiplexada) | | | | |
| Agente/modelo (único vs orquestador) | | | | |
| Tools/datos (MCP directo vs gateway) | | | | |

| Amenazas más repetidas | Veces | Controles más citados |
|---|---|---|
| | | |

| Primeros experimentos | Grupos | Dueño típico |
|---|---|---|
| | | |

**Plantilla de diapositiva de síntesis (1 lámina):**

- **Título:** «Lo que decidimos hoy: patrones de los grupos» (la lámina «Lo que se lleva cada grupo del workshop» ya trae los números: 5 decisiones, 3 a 5 amenazas, 3 a 5 ítems de backlog, 1 arquitectura objetivo).
- **Columna 1 · Convergencias:** las decisiones que repitieron la mayoría de los grupos, con la cifra (por ejemplo, «7 de 9 eligieron identidad delegada para datos por cliente»).
- **Columna 2 · Divergencias que merecen ADR:** dimensiones donde los grupos se dividieron y por qué (criterio o supuesto distinto).
- **Columna 3 · Amenazas y riesgos más citados:** top 3 con su control principal.
- **Pie · Siguientes pasos:** los 3 a 5 primeros experimentos más repetidos, conectados con el 30/60/90 de la lámina «Próximos pasos: 30 / 60 / 90 días».

## 8. Puesta en común y cierre ejecutivo (12:40–13:00)

Con unos 9 grupos, 3 minutos por grupo sumarían 27 minutos, más de los 20 disponibles (que además incluyen el cierre ejecutivo). **Decisión pendiente de los trainers:** elijan antes de la sesión uno de estos planes.

| | Plan A (recomendado) | Plan B |
|---|---|---|
| Idea | Presentan 4 grupos de 3 min (2 en sala y 2 por Teams, elegidos al azar o por diversidad de enfoques); el resto deja su archivo y una frase en el chat. | Presentan los 9 grupos en 90 segundos: decisión principal, supuesto crítico, primer experimento (una frase cada uno). |
| Agenda | 12:40 transición (1 min) · 12:41–12:53 cuatro puestas en común (12 min) · 12:53–13:00 síntesis y cierre (7 min) | 12:40 transición (1 min) · 12:41–12:54 nueve puestas en común (≈13,5 min) · 12:54–13:00 cierre (6 min) |
| Ventaja | Más profundidad y calidad de conversación. | Todos hablan; más justo. |
| Riesgo | Los grupos que no presentan sienten que su trabajo se pierde: compénsalo leyendo en voz alta sus aportes únicos. | Poca profundidad; el reloj es implacable. |

**Estructura de cada puesta en común (3 min o 90 s):** 1) decisión principal; 2) supuesto crítico; 3) primer experimento. Los trainers toman nota de patrones repetidos y de divergencias.

**Cierre ejecutivo (últimos 5 a 7 min):** presenta la lámina de síntesis (§7), conecta con el 30/60/90 y cierra con la lámina «Los tres días en una idea por día» y los recursos públicos. Menciona dónde quedan los materiales (carpeta compartida), que el checklist de producción, seguridad y GenAIOps (`checklist-produccion-seguridad-genaiops.docx`) es el entregable para llevar y cómo continuar con el caso real: cada ítem pendiente del checklist debería terminar como fila del backlog.

## 9. Si vas atrasado (qué recortar)

Revisa el reloj en cada punto de control y aplica el recorte sin discutirlo con el grupo.

| Punto de control | Si el grupo está… | Acción inmediata |
|---|---|---|
| 12:09 | Todavía leyendo el caso | Pide que anoten solo 2 supuestos y pasen al canvas. |
| 12:17 | Con menos de 3 filas del canvas | Prioriza **Identidad, Sesión y Tools/datos**; Canal y Agente/modelo quedan como supuesto en una línea. |
| 12:25 | Sin amenazas definidas | Pide solo 3 amenazas (una por entrada, herramienta, datos) y salta el mapa de riesgos: se completa después. |
| 12:32 | Sin métricas | Reduce a **Calidad y Seguridad**; sin cifras, solo métrica y fuente. |
| 12:38 | Sin backlog | Pide 3 ítems con dueño y un primer experimento; el criterio de éxito en una frase. |
| 12:40 | Fuera de hora | Pasa a Plan B (90 s) o recorta a decisión principal y primer experimento. |

Si todo el bloque inicia tarde, mantén el cierre ejecutivo (es el entregable de la sesión) y recorta primero las puestas en común.

## 10. Opciones de arquitectura de referencia (hoja de apoyo)

Úsala para ayudar al grupo a comparar, no para elegir por ellos. Referencias en `docs-oficiales\…` y su equivalente público en Microsoft Learn. Si un patrón depende de una función en preview, aparece marcado. La regla de partida del Architecture Center: usa el **nivel más bajo de complejidad** que cumpla el requisito (llamada directa < agente único con herramientas < multiagente), y justifica el siguiente nivel por complejidad real, sobrecarga de herramientas o fronteras de seguridad distintas.

| # | Patrón | Cuándo usarlo | Cuándo no | Costo o riesgo principal | Documentación |
|---|---|---|---|---|---|
| 1 | **Agente único en Hosted Agent, sesión 1:1** | Un dominio, concurrencia dentro del límite de sesiones, aislamiento fuerte por diseño (cada sesión corre en su propio entorno aislado) y archivos persistentes por sesión. | Concurrencia sostenida por encima del límite regional (por defecto 1.000 sesiones concurrentes por suscripción y región; cuenta las sesiones con cómputo provisionado o en ejecución). | Costo por CPU y memoria de las sesiones activas; error `session_quota_exceeded` (429) al superar el límite. | [Hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agents) · [Límites y cuotas](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/limits-quotas-regions) · `agents\concepts\hosted-agents.md` |
| 2 | **Hosted Agent multiplexado + Session Gateway** (en la documentación: servicio de capa intermedia) | Muchos usuarios y sesiones cortas; necesitas reducir costo o superar el límite; aceptas la responsabilidad de aislar. | Si no puedes garantizar la partición de tus propios datos por (sesión, usuario) o no puedes limitar el permiso de suplantación de usuario. | La plataforma aísla el historial de conversación, pero **tú** particionas lo que guarda tu contenedor; hay que construir, operar y probar (A-A-B) la capa intermedia; el permiso `UserIdentityImpersonation` no viene en roles integrados. | [Multiplexar sesiones](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/multiplex-session-users) · [Aislar sesiones por usuario](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/isolate-sessions-per-user) · [Permisos](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agent-permissions) |
| 3 | **Orquestador + especialistas** (secuencial, concurrente, handoff, group chat, magentic) | Complejidad del prompt que no cabe en un agente, sobrecarga de herramientas o fronteras de seguridad distintas por dominio (por ejemplo, un especialista de Comex). | Un solo dominio con herramientas manejables; añade latencia, costo y más superficie de auditoría. | Más saltos, más trazas que seguir; define límites de iteración. Los Workflows de Foundry están en preview y su retiro está anunciado para el 1-dic-2026: para desarrollo nuevo, usa Microsoft Agent Framework. | [Patrones de diseño de agentes](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) · [Disponibilidad GA](https://learn.microsoft.com/en-us/azure/foundry/concepts/general-availability) |
| 4 | **MCP gobernado por APIM / AI Gateway** (y Toolbox) | Muchas herramientas compartidas por varios agentes; necesitas catálogo aprobado, autenticación central, límites y auditoría. | Una sola API simple para un solo agente: un MCP o una función directa puede bastar. | Un salto más (latencia), posible punto único de falla y mayor superficie de ataque; el gateway ve los datos en claro. El gobierno de herramientas con AI Gateway está en preview; Toolbox (un único endpoint MCP con autenticación central) es GA. | [Toolbox](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/toolbox-overview) · [Buenas prácticas de herramientas](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-best-practice) · [Gateway de IA generativa](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/generative-ai-gateway) · [Autenticación MCP](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/mcp-authentication) |
| 5 | **Federación A2A** | Agentes de equipos o dominios distintos que deben colaborar sin compartir código; frontera organizacional clara. | Si basta una herramienta MCP o una función; añade complejidad de identidad y confianza. | Elegir autenticación (compartida o individual; OAuth identity passthrough conserva al usuario); A2A v1.0 es GA y v0.3 preview; para destinos de agentes Foundry, solo modalidad de texto y sin respuestas en streaming según la documentación de la herramienta A2A. | [Herramienta A2A](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/agent-to-agent) · [Autenticación A2A](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/agent-to-agent-authentication) |
| 6 | **Prompt agent con Toolbox y conocimiento** (bajo código) | Prueba de concepto rápida o casos simples: instrucciones, modelo y herramientas por configuración; sin código ni contenedores. | Cuando necesitas tu propio framework, protocolos personalizados, entorno por sesión con archivos o control fino del ciclo de vida. | Menos control; revisa qué herramientas y guardrails soporta cada tipo de agente. | [Visión general de agentes](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) |

**Transversal (se combina con cualquiera de los patrones):**

- **Gateway de modelos y cuotas.** Control Plane y AI Gateway pueden aplicar límites de TPM (error 429) y cuotas de tokens por período por proyecto (preview); la integración de AI Gateway del portal documentada hoy aplica a prompt agents: confirma con la documentación vigente si tu patrón la usa. Referencia: [Control Plane](https://learn.microsoft.com/en-us/azure/foundry/control-plane/overview) · [Límites de modelos](https://learn.microsoft.com/en-us/azure/foundry/control-plane/how-to-enforce-limits-models).
- **Aprobación humana durable** para cualquier acción con efecto: [human-in-the-loop](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/add-human-in-the-loop).
- **Memoria (preview), AI Search con recorte de seguridad y observabilidad (OpenTelemetry a Application Insights)** se deciden siempre junto con la identidad y la sesión.

Para decisiones puntuales («¿cuándo multiplexar?», «¿MCP o API directa?», «¿OBO o identidad propia?»), usa `matriz-referencia-decisiones.md`.

## 11. Lista de verificación del facilitador

- [ ] Coorganizador en Teams confirmado; salas creadas; lista de grupos publicada.
- [ ] Carpeta compartida y archivos por grupo probados (abrir, editar, guardar).
- [ ] Impresiones: caso, plantillas, ADR en blanco; cronómetro visible.
- [ ] Decisión Plan A o B de puestas en común tomada y comunicada.
- [ ] Reparto de trainers por mesas/salas y por temas acordado.
- [ ] `ejemplo-resuelto\` a mano pero sin compartir.
- [ ] Mensaje final preparado: dónde quedan los archivos y cómo continuar con el caso real.

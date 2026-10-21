# Runbook de facilitación · Microsoft AI Foundry BCI Training Day (3 días, híbrido)

**Fechas:** mié 21 (L100), jue 22 (L200) y vie 23 (L300) de octubre de 2026 · **Horario:** 09:00–13:00 hora de Chile los Días 1 y 2; 09:00–12:30 el Día 3 (termina 30 min antes al eliminar "AI Search avanzado" sin reemplazo) · **Lugar:** Microsoft Chile (Las Condes) + Teams · **Inscritos:** ~48 (21 presenciales / 27 en Teams).
**Equipo:** Pablo Braconi y Valentina Grajales (instructores) · Robert Escalante (organizador) · Diego Bell Tineo (contacto de BCI, líder de arquitectura) · administrador Azure de BCI `<ADMIN-BCI>` (de guardia 08:30–13:30).
**Enlaces (marcadores):** `<LINK-TEAMS>` · `<LINK-REPO>` · `<LINK-FEEDBACK>` · `<LINK-PARKING>` · `<LINK-PLANB>` (carpeta `plan-b\`) · `<LINK-CANVAS>` (plantilla del Día 3).

> Este runbook asume el entorno real descrito al inicio de `guia-entorno-admin-bci.md` («Actualización 20-oct»): una cuenta Foundry y un proyecto `lab-NN` por participante en su grupo de recursos `rg-bci-lab-NN`, con los modelos ya desplegados `gpt-5.6-luna` (principal del Día 1, 4K TPM por cuenta), `gpt-5-mini` (respaldo) y `text-embedding-3-small`, más Azure AI Search, Document Intelligence, Application Insights y el recurso compartido `rg-bci-lab-compartido`. Los participantes inician sesión con cuentas `labNN@mngenvmcap219366.onmicrosoft.com` y un **Temporary Access Pass (TAP)**. **`gpt-5.6-luna` con Foundry Agent Service + file search aún no se probó desde una cuenta de participante.** Todo lo marcado como **verificar** debe confirmarse antes del evento. Los tiempos y las diapositivas citadas provienen de `presentaciones\content\day1.json`, `day2.json` y `day3.json` (cronograma del Día 1 actualizado según la decisión del organizador; la numeración de diapositivas es *por confirmar* con el deck vigente).

---

## 1. Decisiones que hay que cerrar HOY (T-1)

| # | Decisión | Propuesta por defecto | Quién decide |
|---|---|---|---|
| D1 | Quién monitorea Teams mientras el otro instructor presenta | **Robert** monitorea el chat y filtra preguntas; el instructor que no presenta hace soporte de laboratorio. Respaldo: un voluntario de BCI o rotación de 15 min entre instructores | Robert + Pablo |
| D2 | Lenguaje del laboratorio pro-code | **Python** (según slides del Día 2); .NET solo como alternativa de mostrar. Confirmar con BCI | Diego |
| D3 | Quién administra el ambiente | El entorno ya está aprovisionado con cuentas `labNN` en el tenant del evento (`mngenvmcap219366…`); quién lo administra y quién reemite TAP durante el taller: *por confirmar*. El límite de ~16 sesiones de un entorno compartido de Microsoft no aplica | Diego / `<ADMIN-BCI>` |
| D4 | ¿Se permite Codespaces/GitHub en BCI? | *Verificar* hoy; si no, plan de pares/demo | Diego |
| D5 | ¿Preview habilitado en la suscripción (trazas, evaluaciones, agentic retrieval)? | *Verificar* con la prueba de validación; si falla, demo en vivo sustituida por grabación (`plan-b-demos.md`) | Pablo |
| D6 | Política de grabación (consentimiento, retención, quién accede) | Se avisa al inicio de cada día; acceso solo a inscritos; eliminar según política de BCI/Microsoft (*verificar*) | Robert |

---

## 2. Roles en la entrega híbrida

| Rol | Responsabilidad | Titular por defecto |
|---|---|---|
| **Presentador** | Conduce el módulo, comparte pantalla, habla a la sala y a Teams a la vez («para quienes nos siguen por Teams…») | Instructor del módulo (tabla 3) |
| **Monitor de Teams/chat** | Lee el chat, agrupa preguntas, las dice en voz alta en pausas/cada ~10 min, etiqueta bloqueos de laboratorio, avisa si el audio de Teams falla | Robert (por defecto) |
| **Soporte de laboratorio** | Resuelve bloqueos en la sala y por Teams con la cola de bloqueos; decide el paso a «modo pareja/demo» | Instructor que no presenta (+ voluntario de BCI en sala, *si está disponible*) |
| **Tiempo** | Lleva el reloj, avisa T-10/T-5/T-0 por módulo, aplica las reglas de recorte (sección 6) | Robert (con apoyo de un temporizador visible en sala) |
| **Escalamiento de BCI** | Acceso, permisos, acceso condicional, red | `<ADMIN-BCI>` / Diego |

**Reglas de la dinámica híbrida**
- Dirígete a ambos públicos: nombra a quienes están en la sala y a quienes están en Teams; nunca «como ven aquí».
- Los asistentes de la sala también usan el chat de Teams para preguntas escritas (un solo canal de preguntas).
- Todo lo que se pregunta en la sala se repite con el micrófono para la grabación y para Teams.
- Presencial: mesas de 3 personas (los labs piden «parejas o tríos»; en el Día 1 las parejas y tríos **comparten un solo agente** para respetar la cuota de 4K TPM de `gpt-5.6-luna` por cuenta; guía, sección 5). Teams: trabajo individual o en parejas por chat/llamada.
- **Cola de bloqueos (semáforo):** 🟢 listo · 🟡 bloqueado leve (levanta la mano / escribe `LAB-AMARILLO`) · 🔴 bloqueado (`LAB-ROJO` + mensaje de error + captura). Meta: 5 minutos por caso; si no se resuelve, pasa a **modo pareja o demo** y el bloqueo se atiende después.

### Asignación sugerida de módulos (confirmar; en `MATERIALS_INDEX.md` algunos módulos figuran «sin asignar»/«compartido»)

| Día | Módulo | Presenta (propuesta) | Soporte/chat |
|---|---|---|---|
| 1 | Contexto y fundamentos | Valentina | Pablo / Robert |
| 1 | Plataforma Foundry (demos de portal y catálogo) | Pablo | Valentina / Robert |
| 1 | Azure AI Services (incluye demo en vivo de Document Intelligence ≈10:40–10:50) | Valentina (la demo: *por confirmar*; guion en `dia1-lab-guiado\demo-document-intelligence.md`) | Pablo / Robert |
| 1 | Agentes y conocimiento (demo de agente en portal) | Pablo, con Valentina en RAG/MCP | — |
| 1 | Laboratorio guiado (A entorno, B agente, C OCR) | Pablo conduce A y C; Valentina conduce B; el otro da soporte (ver `dia1-lab-guiado\guia-facilitador.md`, sección 2) | Robert (chat) |
| 2 | Arquitectura y runtime (demo agente hospedado) | Pablo | Valentina / Robert |
| 2 | Tools e integración | Valentina (diseño de tools) + Pablo (MCP) | Robert |
| 2 | RAG y Azure AI Search (demo retrieval) | Pablo | Valentina / Robert |
| 2 | Laboratorio pro-code | Pablo conduce; Valentina soporte | Robert (chat) |
| 3 | Protocolos y multiagente | Valentina | Pablo / Robert |
| 3 | Arquitectura empresarial (demo AI Gateway) | Valentina | Pablo |
| 3 | Seguridad y gobierno | Pablo | Valentina |
| 3 | Observabilidad y ciclo de vida (ejercicio de trazas) | Valentina | Pablo |
| 3 | Workshop BCI + cierre ejecutivo | Ambos | Robert (tiempo y mesas virtuales) |

---

## 3. Configuración de la reunión de Teams

Revisa esto en una **reunión de prueba** con el organizador (hoy). Algunas opciones dependen de políticas del tenant de Microsoft: *verificar* qué está disponible.

| Ajuste | Configuración recomendada | Notas |
|---|---|---|
| Tipo de reunión | Reunión programada de Teams con enlace único para los 3 días (`<LINK-TEAMS>`) o 3 enlaces; sala de Microsoft Chile con dispositivo de sala | Si los invitados externos (BCI) tienen sala de espera, abre el lobby 30 min antes y deja pasar a todos. |
| Quién puede presentar | Solo organizadores/instructores como **presentadores**; participantes como asistentes | Evita que alguien comparta pantalla por accidente. |
| Grabación | Activar **grabación** (y transcripción) al inicio de cada día, después de **anunciar el consentimiento** en voz alta y en el chat | Inicia la grabación a las 09:00 y detenla en la pausa solo si es necesario; al final confirma que se generó el archivo. |
| Transcripción / subtítulos | Activar transcripción y subtítulos en vivo en español (elige la variante regional disponible; *verificar*) | Útil para accesibilidad y para el resumen post-evento. |
| Chat | Habilitado para todos; fijar un mensaje con las convenciones: `[P]` pregunta, `[LAB]` bloqueo, `[PARK]` tema para el parking lot | El monitor de Teams mantiene el hilo ordenado. |
| Preguntas y respuestas (Q&A) | Usar el **Q&A de Teams** si está habilitado en la reunión (*verificar*); si no, chat con etiquetas | Ver sección 7. |
| Mano levantada / reacciones | Habilitadas | El monitor avisa al presentador. |
| Salas para grupos | **No dividir a todos los remotos** (27 personas ≈ 9 salas, inmanejable). Usa **2 salas de ayuda opcionales** (acceso/permisos y código) atendidas por el instructor de soporte; el resto permanece en la sala principal con el chat | La grabación puede no incluir las salas: *verificar* en la reunión de prueba. |
| Audio sala | Probar micrófono de sala, parlantes y eco con una persona remota; un micrófono de mano para preguntas de la sala | Ensayo en el T-60. |
| Compartir pantalla | Un solo equipo «de presentación» por bloque; el segundo instructor usa su equipo para monitorear Teams y entorno | Evita ecos: solo un equipo con audio de reunión en la sala. |
| Asistencia | Descargar el informe de asistencia al final de cada día | Útil para el cierre y los entregables. |

---

## 4. Pre-flight diario (T-60 / T-30 / T-5)

### Todos los días

| Cuándo | Qué | Responsable |
|---|---|---|
| **T-60 (08:00)** | Instructores en sala. Abre las diapositivas del día en ambos equipos y la carpeta `plan-b\` **sin conexión** (también en un pendrive o carpeta local). Ejecuta `python scripts\02_validar_entorno.py` con la cuenta de prueba **solo miembro del grupo** (Días 1 y 2). Revisa cuota/errores 429 en el portal de Azure (guía, sección 5). Prueba audio de sala. | Pablo / Valentina |
| **T-60** | `<ADMIN-BCI>` confirma el estado del grupo `grp-bci-foundry-participantes` (altas tardías) y que no hay incidentes de Azure/Entra ni de Teams. | Robert / Diego |
| **T-30 (08:30)** | Abre la reunión de Teams, configura grabación/subtítulos, pega los enlaces y las convenciones del chat. Abre el lobby. Mensaje de bienvenida con `<LINK-REPO>` y el autochequeo. | Robert |
| **T-30** | Si el validador falla: aplica la decisión de la sección 5 (Go/No-Go de la mañana). | Pablo |
| **T-5 (08:55)** | Recuerda a los remotos: micrófono silenciado, cámara opcional, chat. Anuncia **grabación y datos ficticios**. Confirma el rol de cada persona (tabla 2) y quién lleva el tiempo. | Presentador del bloque inicial |

### Específico por día

| Día | Pre-flight adicional |
|---|---|
| **1** | Cuenta de prueba `labNN` con **TAP vigente** (válido el miércoles 21 de 06:30 a 14:30; verificado con `az login --use-device-code` y en `https://ai.azure.com`). Proyecto `lab-NN` con `gpt-5.6-luna`, `gpt-5-mini` y `text-embedding-3-small` **ya desplegados** (para las demos 11, 14 y 26: portal, catálogo, agente). Prueba con la cuenta de participante la **subida de un archivo a file search** y el agente con `gpt-5.6-luna` (**no probado todavía**; si da 403, ver guía, sección 6.1 y el riesgo R21; si el agente falla con ese modelo, usa `gpt-5-mini`). Hoja de cuentas `labNN` ↔ participante y proyecto `lab-NN` (sin datos sensibles) y TAP listos para entregar. Document Intelligence Studio accesible con la cuenta de prueba; documentos ficticios del Bloque C descargados. **Demo en vivo de Document Intelligence** (Receipt sobre `03-comprobante-compra.pdf`, ≈10:40–10:50): ensayada **y** plan B listo (PB-D1-01; ver `dia1-lab-guiado\demo-document-intelligence.md`). |
| **2** | Índice de Azure AI Search **ya creado y con datos ficticios** de normativa; variables de entorno del starter verificadas con `python src\00_verificar_entorno.py --probar-modelo` (cuenta de participante; `FOUNDRY_MODEL=gpt-5-mini`, `FOUNDRY_EMBEDDING_MODEL=text-embedding-3-small`, `AZURE_SEARCH_INDEX_NAME=normativa-austral`; guía, sección 18.2); **Application Insights con trazas visibles** para un usuario con el rol de participante (Log Analytics Reader; Monitoring Reader es complementario). Demos del agente hospedado (diapositivas 10 y 30): *si el hospedaje no está operativo, usa el plan B*. Rama/carpeta `solucion\` lista por si hay que recuperar un bloqueo. **Importante:** el proyecto/recursos de `dia2-lab-procode\` deben quedar intactos al cierre del día — se reutilizan el Día 3 para el ejercicio de trazas (el TAP de acceso se regenera a diario, pero el proyecto y los recursos de Azure persisten los 3 días). |
| **3** | **Sin laboratorio en la nube propio del día**, salvo el ejercicio de trazas que reutiliza el proyecto del Día 2 (`dia2-lab-procode\`): verifica que siga accesible con el TAP regenerado y que el caso fallido quede preparado para la Tarea de diagnóstico (ex Tarea 4). Grabación de la demo del AI Gateway (diapositiva 21) cargada. Plantilla del canvas (`<LINK-CANVAS>`) compartida y caso ficticio «Austral Bank» listo. Mesas/pizarras en sala y grupos virtuales definidos para el workshop. Nota: en la diapositiva 2 las notas del orador hablan de «el workshop de la tarde», pero el evento termina a las 12:30; el workshop es 11:35–12:10. |

---

## 5. Go/No-Go de la mañana (T-30) y modos de entrega

| Resultado | Decisión |
|---|---|
| Validador PASS + ≥ 90 % de los asistentes pasó el autochequeo | **Modo normal** (hands-on). |
| Validador PASS pero 10–30 % bloqueados (SSO, MFA, red) | **Modo mixto:** los bloqueados trabajan en pareja o en el flujo del instructor; el instructor de soporte atiende en paralelo. |
| Validador FAIL en modelos/proyecto, o > 30 % bloqueados | **Modo demo guiada:** el instructor ejecuta el laboratorio en vivo con su proyecto, los participantes siguen y reciben el material para repetirlo luego. Activa `plan-b-demos.md`. |
| Validador FAIL en Search o App Insights (Día 2) | Mantén el lab hasta la Tarea 2; las tareas que dependen de lo que falla se hacen como demo del instructor con grabación. |

---

## 6. Desarrollo por día y reglas de recorte

> **Regla general:** el tiempo lo cuida Robert con avisos T-10/T-5/T-0 por módulo. Si el atraso acumulado supera **5 min** al llegar a la pausa, aplica el primer recorte del módulo siguiente; si supera **10 min**, aplica todos los recortes de la columna. **Nunca** se recorta: las pausas de 10 min en la agenda (se usan para acceso al entorno) ni el cierre con feedback.

### Día 1 — L100 · Fundamentos (09:00–13:00)

| Hora | Módulo | Qué se recorta si vamos tarde | Mínimo indispensable |
|---|---|---|---|
| 09:00–09:30 | **Presentación de apertura** (franja de 30–40 min; el horario fijado es 09:00–09:30, *por confirmar*) | Si se extiende, recorta presentaciones y logística (propuesta); el atraso se absorbe en Contexto y fundamentos (15′) | Objetivos de los 3 días, dinámica híbrida, aviso de grabación, datos ficticios y recordatorio de TAP/prerrequisitos |
| 09:30–09:45 | Contexto y fundamentos | Diapositivas 7 y 8 (evolución de la plataforma y quién hace qué) en una frase (*por confirmar* la numeración con el deck actualizado) | Qué cambió con la IA generativa + Foundry en una vista |
| 09:45–10:15 | Plataforma Foundry (demos 11 y 14) | Demo 14: no crees el deployment en vivo, muestra el modelo ya desplegado; diapositivas 16 y 17 como lectura | Organización del proyecto, elección de modelo, tipos de deployment |
| 10:15–10:55 | Azure AI Services (incluye la **demo en vivo de Document Intelligence**, ≈10:40–10:50) | Diapositiva 21 (resto de Foundry Tools) en lectura; si vamos > 5′ tarde, la demo pasa a 7′ y se omite Read (guion: `dia1-lab-guiado\demo-document-intelligence.md`); si Studio falla, plan B (PB-D1-01) | Document Intelligence (lo usa el Bloque C) y «qué servicio en cada escenario» |
| 10:55–11:30 | Agentes y conocimiento (demo 26) | Toolbox (27), Foundry IQ (29) y MCP (30) en 1–2 min cada uno | Anatomía del agente, prompt vs hosted, **demo 26 completa** (prepara el Bloque B) |
| 11:30–11:40 | **Pausa** | No se recorta. Los remotos dejan a mano su cuenta `labNN` y su **TAP** | — |
| 11:40–12:45 | **Laboratorio guiado** (65′: **A** entorno y prerrequisitos 15′ · **B** tu primer agente 25′ · **C** OCR con Document Intelligence 25′) | Cortes duros: 11:55 (pasa a B aunque haya grupos atrasados), 12:20 (pasa a C aunque haya grupos en B.5; el JSON de respaldo cubre el entregable) y 12:45. Si a las 12:09 más de un tercio no terminó la subida de archivos (B.4): prueba con `gpt-5-mini` o pasa a demo guiada. Si Document Intelligence no abre para la mayoría a las 12:20, C se hace en modo demostración con resultados pre-extraídos (detalle en `dia1-lab-guiado\guia-facilitador.md`, sección 4.3) | Cada persona/pareja deja **entorno verificado** (A), **un agente probado** (B) y **un documento con campos extraídos** (C) |
| 12:45–13:00 | Preguntas y cierre (15′) | Preguntas del parking lot se responden por correo | Resumen, adelanto del Día 2 (nuevo TAP), **pulso de feedback** (3 preguntas) |

### Día 2 — L200 · Agentes y RAG (09:00–13:00)

| Hora | Módulo | Qué se recorta si vamos tarde | Mínimo indispensable |
|---|---|---|---|
| 09:00–09:40 | Arquitectura y runtime (demo 10) | Diapositivas 8 y 9 (protocolo, MAF en una vista) condensadas | Tres formas de construir un agente + demo del agente con tool |
| 09:40–10:20 | Tools e integración | MCP (14–17) a una diapositiva; autenticación MCP solo mención | Diseño de tools y las 4 reglas de contratos |
| 10:20–11:05 | RAG y Azure AI Search (demo 26) | Diapositiva 24 (calidad) en síntesis; mantén seguridad en RAG | Pipeline de indexación, híbrida, retrieval agéntico, **demo 26** |
| 11:05–11:15 | **Pausa** | No se recorta. **Los remotos abren VS Code y validan el entorno** (autochequeo) | — |
| 11:15–12:30 | **Laboratorio pro-code** (preparación 10′ · Tareas 1–2 25′ · Tarea 3 20′ · revisión en parejas y preguntas 20′) | Si la preparación supera 12′: salta a *modo pareja/demo* para los bloqueados. Si T3 se atrasa: entrega la función ya implementada (`solucion\`) y recorta el bloque de revisión | Al menos: agente con grounding (T1–T2) + una tool funcionando (T3); la traza se revisa a fondo el Día 3 |
| 12:30–13:00 | Preguntas y cierre | Checklist de producción en lectura | Resumen, adelanto del Día 3, pulso de feedback |

### Día 3 — L300 · Arquitectura, seguridad y operación (09:00–12:30)

| Hora | Módulo | Qué se recorta si vamos tarde | Mínimo indispensable |
|---|---|---|---|
| 09:00–09:40 | Protocolos y multiagente | Diapositivas 13–14 en síntesis | MCP vs A2A y gobierno |
| 09:40–10:15 | Arquitectura empresarial (demo 21) | **Demo del AI Gateway: usa la grabación (3 min)** | Hosted agents (identidad, aislamiento), sesión 1:1 vs multiplexado, AI Gateway |
| 10:15–10:25 | **Pausa** | No se recorta | — |
| 10:25–11:05 | Seguridad y gobierno | Diapositiva 27 (red teaming vs guardrails) en 1 minuto | Amenazas vs controles + identidad y mínimo privilegio |
| 11:05–11:35 | Observabilidad y ciclo de vida (ejercicio de trazas) | Teoría (cómo viaja una traza) en síntesis si falta tiempo | Cómo viaja una traza + diagnóstico del caso 1 usando el proyecto del Día 2 |
| 11:35–12:10 | **Workshop BCI** (5′ contexto · 10′ canvas · 8′ amenazas · 7′ SLOs · 5′ backlog) | Se protege: reduce teoría previa, no este bloque. Mínimo 25′; recorta primero «SLOs» a 4′ y «Backlog» a 3′ | Canvas completo, 3 amenazas con control, backlog de 3 elementos |
| 12:10–12:30 | Cierre ejecutivo | — | Arquitectura objetivo, backlog, próximos pasos, **formulario final** |

---

## 7. Preguntas y respuestas, parking lot y feedback

**Cómo se hacen las preguntas**
- Un solo canal: chat de Teams (también para la sala) con etiqueta `[P]`; el monitor las numera y las dice en voz alta en las transiciones o cuando el presentador lo indique. Sala: levantar la mano; micrófono de mano.
- Regla de los 60 segundos: si la respuesta es corta se responde; si no, va al **parking lot** (`[PARK]`) con quién responde y cuándo.
- Preguntas sobre datos/políticas de BCI específicas: se anotan y se responden por separado (no se improvisa sobre arquitectura propia de BCI sin contexto).

**Parking lot** (`<LINK-PARKING>`, un documento compartido con columnas: pregunta, día, módulo, responsable, estado) — se revisa en el cierre de cada día y los pendientes se responden por correo con la comunicación de cierre.

**Feedback intermedio**
| Cuándo | Qué | Cómo |
|---|---|---|
| Fin del Día 1 (12:45–13:00) | Pulso de 3 preguntas: ritmo (lento/justo/rápido), claridad del laboratorio, qué ajustar mañana | Encuesta rápida en Teams/Forms (`<LINK-FEEDBACK>`); resultados leídos al inicio del Día 2 |
| Pausa del Día 2 (11:05) | 1 pregunta: «¿Puedes ejecutar el agente base? sí/no/necesito ayuda» | Chat/encuesta; define el modo del laboratorio |
| Fin del Día 3 | Formulario final con calificación por día y comentarios | `<LINK-FEEDBACK>`, enviado también por correo |

**Ajuste entre días:** después de cada día, 15 min de retro de instructores (qué recortar, qué reforzar, bloqueos recurrentes) y actualiza el chat de convenciones y el riesgo correspondiente.

---

## 8. Reglas de manejo de datos y grabaciones

1. **Solo datos ficticios.** Ningún documento, prompt, ticket ni caso real de BCI o de sus clientes. Los casos del taller son inventados («Austral Bank», normativa interna ficticia). Si alguien comparte datos reales: detener, borrar el mensaje y recordar la regla.
2. **No pegues secretos** (claves, cadenas de conexión completas, tokens) en el chat ni en la pantalla compartida; usa autenticación Entra (sin claves) y oculta variables de entorno al mostrarlas.
3. **Trazas y logs** contienen prompts y respuestas: tratar como datos del taller; no exportar fuera del entorno. Qué registrar y qué no: diapositiva 29 del Día 2.
4. **Grabación:** se anuncia al inicio; se comparte solo con los inscritos; conservación y eliminación según política acordada con BCI (*verificar*). No se graba el trabajo en salas de ayuda salvo acuerdo.
5. **Capturas de pantalla** de participantes: solo con permiso y sin datos sensibles.
6. **Limpieza:** tras el evento se elimina el grupo de recursos con `scripts\03_limpieza.ps1` (con confirmación explícita) y se revisa el *soft-delete* de 48 h (guía, sección 12).

---

## 9. Entregables post-evento

| Entregable | Qué incluye | Responsable | Plazo sugerido |
|---|---|---|---|
| Grabaciones (3) | Enlaces a las grabaciones de los tres días (+ transcripción si existe), con acceso controlado | Robert | Fecha del evento + 2 días hábiles |
| Repositorio | `<LINK-REPO>`: starter de los labs, soluciones, guías, scripts del kit (sin secretos) | Pablo | Evento + 2 días hábiles |
| Presentaciones | Los 3 decks (`presentaciones\BCI_Foundry_Dia1…Dia3.pptx`, versión revisada) | Valentina | Evento + 2 días hábiles |
| Respuestas del parking lot | Documento con preguntas pendientes respondidas | Pablo / Valentina | Evento + 3 días hábiles |
| Formulario de feedback | Enlace enviado el Día 3; consolidado de resultados | Robert | Envío: 23-oct; consolidado: +5 días hábiles |
| Closeout con BCI | Resumen ejecutivo: asistencia, hallazgos, próximos pasos, lecciones del entorno | Pablo + Diego | Evento + 5 días hábiles |
| Cierre del entorno | Eliminación del grupo de recursos, purga de recursos en soft-delete, retiro de roles/grupos, confirmación de costos | `<ADMIN-BCI>` + Pablo | Fecha de eliminación acordada (la guía propone `2026-10-26`) |
| Correo de agradecimiento | `comunicaciones.md` (borrador 3) | Robert | Viernes 23-oct (tarde); si algún enlace no está listo, indicar la fecha de entrega |

---

## 10. Registro de riesgos

Probabilidad (P) e impacto (I): A = alta, M = media, B = baja (estimación cualitativa del equipo; no proviene de datos medidos).

| ID | Riesgo | P / I | Señal de alerta | Mitigación (antes) | Contingencia (durante) | Responsable |
|---|---|---|---|---|---|---|
| R1 | **Funciones en preview** no disponibles por región/modelo/SDK: trazas de agentes de flujo de trabajo o externos (GA solo para agentes de prompt y hospedados), planificación/síntesis del agentic retrieval, evaluación con `azd ai agent eval` y monitoreo | M / A | El validador o la prueba manual no muestra trazas/retrieval agéntico | Verificar hoy con la cuenta de prueba (región, modelo y SDK) y confirmar si el agente del starter cuenta como «externo» para el rastreo (`docs-oficiales\foundry\observability\how-to\trace-agent-setup.md`); documentar versiones; tener plan B | Demo con **grabación**/capturas; el laboratorio mantiene lo disponible (grounding clásico, tool) | Pablo |
| R2 | **Cuota o capacidad** insuficiente: errores **429** reales con `gpt-5.6-luna` (≈4K TPM por cuenta; con ≈3K tokens de entrada dos veces seguidas se supera) | A / A | 429 en las primeras pruebas del Bloque B o de la comparación del Bloque C | Parejas/tríos comparten un solo agente; textos cortos (la guía lo pide); cuota total: 62 cuentas × 4K = 248K TPM (GlobalStandard 37 cuentas, DataZoneStandard 25; guía, sección 5); `gpt-5-mini` (10K TPM) desplegado como respaldo | Esperar ≈10 s, acortar el prompt o cambiar el modelo del agente a `gpt-5-mini`; modo pareja/trío; escalar a `<ADMIN-BCI>` | Pablo / `<ADMIN-BCI>` |
| R3 | **SSO / acceso condicional / MFA** bloquea a participantes: AADSTS50079/50076 (no usan el TAP), TAP aún no válido (antes de 06:30) o expirado (después de 14:30), cookies de terceros bloqueadas (AADSTS50058 en Document Intelligence Studio), red de invitados, remotos | M / A | Fallo de inicio de sesión en el Bloque A | Entregar los TAP con instrucciones (**Use a Temporary Access Pass instead**); probar con un usuario real desde red de invitados; definir quién reemite TAP (*por confirmar*); excepción temporal por grupo (guía, sección 10.3) | Reemitir TAP o alta de excepción en vivo por `<ADMIN-BCI>`; mientras tanto, modo pareja/demo | Diego / `<ADMIN-BCI>` |
| R4 | **Bloqueo de red/egress** (proxy, firewall, SSL inspection) hacia `ai.azure.com`, Search, PyPI, GitHub | M / M | `02_validar_entorno.py --egress` falla | Compartir la lista de destinos (guía, sección 10.2) con el equipo de red | Hotspot/Wi-Fi alternativo de la sala, Codespaces, o demo | Diego / red BCI |
| R5 | **Modelo no disponible** en la región/versión o retirado | B / A | La lista de despliegues no muestra `gpt-5.6-luna` | Verificar hoy que `gpt-5.6-luna`, `gpt-5-mini` y `text-embedding-3-small` estén desplegados en cada cuenta (`02_validar_entorno.py`); `Add-Modelo.ps1` es idempotente y vuelve a desplegar `gpt-5.6-luna` | Día 1: elegir en el portal `gpt-5-mini`; Día 2: cambiar `FOUNDRY_MODEL` en el `.env` (el starter usa variables) | Pablo |
| R6 | **TAP inválido o expirado** (antes de las 06:30 o después de las 14:30 del miércoles; Día 2/3: TAP regenerado cada noche y no entregado) | M / A | AADSTS50079/50076 persistente aun usando el TAP; «TAP no válido» | Entregar los TAP del Día 1 el miércoles después de las 06:30 y los de los días 2 y 3 cada mañana; hoja de cuentas ↔ TAP lista | Un facilitador/organizador reemite el TAP (*por confirmar* quién); mientras tanto, pareja con una cuenta ya autenticada | Robert / `<ADMIN-BCI>` |
| R7 | **27 usuarios remotos saturan el laboratorio** (soporte, ancho de banda, límites de tasa) | A / M | Cola de bloqueos > 5 casos simultáneos | Autochequeo previo; Robert filtra el chat; 2 salas de ayuda opcionales; guías con capturas | Priorizar bloqueos 🔴, pasar a parejas, ofrecer sesión de soporte posterior | Pablo / Robert |
| R8 | **Nadie monitorea Teams** mientras un instructor presenta | M / M | Preguntas del chat sin respuesta | Cerrar D1 de la sección 1 hoy | Rotación de 15 min entre instructores; el presentador revisa el chat en cada transición | Robert |
| R9 | **Altas tardías / roles que no propagan** | M / M | Usuario sin ver el proyecto | Cerrar altas con ≥ 4 h de anticipación (guía, sección 11); reservas `lab-reserva-0X` | Asignar un proyecto de reserva; modo pareja | `<ADMIN-BCI>` |
| R10 | **Notebook corporativo bloqueado** (no puede instalar VS Code, Python 3.13, Git o Azure CLI, prerrequisitos del Bloque A) | A / M | Respuestas al onboarding y al autochequeo previo (`code/python/git/az --version`) | `onboarding-participantes.md` con alternativas (Codespaces, pareja, demo); instalar con `winget` antes de la sesión | Pareja con compañero (B y C se hacen en el navegador); seguir la demo del instructor | Robert / Diego |
| R11 | **Problemas de audio/video híbrido** (eco, micrófono de sala) | M / M | Prueba de sala con un remoto | Ensayo en T-60; un solo equipo con audio de reunión; micrófono de mano | Segundo equipo con chat y cámara; el monitor avisa por chat | Robert |
| R12 | **Idioma del lab pro-code sin confirmar** (Python vs .NET) | M / M | Respuesta de BCI pendiente | Python por defecto; avisar a los inscritos en el onboarding | .NET como demo del instructor | Diego / Pablo |
| R13 | **Datos reales o secretos** aparecen en chat/pantalla/grabación | B / A | Menciones de clientes, claves en pantalla | Reglas de la sección 8 al inicio de cada día; plantillas ficticias | Detener, borrar el mensaje, editar o eliminar fragmento de la grabación | Todos |
| R14 | **Desfase de tiempo** (especialmente el laboratorio del Día 1) | A / M | Atraso > 5 min en la pausa | Reglas de recorte de la sección 6; módulos con avisos T-10/T-5 | Aplicar recortes; mover preguntas al parking lot | Robert (tiempo) |
| R15 | **Demo de agente hospedado no operativa** (ACR, permisos, región) | M / M | El despliegue falla en el ensayo | Preparar hoy el agente; roles de instructor (guía, sección 6.4) | Reproducir con la grabación y la traza capturada | Pablo |
| R20 | **`gpt-5-mini` no soporta la herramienta o función que usa el agente del Día 2** (la matriz de herramientas por modelo marca Azure AI Search y Functions = No para `gpt-5-mini`; *verificar* si aplica al flujo del lab: `docs-oficiales\foundry\agents\concepts\limits-quotas-regions.md`) | M / A | `00_verificar_entorno.py --probar-modelo` o `03_agente_con_search.py` falla en la prueba de hoy | Probar hoy con la cuenta de participante; `gpt-5.6-luna` y `gpt-4.1-mini` como alternativas si están desplegados (*verificar*); el `.env` usa `FOUNDRY_MODEL` | Cambiar `FOUNDRY_MODEL` por otro deployment disponible, avisarlo en el chat y reiniciar la terminal | Pablo |
| R21 | **Subida de archivos a file search da 403** (Día 1, Bloque B) por falta de Storage Blob Data Contributor sobre el Storage del proyecto: el aprovisionamiento solo asigna Foundry User y Reader (*verificar*) | M / M | Error 403 al subir el documento con la cuenta de prueba | Probar hoy; asignar el rol con `01_crear_grupo_y_roles.ps1 -StorageProyecto` (guía, sección 6.1) | El instructor sube el documento en un proyecto compartido o se usa la demo PB-D1-02 | Pablo / `<ADMIN-BCI>` |
| R23 | **`gpt-5.6-luna` + Foundry Agent Service + file search NO probado** desde una cuenta de participante (solo se probaron llamadas básicas con Chat Completions y Responses API en eastus2) | M / A | El agente no se guarda, no usa file search o responde con error en la prueba de `checklist-validacion.md` (pasos 8 a 11) | Probar hoy con una cuenta de participante; documentar el resultado en la checklist | Cambiar el modelo del agente a `gpt-5-mini` (ya desplegado) y continuar; si el agente falla con ambos, B en modo demo guiada (PB-D1-02) | Pablo |
| R22 | **Ranker semántico, embeddings o autenticación de Application Insights no disponibles** (Día 2) | M / M | Errores en `01_crear_indice.py`, en la consulta o al exportar trazas | Probar hoy con el validador del lab; confirmar si la autenticación local de Application Insights está deshabilitada (guía, sección 18.2) | Planes B del lab: `LAB_SIN_SEMANTICO=true`; `FOUNDRY_EMBEDDING_MODEL=` vacío (consulta solo de texto); `ENABLE_CONSOLE_EXPORTERS=true` (spans en consola); `LAB_APPINSIGHTS_ENTRA` (requiere Monitoring Metrics Publisher) | Pablo |
| R16 | **Índice de Search vacío o sin permisos** | B / A | El validador falla en el índice | Instructores crean y verifican el índice; Search Index Data Reader | Mostrar los resultados con capturas; Tarea 2 como demo | Pablo |
| R17 | **Demos del Día 3 sin artefactos** (panel APIM ilustrativo, eval como código) | M / M | No existe entorno/panel listo | Definir hoy qué artefacto se usa; grabar con tiempo | Usar la grabación y explicar el flujo en la pizarra | Valentina |
| R18 | **Costos** por encima de lo esperado | B / M | Alertas del presupuesto | Alertas de presupuesto y etiquetas (guía, sección 12) | Reducir capacidad de modelos o pausar proyectos de reserva | `<ADMIN-BCI>` |
| R19 | **Nombres bloqueados por soft-delete** al reutilizar/recrear recursos | B / B | Error al recrear el recurso | Nombres únicos; purga con `03_limpieza.ps1 -Purgar` | Esperar 48 h o purgar | `<ADMIN-BCI>` |

---

## 11. Escalamiento y comunicación durante el evento

| Situación | Acción | Responsable | Canal |
|---|---|---|---|
| Fallo general de Azure/modelos (todos bloqueados) | Pasar a modo demo guiada; revisar estado del servicio; avisar a `<ADMIN-BCI>` | Pablo | Chat + llamada |
| Acceso/permisos individual | Cola de bloqueos; si > 5 min, modo pareja | Instructor de soporte | Chat |
| Preguntas de seguridad/arquitectura específicas de BCI | Parking lot; responder en Día 3 o por correo | Pablo / Valentina | Parking lot |
| Incidente de privacidad (dato real/secreto) | Detener, borrar, informar a Robert; evaluar edición de la grabación | Robert | Directo |

---

## Fuentes
- Agenda, módulos, demos y laboratorios: `presentaciones\content\day1.json`, `day2.json`, `day3.json`; `MATERIALS_INDEX.md` (§1–§4, §6).
- Entorno, cuotas, roles, red, costos y limpieza: `laboratorios\entorno-y-facilitacion\guia-entorno-admin-bci.md` (secciones 5, 6, 10, 11, 12) y las fuentes citadas allí (`docs-oficiales\foundry\openai\quotas-limits.md`, `docs-oficiales\foundry\openai\how-to\quota.md`, `docs-oficiales\foundry\concepts\rbac-foundry.md`); aprovisionamiento real: `laboratorios\entorno-y-facilitacion\provisionamiento\` (`Provision-Lab.ps1`, `Add-Modelo.ps1`).
- Laboratorio del Día 1: `laboratorios\dia1-lab-guiado\guia-facilitador.md`, `demo-document-intelligence.md` y `checklist-validacion.md`.
- Validación previa de entorno: `laboratorios\entorno-y-facilitacion\scripts\02_validar_entorno.py`; limpieza: `scripts\03_limpieza.ps1`; base del preflight: `repos\publico-workshops\foundry-hosted-agents-workshop\.workshop\scripts\preflight.py`.
- Rastreo y estado de preview: `docs-oficiales\foundry\observability\how-to\trace-agent-setup.md`.
- Configuración de Teams (grabación, transcripción, Q&A, salas): funciones estándar del producto sujetas a políticas del tenant → *verificar* en la reunión de prueba (no hay documentación de Teams en `docs-oficiales\`).
- Probabilidades e impactos del registro de riesgos: estimación cualitativa del autor; sin datos medidos.

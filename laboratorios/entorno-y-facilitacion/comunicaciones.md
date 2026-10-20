# Comunicaciones: borradores (no enviar sin revisión)

> **Solo borradores.** No se envió nada. Reemplaza los marcadores `<...>` antes de enviar. Tono: español neutro, tuteo. Hoy es T-1 (20-oct-2026); el evento comienza mañana, 21-oct, 09:00 (hora de Chile).

---

## Borrador 1 · Correo al administrador Azure de BCI: checklist del entorno (enviar HOY, primera hora)

**Para:** `<ADMIN-BCI>` · **CC:** Diego Bell Tineo `<CORREO-DIEGO>`, Robert Escalante `<CORREO-ROBERT>`, Valentina Grajales `<CORREO-VALENTINA>`
**Asunto:** Microsoft AI Foundry BCI Training Day · Checklist de entorno para mañana 09:00 (necesitamos tu confirmación hoy)

Hola `<NOMBRE>`:

Mañana (21-oct) comienza el Training Day con ~48 participantes (21 presenciales y 27 por Teams). Para que el laboratorio del **Día 1** funcione, necesitamos confirmar hoy el estado del entorno. Adjuntamos la **guía de entorno** (`guia-entorno-admin-bci.docx`, con la sección 14 «camino mínimo de 24 horas») y los scripts de apoyo (revísalos con `-WhatIf` antes de ejecutarlos).

**¿Puedes confirmarnos hasta las `<HORA>` de hoy?**
1. Suscripción y región del laboratorio (East US 2) y quién administra el tenant del evento (`mngenvmcap219366.onmicrosoft.com`; *por confirmar*).
2. Un grupo de recursos `rg-bci-lab-NN` por participante, con su recurso Foundry y su proyecto `lab-NN`, y los despliegues ya creados con el mismo nombre que el modelo: `gpt-5.6-luna` (modelo principal del Día 1; 4K TPM por cuenta), `gpt-5-mini` (respaldo; 10K TPM) y `text-embedding-3-small`. La cuota total de `gpt-5.6-luna` es 62 cuentas × 4K = 248K TPM (GlobalStandard en 37 cuentas y DataZoneStandard en 25). Por favor no renombres los despliegues: sus nombres llegan a los participantes en el `.env` del Día 2 (`FOUNDRY_MODEL`, `FOUNDRY_EMBEDDING_MODEL`). Cuota disponible en la suscripción (guía, sección 5) y, si hace falta, la solicitud de aumento.
3. Grupos de Entra `grp-bci-lab-participantes` y `grp-bci-lab-instructores`, con los roles **Foundry User** y **Reader** sobre cada `rg-bci-lab-NN`, y la lista de participantes cargada **a más tardar a las `<HORA>`**. ¿Hace falta algún rol adicional (por ejemplo, Storage Blob Data Contributor para subir archivos a file search o Cognitive Services User para Document Intelligence Studio)?
4. Document Intelligence (S0) para el Día 1 (¿qué recurso usa cada cuenta `labNN` en Studio?, *por confirmar*); Azure AI Search, Application Insights y Log Analytics para el Día 2 (pueden terminar mañana en la tarde).
5. **Temporary Access Pass (TAP)** y red: las cuentas `labNN@mngenvmcap219366.onmicrosoft.com` están protegidas con MFA y los participantes no pueden registrarlo, por lo que inician sesión con un TAP (el del Día 1 vale solo el miércoles 21 entre 06:30 y 14:30, hora de Chile; los de los días 2 y 3 se regeneran cada noche). ¿Quién los entrega y quién puede reemitirlos durante el taller? ¿Podrán conectarse los asistentes remotos y la red de invitados de la sala, y permitir cookies de terceros para Document Intelligence Studio (AADSTS50058)? Lista de destinos a permitir en la guía, sección 10.
6. Cuentas de prueba (una de participante y una de instructor) para validar antes de las 08:00.
7. Lenguaje del laboratorio de código del Día 2: ¿Python? (es nuestra propuesta por defecto).
8. Tu contacto de guardia mañana entre las 08:30 y las 13:30.

Si prefieres, coordinemos una llamada de 20 minutos hoy para recorrer la lista. Gracias por tu apoyo.

Saludos,
`<FIRMA: Pablo Braconi / Robert Escalante>`

---

## Borrador 2 · Mensaje a los asistentes: preparación y enlaces (enviar HOY por correo; versión corta para Teams)

**Para:** Lista de inscritos (CCO) `<LISTA-ASISTENTES>` · **Asunto:** Mañana comienza el Microsoft AI Foundry BCI Training Day: 15 minutos de preparación

Hola:

¡Mañana comenzamos! Estas son las fechas y los enlaces:

- **Cuándo:** 21, 22 y 23 de octubre, de 09:00 a 13:00 (hora de Chile).
- **Dónde:** Microsoft Chile (Las Condes) o por Teams: `<LINK-TEAMS>`.
- **Material y repositorio:** `<LINK-REPO>`.

**Antes de las 09:00 de mañana (≈15 minutos):**
1. **Instala los prerrequisitos** (en Windows, con PowerShell): `winget install -e --id Microsoft.VisualStudioCode`, `winget install -e --id Python.Python.3.13`, `winget install -e --id Git.Git` y `winget install -e --id Microsoft.AzureCLI`. Cierra y abre la terminal y verifica con `code --version`, `python --version` (debe ser 3.13.x; 3.14 aún no es compatible), `git --version` y `az --version`.
2. **Tu cuenta y tu TAP:** te enviaremos tu cuenta del taller (`labNN@mngenvmcap219366.onmicrosoft.com`; no es tu cuenta corporativa de BCI) y los organizadores te entregarán un **Temporary Access Pass (TAP)** `<CANAL-ENTREGA-TAP>`. Con el TAP inicias sesión en `https://ai.azure.com` y en Azure CLI; **solo es válido el miércoles 21 entre las 06:30 y las 14:30 (hora de Chile)**, así que la prueba de inicio de sesión la haremos mañana.
3. **El laboratorio del Día 1 comienza con una verificación de entorno de 15 minutos** (a las 11:40): instalarás la extensión Foundry Toolkit para VS Code, iniciarás sesión con tu TAP y comprobarás que ves tu proyecto y los modelos ya desplegados. Para el **Día 2** usaremos lo mismo (instrucciones y autochequeo con capturas: `<LINK-SELFCHECK>`); los nombres de los despliegues de modelo te los entregamos ese día en el archivo `.env`.

¿Tu notebook está restringido? No te preocupes: puedes trabajar en pareja, usar Codespaces (Día 2) o seguir la demo del instructor. Escríbenos a `<CORREO-SOPORTE>`.

Recuerda: usaremos **solo datos ficticios** y las sesiones serán **grabadas**.

Nos vemos mañana,
`<FIRMA: Equipo Microsoft · Pablo Braconi, Valentina Grajales, Robert Escalante>`

**Versión breve para el chat de Teams / WhatsApp corporativo:**
> ¡Mañana comenzamos el Microsoft AI Foundry BCI Training Day (09:00–13:00, hora de Chile)! Antes de dormir, instala VS Code, Python 3.13, Git y Azure CLI y verifica las versiones (`code --version`, `python --version`, `git --version`, `az --version`). Mañana recibirás tu cuenta `labNN` y un TAP (Temporary Access Pass, válido solo el miércoles 21 de 06:30 a 14:30): el laboratorio de las 11:40 empieza con una verificación de entorno de 15 minutos. Enlaces: Teams `<LINK-TEAMS>` · material `<LINK-REPO>` · autochequeo `<LINK-SELFCHECK>`. Si algo no funciona: `<CORREO-SOPORTE>`.

---

## Borrador 3 · Agradecimiento post-evento con entregables (enviar el viernes 23-oct en la tarde; si algún enlace aún no está listo, indica la fecha de entrega)

**Para:** Lista de asistentes `<LISTA-ASISTENTES>` · **CC:** Diego Bell Tineo `<CORREO-DIEGO>` · **Asunto:** Gracias por participar: grabaciones, repositorio y presentaciones del BCI Training Day

Hola:

Gracias por tres jornadas de trabajo, preguntas y buenas conversaciones. Aquí tienes los materiales del evento:

- **Grabaciones:** Día 1 `<LINK-GRABACION-D1>` · Día 2 `<LINK-GRABACION-D2>` · Día 3 `<LINK-GRABACION-D3>` (acceso solo para los inscritos).
- **Repositorio** con los laboratorios, las soluciones y las guías: `<LINK-REPO>`.
- **Presentaciones** de los tres días: `<LINK-PRESENTACIONES>`.
- **Respuestas a las preguntas pendientes** (parking lot): `<LINK-PARKING>` (te avisaremos si falta alguna).

**Tu opinión es muy valiosa:** completa el formulario de feedback (3 minutos) hasta el `<FECHA-LIMITE>`: `<LINK-FEEDBACK>`.

**Sobre el entorno de laboratorio:** el equipo de TI de BCI eliminará los recursos del laboratorio el `<FECHA-ELIMINACION>`; guarda hoy lo que quieras conservar (todo el código está en el repositorio). Recuerda que los datos usados fueron ficticios.

¿Quieres continuar? Coordinaremos con Diego los próximos pasos (arquitectura objetivo y backlog del Día 3).

Saludos,
`<FIRMA: Pablo Braconi, Valentina Grajales, Robert Escalante>`

---

## Fuentes
- Fechas, modalidad, cifras de asistencia y alcance por día: `MATERIALS_INDEX.md` y `presentaciones\content\day1.json`, `day2.json`, `day3.json`.
- Entorno, roles, cuota, red y camino mínimo de 24 h: `laboratorios\entorno-y-facilitacion\guia-entorno-admin-bci.md` (secciones 5, 6, 10, 14); pre-trabajo de participantes: `laboratorios\entorno-y-facilitacion\onboarding-participantes.md`.
- Entregables y fechas de cierre: `laboratorios\entorno-y-facilitacion\runbook-facilitacion-3-dias.md` (sección 9). Todos los enlaces y correos son marcadores.

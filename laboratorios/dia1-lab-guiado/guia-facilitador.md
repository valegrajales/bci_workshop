# Guía del facilitador — Día 1: jornada y laboratorio guiado (65 min)

**"Prepara tu entorno, crea tu primer agente y prueba OCR con Document Intelligence"** · Microsoft AI Foundry BCI Training Day · Miércoles 21 de octubre de 2026 · Laboratorio: 11:40–12:45 (hora de Chile)

> Documento para los facilitadores. Todos los ejemplos usan el banco ficticio **Austral Bank**. No uses datos reales, claves, TAP ni endpoints en pantalla compartida: usa los marcadores `<TU-ENDPOINT>`, `<TU-CLAVE>`, `<TU-TAP>`.
>
> **Importante (estado de la validación):** hasta ahora solo se probaron llamadas básicas a `gpt-5.6-luna` (Chat Completions y Responses API, región eastus2). **Todavía NO se probó `gpt-5.6-luna` con Foundry Agent Service + file search desde una cuenta de participante.** Ejecuta `checklist-validacion.md` antes del taller (hoy o mañana temprano) y, si falla con `gpt-5.6-luna`, usa `gpt-5-mini` como modelo del agente. Ajusta los nombres de la interfaz si difieren.

## 1. Datos del evento y de la sala

| | |
|---|---|
| Asistentes | ≈48 según el plan: 21 presenciales + 27 por Teams (formato híbrido). Hay 58 cuentas de participante provisionadas (`lab01`–`lab58`) y 4 de instructor (`inst01`–`inst04`): número final de asistentes **por confirmar** |
| Nivel | L100, experiencia mixta, sin experiencia previa en Foundry |
| Duración del laboratorio | 65 min: **A ≈15** (entorno y prerrequisitos) · **B ≈25** (tu primer agente) · **C ≈25** (OCR con Document Intelligence) |
| Antes | 11:30–11:40 pausa. El módulo Agentes y conocimiento (10:55–11:30) incluye la demo de crear un agente (número de diapositiva: **por confirmar** con el equipo de presentaciones) |
| Demo previa | Demo en vivo de Document Intelligence (≈10 min) dentro del módulo Azure AI Services, ≈10:40–10:50 (sección 4.2) |
| Después | 12:45–13:00 preguntas y cierre (15 min) |
| Cuentas | `labNN@mngenvmcap219366.onmicrosoft.com` (NN = 01 a 58; instructores `instNN`), tenant `eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc`, con MFA/acceso condicional. Inicio de sesión **con TAP** (válido solo el miércoles 21 de octubre, 06:30–14:30, hora de Chile) |
| Entorno por persona | Grupo de recursos `rg-bci-lab-NN` con cuenta Foundry y proyecto `lab-NN`; roles Foundry User + Reader; modelos predesplegados `gpt-5.6-luna` (principal, 4K TPM), `gpt-5-mini` (alternativa, 10K TPM) y `text-embedding-3-small` |
| Grupos | Parejas o tríos que **comparten una sola cuenta `labNN` y un solo agente** desde el Bloque B (cuota de 4K TPM). Con tríos: 7 grupos presenciales + 9 remotos = ≈16 grupos activos en B y C (cálculo de planificación). En el Bloque A cada persona verifica **su propio** entorno. El límite de 16 sesiones de un entorno compartido de Microsoft no aplica porque las cuentas son individuales |
| Documentos | Guía del participante (`README.md` y `Guia_del_participante_Dia1.docx`), carpeta `datos\`, `prompts.md`, `demo-document-intelligence.md` |

## 2. Roles

| Rol | Persona | Bloque A (entorno) | Bloque B (agente) | Bloque C (OCR) |
|---|---|---|---|---|
| **Facilitador 1** | Pablo Braconi | Maneja la pantalla compartida y narra cada paso | Soporte en sala y revisión de checkpoints | Maneja la pantalla y narra |
| **Facilitador 2** | Valentina Grajales | Recorre la sala (ayuda individual con `az`, TAP y VS Code) | Maneja la pantalla y narra | Soporte en sala y modera la comparación (C.5) |
| **Monitor de Teams** | Por confirmar (puede ser un tercer miembro del equipo o un colaborador de Microsoft Chile) | Lee el chat, responde con plantillas, recoge los ✔ de checkpoint y avisa los bloqueos de acceso (TAP) | Igual; comparte el JSON de respaldo | Igual; recoge preguntas |

Reglas del equipo:

- Un solo facilitador habla a la vez; el otro observa la sala o el chat.
- El facilitador que maneja la pantalla **no** resuelve bloqueos individuales.
- El monitor de Teams anota en una lista compartida (o en un bloc) cada bloqueo con la hora, el grupo y la causa, para la retrospectiva.
- Si el entorno cae para todos, cualquiera de los dos facilitadores puede declarar **plan B** (sección 7).
- Quién puede reemitir un TAP vencido o no válido durante la jornada: **por confirmar** con los organizadores (define una persona de contacto antes del miércoles).
- Demo en vivo de Document Intelligence (10:40–10:50): la presenta quien dicta el módulo Azure AI Services (en el runbook, Valentina; **por confirmar**); el otro facilitador monitorea el chat y tiene el Plan B abierto.

## 3. Antes del día (hoy) y listas T-30

### 3.1 Hoy o mañana temprano

- [ ] Ejecutar `checklist-validacion.md` completo en el entorno real (cuenta con TAP, `az`, modelo `gpt-5.6-luna`, agente + file search, Document Intelligence, demo en vivo).
- [ ] Probar **`gpt-5.6-luna` con Foundry Agent Service + file search desde una cuenta de participante** (no está probado). Si falla, documentar el error y decidir el uso de `gpt-5-mini` como modelo del agente.
- [ ] Provocar y registrar un `429` real con `gpt-5.6-luna` (≈4K TPM: dos mensajes de ≈3K tokens seguidos lo superan) y confirmar que el cambio a `gpt-5-mini` resuelve.
- [ ] Confirmar quién provisiona y qué incluye: grupos de recursos, modelos, recurso de Document Intelligence, roles (ver README, sección 4.2).
- [ ] Confirmar que los participantes recibieron la cuenta y el TAP (o cómo los recibirán) y el correo de pre-trabajo: **instalar VS Code, Python 3.13, Git y Azure CLI antes de la sesión** (`entorno-y-facilitacion\onboarding-participantes.md`).
- [ ] Enviar a los participantes la carpeta `datos\` y la guía (Teams o SharePoint) **antes de las 11:30**.
- [ ] Preparar el plan B: grabaciones y capturas (sección 7). Guardarlas en una carpeta local y también en el equipo del segundo facilitador.
- [ ] Guardar un `resultado-factura.json` **real** obtenido en el entorno (de tu propio análisis de `01-factura.png`) para compartirlo con quienes vayan atrasados en C.5.
- [ ] Ensayar la **demo en vivo de Document Intelligence** con `03-comprobante-compra.pdf` y guardar capturas y JSON (`demo-document-intelligence.md`, sección 7).
- [ ] Confirmar quién es el monitor de Teams y probar el chat.

### 3.2 Lista T-30 de la demo (a las 10:10, antes del módulo Azure AI Services)

| # | Verificación | Quién | Listo |
|---|---|---|---|
| 1 | Document Intelligence Studio abre con la cuenta de demo y el recurso correcto; `03-comprobante-compra.pdf` se analiza con **Receipt** | F2 | ☐ |
| 2 | Cookies de terceros permitidas en el navegador de la demo; TAP vigente (válido hasta las 14:30) | F2 | ☐ |
| 3 | Plan B de la demo abierto y reproducible (capturas, JSON y video, si existe) | F1 | ☐ |
| 4 | Pantalla limpia: sin claves, correos ni otras pestañas | F2 | ☐ |

### 3.3 Lista T-30 del laboratorio (a las 11:10, mientras corre el módulo Agentes y conocimiento)

| # | Verificación | Quién | Listo |
|---|---|---|---|
| 1 | Portal `https://ai.azure.com` abre con la cuenta del taller (TAP); **New Foundry** activado | F1 | ☐ |
| 2 | `az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc` funciona en el equipo de demostración y `az account show` muestra la cuenta | F1 | ☐ |
| 3 | El proyecto de demostración abre y `gpt-5.6-luna` (con `gpt-5-mini` de respaldo) está desplegado y responde | F1 | ☐ |
| 4 | Un agente de prueba con file search responde con cita (preguntas 1 y 6 de `prompts.md`) usando `gpt-5.6-luna`; si no, repetir con `gpt-5-mini` | F1 | ☐ |
| 5 | Document Intelligence Studio abre con el recurso correcto y `01-factura.png` se analiza | F2 | ☐ |
| 6 | Plan B abierto y reproducible (capturas, JSON y la captura de un `429` real) | F1 | ☐ |
| 7 | Carpeta `datos\` y guía publicadas en el canal/chat del taller; enlace visible en la pantalla | Monitor | ☐ |
| 8 | Pantalla compartida muestra solo la terminal o el portal (sin claves, TAP, correos ni otras pestañas) | F1 | ☐ |
| 9 | Chat de Teams: mensaje de bienvenida con el enlace, el código "Ayuda Bloque A/B/C" (A = entorno, B = agente, C = OCR) y los grupos | Monitor | ☐ |
| 10 | Lista de grupos (parejas/tríos), cuenta `labNN` que usará cada grupo desde el Bloque B y nombre de agente con sufijo si comparten proyecto | F2 | ☐ |
| 11 | Persona de contacto de los organizadores localizable para reemitir un TAP (**por confirmar**) | Monitor | ☐ |

## 4. Flujo del Día 1

### 4.1 Cronograma de la jornada (hora de Chile)

| Hora | Módulo | Notas |
|---|---|---|
| 09:00–09:30 | Presentación de apertura | Franja de 30–40 min; el horario fijado es 09:00–09:30 (si se extiende, el recorte lo decide el runbook; **por confirmar**) |
| 09:30–09:45 | Contexto y fundamentos | |
| 09:45–10:15 | Plataforma Foundry | |
| 10:15–10:55 | Azure AI Services | Incluye la **demo en vivo de Document Intelligence** (≈10:40–10:50, sección 4.2) |
| 10:55–11:30 | Agentes y conocimiento | |
| 11:30–11:40 | Pausa | Publicar enlaces; participantes con la cuenta y el TAP a mano |
| **11:40–12:45** | **Laboratorio guiado (65 min)** | **A** 11:40–11:55 · **B** 11:55–12:20 · **C** 12:20–12:45 (sección 4.3) |
| 12:45–13:00 | Preguntas y cierre (15 min) | Sección 9 |

### 4.2 Demo en vivo de Document Intelligence (≈10 min, 10:40–10:50)

| | |
|---|---|
| Dónde | Dentro del módulo Azure AI Services (10:15–10:55): contenido del módulo hasta ≈10:40, demo ≈10:40–10:50 y cierre del módulo ≈10:50–10:55 (reparto del módulo: **por confirmar**) |
| Qué | Documento `datos\documentos-ocr\03-comprobante-compra.pdf` con el modelo prebuilt **Receipt**; luego **Layout** o **Read** sobre el mismo archivo para contrastar OCR con extracción estructurada |
| Por qué el 03 | El laboratorio de los participantes usa `01-factura` (Invoice) y `02-solicitud-credito` (Layout); la demo usa el archivo que no se usa en el laboratorio |
| Guion | `demo-document-intelligence.md` (minuto a minuto, campos esperados solo de `campos-esperados.md`, puntos de confianza, puentes y Plan B) |
| Prerrequisitos | Studio `https://documentintelligence.ai.azure.com`, rol **Cognitive Services User** sobre el recurso (**por confirmar**), cookies de terceros permitidas, TAP vigente |
| Plan B | Capturas y JSON guardados del ensayo (PB-D1-01 en `entorno-y-facilitacion\plan-b-demos.md`); si Studio tarda o falla, pasa a ellos sin disculpas largas |
| Puente | Bloque C: los participantes repiten con factura y solicitud de crédito. Día 2 (Tarea 3): herramienta propia de un agente |

### 4.3 Plan minuto a minuto del laboratorio (11:40–12:45)

| Hora | Min lab | Qué pasa | Pantalla / acción | F1 | F2 | Monitor |
|---|---|---|---|---|---|---|
| 11:30–11:40 | — | Pausa | Muestra en pantalla el enlace a la guía y `datos\` | Prepara la pantalla | Forma grupos presenciales | Publica enlaces, forma grupos remotos |
| **11:40–11:42** | 0–2 | **A.1** Kickoff (1 min: objetivo, grupos, cómo pedir ayuda) y verificar herramientas | Terminal: `az --version`, `python --version`, `git --version`, `code --version` | Narra | Recorre la sala | Pide ✔ "A1" |
| 11:42–11:46 | 2–6 | **A.2** Inicio de sesión con TAP | `az login --use-device-code --tenant ...`, `https://login.microsoft.com/device`, **Use a Temporary Access Pass instead** | Narra (sin mostrar el TAP) | Ayuda con AADSTS50079/50076 y con TAP rechazados | Anota bloqueos de acceso |
| 11:46–11:49 | 6–9 | **A.3** Entorno personal | `az group show`, `az cognitiveservices account list`, lista de deployments | Narra | Ayuda | Recoge ✔ "A2" |
| 11:49–11:52 | 9–12 | **A.4** Foundry Toolkit for VS Code | Extensions > Foundry Toolkit for VS Code, iniciar sesión | Narra | Ayuda | — |
| 11:52–11:54 | 12–14 | **A.5** Portal y proyecto | `https://ai.azure.com`, **New Foundry**, proyecto `lab-NN` | Narra | Ayuda | — |
| 11:54–11:55 | 14–15 | **A.6** Descargar `datos\` y definir roles | `datos\prompts.md` | Narra | Verifica pareja/trío y cuenta compartida | Recoge ✔ "A3" |
| **11:55–11:59** | 0–4 | **B.1** Modelo `gpt-5.6-luna` | Lista de modelos del proyecto, playground, "Hola, ¿qué puedes hacer?" | Soporte | Narra | Recoge ✔ "B1" |
| 11:59–12:02 | 4–7 | **B.2** Instrucciones | Pegar `prompts.md` 1.1 | Soporte | Narra | — |
| 12:02–12:04 | 7–9 | **B.3** Guardar agente | **Save as agent** | Soporte | Narra (si no aparece, **Build > Agents**) | — |
| 12:04–12:09 | 9–14 | **B.4** File search | **Tools > Add > File search > Upload files > Attach**, esperar indexación | Revisa 403 y archivos | Narra y muestra el estado de indexación | Recoge ✔ "B2" |
| 12:09–12:16 | 14–21 | **B.5** Pruebas | Preguntas 1, 3, 6 y 7 de `prompts.md`, **de a una** por la cuota | Ayuda; vigila `429` | Narra la 6 (no inventa) y la 7 (rechaza) | Recoge ✔ "B3" |
| 12:16–12:20 | 21–25 | **B.6** Versión y Día 2 | Cambio pequeño, **Save**, nueva versión, **Build > Agents** | Soporte | Narra | Recuerda la sección 9 de la guía |
| **12:20–12:24** | 0–4 | **C.1** Studio | Abrir Document Intelligence Studio, **Settings > Resource** | Narra | Revisa permisos/cookies | Recoge ✔ "C1" |
| 12:24–12:29 | 4–9 | **C.2** Invoice | Tile **Invoices**, `01-factura.png`, **Analyze options**, **Run analysis** | Narra | Soporte | — |
| 12:29–12:33 | 9–13 | **C.3** Validar campos | `campos-esperados.md`; confianza y aritmética | Narra | Soporte | Recoge ✔ "C2" |
| 12:33–12:38 | 13–18 | **C.4** Layout y formulario | Modelo **Layout**, `02-solicitud-credito.png`, pares clave-valor | Narra | Soporte | — |
| 12:38–12:44 | 18–24 | **C.5** Comparar con modelo/agente | Playground de `gpt-5.6-luna`, `prompts.md` 3.1, pegar solo campos principales | Soporte; vigila `429` | Narra la idea clave: extraer vs. razonar | Comparte JSON de respaldo |
| 12:44–12:45 | 24–25 | **C.6** Guardar | `resultado-factura.json` o captura | — | — | — |
| 12:45–13:00 | — | Preguntas y cierre (fuera del lab) | Sección 9 | | | |

**Cortes duros:**

- **11:55:** pasa a B aunque haya grupos atrasados. Que usen "Si vas atrasado en el Bloque A" (lo mínimo: `az login` con TAP y el portal) y retomen en la pausa o en casa; B y C se hacen en el portal.
- **12:20:** pasa a C aunque haya grupos en B.5. El JSON de respaldo cubre el entregable.
- **12:45:** cierra el lab; las preguntas continúan hasta las 13:00.

**Puntos de decisión:**

| Hora | Si ocurre | Haz esto |
|---|---|---|
| 11:46 | Más de un tercio de los grupos no puede iniciar sesión con el TAP | F1 repite el flujo en pantalla (**Use a Temporary Access Pass instead**); F2 y el monitor verifican TAP vigente y escalan a los organizadores. Los que no logran ingresar trabajan con la cuenta de su pareja o trío |
| 11:52 | Más de un tercio no tiene `az`, `python` 3.13, `git` o `code` | Se emparejan con quien sí los tiene; B y C se hacen solo en el portal. Resolver después de la sesión, antes del Día 2 |
| 12:02 | Errores `429` o `gpt-5.6-luna` no responde para varios grupos | Cambiar el modelo del agente a `gpt-5-mini` y continuar |
| 12:09 | Más de un tercio no terminó B.4 (indexación, 403 o file search con `gpt-5.6-luna`) | Probar con `gpt-5-mini`; si persiste, F2 muestra B.4 y B.5 en modo demo y los demás repiten cuando puedan |
| 12:20 | Document Intelligence no abre para la mayoría | F1 conduce **C en modo demostración** con su propia pantalla; los grupos observan y validan contra `campos-esperados.md` (usa también el Plan B de la demo) |

## 5. Qué verificar por bloque (checkpoints en vivo)

| Bloque / minuto | Señal verde | Quién comprueba | Si no se cumple |
|---|---|---|---|
| A1 (min 2) | `az`, `python` (3.13.x), `git` y `code` responden | F2 en la sala y monitor en el chat | Bloqueos 17 y 18 de la sección 6 |
| A2 (min 9) | `az account show` muestra su cuenta `labNN`; ve su grupo de recursos y los modelos | F2 | Bloqueos 19 a 21 de la sección 6 |
| A3 (min 15) | Foundry Toolkit con sesión, proyecto `lab-NN` visible en `https://ai.azure.com` con **New Foundry**, `datos\` descargada | F2 / monitor | Bloqueos 1, 2 y 20 de la sección 6 |
| B1 (min 4) | `gpt-5.6-luna` responde "Hola" en el playground | F2 | Bloqueos 3 y 9 (usar `gpt-5-mini`) |
| B2 (min 14) | Agente guardado con **File search** y 4 archivos indexados | F1 / monitor | Esperar indexación; revisar roles (bloqueos 5 y 6) |
| B3 (min 21) | 2–3 preguntas como mínimo, una con cita y un rechazo o "no encuentro" | F2 al azar pide a un grupo que lo muestre | Revisar instrucciones guardadas, línea 1.3 de `prompts.md` y bloqueo 7 |
| Entregable B | Agente en **Build > Agents** con versión guardada | Monitor (lista) | Guardar de nuevo |
| C1 (min 4) | Studio abierto con un recurso seleccionado | F2 / monitor | Cookies, recurso, rol (bloqueos 10 a 12 de la sección 6) |
| C2 (min 13) | Factura analizada + 1 observación anotada | F2 | Usar captura/JSON de respaldo |
| Entregable C | `resultado-factura.json` o captura + comparación completada | Monitor | JSON de respaldo |

Valores que debes tener a mano para validar C (de `datos\documentos-ocr\campos-esperados.md`): factura **F-000458**, proveedor *Suministros Pacífico SpA*, total **$1.190.000** (neto $1.000.000 + IVA $190.000), fecha de emisión **05-10-2026**.

## 6. Bloqueos típicos y soluciones rápidas

| # | Síntoma | Causa probable | Solución rápida |
|---|---|---|---|
| 1 | No ven la interfaz del laboratorio o falta algún menú | Interfaz clásica en lugar de **New Foundry** | Activar el interruptor **New Foundry** en la barra superior |
| 2 | Error de permisos al abrir el proyecto o crear el agente | Falta el rol **Foundry User**, o sesión con otra cuenta | Confirmar con `az account show` que usa su cuenta `labNN`; escalar al equipo de entorno para el rol. No pierdas más de 2 minutos |
| 3 | `gpt-5.6-luna` no aparece en el proyecto o no responde | Proyecto equivocado, deployment pendiente o falla del modelo | Usar `gpt-5-mini` (también predesplegado) y avisar al equipo de entorno |
| 4 | No existe **Save as agent** | Diferencias de interfaz | **Build > Agents > Create agent** y pegar instrucciones (README B.3) |
| 5 | 403/"no autorizado" al subir archivos a file search | Falta **Storage Blob Data Contributor** sobre el almacenamiento del proyecto, o **Foundry User** (el aprovisionamiento actual solo asigna Foundry User + Reader: **por confirmar**) | Escalar al equipo de entorno. Mientras tanto el grupo mira el agente de otro grupo en modo demo. No repetir el intento muchas veces |
| 6 | La indexación de file search no termina | Archivos grandes, sistema ocupado | Subir solo 2 documentos (gastos de viaje y reclamos). Si pasan >5 min, escalar |
| 7 | El agente no cita ni usa los documentos | File search no adjunto, indexación incompleta, o el modelo no llamó a la herramienta (`gpt-5.6-luna` + file search **no está validado**) | Revisar **Tools**, esperar, agregar la línea de `prompts.md` 1.3 y **Save**; probar en un chat nuevo; si persiste, cambiar el modelo del agente a `gpt-5-mini` |
| 8 | Respuesta inventada ante la pregunta 6 (vacaciones) | Instrucciones sin guardar o modelo más pequeño | **Save**, chat nuevo, reforzar la regla 3. Es un buen momento didáctico: "así se ve una alucinación" |
| 9 | Errores 429 o "rate limit" | Cuota de `gpt-5.6-luna` de ≈4K TPM por cuenta: dos mensajes de ≈3K tokens de entrada seguidos la superan (ocurre de verdad) | Pedir esperar unos 10 s y reintentar con mensajes más cortos; una sola persona por cuenta pregunta a la vez; si persiste (hasta 1 min), cambiar a `gpt-5-mini` (10K TPM) |
| 10 | Error **AADSTS50058** al abrir Studio | Cookies de terceros bloqueadas | Permitir cookies de terceros para Document Intelligence Studio o abrir otra ventana de navegación |
| 11 | `PermissionDenied`/403 al analizar en Studio | Falta **Cognitive Services User** en el recurso (Contributor no basta si la clave local está deshabilitada) | Escalar al equipo de entorno; usar JSON/captura de respaldo |
| 12 | Studio no muestra recursos | No hay recurso seleccionado | **Settings > Resource** y elegir el indicado; autenticación **Microsoft Entra ID** |
| 13 | El archivo no se acepta | Límites del nivel F0: 4 MB y 2 páginas | Los archivos de `datos\` cumplen ambos; confirmar que subieron el correcto |
| 14 | Montos en pesos con símbolo/formato distinto o sin moneda | Normalización de la API; CLP puede no figurar entre las monedas listadas | Úsalo como conversación: tipo de dato vs. texto impreso (README C.3 punto 5) |
| 15 | Faltan campos opcionales (por ejemplo, `PaymentTerm`) | Campo opcional | Resultado válido; revisar manualmente |
| 16 | No hay pares clave-valor en Layout | Opción desactivada | **Analyze options** y activar la detección de pares clave-valor (el nombre puede variar) |
| 17 | `az`, `code`, `git` o `python` no se reconocen | Instalación hecha con la terminal abierta o incompleta | Cerrar y abrir la terminal; si persiste, instalar con `winget install -e --id Microsoft.AzureCLI` (o `Microsoft.VisualStudioCode`, `Python.Python.3.13`, `Git.Git`) |
| 18 | `python --version` muestra 3.14 u otra versión | Python 3.14 todavía no está soportado (lab probado con 3.13.12) | Instalar Python 3.13 (`winget install -e --id Python.Python.3.13`) y abrir una terminal nueva |
| 19 | **AADSTS50079** o **AADSTS50076** al iniciar sesión | No usan el TAP; en este tenant no pueden registrar MFA | Elegir **Use a Temporary Access Pass instead** e ingresar el TAP. No intentar registrar MFA |
| 20 | El TAP no es aceptado, está vencido o "todavía no es válido" | El TAP solo vale el 21 de octubre de 06:30 a 14:30 (hora de Chile); los de los días 2 y 3 se regeneran cada noche | Escalar al facilitador/organizadores para reemitirlo (persona de contacto: **por confirmar**). Mientras tanto, trabaja con la cuenta de la pareja o trío |
| 21 | `az account list` no muestra ninguna suscripción | El inicio de sesión no ve una suscripción | Repetir `az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc --allow-no-subscriptions` y avisar a un facilitador |
| 22 | Colisión de nombres de agente en un proyecto compartido | Mismo nombre en varios grupos | Usar el sufijo por grupo (`-g01`, `-g02`…) |

## 7. Plan B — qué preparar y cuándo activarlo

### 7.1 Cuándo activarlo

- **Demo en vivo de Document Intelligence:** si Studio no carga, da 403, el TAP falla o el análisis se demora demasiado, pasa a las capturas y al JSON del ensayo (ver `demo-document-intelligence.md`, sección 7).
- **Lab completo (A, B y C):** si más de la mitad de los grupos sigue bloqueada pasados 10 minutos desde el inicio de un bloque, un facilitador conduce el bloque en pantalla compartida y los grupos lo replican cuando puedan.
- **Bloque A (acceso):** si el TAP falla para muchos, los grupos trabajan con una cuenta que sí funcione (la de un integrante); B y C se hacen solo en el portal.
- **`gpt-5.6-luna` con problemas** (`429` persistente o no usa file search): cambiar el modelo del agente a `gpt-5-mini`.

### 7.2 Qué grabar y capturar (hoy, durante el checklist de validación)

| # | Archivo sugerido | Qué muestra | Quién |
|---|---|---|---|
| 1 | `a-01-az-login-tap.png` | Flujo `az login --use-device-code` con la pantalla de **Use a Temporary Access Pass instead** (sin TAP ni cuenta visibles) | F1 |
| 2 | `a-02-verificacion-entorno.png` | `az account show`, `az group show` y la lista de deployments (`gpt-5.6-luna`, `gpt-5-mini`, `text-embedding-3-small`) | F1 |
| 3 | `a-03-foundry-toolkit.png` | Foundry Toolkit for VS Code con sesión iniciada | F1 |
| 4 | `b-01-new-foundry.png` | Barra superior con **New Foundry** activado y el proyecto `lab-NN` | F1 |
| 5 | `b-02-modelo-luna.png` | Lista de modelos del proyecto y playground de `gpt-5.6-luna` respondiendo | F1 |
| 6 | `b-03-instrucciones.png` | Playground con las instrucciones pegadas | F1 |
| 7 | `b-04-save-as-agent.png` | **Save as agent** y nombre del agente | F1 |
| 8 | `b-05-file-search.png` | **Tools > File search** con los 4 archivos indexados | F1 |
| 9 | `b-06-pregunta-1-cita.png` | Respuesta con cita (pregunta 1) | F1 |
| 10 | `b-07-pregunta-6-no-sabe.png` | Respuesta de "no encuentro" (pregunta 6) | F1 |
| 11 | `b-08-pregunta-7-rechazo.png` | Rechazo ante la inyección de prompt (pregunta 7) | F1 |
| 12 | `b-09-versiones.png` | Selector de versiones tras guardar un cambio | F1 |
| 13 | `b-10-error-429.png` | Error `429` real de `gpt-5.6-luna` y la misma consulta con `gpt-5-mini` | F1 |
| 14 | `b-video-completo.mp4` | Flujo completo de B en 3–4 min | F1 |
| 15 | `c-01-studio-invoice.png` | Tile **Invoices** con la factura cargada | F2 |
| 16 | `c-02-campos-factura.png` | Campos extraídos con su confianza | F2 |
| 17 | `c-03-layout-kv.png` | **Layout** con pares clave-valor de la solicitud | F2 |
| 18 | `resultado-factura.json` | JSON **real** de la factura (para C.5 de rezagados) | F2 |
| 19 | `c-04-comparacion.png` | Respuesta del modelo con el JSON pegado (`prompts.md` 3.1) | F2 |
| 20 | Archivos de la demo (PB-D1-01) | Capturas y JSON de **Receipt** y **Layout** sobre `03-comprobante-compra.pdf` (ver `demo-document-intelligence.md`, sección 7) | F2 |

Reglas: solo datos ficticios; sin claves, TAP ni endpoints reales visibles (tapa el endpoint o usa `<TU-ENDPOINT>`); no los subas a un sitio público.

### 7.3 Qué decir al activar el plan B

> "Esta parte depende de configuraciones del entorno que hoy no están disponibles para todos; les muestro cómo se ve y lo repiten después con su proyecto. Lo importante es entender el patrón."

## 8. Niveles mixtos: apoyo y extensiones

### 8.1 Formación de grupos y dinámica

- **Trío ideal:** una persona con experiencia en cloud/IA, una de datos/negocio y una de riesgo/seguridad o principiante.
- Roles rotativos: **maneja el teclado** (driver) cambia entre bloques A → B → C; las otras dos leen la guía y verifican los checkpoints (navigator). En el Bloque A cada persona verifica su propio equipo; desde el B comparten una sola cuenta y un solo agente.
- En Teams, los grupos remotos se organizan por orden de la lista; quien comparte pantalla es el driver. Si tienes salas de grupo (breakout rooms) disponibles, úsalas para que cada trío converse sin ruido; el chat principal queda para pedir ayuda.
- Pide que cada persona **al menos una vez** use el teclado.

### 8.2 Apoyo a principiantes

- Mostrar el glosario mínimo en la primera diapositiva o en el chat: **modelo** (cerebro), **instrucciones** (reglas del agente), **tool** (capacidad extra), **file search** (buscar en documentos), **playground** (zona de pruebas), **versión** (foto de la configuración), **OCR** (leer texto de una imagen), **modelo prebuilt** (modelo ya entrenado para un tipo de documento), **TAP** (código temporal para iniciar sesión sin registrar MFA).
- Usar la versión corta de instrucciones (`prompts.md` 1.2) y solo 2 documentos si van atrasados.
- Mostrar en pantalla el mismo paso mientras lo describes; no avances hasta ver ✔ en el chat de al menos la mitad.
- Evitar jerga innecesaria: di "pega este texto" en lugar de "inyecta el prompt".

### 8.3 Extensiones para quienes terminan antes

| Nivel | Extensión | Bloque |
|---|---|---|
| Fácil | Leer `datos\README.md` y `prompts.md` (secciones 1 a 3) | A |
| Fácil | Clonar `https://github.com/MicrosoftLearning/mslearn-ai-agents.git` para comprobar que Git funciona (no es necesario hoy) | A |
| Fácil | Revisar la pestaña **YAML** y leer `kind: prompt` y las instrucciones | B |
| Fácil | Probar las preguntas 2, 4, 5 y 8 de `prompts.md` | B |
| Intermedio | Cambiar el modelo del agente a `gpt-5-mini`, guardar y comparar la misma pregunta (calidad, velocidad, cita) | B |
| Intermedio | Escribir 3 preguntas adversariales propias y ver cómo responde | B |
| Intermedio | Abrir **Guardrails** y revisar controles de contenido (guardrails de agentes: **(preview)**; no cambiar el proyecto compartido) | B |
| Avanzado | Reescribir las instrucciones para otra área (por ejemplo, onboarding) y probar con las preguntas 4 y 5 | B |
| Fácil | Analizar `03-comprobante-compra.png` con **Receipt** (el mismo documento de la demo) | C |
| Intermedio | Comparar `01-factura.png` (escaneada) con `pdf-texto-nativo\01-factura.pdf` | C |
| Intermedio | `prompts.md` 3.2 (solo texto) y 3.3 (imagen, si el modelo admite imágenes) | C |
| Avanzado | Revisar el código de `Labfiles\03-document-intelligence\prebuilt` del laboratorio oficial `mslearn-ai-information-extraction` (no hace falta ejecutarlo) | C |

### 8.4 Plantillas de mensajes para el chat de Teams (monitor)

- **Inicio:** "¡Bienvenidos al laboratorio! Guía y datos aquí: <ENLACE>. Ten a mano tu cuenta `labNN` y tu TAP. Si te atascas más de 3 minutos, escribe 'Ayuda Bloque A/B/C' (A = entorno, B = agente, C = OCR) y tu grupo."
- **A1 (min 2):** "Confirma con ✔ si `az`, `python` (3.13), `git` y `code` responden en tu terminal."
- **A2 (min 9):** "Confirma con ✔ si `az account show` muestra tu cuenta `labNN` y ves tus modelos. Si ves AADSTS50079 o AADSTS50076, elige 'Use a Temporary Access Pass instead'."
- **A3 (min 15):** "Confirma con ✔ si ves tu proyecto `lab-NN` en ai.azure.com con New Foundry activo."
- **B1 (min 4):** "Confirma con ✔ si `gpt-5.6-luna` responde 'Hola'. Si ves un 429, espera unos 10 segundos; si persiste, usa `gpt-5-mini`."
- **B2 (min 14):** "Confirma con ✔ cuando tu agente tenga file search con los 4 archivos indexados."
- **B3 (min 21):** "¿Probaste 2–3 preguntas? Escribe qué pasó con la pregunta de vacaciones (¿inventó o dijo que no lo sabe?). Recuerda: una pregunta a la vez por cuenta."
- **C1 (min 4):** "Confirma con ✔ si Studio abre con tu recurso."
- **C2 (min 13):** "Escribe un campo que salió correcto y uno dudoso."
- **Atrasados:** "Si vas atrasado, usa la sección 'Si vas atrasado' del bloque; mañana retomamos."
- **Cierre:** "Guarda el nombre de tu agente, tu proyecto y la versión. No elimines nada: mañana lo reutilizamos. Mañana recibirás un TAP nuevo."

## 9. Cierre del laboratorio y puente al Día 2 (12:45–13:00)

Distribución sugerida de los 15 min: ≈5 min para el recordatorio de qué guardar y el puente al Día 2, y ≈10 min para preguntas.

- 12:45: recordar la sección 9 de la guía ("qué guardar para el Día 2"): nombre del agente y proyecto, versión, `<TU-ENDPOINT>`, instrucciones, preguntas de prueba y `resultado-factura.json`.
- Recalcar: **no eliminar** proyectos ni agentes. El entorno local (VS Code, Python 3.13, Git, Azure CLI) quedó verificado en el Bloque A y es el prerrequisito del laboratorio pro-code del Día 2; mañana se entrega un **TAP nuevo**.
- Pregunta para pensar: "¿Qué datos o sistemas del banco querrías que un agente pudiera consultar? ¿Qué nunca debería hacer?"
- Registrar en la retrospectiva: qué bloque fue más difícil, qué errores hubo (TAP, `429`, `gpt-5.6-luna` + file search), qué cambiar en la guía.

### Preguntas esperables y cómo responder

| Pregunta | Respuesta sugerida |
|---|---|
| "¿Esto está listo para producción?" | El núcleo de agentes está disponible de forma general (GA); guardrails de agentes y memoria están en **(preview)** según la documentación. Hoy es un laboratorio de aprendizaje. Verifica el estado vigente en la página de estado de funcionalidades antes de comprometer algo |
| "¿Dónde quedan mis documentos?" | En el servicio de file search del proyecto (configuración básica: almacenamiento y búsqueda administrados por Microsoft). No subas datos reales hoy. Para el detalle de residencia y cumplimiento, toma la pregunta y responde con documentación oficial |
| "¿Cuánto cuesta?" | Depende de modelo, tokens y herramientas. No des cifras; enviar el enlace de precios después |
| "¿Cuándo uso Document Intelligence y cuándo un modelo?" | Document Intelligence para extraer campos de forma repetible con ubicación y confianza; el modelo/agente para razonar y decidir. En producción se combinan |
| "¿Por qué me dio un error 429?" | La cuota de `gpt-5.6-luna` en cada cuenta del laboratorio es baja (≈4K TPM) para que alcance para todos; no es representativa de producción. Espera unos segundos, usa mensajes cortos o cambia a `gpt-5-mini` |
| "¿Por qué iniciamos sesión con un TAP?" | Las cuentas del taller están protegidas con MFA y en este tenant no se pueden registrar métodos; el TAP es un código temporal que entregan los organizadores y solo vale por una ventana limitada |
| "¿Puedo usar mis propios modelos?" | El catálogo ofrece distintos modelos; la disponibilidad depende de región y cuota. Revisa el catálogo de tu proyecto y consulta la documentación para opciones de modelos propios |

## 10. Documentos relacionados

- `README.md` — guía del participante (con éxito por bloque y fuentes oficiales).
- `demo-document-intelligence.md` — guion de la demo en vivo de Document Intelligence (≈10 min, módulo Azure AI Services).
- `datos\prompts.md` — instrucciones del agente, preguntas de prueba y prompts de comparación.
- `datos\documentos-ocr\campos-esperados.md` — valores esperados de los documentos.
- `checklist-validacion.md` — prueba de humo para el entorno real.
- `..\entorno-y-facilitacion\runbook-facilitacion-3-dias.md`, `plan-b-demos.md` y `onboarding-participantes.md` — runbook, plan B y correo de pre-trabajo.

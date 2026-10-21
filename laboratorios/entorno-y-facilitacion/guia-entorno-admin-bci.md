# Guía de entorno de laboratorio para el administrador Azure de BCI

**Evento:** Microsoft AI Foundry BCI Training Day · 21, 22 y 23 de octubre de 2026 · 09:00–13:00 (hora de Chile) · Microsoft Chile (Las Condes) + Teams
**Versión:** 1.2 (borrador para revisión; alineada con los kits de laboratorio de los días 1 a 3 y con el entorno aprovisionado; ver recuadro «Actualización 20-oct») · **Fecha:** 20-oct-2026 (T-1 día) · **Responsables Microsoft:** Pablo Braconi, Valentina Grajales · **Organizador:** Robert Escalante · **Contacto BCI:** Diego Bell Tineo

> **Actualización 20-oct (v1.2): estado real del entorno. Prevalece sobre cualquier pasaje de este documento que lo contradiga.** Esta guía se escribió para la propuesta original (1 recurso Foundry + ≈54 proyectos `lab-pXX`, cuentas corporativas de BCI, `gpt-5-mini` con ≥ 600 K TPM, demo de voz/avatar y límite de ≈16 sesiones). Las secciones 3, 6, 10, 11, 12 y 14 conservan ese diseño como **propuesta original** y no se reescribieron por completo. El entorno que se aprovisiona con los scripts de `provisionamiento\` es:
> - **Tenant y región:** tenant del evento `mngenvmcap219366.onmicrosoft.com` (id `eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc`), región East US 2. Quién administra el tenant: *por confirmar*. El límite de ≈16 sesiones de un entorno compartido de Microsoft no aplica.
> - **Cuentas y acceso:** `labNN@mngenvmcap219366.onmicrosoft.com` (NN = 01–58) para participantes e `instNN` para instructores, protegidas con MFA. Los participantes **no pueden registrar MFA**: inician sesión (portal, `az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc`, Foundry Toolkit) con un **Temporary Access Pass (TAP)** entregado por los organizadores. El TAP del Día 1 es válido solo el miércoles 21 de 06:30 a 14:30 (hora de Chile); los de los días 2 y 3 se regeneran cada noche. AADSTS50079/50076 significa «no estás usando el TAP».
> - **Topología real:** un grupo de recursos `rg-bci-lab-NN` por participante (instructores: `rg-bci-inst-NN`) con **una cuenta Foundry y un proyecto `lab-NN`**; recursos compartidos (Azure AI Search Basic, Log Analytics, Application Insights) en `rg-bci-lab-compartido`. Roles asignados: **Foundry User** y **Reader** en el RG y **Cognitive Services User** sobre la cuenta Foundry de cada usuario. El aprovisionamiento no asigna *Storage Blob Data Contributor*; ver 6.1 (*por confirmar* si hace falta).
> - **Modelos predesplegados en cada cuenta** (nombre del despliegue = nombre del modelo): `gpt-5.6-luna` (**modelo principal del Día 1**; 4K TPM por cuenta), `gpt-5-mini` (respaldo; 10K TPM) y `text-embedding-3-small` (10K TPM). `gpt-5.6-luna` se despliega con `provisionamiento\Add-Modelo.ps1` (versión 2026-07-09, capacidad 4; idempotente) y también está en `participante.bicep`. **Cuota total usada de `gpt-5.6-luna`: 62 cuentas × 4K = 248K TPM**, repartida en GlobalStandard (37 cuentas: inst01–04 y lab01–lab33, 148K de 150K disponibles) y DataZoneStandard (25 cuentas: lab34–lab58, 100K). La cuota efectiva de `gpt-5-mini` y de embeddings en la suscripción: *verificar*.
> - **Estado de las pruebas:** `gpt-5.6-luna` responde con Chat Completions y con la Responses API en eastus2. Con ≈3K tokens de entrada dos veces seguidas se supera la cuota de 4K TPM y devuelve `429`: **los `429` son reales** en el laboratorio. **Aún no se probó `gpt-5.6-luna` con Foundry Agent Service + file search desde una cuenta de participante**; el respaldo es `gpt-5-mini`.
> - **Plan del Día 1 (hora de Chile):** 09:00–09:30 Presentación de apertura · 09:30–09:45 Contexto y fundamentos · 09:45–10:15 Plataforma Foundry · 10:15–10:55 Azure AI Services (con demo en vivo de Document Intelligence ≈10:40–10:50) · 10:55–11:30 Agentes y conocimiento · 11:30–11:40 Pausa · **11:40–12:45 Laboratorio guiado (65 min): Bloque A entorno y prerrequisitos (≈15 min), Bloque B primer agente (≈25 min), Bloque C OCR con Document Intelligence (≈25 min)** · 12:45–13:00 Preguntas y cierre. La demo de voz/avatar **se eliminó**: no hay requisitos de Speech, Voice Live ni `gpt-realtime` para el laboratorio.
> - **Parejas y tríos comparten un solo agente** para respetar los 4K TPM de `gpt-5.6-luna`.
> - **Pendiente (*por confirmar*):** qué recurso de Document Intelligence usa cada cuenta `labNN` en Studio (el Bicep no crea uno por separado), y quién reemite TAP durante el taller.

> **Cómo leer este documento.** Todo lo que tiene respaldo en la documentación oficial indica su archivo en la sección *Fuentes* (rutas relativas a `BCI-Foundry-Workshop\`). Donde la documentación no entrega un número o un dato, aparece **«verificar»** y debe confirmarse en la suscripción o en el portal antes del Go/No-Go. Las cifras de capacidad de la sección 5 son **estimaciones de planificación**, no mediciones. No se incluyen precios.

---

## 1. Resumen ejecutivo

| Tema | Recomendación | Estado |
|---|---|---|
| Quién provisiona | **Entorno ya aprovisionado en el tenant del evento** (`mngenvmcap219366…`; quién lo administra: *por confirmar*). El límite de ≈16 sesiones de un entorno compartido de Microsoft no aplica | **Confirmar con BCI hoy** |
| Topología | **Real:** un grupo de recursos `rg-bci-lab-NN` por participante con su cuenta Foundry y su proyecto `lab-NN` (58 cuentas `lab` + instructores `instNN`). *Propuesta original (secciones 3 y siguientes): 1 recurso Foundry + ≈54 proyectos* | Aprovisionado (ver recuadro de actualización) |
| Región | **East US 2** (único punto que reúne chat, embeddings, agentes y los modelos del evento según la documentación) | Verificar cuota en la suscripción |
| Modelos | **`gpt-5.6-luna`** como modelo principal del Día 1 (predesplegado; 4K TPM por cuenta); respaldo **`gpt-5-mini`** (10K TPM); `text-embedding-3-small` para embeddings (Día 2). *Propuesta original: `gpt-5-mini` principal con respaldo `gpt-4.1-mini` y `gpt-realtime` opcional* | `gpt-5.6-luna` + Agent Service + file search **no probado**; verificar herramientas por modelo (5.2) |
| Alineación con los labs | Variables, nombres de despliegue y roles que espera cada lab (sección 18) | Revisar con los autores de los labs |
| Red | **Endpoint público + autenticación Entra ID + RBAC** (sin red privada) | Confirmar política de BCI |
| Identidad | Real: cuentas `labNN`/`instNN` con **TAP** (MFA) y grupos Entra `grp-bci-lab-participantes` y `grp-bci-lab-instructores`. *Propuesta original: `grp-bci-foundry-participantes` y `grp-bci-foundry-instructores`* | Aprovisionado |
| Datos | **Solo datos ficticios** | Regla fija |
| Limpieza | Etiqueta `eliminar-despues-de` + borrado del grupo de recursos + purga de cuentas eliminadas | Programar |

**Lo que necesitamos de BCI (ver sección 16):** suscripción y región, rol del administrador, creación de los dos grupos Entra, excepciones de acceso condicional para el evento, lista de salida (egress) a internet, decisión sobre red privada, idioma del lab pro-code (Python por defecto) y acceso a GitHub/Codespaces.

---

## 2. Objetivo y alcance

El entorno debe permitir que ~48 personas (21 presenciales, 27 por Teams) realicen los laboratorios de los días 1 y 2. El día 3 (arquitectura) **no usa laboratorio en la nube**.

| Día | Nivel | Bloque de laboratorio | Qué exige al entorno |
|---|---|---|---|
| **1** | L100 | A (≈15 min): preparación del entorno y prerrequisitos (VS Code, suscripción Azure activa, Python 3.13, Git, Foundry Toolkit for VS Code, Azure CLI y `az login`; inicio de sesión con TAP) | Cuenta `labNN` con TAP vigente, cuenta Foundry + proyecto `lab-NN`, equipos con las herramientas instaladas |
| | | B (≈25 min): primer agente de prompt en el portal Foundry con `gpt-5.6-luna` + herramienta de búsqueda de archivos | Proyecto Foundry por pareja/persona, modelos predesplegados (`gpt-5.6-luna`, respaldo `gpt-5-mini`), rol *Foundry User*, documentos ficticios para búsqueda de archivos |
| | | C (≈25 min): Document Intelligence (OCR, modelos *prebuilt* Invoices y Layout). Además, **demo en vivo de los facilitadores** (Receipt, ≈10 min, dentro del módulo Azure AI Services) | Acceso a Document Intelligence Studio con Entra ID, documentos ficticios; recurso y rol por confirmar |
| **2** | L200 | Agente Python (Agent Framework) con grounding en Azure AI Search + herramienta personalizada + trazas | Endpoint de proyecto, despliegue de chat y de embeddings, índice de AI Search pre-creado, App Insights conectado, rol de lectura de trazas, Python 3.13 (el lab del Día 2 acepta 3.10+; 3.14 aún no está soportado) |
| **3** | L300 | Taller de decisiones de arquitectura | Nada de nube. Solo Teams y presentaciones |

Fuentes: `presentaciones\content\day1.json`, `day2.json`; `MATERIALS_INDEX.md` §4.

**Diferencias a resolver con los autores de los labs** (detectadas al leer los repositorios):

1. El slide del día 1 dice *file search*; el laboratorio oficial `mslearn-agent-quickstart` usa `gpt-5-mini` con **web_search**. **Resuelto en el kit del Día 1** (`laboratorios\dia1-lab-guiado\README.md`): usa **File Search** con documentos ficticios y, como modelo principal, `gpt-5.6-luna` (respaldo `gpt-5-mini`, para el que la matriz de herramientas indica File Search = Sí; `agents\concepts\limits-quotas-regions.md`). **`gpt-5.6-luna` con Agent Service + file search no se ha probado** y falta confirmar la carga de archivos con una cuenta de participante (rol de almacenamiento, sección 6.1).
2. `mslearn-agent-quickstart` pide Python 3.13+, el taller de agentes hospedados Python 3.10+ y el lab del Día 2 acepta **3.10+** (recomendado 3.12 o 3.13; probado con 3.13). Para el Día 1 el pre-trabajo exige **Python 3.13** (probado con 3.13.12; **3.14 aún no es compatible**), siguiendo los prerrequisitos del ejercicio público de Microsoft Learn (`https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/02-agent-custom-tools.html#prerequisites`).
3. El ejercicio de Document Intelligence de Learn usa **clave API** y plan F0 «si está disponible»; el lab del Día 1 usa el Studio con **Microsoft Entra ID** (rol *Cognitive Services User*, sin claves). Con muchas personas no se debe usar F0 (ver sección 8).

---

## 3. Arquitectura recomendada

> **Propuesta original.** Esta sección (3.1 a 3.5) describe la arquitectura propuesta antes de aprovisionar: 1 recurso Foundry con ≈54 proyectos `lab-pXX` y ≈16 grupos de tríos por el límite de sesiones. **El entorno real es distinto** (una cuenta Foundry + un proyecto `lab-NN` por participante, en `rg-bci-lab-NN`; ver el recuadro «Actualización 20-oct» al inicio). Se conserva como referencia de la comparación de opciones y de los límites de la plataforma.

### 3.1 Comparación de opciones

| Opción | Ventajas | Riesgos | Veredicto para 48 personas |
|---|---|---|---|
| **A. 1 recurso Foundry + 1 proyecto compartido** | Mínimo de configuración | Agentes, archivos y vector stores de 48 personas en el mismo espacio; colisiones de nombres; nadie sabe qué es suyo | No recomendado |
| **B. 1 recurso Foundry + N proyectos (1 por persona/pareja)** | Los despliegues de modelos y la red se comparten; cada proyecto aísla agentes, archivos e índices; una sola asignación de rol por grupo; costo y operación simples | Cuota compartida por todos (*blast radius* de agotamiento de cuota); el aislamiento entre proyectos es por convención si el rol se asigna al recurso | **Recomendada** |
| **C. 48 recursos Foundry (uno por persona)** | Aislamiento total y cuota separada por recurso | Límite de 100 recursos Foundry por región/suscripción; 48 despliegues de modelo × cuota; 48 conexiones a Search/App Insights; imposible de preparar en 24 h | No recomendado |

**Justificación (documentación):**

- Para entornos de exploración la guía de planificación recomienda **colocar cargas de trabajo en un recurso con varios proyectos**, aceptando como contrapartida el riesgo de agotar cuota compartida (`docs-oficiales\foundry\concepts\planning.md`). El aislamiento total por recurso se reserva a producción.
- Los proyectos comparten red, despliegues e integraciones del recurso padre y admiten control de acceso propio; los proyectos distintos del predeterminado soportan agentes, evaluaciones, trazas, índices, conexiones y playgrounds (`how-to\create-projects.md`). En proyectos no predeterminados, la API OpenAI expone **Responses, Files y Conversations**; *Batch*, *fine-tuning* y *stored completions* solo existen en el proyecto predeterminado (no se usan en este evento).
- Límites: 100 recursos Foundry por región/suscripción, **250 proyectos máx. por recurso** y **32 despliegues máx. por recurso** (`foundry-models\quotas-limits.md`). Con ≈54 proyectos y ≈5 despliegues hay holgura amplia.
- Los agentes, respuestas, evaluaciones, datasets, índices y archivos admiten aislamiento de RBAC por proyecto; **Speech, Language y Content Understanding no** (requieren rol en el recurso) (`concepts\planning.md`). Por eso Document Intelligence y Speech se tratan como recursos propios con rol de recurso (secciones 6 y 8).

### 3.2 Diagrama lógico

```
Suscripción BCI (etiqueta: evento=bci-foundry-training-2026-10)
└─ Grupo de recursos: rg-bci-foundry-lab-eus2   (región: eastus2)
   ├─ Recurso Foundry (kind AIServices, project management habilitado)  bci-foundry-lab-eus2
   │   ├─ Despliegues: gpt-5.6-luna (principal del Día 1) · gpt-5-mini (respaldo) · text-embedding-3-small
   │   ├─ Proyectos: lab-p01 … lab-p48 · lab-instr-01..03 · lab-reserva-01..03   (propuesta original; real: una cuenta + proyecto lab-NN por participante)
   │   └─ Conexiones: Application Insights · Azure AI Search
   ├─ Azure AI Search (Basic o superior, RBAC habilitado)      bci-lab-search-eus2   ← índice «normativa ficticia» creado por instructores
   ├─ Document Intelligence (S0)                               bci-lab-di-eus2
   ├─ Application Insights (basado en espacio de trabajo)      bci-lab-appi-eus2
   └─ Log Analytics workspace                                  bci-lab-law-eus2
Entra ID: grp-bci-foundry-participantes · grp-bci-foundry-instructores   (real: grp-bci-lab-participantes · grp-bci-lab-instructores)
```

### 3.3 Modo de configuración del agente: Básico vs Estándar

La documentación define tres modos: **Básico** (almacenamiento administrado por Microsoft), **Estándar** (Storage + Cosmos DB + AI Search propios) y **Estándar con VNet propia** (`docs-oficiales\foundry\agents\environment-setup.md`).

**Recomendación:** **Básico, red pública**, plantilla `40-basic-agent-setup` (referencia en `scripts\04_infra_referencias.md`).
Motivos: se aprovisiona en minutos (la documentación indica típicamente 5–10 min), no requiere Cosmos DB (la plantilla estándar exige ≥3.000 RU/s en 3 contenedores de 1.000 RU/s) ni permisos de *Role Based Access Control Administrator* sobre varios recursos, y el evento no maneja datos reales. Pasa a Estándar solo si la política de BCI lo exige; en ese caso suma un día de preparación.

> Límite del modo Básico: no admite recursos de Azure AI Search privados ni con acceso público deshabilitado (`agents\how-to\tools\ai-search.md`). Con Search público (recomendado aquí) no hay problema.

### 3.4 Convención de nombres y etiquetas

- Grupo de recursos: `rg-bci-foundry-lab-eus2`. Proyectos: `lab-p01`…`lab-p48`. Los nombres de recursos con dominio personalizado deben ser **globalmente únicos** (`CustomDomainInUse` si no) → *verificar* disponibilidad antes del día del evento.
- Etiquetas obligatorias en el grupo de recursos y en cada recurso: `evento=bci-foundry-training-2026-10`, `propietario=<correo-admin>`, `eliminar-despues-de=2026-10-26`, `datos=ficticios`.
- Cada proyecto Foundry queda etiquetado automáticamente con la etiqueta `project` en el uso subyacente (atribución de costos por proyecto, vista previa; solo modelos vendidos por Azure) (`concepts\manage-costs.md`).
- Reparto de asientos: el día 1 la pareja o el trío comparte pantalla y usa el proyecto de quien «maneja» (el lab los hace alternar); el día 2 cada persona usa **su** proyecto. Publica una tabla `participante → proyecto`; el modelo es el mismo para todos y solo cambia si se activa el respaldo (ver 5.4). Relación con los tríos del lab: ver 3.5.

### 3.5 Proyectos por participante (≈54) y grupos de tríos (≈16, límite de 16 sesiones)

> **Estado real:** el entorno se aprovisionó en el tenant del evento, por lo que el límite de ≈16 sesiones **no aplica**. Cada cuenta `labNN` tiene su propio proyecto `lab-NN`. Aun así, en el Día 1 las parejas o tríos comparten **un solo agente** (una sola cuenta) para respetar los 4K TPM de `gpt-5.6-luna` por cuenta. El texto siguiente describe la propuesta original.

Son dos cosas distintas que no se contradicen. Los **≈54 proyectos** (48 participantes + 3 instructores + 3 de reserva) son la recomendación para un entorno **aprovisionado por BCI**, donde la propuesta no indica límite de sesiones: cada persona tiene su propio proyecto y su propio `FOUNDRY_PROJECT_ENDPOINT`, lo que el día 2 (individual) necesita. Los **grupos de tríos (≈16: 7 presenciales + 9 remotos)** de la nota del lab del Día 1 responden al **límite de 16 sesiones, que aplica solo si Microsoft aprovisiona el entorno** (`laboratorios\dia1-lab-guiado\README.md` §4.2; `MATERIALS_INDEX.md` §4); además, trabajar en parejas o tríos es una decisión pedagógica del lab (uno maneja, otros verifican). Con entorno de BCI, el día 1 puede ejecutarse en tríos (cada trío usa el proyecto de una de sus tres personas; N≈16 en 5.3) o de forma individual en el proyecto propio, sin que exista el tope de 16. Si al final provisiona Microsoft: día 1 con ≈16 proyectos (uno por trío, o un proyecto compartido con agentes de nombre distinto) y, para el día 2, **confirmar con Microsoft** si el límite también aplica, porque el lab del Día 2 es individual (admite un proyecto compartido o uno por ≈12 participantes si la cuota lo exige: `laboratorios\dia2-lab-procode\guia-facilitador.md` §1.1).

---

## 4. Recursos Azure por día

| Recurso | Día 1 | Día 2 | Día 3 | Notas |
|---|:---:|:---:|:---:|---|
| Grupo de recursos + etiquetas | ✔ | ✔ | — | |
| Recurso Foundry (AIServices) + proyectos | ✔ | ✔ | — | CLI: `az cognitiveservices account create … --kind AIServices --assign-identity --allow-project-management true` (la opción de gestión de proyectos **no se puede cambiar** después) |
| Despliegues de chat: `gpt-5.6-luna` (principal Día 1) y `gpt-5-mini` (respaldo; principal propuesto del Día 2) | ✔ | ✔ | — | Predesplegados por el equipo en cada cuenta (nombre del despliegue = nombre del modelo); `gpt-5.6-luna` con `provisionamiento\Add-Modelo.ps1` |
| Despliegue de embeddings (`text-embedding-3-small`) | — | ✔ | — | Para el índice y consultas vectoriales |
| Azure AI Search (Basic o superior) | — | ✔ | — | Índice pre-creado por instructores |
| Document Intelligence S0 | ✔ (Bloque C y demo en vivo) | — | — | Studio con Entra ID (modelos *prebuilt* Invoices, Layout y, en la demo, Receipt); qué recurso usa cada cuenta `labNN`: *por confirmar* |
| Application Insights + Log Analytics | opcional | ✔ | — | Trazas del día 2 |
| Azure Container Registry | — | demo | — | Solo para la demo del instructor de un agente *hospedado* (diapositivas 10 y 30 del Día 2); si no está listo, se usa el plan B (`plan-b-demos.md`) |
| Cuenta de Storage/Cosmos DB propias | — | — | — | Solo modo Estándar |
| Demos del instructor del Día 3 (AI Gateway/APIM, `azd ai agent eval`) | — | — | demo | **Sin laboratorio para participantes.** Requieren artefactos propios (panel APIM ilustrativo; extensión `azd` con evaluación de agentes, funcionalidad en evolución): *verificar* disponibilidad o usar grabación (plan-b-demos.md) |

Fuentes: `agents\environment-setup.md`, `how-to\create-projects.md`, `agents\concepts\hosted-agent-permissions.md`.

---

## 5. Región y modelos

### 5.1 Región recomendada: East US 2 (`eastus2`)

| Requisito | East US 2 | Fuente |
|---|---|---|
| `gpt-5-mini` / `gpt-4.1-mini` (Global Standard) | Disponible (no lo está en `canadacentral`) | `foundry-models\concepts\models-sold-directly-by-azure-region-availability.md` |
| `gpt-5.4-mini` (alternativa del lab del Día 1) | Disponible en las regiones de América de la tabla, incluida `canadacentral`. `gpt-5-nano` (otra alternativa del lab): *verificar* | ídem |
| `text-embedding-3-small` | Disponible en las regiones de América de la tabla | ídem |
| `gpt-5.6-luna` (Global Standard y Data Zone Standard) | Desplegado y probado en `eastus2`: llamadas básicas OK con Chat Completions y Responses API (pruebas del equipo previas al taller). **Con Foundry Agent Service + file search: no probado** | Pruebas del equipo (no figura en la documentación revisada) |
| Agentes, Responses, VNet privada | Listada | `agents\concepts\limits-quotas-regions.md` |
| Sesiones simultáneas de agentes hospedados por suscripción/región | 2.000 (East US 2) | `agents\concepts\limits-quotas-regions.md` |

**Por qué no Brasil Sur** (más cercana a Chile): la documentación indica que *File Search* no está disponible en Brazil South, tampoco la herramienta *Function*. No hay región de Chile en las listas. La latencia desde Chile a cada región **no figura en la documentación** → *verificar* con una prueba real el día 1 a las 08:00.

**Tipo de despliegue:** *Global Standard* (punto de partida recomendado: menor precio, mayor cobertura regional; el procesamiento puede ocurrir en cualquier región) (`foundry-models\concepts\deployment-types.md`). Como los datos son ficticios no hay impacto de residencia. **En el entorno real**, `gpt-5.6-luna` está en Global Standard en 37 cuentas (inst01–04 y lab01–lab33) y en **Data Zone Standard** en 25 cuentas (lab34–lab58); `gpt-5-mini` y `text-embedding-3-small` van en Global Standard (`participante.bicep`). Si BCI exige *Data Zone*, la cuota por defecto del nivel 1 es mucho menor (`gpt-5-mini` DataZoneStandard: 300 RPM / 300.000 TPM) y **no cubre** los escenarios de 48 usuarios de 5.3 (sí el de tríos del día 1).

### 5.2 Tabla de despliegues

> **Entorno real (v1.2).** Cada cuenta `labNN`/`instNN` tiene predesplegados `gpt-5.6-luna`, `gpt-5-mini` y `text-embedding-3-small` (nombre del despliegue = nombre del modelo). Capacidades **por cuenta**: 4K TPM, 10K TPM y 10K TPM respectivamente. Las filas «≥ 600» y `gpt-4.1-mini` de la tabla describen la propuesta original (1 despliegue compartido).

| Uso | Modelo (versión) | Nombre de despliegue | Tipo | Capacidad inicial (miles de TPM) | Día |
|---|---|---|---|---|---|
| **Chat principal del Día 1** (**real**) | `gpt-5.6-luna` (2026-07-09) | `gpt-5.6-luna` | Global Standard (37 cuentas) / Data Zone Standard (25 cuentas) | **4 por cuenta** (62 cuentas × 4 = 248 en total) | 1 |
| **Chat de respaldo del Día 1 / chat del Día 2** (**real**) | `gpt-5-mini` (2025-08-07) | `gpt-5-mini` | Global Standard | **10 por cuenta** (la cuota efectiva de la suscripción: *verificar*) | 1 (respaldo) y 2 |
| *Propuesta original:* chat principal único (días 1 y 2) | `gpt-5-mini` (2025-08-07) | `gpt-5-mini` | Global Standard | ≥ 600 en un solo despliegue (estimación; ver 5.3) | 1 y 2 |
| *Propuesta original:* chat de respaldo (se activa cambiando solo `FOUNDRY_MODEL`; también para demos con la herramienta de Azure AI Search del agente) | `gpt-4.1-mini` (2025-04-14) | `gpt-4.1-mini` | Global Standard | **No está predesplegado** en las cuentas reales; habría que desplegarlo (*por confirmar*) | 1 y 2 (solo si falla el principal) |
| Embeddings | `text-embedding-3-small` (v1) | `text-embedding-3-small` | Global Standard | 10 por cuenta (**real**; consumo estimado ≈ 22 en total, ver 5.3) | 2 |

Notas:
- **Nombres de despliegue y comunicación a los participantes.** El nombre del despliegue es el mismo nombre del modelo (`gpt-5.6-luna`, `gpt-5-mini`, `text-embedding-3-small`), que es lo que busca el lab del Día 1 en el portal. Los nombres se comunican a los participantes mediante el `.env` del Día 2 (`FOUNDRY_MODEL`, `FOUNDRY_EMBEDDING_MODEL`; ver sección 18): el código del lab es agnóstico, por lo que un cambio de modelo solo cambia ese archivo.
- **Día 1: `gpt-5.6-luna` y `gpt-5-mini` ya están predesplegados** en cada cuenta (los despliegues pertenecen al recurso y su proyecto los ve) para que nadie tenga que desplegar. `gpt-5.6-luna` se despliega con `provisionamiento\Add-Modelo.ps1` (versión 2026-07-09, capacidad 4, 37 cuentas en Global Standard y el resto en Data Zone Standard; el script es idempotente) y también está contemplado en `participante.bicep`. El lab acepta `gpt-5-mini` como respaldo si `gpt-5.6-luna` da `429` o falla.
- **Riesgo a verificar en T-1 (matriz de herramientas).** **`gpt-5.6-luna` con Foundry Agent Service + file search desde una cuenta de participante no se ha probado**: ejecútalo con una cuenta `labNN` real antes del taller (pasos 8 a 11 de `laboratorios\dia1-lab-guiado\checklist-validacion.md`). Para `gpt-5-mini`, `agents\concepts\limits-quotas-regions.md` indica: Azure AI Search = No, Functions = No, File Search = Sí, Code Interpreter = Sí, MCP = Sí, Web Search = Sí; y para `gpt-4.1-mini`: Azure AI Search = Sí, Functions = Sí, File Search = Sí. El día 1 solo exige File Search. El día 2 usa Agent Framework con herramientas de función **locales** y consulta Azure AI Search con el SDK `azure-search-documents` (no con la herramienta de Azure AI Search del Agent Service), por lo que no debería afectar; aun así **verifícalo en la prueba de T-1** con `src\00_verificar_entorno.py --probar-modelo` y `src\03_agente_con_search.py` del lab del Día 2. Si falla, el respaldo documentado es `gpt-4.1-mini`, que **no está predesplegado** en las cuentas (habría que desplegarlo; *por confirmar*).
- **Registro de acceso.** La documentación indica que para modelos `gpt-5` se requiere registro (enlace a `gpt-5-2025-08-07`; `agents\concepts\limits-quotas-regions.md`, solución de problemas) y no aclara si cubre `gpt-5-mini` ni `gpt-5.6-luna` → **verificar** al crear el despliegue (T-1).
- **Modelo de razonamiento.** `gpt-5-mini` admite Chat Completions y Responses, salidas estructuradas y llamadas a funciones en paralelo; contexto de 400.000 tokens (`foundry-models\concepts\models-sold-directly-by-azure.md`). Los tokens de razonamiento se facturan como salida y comparten la ventana de contexto (`openai\how-to\reasoning.md`), por eso el parámetro `t` de 5.3 los incluye.
- **No se despliegan** `gpt-4.1` ni `gpt-5` (completo): ningún lab los necesita.
- **Cuota de `gpt-5.6-luna`: 4K TPM por cuenta (límite real).** Con ≈3K tokens de entrada dos veces seguidas se supera la cuota y devuelve `429` (probado). Por eso las parejas y tríos comparten **un solo agente**, los prompts del lab son cortos y el respaldo `gpt-5-mini` (10K TPM) está predesplegado.
- El asistente de *agentic retrieval* del portal de Azure AI Search soporta `gpt-4o`, `gpt-4o-mini`, `gpt-5`, `gpt-5-mini` y `gpt-5-nano` (`azure-ai-search\get-started-portal-agentic-retrieval.md`), así que sirve con el despliegue de `gpt-5-mini`; por la vía programática se documenta `gpt-4.1-mini` (`foundry\agents\how-to\foundry-iq-connect.md`) → para esa demo usa el respaldo.
- Capacidad y cuota se expresan en **miles de TPM** (la línea de cuota se llama «Tokens Per Minute (thousands) - <modelo>», con nombre `{Proveedor}.{TipoDeDespliegue}.{Modelo}`; `docs-oficiales\foundry\openai\how-to\quota.md`). Consulta lo disponible con la API de Usages (`GET https://management.azure.com/subscriptions/{sub}/providers/Microsoft.CognitiveServices/locations/{region}/usages?api-version=2024-10-01`, vía `az rest`) y con la API de capacidades por modelo (`.../providers/Microsoft.CognitiveServices/modelCapacities?api-version=2024-10-01&modelFormat=OpenAI&modelName=<modelo>&modelVersion=<versión>`); ambas están en `scripts\00_prerequisitos.ps1` con `-ConsultarCuota`. Las ediciones de cuota pueden tardar hasta 15 minutos en reflejarse (`docs-oficiales\foundry\how-to\quota.md`).
- Máximo de despliegues por recurso: **32**.

### 5.3 Método de estimación de cuota (≈48 usuarios concurrentes)

> **Propuesta original (un despliegue compartido).** Esta estimación supone un único despliegue de `gpt-5-mini` con ≥ 600K TPM compartido por todos los proyectos. **En el entorno real cada cuenta tiene su propia cuota** (`gpt-5.6-luna`: 4K TPM; `gpt-5-mini`: 10K TPM; embeddings: 10K TPM) y los `429` en `gpt-5.6-luna` son reales (≈3K tokens de entrada dos veces seguidas ya los provocan). Mitigación: parejas/tríos con **un solo agente**, prompts cortos y cambio a `gpt-5-mini`. La suma de `gpt-5.6-luna` (62 cuentas × 4K = 248K TPM) sí consume cuota de la suscripción (GlobalStandard: 148K de 150K disponibles en las 37 cuentas; DataZoneStandard: 100K en 25 cuentas). La capacidad real de `gpt-5-mini` y embeddings en la suscripción: *verificar*.

> **Estimación de planificación.** Los parámetros dependen del guion real del laboratorio y deben medirse en el ensayo.

**Fórmula**

```
TPM_necesarios = N × r × t × k
RPM_necesarios = N × r × k

N = usuarios que ejecutan el lab al mismo tiempo (peor caso: 48)
r = llamadas al modelo por usuario por minuto
    (un «turno» de agente con herramienta suele hacer 2–3 llamadas: plan → herramienta → respuesta)
t = tokens promedio por llamada (entrada + salida; incluye instrucciones, historial, fragmentos recuperados y,
    en `gpt-5-mini`, los tokens de razonamiento)
k = factor de pico (1,5–2 para ráfagas cuando todos presionan «ejecutar» a la vez)
```

**Ejemplo (supuestos ilustrativos, no medidos; solo con los modelos principales)**

| Escenario | N | r | t | k | TPM | RPM |
|---|---|---|---|---|---|---|
| Día 1, agente de prompt + file search (`gpt-5-mini`) | 48 | 2 | 4.000 | 1,5 | **576.000** | **144** |
| Día 1 en tríos (`gpt-5-mini`) | 16 | 2 | 4.000 | 1,5 | 192.000 | 48 |
| Día 2, agente Python con herramienta local + Search (`gpt-5-mini`) | 48 | 2 | 3.500 | 1,5 | **504.000** | **144** |
| Día 2 sin ráfagas (`gpt-5-mini`, k = 1) | 48 | 2 | 3.500 | 1 | 336.000 | 96 |
| Día 2, consultas de embeddings (`text-embedding-3-small`) | 48 | 3 | 100 | 1,5 | ≈ 21.600 | ≈ 216 |

Los días no se ejecutan a la vez, así que **no se suman**: la capacidad a solicitar para `gpt-5-mini` es la del peor escenario redondeada, **≥ 600 (miles de TPM)** — coherente con el pico de 250–350 K TPM con 48 personas que estima el lab del Día 2 (`laboratorios\dia2-lab-procode\guia-facilitador.md` §1.1; el caso k = 1 de la tabla da 336 K). Es una **estimación de planificación**: mídela en el ensayo de T-1 (el checklist del lab del Día 2 incluye una prueba de carga de 5 personas / 10 ejecuciones sin 429).

**Comparación con los máximos por nivel (Global Standard, `openai\quotas-limits.md`)**

| Modelo | Nivel 0 | Nivel 1 | Nivel 2 |
|---|---|---|---|
| `gpt-5-mini` (principal) | 500 RPM / 500.000 TPM | 1.000 RPM / 1.000.000 TPM | 2.000 RPM / 2.000.000 TPM |
| `text-embedding-3-small` (principal) | 1.000.000 TPM | 1.000.000 TPM | 2.000.000 TPM |
| `gpt-4.1-mini` (respaldo; solo informativo) | 200 RPM / 200.000 TPM | 5.000 RPM / 5.000.000 TPM | 16.000 RPM / 16.000.000 TPM |

Lectura del ejemplo:
- **Nivel 1:** ambos días caben en `gpt-5-mini` con holgura (576 K y 504 K de 1.000 K TPM, 58 % y 50 %; 144 RPM de 1.000).
- **Nivel 0:** el máximo de 500 K TPM **no cubre** el caso conservador del día 1 (576 K) ni el del día 2 con ráfagas (504 K); sí cubre el día 1 en tríos (192 K) y el día 2 sin ráfagas (336 K). Opciones: solicitar aumento **hoy**, trabajar en tríos el día 1 o activar el respaldo `gpt-4.1-mini` (pool propio; 5.4).
- El nivel inicial de la suscripción depende del uso y de la relación comercial (EA/MCA-E); se consulta con la API `quotaTiers` (versión `2025-10-01-preview`) — *verificar en la suscripción de BCI*. Los valores de la tabla son **máximos por nivel**; la cuota efectiva puede ser menor (*verificar* en el portal Foundry: *Manage > Quota*).
- Desde el 7-may-2026 la cuota se administra a **nivel de suscripción**; en Global Standard, el mismo modelo y versión comparte un único pool entre regiones (revisar la columna *Scope* en la página Quota) (`foundry-models\quotas-limits.md`). **Cambiar de región no multiplica la cuota**; cambiar de *modelo* sí (cada modelo tiene su pool).
- Aumentos de cuota: formulario `aka.ms/oai/stuquotarequest`; las solicitudes se evalúan individualmente y por orden de llegada (sin plazo garantizado) → **solicítalo hoy** si el nivel no alcanza. Ver (`how-to\quota.md`).
- Todo 429 debe tratarse con reintentos con *backoff* y el encabezado `Retry-After` (`foundry-models\quotas-limits.md`). Los labs deben indicar reintentos en el código del día 2.

### 5.4 Un despliegue principal y conmutación al respaldo (días 1 y 2)

> **Entorno real (v1.2).** En el Día 1 el despliegue principal es `gpt-5.6-luna` (por cuenta, 4K TPM) y el respaldo `gpt-5-mini` (por cuenta, 10K TPM), ambos ya desplegados: ante un `429` sostenido o un fallo, el participante espera ≈ 10 s, acorta el prompt o cambia el agente a `gpt-5-mini`. El texto siguiente describe la propuesta original (`gpt-5-mini` principal y `gpt-4.1-mini` de respaldo).


Todos los participantes usan el **mismo** despliegue principal `gpt-5-mini`, igual que en los labs; no hay reparto por mitades. El nombre del despliegue es un parámetro del `.env` del lab del Día 2 (`FOUNDRY_MODEL`, con alias `AZURE_AI_MODEL_DEPLOYMENT_NAME`; `FOUNDRY_EMBEDDING_MODEL` para embeddings; ver `laboratorios\dia2-lab-procode\.env.example`) y los instructores lo comunican a los participantes con ese archivo (en el día 1 lo dice el equipo al inicio). **Contingencia:** si hay 429 sostenidos o `gpt-5-mini` falla (cuota, registro, herramienta no soportada): (1) espera 30–60 s y reintenta con *backoff*; (2) sube la capacidad del despliegue si el pool lo permite; (3) mueve a una parte o a todos los participantes al respaldo `gpt-4.1-mini` cambiando solo `FOUNDRY_MODEL=gpt-4.1-mini` (cada modelo tiene su propio pool de cuota). **Crea hoy el despliegue de respaldo:** al ser Global Standard (pago por token, `foundry-models\concepts\deployment-types.md`) no consume sin tráfico, pero descuenta capacidad del pool de ese modelo. Si un despliegue no alcanza, el lab del Día 2 sugiere repartir entre 2–4 despliegues o proyectos; eso solo aísla grupos, porque el pool de cuota del modelo es el mismo.

### 5.5 Otros límites útiles

- Embeddings: máximo 2.048 entradas y 300.000 tokens por solicitud (`openai\quotas-limits.md`).
- Voz y avatar: **sin laboratorio** (la demo de voz/avatar se eliminó del Día 1; Speech queda solo como visión general del módulo Azure AI Services).
- Herramienta de archivos (agentes): 10.000 archivos por agente/hilo, 512 MB por archivo, 2.000.000 tokens por archivo para vector store (`agents\concepts\limits-quotas-regions.md`). Los documentos ficticios del lab quedan muy por debajo.

---

## 6. Control de acceso (RBAC)

**Regla general:** usa roles **Foundry**; no asignes roles «Cognitive Services …» ni *Azure AI Developer* para el trabajo en Foundry (excepciones indicadas abajo) (`concepts\rbac-foundry.md`). Los roles se renombraron recientemente (*Azure AI User* → *Foundry User*, etc.); los **GUID no cambian**, así que los scripts usan GUID.

| Rol | GUID |
|---|---|
| Foundry User (antes Azure AI User) | `53ca6127-db72-4b80-b1b0-d745d6d5456d` |
| Foundry Project Manager | `eadc314b-1a2d-4efa-be10-5d325db5065e` |
| Foundry Account Owner | `e47c6f54-e4a2-4754-9501-8e0985b135e1` |
| Foundry Owner | `c883944f-8b7b-4483-af10-35834be79c4a` |
| Foundry Agent Consumer | `eed3b665-ab3a-47b6-8f48-c9382fb1dad6` |

### 6.1 Participantes — grupo `grp-bci-lab-participantes` (propuesta original: `grp-bci-foundry-participantes`)

> **Entorno real (v1.2).** El aprovisionamiento asigna a cada participante **Foundry User** y **Reader** en su grupo de recursos `rg-bci-lab-NN` y **Cognitive Services User** sobre **su cuenta Foundry** (la que usa el Studio de Document Intelligence en el Bloque C y la demo). En despliegues nuevos lo hace `participante.bicep`; en el entorno ya desplegado se agrega con `provisionamiento\Add-RolCognitiveServicesUser.ps1` (idempotente, `-WhatIf`; usa `rol-cognitive-services-user.bicep` con el mismo nombre de asignación, sin redesplegar los modelos). **No** asigna *Storage Blob Data Contributor*: si la subida de archivos a *file search* (Bloque B) da 403, hay que añadirlo → *por confirmar* con una cuenta `labNN` real (paso de file search del `checklist-validacion.md`).


| Rol (nombre integrado) | Ámbito | Para qué | Fuente |
|---|---|---|---|
| **Foundry User** | Recurso Foundry (o proyecto, si se asigna por persona) | Día 1: crear agentes de prompt y usar el modelo; día 2: llamar al modelo y a embeddings desde el código (`FOUNDRY_PROJECT_ENDPOINT`). **No** se da *Foundry Account Owner* a los participantes: el lab del Día 1 solo lo pide si ellos crean su propio recurso o proyecto, y aquí los proyectos ya vienen creados | `concepts\rbac-foundry.md`; labs de los días 1 (README §4.2) y 2 (`guia-facilitador.md` §1.2) |
| **Log Analytics Reader** (+ **Privileged Monitoring Data Reader** si las tablas están protegidas) | Application Insights / workspace de Log Analytics conectado | Ver **trazas** en el portal o con KQL (los roles que nombra el lab del Día 2). *Foundry User* ve métricas pero **no** trazas | `laboratorios\dia2-lab-procode\guia-facilitador.md` §1.2; `observability\how-to\trace-agent-setup.md` |
| **Monitoring Reader** (complementario) | Recurso Application Insights conectado | Es el rol que cita la documentación de agentes hospedados para ver trazas; es de solo lectura, se asigna junto con el anterior y en la prueba de T-1 se verifica cuál basta | `agents\concepts\hosted-agent-permissions.md` |
| **Monitoring Metrics Publisher** (**condicional**) | Recurso Application Insights conectado | **Solo si** la autenticación local de Application Insights está deshabilitada (típico en bancos): permite enviar trazas con Entra ID (`LAB_APPINSIGHTS_ENTRA=true` en el `.env`) | lab del Día 2 `guia-facilitador.md` §1.2; taller `foundry-hosted-agents-workshop` (paso 02) |
| **Search Index Data Reader** | Servicio Azure AI Search | Consultar el índice `normativa-austral` del día 2 (el instructor lo crea) | `agents\how-to\foundry-iq-connect.md`; lab del Día 2 |
| **Cognitive Services User** (**asignado** en el entorno real) | Cuenta Foundry del participante (`rg-bci-lab-NN`) | Día 1: usar el Studio y los modelos *prebuilt* con Entra ID (sin compartir claves); si la autenticación por clave está deshabilitada, *Contributor* no basta. Descrito como rol para «capacidades a nivel de cuenta: Speech, Vision, Language» | `hosted-agent-permissions.md`; README del lab del Día 1 — *verificar con la cuenta de prueba* |
| **Storage Blob Data Contributor** (*verificar*) | Cuenta de Storage del proyecto | El lab del Día 1 lo lista para subir archivos a *file search* y la documentación lo exige para entornos básico o estándar (`agents\how-to\tools\file-search.md`). En modo **Básico** el almacenamiento lo administra Microsoft (`agents\environment-setup.md`) y puede no haber una cuenta visible a la que asignar el rol → **probar la subida con una cuenta de participante en T-1**; ante un 403, asígnalo al grupo en la cuenta de Storage del proyecto (`scripts\01_crear_grupo_y_roles.ps1 -StorageProyecto`) o usa el Plan B (el instructor sube los archivos) | README del lab del Día 1 §4.2 |
| **Reader** (**asignado** en el entorno real) | Grupo de recursos `rg-bci-lab-NN` | Ver los recursos en Azure Portal; el modelo empresarial de la guía de RBAC usa *Foundry User* en proyecto + *Reader* en el recurso | `concepts\rbac-foundry.md` |
| **Cognitive Services Usages Reader** | **Suscripción** | Ver cuota (solo si el participante necesita ver la cuota; **no se recomienda** para participantes) | `how-to\quota.md` |

Notas importantes:
- Crear el recurso Foundry por CLI/SDK **no** asigna *Foundry User* automáticamente (solo la creación desde el portal lo hace al creador); asígnalo explícitamente al grupo.
- Las **claves de API omiten el RBAC** (acceso total). Para el laboratorio usa Entra ID; si BCI exige compartir claves en el ejercicio de Document Intelligence, rótalas al terminar el evento.
- Si el día 2 pide a los participantes **cargar** documentos al índice, añade *Search Index Data Contributor* en vez de *Reader* (decisión a alinear con los autores del lab; por defecto el instructor pre-crea el índice).
- Aislamiento por persona (opcional): asignar *Foundry User* **por proyecto** a cada persona en vez de al recurso. Requiere un archivo de mapeo usuario→proyecto; ver parámetro `-MapaUsuarioProyecto` en `scripts\01_crear_grupo_y_roles.ps1`. Para un evento con datos ficticios, el aislamiento por convención es suficiente.

### 6.2 Instructores — grupo `grp-bci-lab-instructores` (propuesta original: `grp-bci-foundry-instructores`)

| Rol | Ámbito | Para qué |
|---|---|---|
| **Foundry Owner** | Recurso Foundry | Control total de plano de control y de datos del recurso: despliegues, conexiones, agentes (cubre lo que pide el lab del Día 2: *Foundry User* o *Contributor* para crear despliegues). **No** crea asignaciones de rol |
| **Cognitive Services Usages Reader** | Suscripción | Ver cuota en el portal (a nivel de recurso no funciona) |
| **Search Service Contributor** + **Search Index Data Contributor** | Servicio Azure AI Search | Crear el índice y cargar el contenido ficticio |
| **Log Analytics Reader** + **Monitoring Reader** | Application Insights / workspace | Mostrar y depurar trazas en vivo |
| **Cognitive Services User** (+ rol de gestión del recurso si debe crear claves) | Recurso Document Intelligence | Demo en vivo de OCR (Receipt, Layout/Read; `laboratorios\dia1-lab-guiado\demo-document-intelligence.md`) |
| **Contributor** (solo si se hace la demo de agente hospedado) | Grupo de recursos | Crear Azure Container Registry y App Insights (los roles Foundry **no** pueden) |

Si el instructor debe publicar agentes, el mínimo documentado es **Foundry Project Manager** sobre el recurso.

### 6.3 Administrador de BCI (quien aprovisiona)

| Necesidad | Rol mínimo | Ámbito |
|---|---|---|
| Crear grupo de recursos, recurso Foundry, proyectos, App Insights, Search, Document Intelligence | **Owner** o **Contributor** | Grupo de recursos |
| Crear asignaciones de rol | **Owner**, **User Access Administrator** o **Role Based Access Control Administrator** | Recurso / grupo de recursos |
| Desplegar modelos y administrar cuota | **Foundry Account Owner** | Recurso Foundry + suscripción |
| Solicitar aumentos de cuota | **Contributor** | Suscripción |
| Recuperar/purgar cuentas eliminadas | **Contributor** | Suscripción |
| Asignar políticas de Azure | **Resource Policy Contributor** | Suscripción / grupo |
| Crear grupos Entra | Permiso de Entra ID para crear grupos de seguridad — *verificar rol según política de BCI* | Tenant |

Fuentes: `agents\environment-setup.md`, `concepts\administrator-guide.md`, `how-to\quota.md`, `agents\concepts\hosted-agent-permissions.md`.

### 6.4 Identidades administradas (solo si hay demos con agentes hospedados o herramientas administradas)

| Identidad | Rol | Ámbito | Fuente |
|---|---|---|---|
| MI del proyecto | Foundry User | Recurso Foundry | `hosted-agent-permissions.md` |
| MI del proyecto | Container Registry Repository Reader (preferido) o AcrPull | Registro de contenedores | ídem |
| MI del proyecto | Log Analytics Data Reader | Workspace de Log Analytics (necesario para **evaluaciones**) | ídem |
| MI del proyecto | Search Index Data Reader (Contributor si debe escribir) | Servicio de Search | `foundry-iq-connect.md` |
| MI del recurso Foundry (herramienta Azure AI Search sin claves) | Search Index Data Contributor + Search Service Contributor | Servicio de Search | `agents\how-to\tools\ai-search.md` |
| MI del servicio Search (solo si la base de conocimiento usa un LLM) | Cognitive Services User | Recurso Foundry | `foundry-iq-connect.md` |

> **Nota de documentación:** el paso de solución de problemas de `foundry-hosted-agents-workshop\.workshop\docs\steps\01-basic.md` sugiere *Cognitive Services User + Azure AI Developer* ante un 401. La guía oficial de RBAC y la de agentes hospedados indican lo contrario (*Foundry User*; *Azure AI Developer* es insuficiente). **Seguimos la documentación oficial** y avisamos a los autores del taller.

---

## 7. Azure AI Search

| Tema | Guía | Fuente |
|---|---|---|
| Nivel | **Basic o superior**. Los inicios rápidos de Search indican «Basic tier or higher for managed identity support». *Free* no es adecuado (sin identidad administrada ni alta disponibilidad) | `azure-ai-search\get-started-portal-agentic-retrieval.md`, `search-get-started-portal.md` |
| Capacidad | Un índice pequeño de «normativa ficticia» (decenas de documentos) y 48 usuarios con pocas consultas por minuto es una carga baja → **Basic, 1 réplica y 1 partición** como punto de partida. Para tolerar fallas de consultas Microsoft indica ≥2 réplicas (costo ×2). Cuotas por nivel (QPS, almacenamiento, nº de índices): **no están en el material local → verificar** en la documentación de límites de Azure AI Search | `search-get-started-bicep.md` |
| Autenticación | Habilitar **control de acceso basado en roles (o «Ambos» durante la transición)**; las políticas a nivel de suscripción o grupo de recursos pueden anular las asignaciones | `search-get-started-rbac.md` |
| Roles | Instructores: Search Service Contributor + Search Index Data Contributor. Participantes: Search Index Data Reader. Para asignarlos se requiere Owner o User Access Administrator | `search-get-started-rbac.md`, `foundry-iq-connect.md` |
| Ranker semántico | Necesario para consultas `semantic` / `vector_semantic_hybrid` (valor por defecto de la herramienta de agente). Habilitar y *verificar* el plan disponible | `agents\how-to\tools\ai-search.md` |
| *Agentic retrieval* | Los objetos creados en el portal usan la versión `2026-08-01-preview`; parte de la funcionalidad es GA en `2026-04-01`. **Planificación de consultas y síntesis de respuestas son vista previa.** Se requiere una región con soporte (`search-region-support` **no está en el material local → verificar**) | `get-started-portal-agentic-retrieval.md` |
| Red | Público en este evento. Con red privada se exige autenticación de identidad administrada del proyecto (no claves) y modo Estándar | `agents\how-to\tools\ai-search.md` |
| Filtrado por ACL (demo de «2 usuarios simulados») | Vista previa: campos de permisos en el índice + encabezado `x-ms-query-source-authorization` | `foundry-iq-connect.md` |

**Contenido:** el instructor carga los 12 documentos ficticios de «normativa» que trae el lab (`laboratorios\dia2-lab-procode\data\normativa\NOR-001…NOR-012`) y construye el índice `normativa-austral` (texto + vector con `text-embedding-3-small` + ranker semántico) con `src\01_crear_indice.py` **hoy o durante el día 1**. Ese script requiere *Search Service Contributor* y *Search Index Data Contributor* en el servicio de Search y *Foundry User* en el proyecto (mismos roles de instructor de la sección 6); los participantes solo consultan el índice. El filtrado por nivel de acceso del lab (`publico | interno | restringido`) es un filtro sobre un campo del índice, no la función de vista previa de ACL de la fila anterior. Guarda un **índice de respaldo exportable** (ver Plan B).

---

## 8. Document Intelligence y Speech

### 8.1 Document Intelligence (día 1: Bloque C del laboratorio y demo en vivo del instructor)

- **Plan S0, no F0.** F0 permite **1 TPS**, 2 páginas y 4 MB por documento; S0 permite 15 TPS de análisis por defecto (ampliable por soporte) y hasta 500 MB y 2.000 páginas (`ai-services-document-intelligence\service-limits.md`). Con 48 personas en un recurso F0 el lab falla.
- Modelos *prebuilt* disponibles (p. ej. `bankStatement`, `check`, `creditCard`, `invoice`, `idDocument`, `contract`) — usa **solo documentos ficticios**.
- El lab del Día 1 (Bloque C) abre `documentintelligence.ai.azure.com/studio` (o el enlace del lab oficial) y se autentica con **Entra ID** (*Settings > Resource*), usa los modelos **Invoices** y **Layout** y los documentos ficticios `01-factura` y `02-solicitud-credito` de `laboratorios\dia1-lab-guiado\datos\documentos-ocr\`. La **demo en vivo del instructor** (≈10 min, módulo Azure AI Services, ≈10:40–10:50) usa `03-comprobante-compra.pdf` con el modelo **Receipt** y luego Layout/Read (`laboratorios\dia1-lab-guiado\demo-document-intelligence.md`). Requiere el rol *Cognitive Services User* y permitir cookies de terceros (si no, aparece AADSTS50058). Anota en T-1 qué URL del Studio funciona.
- El ejercicio 03 de `mslearn-ai-information-extraction` abre el Studio en `https://contentunderstanding.ai.azure.com/documentintelligence/studio` (no `documentintelligence.ai.azure.com`) y usa clave + endpoint. Permite ambos dominios en la lista de salida.
- **Parte «modelo personalizado» (setup.cmd/.sh): omitir** (no cabe en los 25 min del Bloque C y crea recursos adicionales).
- Disponibilidad por región de Document Intelligence: **no figura en el material local → verificar** que `eastus2` ofrece los modelos necesarios; si no, crear el recurso en otra región (el recurso es independiente del proyecto Foundry).
- Acceso: rol *Cognitive Services User* al grupo de participantes sobre el recurso (Entra, sin claves). Si el notebook exige clave, prepara una variante con `DefaultAzureCredential` o entrega la clave solo por canal controlado y **rótala** el 24-oct.

### 8.2 Speech (solo visión general; sin laboratorio ni demo)

- **La demo de voz/avatar del Día 1 se eliminó.** No se requiere recurso de Speech, Voice Live, avatar ni `gpt-realtime` para el laboratorio. Speech se menciona únicamente como servicio dentro de la visión general del módulo Azure AI Services (`laboratorios\dia1-lab-guiado\README.md`). La referencia de regiones y límites de avatar (`ai-services-speech-service\regions.md`, `speech-services-quotas-and-limits.md`) queda disponible en `docs-oficiales\` por si BCI pide una demo futura.

---

## 9. Trazas y monitoreo (día 2)

1. Crear (o dejar que el portal cree) **Application Insights basado en Log Analytics**. Crearlos exige `Microsoft.Insights/components/write` y `Microsoft.OperationalInsights/workspaces/write` en el grupo de recursos: solo *Owner*/*Contributor*, **no** los roles Foundry (`hosted-agent-permissions.md`). Hazlo el administrador.
2. **Conectar** Application Insights al proyecto/recurso Foundry (Agentes → Trazas → *Conectar*, o *Detalles del proyecto → Recursos conectados*). El rastreo del lado del servidor se activa automáticamente tras la conexión; las trazas aparecen en minutos. El rastreo está **GA** para agentes de prompt y hospedados; para agentes de flujo de trabajo y externos está en **vista previa**; la autenticación Entra para ingesta de trazas también es vista previa (`observability\how-to\trace-agent-setup.md`).
3. **Roles de lectura (según el lab del Día 2):** *Log Analytics Reader* sobre Application Insights / el workspace conectado (+ *Privileged Monitoring Data Reader* si las tablas están protegidas). La documentación de agentes hospedados cita *Monitoring Reader* sobre el recurso Application Insights (sus permisos `*/read` incluyen el workspace): es de solo lectura y se asigna además. La página de configuración de trazas indica *Log Analytics Reader* sobre el recurso conectado → **verificar con la cuenta de prueba cuál es suficiente en el portal**.
4. Si la autenticación local de App Insights está deshabilitada, la identidad que envía las trazas necesita *Monitoring Metrics Publisher*: en el lab del Día 2 son los **participantes** (rol sobre Application Insights y `LAB_APPINSIGHTS_ENTRA=true` en su `.env`); en una demo de agente hospedado, la identidad del proyecto/agente (taller `foundry-hosted-agents-workshop`, paso 02). **Pregunta a BCI si la autenticación local está deshabilitada** y anótalo antes del día 2.
5. Para *evaluaciones* la MI del proyecto necesita *Log Analytics Data Reader* en el workspace. Las plantillas estándar (`41-standard-agent-setup`) ya lo hacen con `deployApplicationInsights=true`.
6. La retención y la facturación siguen la configuración de Application Insights y Log Analytics. **Las trazas pueden contener contenido de prompts/respuestas** → datos ficticios únicamente.
7. Plan B si no aparecen trazas: capturas/grabación del instructor (ver `plan-b-demos.md`).

---

## 10. Red y salida a internet (egress)

### 10.1 Público vs privado

Un recurso Foundry creado sin configuración de red es **público** en entrada y salida (`agents\concepts\networking-options.md`). Las opciones privadas (VNet propia, VNet administrada, punto de conexión privado) existen, pero para este evento **no se recomienda red privada**:

- 27 personas por Teams y 21 en la sala de Microsoft Chile no están en la red de BCI; un endpoint privado exigiría VPN/VNet para todas.
- El modo Básico no admite Search privado; el modo Estándar con VNet agrega Cosmos DB, Storage, DNS privado, y su limpieza es más lenta (hasta 24 h en subredes con SAL; cuentas eliminadas se conservan 48 h — `deployment-tools\cleanup\README.md`).
- Los datos son ficticios. La protección es **Entra ID + RBAC + acceso condicional (MFA)**.

Si BCI exige red privada: plantilla `15-private-network-standard-agent-setup` u `18-managed-virtual-network` (ver `scripts\04_infra_referencias.md`), con asistentes conectados por VPN corporativa. **Confirma con Diego Bell Tineo si es requisito.**

### 10.2 Destinos a permitir (lista de partida — *verificar*)

La documentación local **no** trae una lista oficial de FQDN para equipos cliente; solo indica (para Azure Firewall) permitir los FQDN de identidad administrada o la etiqueta de servicio `AzureActiveDirectory` (`agents\faq.md`). La siguiente lista deriva de las URL que usan los laboratorios y debe **validarse desde un equipo representativo de BCI y desde la red de Microsoft Chile**.

| Destino | Uso | Origen del dato |
|---|---|---|
| `ai.azure.com` | Portal Foundry | `agents\overview.md` |
| `portal.azure.com`, `management.azure.com` | Azure Portal / ARM (CLI) | Labs |
| `login.microsoftonline.com` y dominios de Entra asociados | Inicio de sesión | *verificar lista completa* |
| `<recurso>.services.ai.azure.com` | Endpoint de proyecto Foundry (`/api/projects/<proyecto>`) | `foundry-iq-connect.md` |
| `<recurso>.cognitiveservices.azure.com`, `<recurso>.openai.azure.com` | Endpoints de cuenta | *verificar cuál usa cada SDK* |
| `<search>.search.windows.net` (`*.search.windows.net`) | Azure AI Search | `foundry-iq-connect.md`; lab del Día 2 |
| `contentunderstanding.ai.azure.com` y `documentintelligence.ai.azure.com` | Studio de Document Intelligence | `mslearn-ai-information-extraction`, docs DI |
| `*.applicationinsights.azure.com` y otros dominios de Azure Monitor (*verificar lista*) | Trazas | lab del Día 2 (`guia-facilitador.md`) |
| `login.microsoft.com` (`/device`) | Flujo de código de dispositivo de `az login --use-device-code` (Bloque A) | Bloque A del lab del Día 1 |
| `github.com`, `raw.githubusercontent.com`, `codeload.github.com` | Clonar repo del lab | Labs |
| `pypi.org`, `files.pythonhosted.org` | `pip install` | Labs |
| `marketplace.visualstudio.com`, `update.code.visualstudio.com` | VS Code y extensiones | *verificar* |
| `*.github.dev`, `github.com/codespaces` | Codespaces (alternativa) | *verificar* |

Permite también **cookies de terceros** para `ai.azure.com` y el Studio (si se bloquean aparece AADSTS50058; lab del Día 1). El script `02_validar_entorno.py` comprueba por TCP/HTTPS los endpoints Azure; para el resto usa `Test-NetConnection` desde un equipo de BCI (instrucciones en el encabezado de `00_prerequisitos.ps1`).

### 10.3 Acceso condicional (riesgo alto)

Los asistentes presenciales usarán la red de invitados de Microsoft Chile y los remotos redes domésticas. Si el tenant exige **dispositivo conforme/híbrido** o **ubicación de confianza**, parte del grupo quedará bloqueada. En el entorno real las cuentas `labNN` están protegidas con **MFA** y los participantes entran con un **Temporary Access Pass (TAP)** (no pueden registrar MFA); verifica en T-1 que el TAP funcione desde la red de invitados y desde una red doméstica. Si hubiera políticas de dispositivo, acuerda una **exclusión temporal** del grupo `grp-bci-lab-participantes` (propuesta original: `grp-bci-foundry-participantes`) para las aplicaciones *Azure Portal*, *Azure Management* y *Microsoft Foundry* durante el 21–23 de octubre (manteniendo MFA), o define la alternativa (Codespaces / demo guiada) para equipos bloqueados.

---

## 11. Identidad y grupos

> **Entorno real (v1.2).** Los grupos son `grp-bci-lab-participantes` y `grp-bci-lab-instructores`, con cuentas `labNN` (01–58) e `instNN` en el tenant `mngenvmcap219366.onmicrosoft.com` (quién lo administra: *por confirmar*). Todas usan **TAP** porque no pueden registrar MFA: el TAP del Día 1 es válido solo el miércoles 21-oct de 06:30 a 14:30 (hora de Chile) y los de los días 2 y 3 se regeneran cada noche (quién los reemite y por qué canal se entregan: *por confirmar*; en los documentos aparece `<CANAL-ENTREGA-TAP>`). Los pasos 1 a 5 siguientes describen la propuesta original (tenant de BCI, grupos `grp-bci-foundry-*`).

1. Crear dos **grupos de seguridad** en Entra ID: `grp-bci-foundry-participantes` y `grp-bci-foundry-instructores`. Asignar roles **al grupo**, no a personas (`concepts\rbac-foundry.md`).
2. Poblar el grupo de participantes con los ~48 registrados. Los usuarios deben estar en el **tenant de BCI** (si el entorno lo provisionara Microsoft serían invitados B2B, con más fricción de acceso condicional: otra razón para el entorno propio de BCI).
3. Propietario del grupo: administrador de BCI. Instructores: Pablo Braconi y Valentina Grajales (cuentas del tenant de BCI o invitados autorizados — *confirmar*).
4. Los cambios de pertenencia a grupos y de roles pueden tardar en propagarse (la cuota hasta 15 min según `docs-oficiales\foundry\how-to\quota.md`; para roles, *verificar*). **Cierra el alta de usuarios al menos 4 h antes** del inicio.
5. Probar siempre con una **cuenta de prueba que sea solo miembro del grupo** (no con la cuenta de administrador; esta oculta fallos de permisos).

---

## 12. Control de costos y limpieza

### 12.1 Qué genera costo (sin precios)

| Fuente de costo | Comportamiento | Fuente |
|---|---|---|
| Tokens de modelos de chat y embeddings | Por uso (token), medidor por modelo y tipo de despliegue; en `gpt-5.6-luna` y `gpt-5-mini` los tokens de razonamiento cuentan como salida (`openai\how-to\reasoning.md`; para `gpt-5.6-luna`: *por confirmar*) | `concepts\manage-costs.md` |
| Document Intelligence S0 | Por página analizada — *verificar* medidores | |
| Azure AI Search | Costo fijo por tiempo mientras el servicio existe (por nivel/unidades) | |
| Application Insights / Log Analytics | Ingesta y retención de trazas (aparece en esos servicios, **no** en el recurso Foundry) | `manage-costs.md` |
| Cosmos DB, Storage, ACR | Solo modo Estándar o demo de agente hospedado | `41-standard-agent-setup\README.md` |

Para estimar el costo del evento usa la calculadora de Azure con los mismos supuestos de la sección 5.3 (referencia de la propia documentación de costos). **No hay un límite duro de gasto para Azure OpenAI**; solo presupuestos y alertas, con automatización opcional vía grupos de acciones (`manage-costs.md`).

### 12.2 Controles

1. **Presupuesto** sobre el grupo de recursos (Cost Management → Budgets) con alertas en umbrales sugeridos de 50 %, 80 % y 100 % del monto aprobado (el monto lo define el responsable del entorno). Las alertas pueden llegar con retraso. **En el entorno real**, `participante.bicep` define un presupuesto (por defecto 10, moneda no especificada: *por confirmar*) por grupo de recursos con alertas al 50/80/100 %, que **solo se crea si se indican correos de contacto**; inicio 2026-10-01.
2. **Etiquetas** en todos los recursos (sección 3.4) y vistas de *Cost analysis* agrupadas por **Recurso** y **Medidor**; filtro por etiqueta `project` para ver el gasto por proyecto.
3. **Aviso de cuota:** monitorea la página *Quota* durante el día 1 y el día 2 (la cuota agotada produce 429).
4. **Limpieza programada:** `scripts\03_limpieza.ps1` (con confirmación explícita). Fecha sugerida: **26-oct-2026** (3 días después del cierre, para mantener el entorno durante la entrega de materiales; ajustar según política). **En el entorno real**, los recursos llevan la etiqueta `DeleteAfter` = 2026-10-30 (`participante.bicep`); alinea ambas fechas.
5. **Purga:** las cuentas de Cognitive Services eliminadas quedan en *soft-delete* **48 horas**; reutilizar el nombre exige purgar (*Contributor* a nivel de suscripción) (`deployment-tools\cleanup\README.md`, `concepts\administrator-guide.md`).
6. Si se usó Application Insights con *auto-cleanup* de datos: definir retención corta (*verificar* opción en el recurso).
7. Antes de eliminar: exportar la configuración de despliegues y los resultados del día 3 (no dependen de la nube) y confirmar con Pablo/Valentina que ya no se necesita el entorno.

---

## 13. Política de datos

- **Solo datos ficticios.** Prohibido cargar documentos, nombres, RUT, cuentas, correos o imágenes reales de clientes o colaboradores de BCI en el portal, índices, vector stores o prompts.
- Las trazas y las grabaciones de Teams pueden contener lo que se escriba en pantalla: no mostrar datos reales.
- Los documentos de ejemplo (facturas, estados de cuenta, normativa) serán **generados sintéticamente** por los instructores; se almacenarán en el repositorio del evento (`<LINK-REPO>`).
- Evita compartir claves o *connection strings* por chat; usa Entra ID.
- Al cerrar: eliminar proyectos, índices, vector stores y archivos; la limpieza del grupo de recursos lo cubre.

---

## 14. Cronograma T-5 → T-0 y camino mínimo de 24 horas

### 14.1 Cronograma de referencia

> **Estado real (v1.2):** el entorno ya está aprovisionado con `provisionamiento\Provision-Lab.ps1`, `Add-Modelo.ps1` y los Bicep; las filas siguientes son el cronograma original y sirven de referencia para las verificaciones de T-1 (cuenta `labNN` de prueba con TAP, modelos, Studio de Document Intelligence).


| Cuándo | Acción | Responsable |
|---|---|---|
| **T-5** (16-oct) | Confirmar quién provisiona; suscripción, región y rol del administrador; solicitar aumento de cuota si el nivel no alcanza | Pablo / admin BCI |
| **T-4** (17-oct) | Crear grupos Entra; revisar acceso condicional y lista de egress | Admin BCI |
| **T-3** (18-oct) | Aprovisionar RG, recurso Foundry, proyectos, despliegues (plantilla 40 + bucle de proyectos) | Admin BCI |
| **T-2** (19-oct) | Search, Document Intelligence, App Insights; roles con `01_crear_grupo_y_roles.ps1`; índice de normativa ficticia | Admin BCI + Valentina |
| **T-1** (20-oct) | Validación con cuenta de prueba (`02_validar_entorno.py`); piloto con 3–5 usuarios; envío de pre-trabajo (VS Code, Python 3.13, Git, Azure CLI; inicio de sesión con TAP); capturas Plan B (incluye la demo de Document Intelligence) | Pablo / Valentina |
| **T-0** (21-oct) | T-60 min: preflight en `runbook-facilitacion-3-dias.md`; Go/No-Go a las 08:15 | Equipo |

### 14.2 Camino mínimo si solo tenemos 24 horas (estamos en T-1)

**Principio:** el día 1 depende solo de Foundry + modelo + Document Intelligence; **el día 2 (Search, App Insights, trazas) puede terminar durante el día 1 por la tarde**, ya que tiene 24 h extra.

| Hora (aprox.) | Acción | Hecho cuando |
|---|---|---|
| **H+0 a H+2** (hoy) | Decidir con BCI: suscripción, región (**East US 2**), quién ejecuta. Admin ejecuta `00_prerequisitos.ps1`. Crear grupos Entra y cargar participantes (o al menos 5 usuarios de prueba) | Script sin errores; grupos creados |
| **H+2 a H+4** | Crear RG + recurso Foundry (Básico, público) + despliegues `gpt-5.6-luna` (principal del día 1, predesplegado) y `gpt-5-mini` (respaldo) + **proyectos mínimos: ≈16 a 24 (tríos/parejas)** o 1 proyecto compartido con agentes nombrados `ag-<iniciales>` como último recurso. *(Ya resuelto en el entorno real: una cuenta + proyecto `lab-NN` por participante; los equipos comparten un agente.)* | Despliegues en estado *Succeeded* |
| **H+4 a H+5** | `01_crear_grupo_y_roles.ps1 -WhatIf`, luego ejecución real (Foundry User al grupo; Usages Reader a instructores) | Rol visible en IAM |
| **H+5 a H+6** | Crear Document Intelligence **S0** + rol *Cognitive Services User* | Studio abre con el recurso |
| **H+6 a H+7** | `02_validar_entorno.py` con **cuenta de prueba** (no admin) | PASS en proyecto y despliegues |
| **H+7 a H+9** | Equipo Microsoft: preparar Plan B (grabaciones/capturas, ver `plan-b-demos.md`) y documentos ficticios del día 1 | Archivos en `plan-b\` |
| **21-oct 06:30 a 08:00** | TAP vigente desde las 06:30 (válido hasta las 14:30). Self-check de los asistentes; Go/No-Go 08:15 | Go/No-Go |
| **21-oct 13:00 a 22-oct 08:00** | Search Basic + índice, App Insights + conexión + *Log Analytics Reader*, capacidad extra de `gpt-5-mini` y aumento de cuota si hace falta; ensayo del lab día 2 con la cuenta de prueba | Checklist D2 completo |

**Qué se recorta si algo falla** (en orden):
1. Sin cuota suficiente en `gpt-5.6-luna` (4K TPM por cuenta; `429`) → espera ≈ 10 s, prompts más cortos, un solo agente por pareja/trío y cambio a `gpt-5-mini` (10K TPM, ya predesplegado); solicitar aumento si hace falta.
2. Sin proyectos individuales → 1 proyecto compartido con nombres con iniciales.
3. Sin Document Intelligence → el instructor demuestra el Studio compartiendo pantalla + capturas (Plan B de la demo y del Bloque C; `plan-b-demos.md`).
4. Sin Search/trazas al inicio del día 2 → instructor demuestra con Plan B y los participantes ejecutan el agente **sin** herramienta de Search (solo función personalizada).
5. Sin acceso a Azure para parte del grupo → `mslearn-agent-quickstart` lab 02 (conceptos de agentes **sin Azure**, LLM en el navegador) o demo guiada.

---

## 15. Checklist Go/No-Go

Marca **GO** solo si los ítems críticos (★) están OK. Responsable entre paréntesis. Ejecutar a las **08:15** de cada día.

### Día 1
- [ ] ★ Cuenta de prueba `labNN` (solo miembro del grupo) inicia sesión con **TAP** (portal y `az login --use-device-code`) y pasa `02_validar_entorno.py` (Pablo)
- [ ] ★ Despliegue `gpt-5.6-luna` responde en el playground y por endpoint; `gpt-5-mini` (respaldo) también (Pablo)
- [ ] ★ **Agente con file search sobre `gpt-5.6-luna` (Foundry Agent Service) probado con una cuenta de participante** — no se ha probado todavía; si falla, el lab usa `gpt-5-mini` (Pablo)
- [ ] ★ Subida de archivos a *file search* con la cuenta de prueba, sin 403 (rol de almacenamiento si aplica) (Pablo)
- [ ] ★ ≥ 80 % de asistentes con self-check exitoso a T-30 (Robert / Valentina)
- [ ] ★ Cuota de chat: 4K TPM por cuenta en `gpt-5.6-luna`; plan de reparto aplicado (parejas/tríos con un solo agente) y respaldo `gpt-5-mini` visible (Pablo)
- [ ] Document Intelligence: Studio analiza el documento ficticio con una cuenta `labNN` (Bloque C) y la demo en vivo con `03-comprobante-compra.pdf` (Receipt) está ensayada o con Plan B lista (Valentina)
- [ ] Acceso condicional: grupo exento o probado desde red de invitados de Microsoft Chile (Admin del tenant)
- [ ] Presupuesto y alertas creados; etiquetas aplicadas (Admin del tenant)
- [ ] Grabación y transcripción de Teams verificadas (Robert)

### Día 2 (adicional)
- [ ] ★ Índice de Search accesible por cuenta de prueba con *Search Index Data Reader* (Valentina)
- [ ] ★ Agente Python de inicio ejecuta localmente con `AzureCliCredential`/`DefaultAzureCredential` en 3 equipos distintos (Pablo)
- [ ] ★ Trazas visibles en el portal con cuenta de prueba (*Log Analytics Reader*) (Pablo)
- [ ] `FOUNDRY_MODEL` y `FOUNDRY_EMBEDDING_MODEL` entregados en el `.env` y coinciden con los despliegues (Pablo)
- [ ] Caso de fallo del lab disponible y probado (Valentina)
- [ ] Respaldo Codespaces/devcontainer probado (Valentina)
- [ ] Cuota de `gpt-5-mini` (y de embeddings) revisada tras el día 1 (Pablo)

### Día 3
- [ ] Sin dependencia de nube; revisar acceso a Teams y materiales (Robert)

**No-Go / degradación:** si un ítem ★ falla y no se corrige en 15 min, pasar a **modo demo guiado** de ese bloque (instructor presenta; participantes siguen por Teams/sala) y registrar la incidencia en el registro de riesgos del runbook.

---

## 16. Decisiones y confirmaciones pendientes con BCI

| # | Pregunta | Por qué importa | Recomendación |
|---|---|---|---|
| 1 | ¿Quién provisiona el entorno? | **Resuelto en el entorno real:** aprovisionado en el tenant del evento con los scripts de `provisionamiento\`; el límite de ~16 sesiones no aplica (ver 3.5). Quién lo administra durante el taller: *por confirmar* | Confirmar contacto técnico |
| 2 | Suscripción, tenant y rol del administrador | Define permisos y plazos | Owner/Contributor en RG |
| 3 | Región y nivel de cuota de la suscripción | Define si alcanzan las cuotas de `gpt-5.6-luna` (62 × 4K = 248K TPM), `gpt-5-mini` y embeddings | East US 2; consultar nivel |
| 4 | ¿Red pública con Entra/RBAC o red privada? | Impacta el acceso de 27 remotos | Pública |
| 5 | Acceso condicional / dispositivos conformes | Bloqueo de asistentes | Exclusión temporal del grupo (con MFA) |
| 6 | Lista de salida a internet (egress) | El lab depende de portales, PyPI, GitHub | Validar la lista de 10.2 |
| 7 | Lenguaje del lab pro-code | Python (por defecto) vs .NET | Python 3.13 (3.14 aún no está soportado) |
| 8 | ¿GitHub/Codespaces habilitado en equipos BCI? | Alternativa para equipos restringidos | Probar el día antes |
| 9 | Funciones en vista previa (trazas de agentes no hospedados, evaluaciones, monitoreo, *agentic retrieval*) | Disponibilidad por región/modelo/SDK | Verificar con cuenta de prueba; tener demo Plan B |
| 10 | ¿Quién monitorea el chat de Teams mientras el otro expone? | Pregunta abierta de la propuesta | Robert como monitor de Teams (ver runbook) |
| 11 | Presupuesto máximo del evento y fecha de eliminación | Controles de costo | Definir monto; 26-oct |
| 12 | Política de grabación y almacenamiento | Entregable (grabación, repo, presentaciones) | Solo contenido ficticio |
| 13 | Modelo principal del Día 1 `gpt-5.6-luna`: **Agent Service + file search no probado**, registro de acceso y cuota (4K TPM por cuenta, `429` reales) | Si falla con una cuenta de participante hay que usar el respaldo `gpt-5-mini` | Probar hoy con una cuenta `labNN`; respaldo `gpt-5-mini` (predesplegado) |
| 14 | ¿La autenticación local de Application Insights está deshabilitada? | Define si los participantes necesitan *Monitoring Metrics Publisher* | Preguntar al administrador |
| 15 | ¿Qué recurso de Document Intelligence usa cada cuenta `labNN` en Studio, y con qué rol? | **Resuelto:** su propia cuenta Foundry, con *Cognitive Services User* asignado sobre ella (`participante.bicep` / `Add-RolCognitiveServicesUser.ps1`) | Confirmar en T-1 que el Studio abre con una cuenta `labNN` |
| 16 | ¿Quién reemite los TAP durante el taller y por qué canal se entregan? | El TAP del Día 1 vence a las 14:30 del 21-oct; sin TAP no hay acceso (MFA) | Definir responsable y canal (`<CANAL-ENTREGA-TAP>`) |

---

## 17. Mapa de scripts

| Script | Propósito | Ejecuta |
|---|---|---|
| `scripts\00_prerequisitos.ps1` | Verifica `az login`, suscripción, proveedores de recursos y muestra comandos de consulta de cuota (solo lectura) | Admin / Pablo |
| `scripts\01_crear_grupo_y_roles.ps1` | Asigna roles al grupo Entra (parametrizado; `-WhatIf`); incluye *Log Analytics Reader* (`-LogAnalyticsWorkspaceName`), *Monitoring Metrics Publisher* (condicional: `-AppInsightsSinAuthLocal`) y *Storage Blob Data Contributor* (opcional: `-StorageProyecto`) | Admin |
| `scripts\02_validar_entorno.py` | Validación de solo lectura (PASS/FAIL, sin filtrar secretos; `--dry-run`); comprueba además `gpt-5.6-luna` como verificación **no fatal** (WARN si falta) | Pablo / Valentina con cuenta de prueba |
| `provisionamiento\Add-RolCognitiveServicesUser.ps1` | Asigna *Cognitive Services User* a cada `labNN`/`instNN` sobre su cuenta Foundry en el entorno ya desplegado (idempotente; `-WhatIf`; usa `rol-cognitive-services-user.bicep`) | Admin / Pablo |
| `scripts\03_limpieza.ps1` | Elimina el RG y purga cuentas (requiere `-ConfirmarEliminacion`; `-WhatIf`) | Admin |
| `scripts\04_infra_referencias.md` | Rutas a las plantillas Bicep/Terraform oficiales y fragmentos de CLI | Admin |

> **NO EJECUTAR EN PRODUCCIÓN.** Los scripts son para la suscripción del laboratorio. Ninguno fue ejecutado por Microsoft antes de entregarlos; revísalos con `-WhatIf`/`--dry-run`.

---

## 18. Alineación con los labs

Qué espera cada lab de este entorno (kits ya terminados en `laboratorios\dia1-lab-guiado`, `dia2-lab-procode` y `dia3-workshop-arquitectura`). Los nombres de despliegue se comunican a los participantes con el `.env` del día 2 y, el día 1, de viva voz al inicio. Si un lab cambia, esta tabla manda para el entorno.

### 18.1 Día 1 — lab guiado en el portal (L100)

| Qué espera el lab | Valor en este entorno | Ver |
|---|---|---|
| Portal | `https://ai.azure.com` con **New Foundry** activado; inicio de sesión con `labNN@mngenvmcap219366.onmicrosoft.com` + **TAP** | README del lab §4.2 y Bloque A |
| Proyecto | Cuenta Foundry + proyecto `lab-NN` por participante (grupo de recursos `rg-bci-lab-NN`); las parejas/tríos comparten **un solo agente**; los participantes no crean proyectos | 3.5 |
| Despliegue de chat | `gpt-5.6-luna` (principal; 4K TPM) y `gpt-5-mini` (respaldo; 10K TPM), predesplegados | 5.2 |
| Herramientas del equipo | VS Code, Python 3.13, Git, Azure CLI (`winget`), Foundry Toolkit for VS Code; `az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc` | README del lab §4.1 y Bloque A |
| Herramienta del agente | File Search con 4 documentos ficticios (`datos\politicas-internas\`) | 6.1 |
| Document Intelligence | Studio con Entra ID sobre la cuenta Foundry del participante; modelos Invoices y Layout (Bloque C) y Receipt en la demo en vivo; rol *Cognitive Services User* (asignado) | 8.1 |
| Voz y avatar | **Eliminados** del laboratorio (sin demo, sin Speech/Voice Live/`gpt-realtime`) | 8.2 |
| Roles | *Foundry User* + *Reader* (RG) y *Cognitive Services User* (cuenta Foundry), asignados por el aprovisionamiento; *Storage Blob Data Contributor* si la subida da 403 | 6.1 |
| Red | `ai.azure.com`, `documentintelligence.ai.azure.com`, `contentunderstanding.ai.azure.com`; cookies de terceros permitidas | 10.2 |

### 18.2 Día 2 — lab pro-code en Python (L200)

| Variable del `.env` | Qué es | Valor en este entorno |
|---|---|---|
| `FOUNDRY_PROJECT_ENDPOINT` (alias `AZURE_AI_PROJECT_ENDPOINT`) | Endpoint del proyecto del participante | `https://<recurso>.services.ai.azure.com/api/projects/<proyecto>` (tabla participante → proyecto) |
| `FOUNDRY_MODEL` (alias `AZURE_AI_MODEL_DEPLOYMENT_NAME`) | **Nombre del deployment** de chat (no del modelo) | `gpt-5-mini` (predesplegado, 10K TPM por cuenta). `gpt-5.6-luna` (4K TPM) como alternativa: su uso con los flujos del Día 2 no está probado (*por confirmar*). `gpt-4.1-mini` no está predesplegado |
| `FOUNDRY_EMBEDDING_MODEL` | Nombre del deployment de embeddings; vacío = índice solo texto (Plan B) | `text-embedding-3-small` |
| `AZURE_SEARCH_ENDPOINT` | Endpoint del servicio de Search | `https://<search>.search.windows.net` (Basic o superior, ranker semántico, RBAC o «Ambos») |
| `AZURE_SEARCH_INDEX_NAME` | Índice que consulta el agente | `normativa-austral` (lo crean los instructores con `src\01_crear_indice.py`; 12 documentos) |
| `APPLICATIONINSIGHTS_CONNECTION_STRING` | Trazas (opcional: si está vacío, el lab la obtiene del proyecto) | Application Insights conectado al proyecto; no la compartas por chat |

Otras variables del lab: `LAB_NIVEL_USUARIO` (`publico`, `interno` o `restringido`), `ENABLE_CONSOLE_EXPORTERS`, y las banderas del Plan B `LAB_SIN_SEMANTICO` y `LAB_APPINSIGHTS_ENTRA`. `scripts\02_validar_entorno.py` lee estos mismos nombres.

**Roles requeridos por el lab del Día 2** (`laboratorios\dia2-lab-procode\guia-facilitador.md` §1.2):

| Quién | Ámbito | Rol |
|---|---|---|
| Participantes | Recurso Foundry / proyecto | **Foundry User** |
| Participantes | Servicio de Azure AI Search | **Search Index Data Reader** |
| Participantes | Application Insights / workspace conectado | **Log Analytics Reader** (+ *Privileged Monitoring Data Reader* si las tablas están protegidas) |
| Participantes | Application Insights conectado | **Monitoring Metrics Publisher**, solo si la autenticación local está deshabilitada (`LAB_APPINSIGHTS_ENTRA=true`) |
| Instructores | Servicio de Search | **Search Service Contributor** + **Search Index Data Contributor** |
| Instructores | Proyecto de Foundry | **Foundry User** (o *Contributor* para crear despliegues; aquí lo cubre *Foundry Owner*) |
| Instructores (demo de agente hospedado) | Grupo de recursos / ACR / proyecto | **Contributor** + permiso para asignar roles; la identidad del agente necesita *Search Index Data Reader* |

### 18.3 Día 3 — taller de arquitectura (L300)

Sin entorno en la nube: solo Teams y las presentaciones.

---

## 19. Fuentes

Rutas relativas a `BCI-Foundry-Workshop\`. Dentro del cuerpo del documento, las rutas abreviadas (p. ej. `how-to\quota.md`, `agents\...`, `concepts\...`, `openai\...`) son relativas a `docs-oficiales\foundry\`.

**Contexto del evento**
- `MATERIALS_INDEX.md` (§4 Entorno de laboratorio; §6 Gaps)
- `presentaciones\content\day1.json`, `presentaciones\content\day2.json`

**Kits de laboratorio ya terminados (solo lectura)**
- Día 1: `laboratorios\dia1-lab-guiado\README.md` (§4.1 pre-trabajo, §4.2 prerrequisitos), `guia-facilitador.md`, `checklist-validacion.md`, `datos\prompts.md`, `demo-document-intelligence.md`
- Día 2: `laboratorios\dia2-lab-procode\README.md`, `guia-facilitador.md` (§1.1 preparación, §1.2 roles), `.env.example`, `src\config.py`, `src\00_verificar_entorno.py`, `src\01_crear_indice.py`
- Día 3: `laboratorios\dia3-workshop-arquitectura\` (sin entorno en la nube)

**Documentación oficial (copias locales)**
- `docs-oficiales\foundry\concepts\planning.md` (topología, aislamiento)
- `docs-oficiales\foundry\how-to\create-projects.md` (CLI, múltiples proyectos)
- `docs-oficiales\foundry\concepts\rbac-foundry.md` (roles, GUID, grupos Entra)
- `docs-oficiales\foundry\concepts\administrator-guide.md` (roles del administrador, purga)
- `docs-oficiales\foundry\agents\environment-setup.md` (Básico/Estándar, roles)
- `docs-oficiales\foundry\agents\concepts\hosted-agent-permissions.md` (roles de MI, telemetría, ACR)
- `docs-oficiales\foundry\agents\concepts\limits-quotas-regions.md` (regiones, herramientas por modelo, límites)
- `docs-oficiales\foundry\agents\concepts\networking-options.md`, `agents\faq.md` (red)
- `docs-oficiales\foundry\agents\how-to\tools\ai-search.md`, `agents\how-to\foundry-iq-connect.md` (Search + agentes)
- `docs-oficiales\foundry\foundry-models\quotas-limits.md`, `docs-oficiales\foundry\how-to\quota.md`, `docs-oficiales\foundry\openai\how-to\quota.md` (unidad en miles de TPM, Usages API y capacidades por modelo), `docs-oficiales\foundry\openai\quotas-limits.md` (niveles de cuota)
- `docs-oficiales\foundry\foundry-models\concepts\deployment-types.md`, `models-sold-directly-by-azure-region-availability.md`, `models-sold-directly-by-azure.md` (capacidades de `gpt-5-mini`)
- `docs-oficiales\foundry\openai\how-to\reasoning.md` (tokens de razonamiento); `docs-oficiales\foundry\agents\how-to\tools\file-search.md` (prerrequisitos de File Search)
- `docs-oficiales\foundry\foundry-models\how-to\create-model-deployments.md`
- `docs-oficiales\foundry\concepts\manage-costs.md` (costos)
- `docs-oficiales\foundry\observability\how-to\trace-agent-setup.md` (trazas)
- `docs-oficiales\azure-ai-search\get-started-portal-agentic-retrieval.md`, `search-get-started-rbac.md`, `search-get-started-bicep.md`
- `docs-oficiales\ai-services-document-intelligence\service-limits.md`
- Provisionamiento real (solo lectura): `laboratorios\entorno-y-facilitacion\provisionamiento\` (`Provision-Lab.ps1`, `Add-Modelo.ps1`, `participante.bicep`, `compartido.bicep`)
- Ejercicio público de Microsoft Learn para los prerrequisitos del Bloque A: `https://microsoftlearning.github.io/mslearn-ai-agents/Instructions/Exercises/02-agent-custom-tools.html#prerequisites`; instalación de Azure CLI: `https://learn.microsoft.com/cli/azure/install-azure-cli`

**Repositorios**
- `repos\publico-samples\foundry-samples\infrastructure\infrastructure-setup-bicep\` (`40-basic-agent-setup`, `41-standard-agent-setup`, `15-private-network-standard-agent-setup`, `18-managed-virtual-network`, `deployment-tools\preflight`, `deployment-tools\cleanup`; valores por defecto del modelo en `40-basic-agent-setup\main.bicep`)
- `repos\internal\foundry-launchpad\INFRA.md`
- `repos\publico-workshops\agentic-ai-lab\infrastructure\readme.md`
- `repos\publico-workshops\foundry-hosted-agents-workshop\` (`.env.example`, `.workshop\scripts\preflight.py`, `.workshop\docs\steps\`)
- `repos\microsoftlearning-labs\mslearn-agent-quickstart\Instructions\Labs\`
- `repos\microsoftlearning-labs\mslearn-ai-information-extraction\Instructions\Exercises\03-document-intelligence.md`
- Variables de entorno, índice y roles del lab del Día 2 (solo lectura, ya existente en el repositorio): `laboratorios\dia2-lab-procode\.env.example`, `laboratorios\dia2-lab-procode\src\config.py`, `laboratorios\dia2-lab-procode\src\01_crear_indice.py`.

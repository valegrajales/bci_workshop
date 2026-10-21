# Laboratorio Día 2 — Agente pro-code con grounding y herramientas (versión Codespaces)

**Microsoft AI Foundry BCI Training Day · Día 2 · Jueves 22 de octubre de 2026 · Nivel L200**

**Laboratorio de 85 minutos (11:15 – 12:40, hora de Chile) · Instructores: Pablo Braconi y Valentina Grajales**

> Todo el escenario es ficticio: **Austral Bank** no existe y los documentos, estados y cifras de este kit se
> inventaron para el taller. No hay datos reales de BCI ni llaves o secretos: la autenticación usa
> **Microsoft Entra ID** (`az login` + `DefaultAzureCredential`).

> **¿Por qué esta versión?** Las librerías del laboratorio (Microsoft Agent Framework, `azure-ai-projects` 2.x,
> `azure-monitor-opentelemetry`, `pydantic` 2.14...) exigen **Python 3.10 o superior**; con **Python 3.9 no se pueden instalar**.
> Esta carpeta es idéntica en tareas y código a `dia2-lab-procode`, pero se ejecuta en **GitHub Codespaces**: el
> contenedor trae **Python 3.12** ya configurado, así que **no importa qué Python tengas instalado en tu equipo** (solo necesitas
> un navegador y una cuenta de GitHub). Si ya tienes Python 3.10+ local puedes usar la carpeta `dia2-lab-procode`.

---

## 1. Objetivo

Al terminar este laboratorio habrás construido, en Python, un **asistente de normativa interna** que:

1. Es un **agente pro-code** creado con Microsoft Agent Framework sobre un modelo desplegado en tu proyecto de Microsoft Foundry.
2. Responde con **grounding empresarial**: recupera fragmentos de la normativa de Austral Bank desde **Azure AI Search** (búsqueda híbrida con filtro de acceso) y **cita la fuente**.
3. Usa una **herramienta propia** (`consultar_estado_solicitud`) que devuelve el estado de una solicitud ficticia.
4. Queda listo para observarse y evaluarse: el módulo "Observabilidad y ciclo de vida" del Día 3 presenta de forma conceptual cómo se leen las trazas, se diagnostica una falla y se valida un checklist de éxito sobre un agente como el que construyes hoy.

```
Tu Codespace (Python 3.12)                        Azure
┌──────────────────────────────┐   Entra ID   ┌────────────────────────────────────┐
│  Agent (Agent Framework)     │ ───────────► │ Proyecto de Foundry: modelo de chat│
│   ├─ tool buscar_normativa ──┼────────────► │ Azure AI Search: índice normativa  │
│   └─ tool consultar_estado   │              │   (texto + vector + semántico)     │
│  data/solicitudes.json       │              └────────────────────────────────────┘
└──────────────────────────────┘
```

## 2. Cronograma (85 min)

| Hora (Chile) | Bloque | Duración | Qué haces | Entregable |
|---|---|---|---|---|
| 11:15 – 11:25 | **Preparación del entorno** | 10 min | abrir el Codespace, `az login`, `.env`, verificación de conexión, agente base respondiendo | Entorno listo y `00_verificar_entorno.py` en verde |
| 11:25 – 11:55 | **Tareas 1 y 2** | 30 min | Agente base (≈10 min) + grounding con Azure AI Search, security trimming y citas (≈20 min) | Respuesta con contexto del índice y una cita verificable |
| 11:55 – 12:20 | **Tarea 3** | 25 min | Herramienta propia `consultar_estado_solicitud` adjunta al agente, con prueba de cuándo debe y cuándo no debe usarse | Al menos una llamada exitosa a la tool |
| 12:20 – 12:40 | **Revisión en parejas y preguntas técnicas** | 20 min | Comparar tu agente con el de otro participante, resolver dudas con el instructor | Agente con grounding (T1–T2) y tool (T3) funcionando |

Si te atrasas, **pide ayuda temprano**: lo mínimo esperable al final es *un agente que responde con grounding y una tool funcionando*.
Hay una solución de cada tarea en `solutions/` (úsala solo para comparar) para que no te quedes bloqueado.

## 3. Qué contiene el kit

```
dia2-lab-procode-codespaces/
├─ README.md                  Esta guía
├─ requirements.txt           Dependencias (rangos de los samples oficiales)
├─ .env.example               Plantilla de variables (copia como .env)
├─ scripts/codespaces-setup.sh   Se ejecuta solo al crear el Codespace (instala dependencias y crea .env)
├─ data/
│  ├─ normativa/              12 documentos ficticios (.md) con encabezado: id, título, área, nivel_acceso
│  ├─ solicitudes.json        10 solicitudes ficticias para la herramienta
│  └─ preguntas_evaluacion.jsonl   Preguntas de prueba (extensión opcional)
├─ src/                       Starters: aquí trabajas (marcas TODO)
│  ├─ 00_verificar_entorno.py     Revisa Python, paquetes, .env, credencial e índice (no imprime secretos)
│  ├─ 02_agente_base.py           Tarea 1
│  ├─ 03_agente_con_search.py     Tarea 2
│  ├─ 04_herramienta_estado.py    Tarea 3
│  └─ config.py, normativa.py, solicitudes.py, busqueda.py, agente_lab.py ...   Módulos de apoyo (más material de observabilidad de los instructores que no se usa en este laboratorio)
├─ solutions/                 Versiones completas de las Tareas 1 a 3 (úsalas solo si te atascas)
└─ tests/                     Pruebas locales (pytest) de las partes que no usan Azure
```

> La configuración del contenedor está en `.devcontainer/dia2-lab-procode-codespaces/devcontainer.json` (raíz del repositorio): imagen Python 3.12 + Azure CLI.

> El índice de Azure AI Search **ya fue creado por los instructores** (`01_crear_indice.py`): tú solo lo consultas.
> Si quieres crear el tuyo, mira el recuadro opcional al final de la Tarea 2.

## 4. Prerrequisitos

| Requisito | Detalle |
|---|---|
| Cuenta de GitHub | Cualquier cuenta (gratuita basta). El repositorio es público: Codespaces creará el entorno desde tu cuenta |
| Navegador | Edge o Chrome actualizado (o VS Code con la extensión *GitHub Codespaces*) |
| Python y Azure CLI | **No hace falta instalar nada**: el Codespace trae Python 3.12 y Azure CLI. Tu Python local (incluido 3.9) no se usa |
| Cuota de Codespaces | La cuenta gratuita incluye **120 core-horas/mes**; el Codespace de 2 núcleos consume 2 por hora real (≈ 60 h): sobra para los 85 min del laboratorio. **Detén o elimina el Codespace al terminar** |
| Cuenta del taller | `labNN@...` y el **TAP** del día (te los entregan los instructores) para `az login` |
| Proyecto de Foundry | Endpoint del proyecto y **nombre del deployment** de chat (te los entregan los instructores) |
| Azure AI Search | Endpoint del servicio y nombre del índice (`normativa-austral`) |
| Permisos (Entra ID) | Rol **Foundry User** (antes *Azure AI User*) en el proyecto y **Search Index Data Reader** en el servicio de Search |
| Red | Salida a `*.github.dev`, `github.com`, `*.services.ai.azure.com`, `*.search.windows.net`, `login.microsoftonline.com` y `login.microsoft.com` (equipos corporativos con proxy: pide a TI habilitar Codespaces) |

## 5. Preparación del entorno (10 min)

Los comandos son para el **terminal del Codespace (bash, Linux)**: rutas con `/`. No necesitas crear un entorno virtual.

**5.1 Abre el Codespace**

1. Entra al repositorio `valegrajales/bci_workshop` en GitHub → botón verde **Code** → pestaña **Codespaces** → **Create codespace on main** (o `…` → *New with options* si necesitas elegir la rama; deja la máquina de **2-core**). Si no tienes permisos de escritura, el Codespace se crea igual desde el repositorio público; GitHub solo crea o enlaza un *fork* tuyo si luego haces commit o push (no lo necesitas en este laboratorio).
2. Espera 2–4 min la primera vez: el contenedor instala Python 3.12 y las dependencias (`requirements-dev.txt`) automáticamente y abre este README en el editor del navegador.
3. Abre un terminal (menú **Terminal → Nuevo terminal**) y confirma:

```bash
pwd                  # .../laboratorios/dia2-lab-procode-codespaces
python --version     # Python 3.12.x
```

> Si el terminal no está en la carpeta del laboratorio: `cd /workspaces/*/laboratorios/dia2-lab-procode-codespaces`.
> Si la instalación de dependencias no terminó o falló: `pip install -r requirements-dev.txt`.

**5.2 Inicia sesión en Azure (sin llaves)**

En el Codespace no hay navegador local, así que usa el **código de dispositivo** con tu cuenta del taller y el TAP:

```bash
az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc
az account set --subscription "<id-o-nombre-de-la-suscripción>"   # si los instructores lo indican
```

Abre `https://microsoft.com/devicelogin`, escribe el código que muestra el terminal y entra con `labNN@...` y tu TAP.
Si ves `AADSTS50079`/`AADSTS50076`, no estás usando el TAP.

**5.3 Configura tu `.env`**

El Codespace ya creó `.env` a partir de `.env.example`. Ábrelo (`code .env`) y completa los valores; si no existe: `cp .env.example .env`.

Completa solo estas variables con los valores que te entregan los instructores (sin comillas):

| Variable | Qué es |
|---|---|
| `FOUNDRY_PROJECT_ENDPOINT` | Portal de Foundry → tu proyecto → *Overview* → *Project endpoint* (`https://<recurso>.services.ai.azure.com/api/projects/<proyecto>`) |
| `FOUNDRY_MODEL` | Nombre del **deployment** de chat (no el nombre del modelo) |
| `AZURE_SEARCH_ENDPOINT` | `https://<servicio>.search.windows.net` |
| `AZURE_SEARCH_INDEX_NAME` | `normativa-austral` (ya viene en la plantilla) |
| `FOUNDRY_EMBEDDING_MODEL` | Deployment de embeddings; déjalo vacío si los instructores indican "índice solo texto" |
| `LAB_NIVEL_USUARIO` | `interno` (simula tu nivel de acceso; lo usarás en la Tarea 2) |

> `.env` está en `.gitignore`. No lo compartas ni lo subas a un repositorio.

**5.4 Verifica la conexión**

```bash
python src/00_verificar_entorno.py
```

Salida esperada (ejemplo; las versiones pueden variar):

```
[1] Python y paquetes
 ✔ Python                             3.12.x (se requiere 3.10+; recomendado 3.11+)
 ✔ agent-framework-foundry            1.14.x
 ...
[2] Variables de entorno (.env)
 ✔ FOUNDRY_PROJECT_ENDPOINT           https://<recurso>.services.ai.azure.com
 ✔ FOUNDRY_MODEL                      <deployment>
 ...
[3] Credencial de Microsoft Entra ID (DefaultAzureCredential)
 ✔ Token Foundry (ai.azure.com)       obtenido
 ✔ Token Azure AI Search              obtenido
[4] Índice de Azure AI Search (lectura)
 ✔ Índice normativa-austral           46 fragmentos
Entorno listo ✔
```

**5.5 Agente base sin herramientas (valida el modelo)**

```bash
python src/00_verificar_entorno.py --probar-modelo
```

Debe agregar `✔ Deployment <nombre>  respondió: OK`. Si falla aquí, el problema es de **entorno o permisos**, no de tu código:
resuélvelo ahora (ver [Troubleshooting](#8-troubleshooting)).

✅ **Checkpoint 0** — todo en verde (✔) y `Entorno listo ✔`. Ya puedes empezar con las tareas.

---

## 6. Tareas

En cada tarea editas un archivo de `src/` buscando las marcas **`TODO`**. Los comentarios te dicen qué escribir.

### Tarea 1 — Agente base con Agent Framework (≈10 min)

**Objetivo:** un agente en Python con modelo, instrucciones y sesión, sin herramientas todavía.

Abre `src/02_agente_base.py` y completa:

| TODO | Qué hacer |
|---|---|
| 1.1 | Crear el cliente: `FoundryChatClient(project_endpoint=s.project_endpoint, model=s.model, credential=credential)` |
| 1.2 | Escribir las `INSTRUCCIONES`: rol (asistente de normativa de Austral Bank), idioma español, tono breve y "si no sabes, dilo" |
| 1.3 | Crear el agente: `Agent(client=client, name="asistente-normativa", instructions=INSTRUCCIONES)` |

```bash
python src/02_agente_base.py
```

Salida esperada (ejemplo; el texto del modelo varía):

```
> ¿Qué es el KYC en un banco?
KYC (Know Your Customer) es el proceso con el que un banco identifica y verifica a sus clientes ...

> ¿Cuál es el límite mensual de gasto con tarjeta corporativa para el nivel Jefatura de Austral Bank?
No tengo información sobre ese límite. Te sugiero consultar la normativa interna ...

> ¿Y para el nivel Gerencia?
(la sesión recuerda la pregunta anterior: sigue hablando del límite de tarjeta corporativa)
```

✅ **Checkpoint 1** — responde en español, mantiene el contexto entre preguntas y **no inventa** el límite de Austral Bank
(no tiene acceso a la normativa; por eso necesitamos grounding).

### Tarea 2 — Grounding con Azure AI Search (≈20 min)

**Objetivo:** que el agente responda **solo** con la normativa del índice y **cite** el fragmento usado.

El grounding se implementa como una **herramienta** (`buscar_normativa`) que el modelo decide invocar. Así, cada
recuperación queda registrada como una llamada a tool explícita (la línea `búsqueda realizada`). Para una pregunta con dos partes, el modelo hace
**dos búsquedas** (recuperación agéntica a nivel de agente).

Abre `src/03_agente_con_search.py` y completa:

| TODO | Qué hacer |
|---|---|
| 2.1 | Construir el filtro de acceso: `construir_filtro_acceso(cargar_settings().nivel_usuario)`. **El nivel sale de tu sesión, nunca de un parámetro que decida el modelo** (security trimming) |
| 2.2 | Llamar `await busqueda.buscar(consulta, filtro)`, registrar con `reg.registrar(...)` y devolver `formatear_resultados(fragmentos)`. Borra el `raise NotImplementedError` |
| 2.3 | Instrucciones con 3 reglas: usar **siempre** `buscar_normativa` para normas, límites y plazos; **citar** como `[NOR-001-02]` solo ids devueltos por la tool; si no hay evidencia responder *"No tengo información en la normativa disponible para tu nivel de acceso"* |
| 2.4 | Pasar la herramienta al agente: `TOOLS = [buscar_normativa]` |

**Checkpoint intermedio (sin modelo de lenguaje):** prueba la herramienta sola.

```bash
python src/03_agente_con_search.py --solo-tool
```

```
Nivel de acceso simulado del usuario: interno
[NOR-001-02] Política de límites de gasto corporativo › Límites mensuales por nivel de cargo (nivel: interno)
El límite mensual de gasto con tarjeta corporativa depende del nivel de cargo:
- Nivel Jefatura: 2.500 USD por mes.
...
```

Luego ejecuta el agente completo:

```bash
python src/03_agente_con_search.py
```

Salida esperada (ejemplo):

```
> ¿Cuál es el límite mensual de gasto con tarjeta corporativa para el nivel Jefatura?
El límite mensual para el nivel Jefatura es de 2.500 USD [NOR-001-02].
   · búsqueda realizada: límite mensual tarjeta corporativa Jefatura

> ¿Cuál es el límite de gasto por noche en un viaje nacional y por cuántos años debo conservar los comprobantes de la rendición?
En viajes nacionales el límite es de 350 USD por noche [NOR-002-01]; los comprobantes se conservan 6 años [NOR-004-01].
   · búsqueda realizada: límite de gasto por noche viaje nacional
   · búsqueda realizada: plazo de retención de comprobantes de rendición

> ¿Quién aprueba un crédito a una empresa por 3.000.000 USD?
No tengo información en la normativa disponible para tu nivel de acceso ...

> ¿Cuántos días de vacaciones legales tengo al año?
No tengo información en la normativa disponible ...
```

Observa estas cuatro cosas:

1. **Pregunta simple:** una búsqueda y una cita.
2. **Pregunta compuesta:** **dos** búsquedas (dos subconsultas) y dos citas. Si hace una sola, revisa la regla 1 de tus instrucciones.
3. **Crédito de 3.000.000 USD:** el documento existe (NOR-007), pero es `restringido` y tu nivel es `interno`: el filtro lo oculta.
   Prueba cambiar `LAB_NIVEL_USUARIO=restringido` en tu `.env` y vuelve a ejecutar: ahora responde *Comité de Crédito Central* `[NOR-007-xx]`.
   Devuélvelo a `interno` al terminar. Eso es **security trimming**.
4. **Fuera del corpus:** debe negarse a responder en vez de inventar.

✅ **Checkpoint 2** — al menos una respuesta con contexto del índice y una **cita verificable** (el id existe en `data/normativa/`).

<details>
<summary>Opcional: crear tu propio índice (solo si tienes permisos de contribuidor en el servicio de Search)</summary>

Los instructores ya crearon `normativa-austral`; **no necesitas** hacer esto. Si quieres ver cómo se arma un índice con campos de
texto (analizador español), campo vectorial, configuración semántica y filtro por `nivel_acceso`:

```bash
python src/01_crear_indice.py --dry-run                      # solo valida los documentos (no usa Azure)
python src/01_crear_indice.py --indice normativa-<tu-inicial> # requiere Search Service Contributor + Search Index Data Contributor
```

Luego cambia `AZURE_SEARCH_INDEX_NAME` en tu `.env`. Si no hay deployment de embeddings, agrega `--sin-vectores`.
</details>

### Tarea 3 — Implementa y prueba una herramienta propia (25 min)

**Objetivo:** que el agente use `consultar_estado_solicitud` cuando el usuario da un identificador `SOL-AAAA-NNNN`
y **no** la use para preguntas sobre normas. Los datos están en `data/solicitudes.json` (ficticios).

> El modelo **solo ve el nombre, la descripción y los parámetros** de la herramienta. Una buena descripción es la
> diferencia entre una tool bien usada y una tool llamada de más, de menos o con argumentos incorrectos.

Abre `src/04_herramienta_estado.py` y completa:

| TODO | Qué hacer |
|---|---|
| 3.1a | Describir el parámetro `id_solicitud`: formato **exacto** `SOL-AAAA-NNNN` y un ejemplo |
| 3.1b | Docstring de la tool: qué hace (estado, fecha y responsable de **una** solicitud), cuándo usarla y cuándo **no** |
| 3.1c | Llamar `consultar_estado(id_solicitud)`, registrar con `reg.registrar(..., ok=resultado["encontrada"])` y devolver `json.dumps(resultado, ensure_ascii=False)`. Borra el `raise NotImplementedError` |
| 3.2 | Entregar ambas herramientas al agente: `TOOLS = [buscar_normativa, consultar_estado_solicitud]` |

**Checkpoint intermedio (sin modelo, sin Azure):**

```bash
python src/04_herramienta_estado.py --solo-tool
```

```
SOL-2026-0003 -> {"encontrada": true, "id": "SOL-2026-0003", "tipo": "Destrucción de documentos", "estado": "En revisión", "fecha": "2026-10-12", "responsable": "Área Legal"}
12345 -> {"encontrada": false, "error": "formato_invalido", "mensaje": "'12345' no tiene el formato SOL-AAAA-NNNN (ej.: SOL-2026-0003)."}
```

Con el agente:

```bash
python src/04_herramienta_estado.py
```

Salida esperada (ejemplo):

```
> ¿En qué estado está la solicitud SOL-2026-0003?
La solicitud SOL-2026-0003 (Destrucción de documentos) está En revisión desde el 2026-10-12; la gestiona el Área Legal.
   · tools usadas: ['consultar_estado_solicitud']

> ¿Cuál es el plazo de revisión de una solicitud interna?
El plazo de revisión es de 3 días hábiles [NOR-011-02].
   · tools usadas: ['buscar_normativa']

> ¿En qué estado está la solicitud SOL-2026-0006 y cuánto suele demorar ese estado?
...   · tools usadas: ['consultar_estado_solicitud', 'buscar_normativa']

> Consulta el estado de la solicitud 12345.
El identificador "12345" no es válido; debe tener el formato SOL-AAAA-NNNN ...
```

Preguntas para pensar mientras pruebas: ¿la tool se llamó cuando **no** debía? ¿Qué cambió en la respuesta al
mejorar la descripción? El error `formato_invalido` vuelve **al modelo** como dato (no como excepción): así puede explicarle al usuario.

**Experimento de contraste (≈5 min):** con la tool ya funcionando, vuelve el docstring (TODO 3.1b) a una frase vaga
(p. ej. *"Consulta solicitudes"*) y repite las cuatro preguntas de arriba. Anota qué cambió en `tools usadas` (¿se llama de más, de menos o con
un argumento mal armado?) y restaura la descripción completa. Así compruebas con tu propio agente que
**el modelo solo decide con lo que dice la descripción**.

✅ **Checkpoint 3** — evidencia de **al menos una llamada exitosa** a la tool (línea `tools usadas`) y la pregunta sobre
normas **no** la dispara.

---

## 7. Criterios de éxito y entregables

| Entregable (según la lámina del laboratorio) | ¿Cómo lo compruebas? |
|---|---|
| Agente funcionando con respuesta *grounded* y una tool | Checkpoints 2 y 3 |
| Checklist de diseño completado | Marcas de abajo |

**Checklist de diseño** (marca lo que cumple tu agente):

- [ ] Las instrucciones dicen cuándo usar cada herramienta y qué hacer si no hay evidencia.
- [ ] Cada herramienta tiene nombre claro, descripción con *cuándo usar / cuándo no* y parámetros tipados con ejemplo.
- [ ] Los errores de la herramienta se devuelven como datos que el modelo puede explicar (no se pierden).
- [ ] El nivel de acceso lo decide el código/la identidad, **no** el modelo.
- [ ] Las respuestas citan el fragmento recuperado y no inventan cuando no hay información.

**Mínimo para considerar la sesión lograda:** un agente que responde con grounding y cita (Tareas 1–2) y una tool funcionando (Tarea 3).

## 8. Troubleshooting

| Síntoma | Causa probable | Qué hacer |
|---|---|---|
| `ModuleNotFoundError: agent_framework` | Dependencias sin instalar (falló el `postCreateCommand`) o Python distinto de 3.12 | `python --version` (debe ser 3.12.x) y `pip install -r requirements-dev.txt` |
| `Faltan variables de entorno: ...` | `.env` incompleto o con valores `<...>` de la plantilla | Revisa los valores del paso 5.3 (sin comillas ni `<>`) |
| `DefaultAzureCredential failed to retrieve a token` / `CredentialUnavailableError` | Sin sesión de Azure | `az login --use-device-code --tenant eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc` (y `az account set`); vuelve a ejecutar `00_verificar_entorno.py` |
| `AADSTS50079` / `AADSTS50076` al iniciar sesión | No usaste el TAP | Inicia sesión con `labNN@...` y el TAP del día |
| El Codespace no se crea / "Codespaces is disabled" | Política de GitHub de tu organización o cuenta sin cuota | Usa una cuenta personal de GitHub o pide a los instructores un plan alterno (trabajo en pareja) |
| El código de dispositivo expiró | Pasaron >15 min | Vuelve a ejecutar `az login --use-device-code ...` |
| `401` / `403` / *PermissionDenied* al llamar al modelo | Falta el rol en el proyecto | Pide el rol **Foundry User** en el proyecto; la propagación puede tardar 5–10 min |
| `404` / `DeploymentNotFound` | `FOUNDRY_MODEL` con el nombre del modelo en vez del **deployment** | Copia el nombre del deployment desde el portal de Foundry |
| `403` al consultar Search | Falta **Search Index Data Reader** o el servicio solo admite llaves de API | Pide el rol; el servicio debe permitir autenticación con Microsoft Entra ID |
| Índice no encontrado / `0 fragmentos` | Nombre de índice distinto o índice sin cargar | Revisa `AZURE_SEARCH_INDEX_NAME`; avisa a los instructores |
| Error de ranker semántico | El servicio de Search no tiene habilitado el ranker semántico | Plan B: `LAB_SIN_SEMANTICO=true` en `.env` (los instructores lo confirmarán) |
| Error de embeddings (404 en el deployment de embeddings) | `FOUNDRY_EMBEDDING_MODEL` apunta a un deployment que no existe | Déjalo vacío si el índice es "solo texto", o usa el nombre indicado por los instructores |
| El agente no usa la herramienta | Descripción ambigua, tool no incluida en `tools=[...]` o instrucciones sin la regla | Revisa TODO 2.3/2.4/3.1/3.2 y que la línea `tools usadas` muestre qué herramienta eligió el modelo |
| Respuesta sin cita | La instrucción no exige citar o la búsqueda no devolvió resultados | Revisa TODO 2.3 y ejecuta `--solo-tool` para ver qué fragmentos devuelve la búsqueda |
| `SIN_RESULTADOS` / "No tengo información" para algo que sí está en la normativa | Filtro de acceso (`LAB_NIVEL_USUARIO`) o consulta demasiado vaga | Revisa `LAB_NIVEL_USUARIO` frente al `nivel_acceso` del documento (`data/normativa/`) y prueba la consulta con `--solo-tool` |
| Caracteres raros (`âœ”`) en la consola | Codificación de la terminal | Poco probable en Codespaces (UTF-8); el kit ya fuerza UTF-8 al imprimir |
| `NotImplementedError` o `Faltan TODO por completar` | Dejaste un `TODO` sin resolver | Completa el TODO que indica el mensaje (y borra el `raise NotImplementedError`) |

## 9. Qué pasó si falla (tips de diagnóstico)

1. **Primero el entorno:** `python src/00_verificar_entorno.py --probar-modelo`. Si algo está en ✘, no sigas con código.
2. **Aísla la capa:** prueba la herramienta sola (`--solo-tool`) antes de probarla con el modelo. Si la tool falla sola, el problema no es el modelo.
3. **Mira qué hizo el agente antes de cambiar el prompt:** ¿llamó a la tool (`tools usadas` / `búsqueda realizada`)?, ¿con qué consulta?, ¿el resultado de `--solo-tool` contiene la respuesta?
4. **Un cambio a la vez** y vuelve a ejecutar: así sabes qué lo arregló.
5. **Los resultados del modelo varían** entre ejecuciones; no busques el texto idéntico a los ejemplos, sino el comportamiento (tool usada, cita, dato correcto).
6. **Si te atascas más de 3 minutos**, pide ayuda o abre `solutions/` solo para comparar el TODO que falla.

## 10. Para ir más allá (si terminas antes)

- Pregunta algo fuera de la normativa y confirma que el agente **no inventa**.
- Agrega validación extra a la herramienta (p. ej. rechazar un año distinto de 2026) y comprueba que el error vuelve al modelo como dato.
- Prueba `data/preguntas_evaluacion.jsonl` (pregunta + respuesta esperada): ejecútalas con tu agente y cuéntalas a mano; los instructores muestran cómo automatizarlo con evaluación.
- Pregunta a los instructores por: despliegue como *hosted agent*, una herramienta MCP o recuperación agéntica con una *knowledge base* (**preview**).

---

## Fuentes

Código y documentación oficial en los que se basa el kit (verifica siempre la versión vigente):

- **Microsoft Agent Framework** — samples de Python (`01-get-started`, `02-agents`, observabilidad y embeddings): [github.com/microsoft/agent-framework](https://github.com/microsoft/agent-framework) · docs: [Tools](https://learn.microsoft.com/en-us/agent-framework/agents/tools/), [Function tools](https://learn.microsoft.com/en-us/agent-framework/agents/tools/function-tools), [Observability](https://learn.microsoft.com/en-us/agent-framework/agents/observability).
- **Foundry samples** (quickstart, hosted agents con Agent Framework, `08-observability`, `11-azure-search-rag`): [github.com/microsoft-foundry/foundry-samples](https://github.com/microsoft-foundry/foundry-samples).
- **Workshop `foundry-hosted-agents-workshop`** (`travel_assistant`, de agente simple a herramientas, RAG y memoria): repositorio público de workshops de Foundry.
- **Microsoft Learn Labs — AI Agents** (`mslearn-ai-agents`, ejercicios C0–C4 y D1 *Trace your agent*).
- **Azure AI Search**: [Búsqueda híbrida](https://learn.microsoft.com/en-us/azure/search/hybrid-search-how-to-query), [Crear un índice vectorial](https://learn.microsoft.com/en-us/azure/search/vector-search-how-to-create-index), [Ranking semántico](https://learn.microsoft.com/en-us/azure/search/search-get-started-semantic), [RBAC (Entra ID)](https://learn.microsoft.com/en-us/azure/search/search-get-started-rbac); samples `Quickstart-Vector-Search` y `Quickstart-Document-Permissions-Push-API` en [azure-search-python-samples](https://github.com/Azure-Samples/azure-search-python-samples); *security trimming* a nivel de documento: [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo) (`docs/login_and_acl.md`). Recuperación agéntica / *knowledge bases*: [guía](https://learn.microsoft.com/en-us/azure/search/search-get-started-agentic-retrieval) (**preview**).
- **Foundry — observabilidad**: [Conceptos de trazas](https://learn.microsoft.com/en-us/azure/foundry/observability/concepts/trace-agent-concept), [Configurar tracing en Foundry](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-setup), [Tracing con frameworks de agentes](https://learn.microsoft.com/en-us/azure/foundry/observability/how-to/trace-agent-framework), [Telemetría de hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/configure-hosted-agent-telemetry), [Depurar un hosted agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/debug-hosted-agent).
- **Foundry — agentes y herramientas**: [Configuración del entorno y roles](https://learn.microsoft.com/en-us/azure/foundry/agents/environment-setup), [Function calling](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/function-calling), [Buenas prácticas de herramientas](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/tool-best-practice), [RAG](https://learn.microsoft.com/en-us/azure/foundry/concepts/retrieval-augmented-generation), [Embeddings](https://learn.microsoft.com/en-us/azure/foundry/openai/how-to/embeddings).
- **Evaluación de aplicaciones RAG** (extensión): [ai-rag-chat-evaluator](https://github.com/Azure-Samples/ai-rag-chat-evaluator).

> Las funcionalidades marcadas **(preview)** (p. ej. *knowledge bases* de Azure AI Search y la síntesis de respuestas) pueden cambiar y no se recomiendan para producción.
> El escenario, los documentos y los datos de este laboratorio son **ficticios**.


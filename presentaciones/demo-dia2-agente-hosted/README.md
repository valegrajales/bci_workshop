# Demo Día 2 — Un agente hosted con una tool propia

Código, contenedor y pasos de la lámina **"Demo: un agente hosted con una tool propia"** (`presentaciones\content\day2.json`).
Escenario y datos **ficticios** (Austral Bank): los topes salen de `POL-GV-001 v2.1` (`laboratorios\dia1-lab-guiado\datos\politicas-internas\politica-gastos-de-viaje.md`, sección 3).

## Qué hay en esta carpeta

| Ruta | Contenido |
|---|---|
| `src\agente-gastos-hosted\main.py` | Agente de Microsoft Agent Framework + function tool `consultar_limite_gastos`, servido con `ResponsesHostServer` (protocolo Responses, puerto 8088) |
| `src\agente-gastos-hosted\limites.py` | Datos ficticios y lógica pura de la tool (sin dependencias de Azure) |
| `src\agente-gastos-hosted\Dockerfile` | Imagen `linux/amd64` (Python 3.13 + uv, dependencias bloqueadas en `uv.lock`) |
| `src\agente-gastos-hosted\tests\` | Pruebas pytest de la lógica y del contrato de la tool |
| `azure.yaml` | Proyecto `azd`: proyecto Foundry + modelo + hosted agent en **modo contenedor** |
| `scripts\probar-local.ps1` | Hace la pregunta al agente local y muestra la llamada a la tool |
| `scripts\construir-contenedor.ps1` | `docker build` local o `az acr build` remoto |

La tool devuelve JSON `{encontrado, concepto, ambito, limite, moneda, unidad, vigente_desde, fuente}`. Topes: alojamiento nacional 90.000 CLP/noche, internacional 180 USD/noche (250 USD en Nueva York, Londres y Tokio); alimentación nacional 35.000 CLP/día, internacional 70 USD/día. Entradas inválidas devuelven un error, nunca un valor inventado.

## Requisitos

- Suscripción de Azure y rol **Foundry Project Manager** en el proyecto (o **Owner** del grupo de recursos si vas a crear el proyecto). Ver [permisos de hosted agents](https://learn.microsoft.com/en-us/azure/foundry/agents/concepts/hosted-agent-permissions).
- `azd` ≥ 1.27.1 y la extensión de agentes: `azd ext install azure.ai.agents` (`microsoft.foundry` es un metapaquete que instala el conjunto de extensiones Foundry). `azd auth login`.
- Python 3.13 y [uv](https://docs.astral.sh/uv/) para correr localmente.
- Docker Desktop **solo** si construyes la imagen localmente; por defecto `azd deploy` construye en Azure Container Registry (ACR).
- Un modelo de chat desplegado (el `azure.yaml` aprovisiona `gpt-5.4-mini`; cambia `deployments` si tu región/cuota requiere otro).

## Preparación (antes de la demo)

```powershell
cd presentaciones\demo-dia2-agente-hosted
azd auth login
azd env new demo-dia2          # nombre del entorno azd
azd provision                  # crea proyecto Foundry, modelo, ACR y Application Insights
```

Si ya tienes un proyecto Foundry, **no** uses `azd provision` ni `azd ai agent init -m .\azure.yaml -p ...` (falla con `project directory ... overlaps with template source` o `a project azure.yaml already exists`, porque esta carpeta ya es un proyecto azd). Sigue la alternativa "Proyecto Foundry existente" de la sección de despliegue, ejecutando `azd ai agent init --src ...` desde una carpeta de trabajo **fuera** de esta.

Prueba local (opcional, recomendado el día anterior):

```powershell
cd src\agente-gastos-hosted
copy .env.example .env         # completa FOUNDRY_PROJECT_ENDPOINT y AZURE_AI_MODEL_DEPLOYMENT_NAME
az login
uv run --python 3.13 python main.py      # escucha en http://localhost:8088
# en otra terminal, desde la raíz de la demo:
.\scripts\probar-local.ps1
```

Pruebas unitarias (no requieren Azure): `cd src\agente-gastos-hosted; uv run --python 3.13 pytest -q`.

## Despliegue como hosted agent (contenedor)

```powershell
azd deploy
```

`azd` construye el `Dockerfile` en ACR (build remoto), registra una **versión** del agente en Foundry Agent Service, crea su **identidad Entra** y asigna los permisos de pull de la imagen. Al terminar muestra el enlace al *playground* y el endpoint del agente. Verifica con `azd ai agent show`.

Alternativas:
- **Proyecto Foundry existente, azd construye la imagen desde el código** (flujo probado contra `bci-workshop`). Desde una carpeta de trabajo vacía y **fuera** de esta demo, con el código copiado a una subcarpeta (p. ej. `.\agente-gastos-hosted`):
  1. `azd ai agent init --no-prompt -e <env> --agent-name <nombre> --src .\agente-gastos-hosted --deploy-mode container --project-id <id-del-proyecto> --model-deployment <deployment> --protocol responses`. Genera `azure.yaml` con `docker.remoteBuild: true` y `env: AZURE_AI_MODEL_DEPLOYMENT_NAME`; no construye ninguna imagen todavía.
  2. El proyecto necesita un ACR para guardar la imagen. Para usar uno existente (en vez de que `azd provision` cree uno nuevo):
     ```powershell
     azd env set AZURE_CONTAINER_REGISTRY_ENDPOINT <acr>.azurecr.io
     azd env set AZURE_CONTAINER_REGISTRY_RESOURCE_ID <resource-id-del-acr>
     azd env set AZD_FOUNDRY_ACR_MODE existing
     azd env set AZD_FOUNDRY_ACR_PULL_ASSIGNED true
     azd env set AI_AGENT_PENDING_PROVISION ""
     ```
  3. Da al *managed identity* del proyecto el rol **AcrPull** sobre ese ACR (en registros con ABAC, *Container Registry Repository Reader*). Sin él el deploy falla con `[ImageError] Container registry authentication failed`.
  4. `azd deploy` (construye la imagen en el ACR y registra la versión) y luego `azd ai agent invoke <nombre> "<pregunta>"`.
- **Imagen ya construida** (sin build en `azd`):
  1. `.\scripts\construir-contenedor.ps1 -Registro <acr> -Tag v1` (usa `az acr build`) y el rol AcrPull del punto 3 anterior.
  2. En una carpeta de trabajo: `azd ai agent init --no-prompt -e <env> --agent-name agente-gastos-hosted --project-id <id-del-proyecto> --model-deployment <deployment> --image <acr>.azurecr.io/agente-gastos:v1 --protocol responses`.
  3. Agrega a `azure.yaml`, bajo el servicio, `env: { AZURE_AI_MODEL_DEPLOYMENT_NAME: ${AZURE_AI_MODEL_DEPLOYMENT_NAME} }` y ejecuta `azd env set AZURE_AI_MODEL_DEPLOYMENT_NAME <deployment>`.
  4. `azd deploy` y `azd ai agent invoke agente-gastos-hosted "<pregunta>"`.

  Si `azd deploy` pide `AZURE_CONTAINER_REGISTRY_ENDPOINT`, el entorno no quedó en modo "sin ACR": define `AZD_AGENT_SKIP_ACR=true` y `AZD_FOUNDRY_ACR_MODE=none` con `azd env set`.

Si `azd` indica `not logged in` o un token expirado, haz `azd auth login` o `azd config set auth.useAzCliAuth true` para usar la sesión de `az`. Ver [Deploy a hosted agent](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/deploy-hosted-agent).
- **Docker local en vez de ACR**: descomenta `docker.remoteBuild: false` en `azure.yaml`.

## Guion de la demo (los 4 pasos de la lámina)

| Paso de la lámina | Qué hacer | Resultado esperado |
|---|---|---|
| 1. Mostrar el agente corriendo como hosted agent en Foundry | `azd ai agent show` y, en el portal de Foundry, **Build → Agents → `agente-gastos-hosted`**: versión activa, protocolo `responses`, identidad del agente | Versión en estado `active` |
| 2. El usuario pregunta por su límite de gastos de viaje | `azd ai agent invoke "¿Cuánto es mi límite de alojamiento por noche en un viaje internacional a Tokio?"` (o el playground) | El agente recibe la pregunta en el endpoint hosted |
| 3. El modelo decide llamar a `consultar_limite_gastos` | `azd ai agent monitor --follow` en una segunda terminal; el playground muestra la llamada a la tool | Llamada con `concepto=alojamiento, ambito=internacional, ciudad=Tokio` |
| 4. La tool devuelve el dato y el agente responde citando la fuente | Lee la respuesta final | **USD 250 por noche**, fuente `POL-GV-001 v2.1, sección 3` |

Preguntas de apoyo: *"¿Y la alimentación diaria en un viaje nacional?"* → 35.000 CLP por día; *"¿Cuál es mi límite de alojamiento?"* → el agente pregunta si es nacional o internacional antes de llamar a la tool. Aclara al público que el escenario y los datos son ficticios. Las trazas detalladas (Application Insights) se tratan en el bloque de observabilidad.

## Problemas frecuentes

| Síntoma | Causa probable / acción |
|---|---|
| `azd deploy` falla por permisos | Falta *Foundry Project Manager* en el proyecto, o rol para asignar permisos sobre el ACR |
| La versión queda en `failed` | `azd ai agent monitor` y revisa el error; confirma imagen `linux/amd64` y que `main.py` arranca en el puerto 8088 |
| Error de cuota / modelo no disponible | Cambia `deployments` en `azure.yaml` (nombre, versión, SKU, región) |
| Localmente `DefaultAzureCredential` falla | Ejecuta `az login` y revisa `FOUNDRY_PROJECT_ENDPOINT` |
| El modelo no llama a la tool | Revisa `INSTRUCCIONES` en `main.py` y la descripción de la tool (el modelo solo ve nombre, descripción y parámetros) |

**Plan B:** si el despliegue falla en vivo, usa el video grabado (`PB-D2-04` en `laboratorios\entorno-y-facilitacion\plan-b-demos.md`) o muestra el agente local con `probar-local.ps1`.

## Limpieza

```powershell
azd down      # elimina los recursos aprovisionados por azd (incluye el proyecto Foundry y el ACR)
```

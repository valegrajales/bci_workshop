# 04 · Referencias de infraestructura (Bicep / Terraform)

> **No se reescriben módulos:** este kit **apunta** a las plantillas oficiales ya incluidas en `repos\`. Todas las rutas son relativas a `BCI-Foundry-Workshop\repos\`.
> **NO EJECUTAR EN PRODUCCIÓN.** Ningún comando de este archivo fue ejecutado por Microsoft. Valida cada plantilla (versiones de API, parámetros y regiones) con `az deployment group what-if` antes de aplicar. Los valores entre `<...>` son marcadores de posición.
> **Entorno real del evento:** ya se aprovisiona con `laboratorios\entorno-y-facilitacion\provisionamiento\` (`Provision-Lab.ps1`, `participante.bicep`, `compartido.bicep`, `Add-Modelo.ps1`): un grupo de recursos `rg-bci-lab-NN` con cuenta Foundry + proyecto `lab-NN` por participante. Lo que sigue es material de referencia/propuesta original (1 recurso + ~54 proyectos) para consulta; los despliegues reales son `gpt-5.6-luna` (4K TPM), `gpt-5-mini` (10K TPM) y `text-embedding-3-small` (10K TPM) por cuenta.

## 1. Qué usar y cuándo

| Necesidad | Referencia recomendada | Notas |
|---|---|---|
| **Recurso Foundry + 1 proyecto + modelo (Básico)** — base del laboratorio | `publico-samples\foundry-samples\infrastructure\infrastructure-setup-bicep\40-basic-agent-setup\` (`main.bicep`, `azuredeploy.parameters.json`, `README.md`) | Parámetros: `aiServicesName`, `projectName`, `location` (por defecto `eastus`), `modelName` (por defecto `gpt-4.1`; **sobrescribe con `gpt-5.6-luna` (principal del Día 1) o `gpt-5-mini`**, que también será el nombre del despliegue), `modelVersion` (por defecto `2025-04-14`; `gpt-5.6-luna` usa `2026-07-09` y `gpt-5-mini` `2025-08-07`, *verificar*), `modelSkuName` (`GlobalStandard`), `modelCapacity` (40 por defecto; en el entorno real: 4 para `gpt-5.6-luna` por cuenta; *verificar cuota*). El `azuredeploy.parameters.json` de ejemplo trae `gpt-4o` con capacidad 1: no lo uses tal cual. La plantilla crea **un solo** despliegue: agrega embeddings y el respaldo con la CLI (sección 2). Requiere Foundry Account Owner o Contributor. Crea **un** proyecto: para ~54 proyectos usa el bucle de `az` de la sección 2. |
| Solo recurso + proyecto, sin modelo | `...\infrastructure-setup-bicep\00-basic\` | Útil para separar el aprovisionamiento de los despliegues de modelo. |
| Estándar (Cosmos DB + Storage + Search propios, Application Insights) | `...\infrastructure-setup-bicep\41-standard-agent-setup\` | Requiere Foundry Account Owner **y** Role Based Access Control Administrator; Cosmos con al menos 3000 RU/s. **No recomendado para 24 h**: añade dependencias (ver guía, sección 3.3). |
| Red privada (agente Estándar) | `...\15-private-network-standard-agent-setup\`, `...\18-managed-virtual-network\`, `...\10-private-network-basic\`, `...\11-private-network-basic-vnet\`, `...\16-...apim\` | Solo si BCI exige red privada; fuera del camino de 24 h. |
| Deshabilitar claves locales | `...\04-disable-local-auth\` | Alinea con autenticación solo-Entra. |
| Storage + Speech + Language | `...\02-storage-speech-language\` | Solo referencia: el laboratorio ya no usa Speech (la demo de voz se eliminó). |
| **Prevalidación (preflight)** | `...\deployment-tools\preflight\preflight-check.ps1` (+ `README.md`, `preflight.config.sample`) | Revisa requisitos antes de desplegar. |
| **Diagnóstico** | `...\deployment-tools\diagnostic\diagnostic-check.ps1` (+ `README.md`) | Para escenarios con red privada. |
| **Limpieza** (escenarios VNet) | `...\deployment-tools\cleanup\cleanup.ps1` (+ `README.md`, admite `-DryRun`) | Para el caso simple del laboratorio usa `scripts\03_limpieza.ps1`. |
| Catálogo de plantillas | `...\infrastructure-setup-bicep\README.md` | Índice oficial. |
| **Terraform (AVM)** | `internal\foundry-launchpad\INFRA.md`, `internal\foundry-launchpad\infra\foundry\`, `...\infra\networking\`, `...\infra\capability-host\`, `internal\foundry-launchpad\scripts\deploy-infra.sh` / `destroy-infra.sh` | Envoltorio del módulo AVM `Azure/avm-ptn-aiml-ai-foundry` (v0.11.0 según `INFRA.md`); solo el nivel Básico está completamente soportado. Verificar versión del proveedor antes de usar. |
| **Terraform (taller público)** | `publico-workshops\agentic-ai-lab\infrastructure\*.tf` y `readme.md` (+ `Taskfile.yaml` en la raíz del taller) | Región por defecto `eastus2`; requiere rol Owner en la suscripción y shell POSIX/WSL. Incluye Foundry, Search, modelos, identidades y registros. |
| **Bicep (taller de agentes hospedados .NET)** | `publico-workshops\Hosted_Agents_Workshop_dotNET\infra\` (`main.bicep`, `main.parameters.json`, `abbreviations.json`, `core\`) | Útil si se hace la demo de agente hospedado (requiere ACR; ver guía, sección 6.4). |
| Lista de verificación previa del Día 2 | `publico-workshops\foundry-hosted-agents-workshop\.workshop\scripts\preflight.py` | Base de `scripts\02_validar_entorno.py`. |
| Laboratorios Microsoft Learn (scripts de preparación) | `microsoftlearning-labs\mslearn-agent-quickstart\`, `microsoftlearning-labs\mslearn-ai-agents\` (carpeta Instructions y Allfiles), `microsoftlearning-labs\mslearn-ai-information-extraction\` (`setup.cmd`/`setup.sh` solo para la parte de modelos personalizados, que **omitimos**) | Revisar prerrequisitos de cada laboratorio. |

NOTA: en esta copia local **no existe** una carpeta Terraform dentro de `publico-samples\foundry-samples\infrastructure\`; las referencias Terraform son las dos de la tabla.

## 2. Plantilla mínima con la CLI de Azure (referencia de comandos)

Fuente: `docs-oficiales\foundry\how-to\create-projects.md` y `docs-oficiales\foundry\foundry-models\how-to\create-model-deployments.md`. Requiere Azure CLI **2.80.0 o superior** para los subcomandos de proyecto (verificar con `az version`). Prueba primero con **un** proyecto y **un** deployment.

```powershell
# Variables (ajusta; nombres sugeridos en la guía, sección 3.4)
$sub = "<SUBSCRIPTION-ID>"; $rg = "rg-bci-foundry-lab-eus2"; $loc = "eastus2"
$cuenta = "bci-foundry-lab-eus2"   # también será el subdominio personalizado: debe ser único
az account set --subscription $sub

# 1) Grupo de recursos con etiquetas de control de costos y limpieza
az group create --name $rg --location $loc --tags evento=bci-foundry-training-2026-10 propietario="<OWNER>" eliminar-despues-de=2026-10-26 datos=ficticios

# 2) Recurso Foundry (AIServices) con gestión de proyectos e identidad administrada
az cognitiveservices account create --name $cuenta --resource-group $rg --kind AIServices --sku S0 --location $loc `
  --custom-domain $cuenta --assign-identity --allow-project-management true

# 3) Despliegues de modelos. El nombre del deployment es el valor que viaja en FOUNDRY_MODEL y
#    FOUNDRY_EMBEDDING_MODEL del .env del Día 2 (guía, secciones 5.2 y 18). Versiones según la guía; verificar con list-models.
#    3a) Chat principal del Día 1: gpt-5.6-luna (versión 2026-07-09; capacidad real 4 = 4K TPM por cuenta). En el entorno real lo despliega provisionamiento\Add-Modelo.ps1.
az cognitiveservices account deployment create --name $cuenta --resource-group $rg --deployment-name gpt-5.6-luna `
  --model-name gpt-5.6-luna --model-version "2026-07-09" --model-format OpenAI --sku-name GlobalStandard --sku-capacity 4
#    3b) Respaldo del Día 1 / chat del Día 2: gpt-5-mini (capacidad real 10 = 10K TPM por cuenta)
az cognitiveservices account deployment create --name $cuenta --resource-group $rg --deployment-name gpt-5-mini `
  --model-name gpt-5-mini --model-version "2025-08-07" --model-format OpenAI --sku-name GlobalStandard --sku-capacity 10
#    3c) Embeddings (día 2)
az cognitiveservices account deployment create --name $cuenta --resource-group $rg --deployment-name text-embedding-3-small `
  --model-name text-embedding-3-small --model-version "<VERSION>" --model-format OpenAI --sku-name GlobalStandard --sku-capacity <CAPACIDAD>
#    3d) OPCIONAL (propuesta original; no está predesplegado en el entorno real): gpt-4.1-mini como respaldo del Día 2 (se activa cambiando solo FOUNDRY_MODEL=gpt-4.1-mini); Global Standard es pago por token, pero su capacidad sí descuenta cuota de la suscripción (verificar)
az cognitiveservices account deployment create --name $cuenta --resource-group $rg --deployment-name gpt-4.1-mini `
  --model-name gpt-4.1-mini --model-version "2025-04-14" --model-format OpenAI --sku-name GlobalStandard --sku-capacity <CAPACIDAD>

# 4) Proyectos (p01..p48 + instructores + reserva); prueba con uno antes del bucle
1..48 | ForEach-Object {
  $p = "lab-p{0:d2}" -f $_
  az cognitiveservices account project create --name $cuenta --resource-group $rg --project-name $p --location $loc
}

# 5) Verificación (solo lectura)
az cognitiveservices account deployment list --name $cuenta --resource-group $rg -o table
az cognitiveservices account list-models --name $cuenta --resource-group $rg -o table   # modelos disponibles en la región
```

- `<VERSION>` y `<CAPACIDAD>`: **verificar** con `az cognitiveservices account list-models` y con las consultas de cuota de `scripts\00_prerequisitos.ps1`; la capacidad se expresa en miles de TPM (`docs-oficiales\foundry\openai\how-to\quota.md`). Un ejemplo de parámetros de despliegue figura en `40-basic-agent-setup` (valores por defecto `gpt-4.1` / `2025-04-14`, que **no** son los de este evento).
- Límites relevantes: 32 deployments por recurso y 250 proyectos por recurso (`docs-oficiales\foundry\agents\concepts\limits-quotas-regions.md`; verificar vigencia).
- Eliminar un deployment: `az cognitiveservices account deployment delete --name $cuenta --resource-group $rg --deployment-name <NOMBRE>`.

## 3. Orden sugerido de despliegue (camino de 24 h)

1. `scripts\00_prerequisitos.ps1` (proveedores, cuota) → 2. Recurso + modelos + proyectos (sección 2 o `40-basic-agent-setup`) → 3. `scripts\01_crear_grupo_y_roles.ps1 -WhatIf` y luego real → 4. Document Intelligence S0 (+ Search y Application Insights para el Día 2) → 5. `scripts\02_validar_entorno.py` con una cuenta de prueba **solo miembro del grupo** → 6. Go/No-Go (guía, sección 15) → 7. Tras el evento: `scripts\03_limpieza.ps1`.

## Fuentes
- `repos\publico-samples\foundry-samples\infrastructure\infrastructure-setup-bicep\README.md` y subcarpetas citadas (verificadas en el árbol local).
- `repos\internal\foundry-launchpad\INFRA.md` y carpetas `infra\`, `scripts\`.
- `repos\publico-workshops\agentic-ai-lab\infrastructure\readme.md`; `repos\publico-workshops\Hosted_Agents_Workshop_dotNET\infra\`; `repos\publico-workshops\foundry-hosted-agents-workshop\.workshop\scripts\preflight.py`.
- Labs terminados: `laboratorios\dia1-lab-guiado\README.md` (§4.1 y §4.2) y `laboratorios\dia2-lab-procode\.env.example` (nombres de despliegue y variables).
- `docs-oficiales\foundry\how-to\create-projects.md`; `docs-oficiales\foundry\foundry-models\how-to\create-model-deployments.md`; `docs-oficiales\foundry\openai\how-to\quota.md`; `docs-oficiales\foundry\agents\concepts\limits-quotas-regions.md`.

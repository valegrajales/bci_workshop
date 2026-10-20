<#
.SYNOPSIS
    00_prerequisitos.ps1 - Verifica los prerrequisitos de Azure para el laboratorio BCI Foundry (solo lectura por defecto).

.DESCRIPTION
    Revisa, sin crear recursos:
      1. Azure CLI instalada y con versión suficiente (>= 2.80.0 para los comandos de proyectos Foundry).
      2. Sesión iniciada (az login) y suscripción activa correcta.
      3. Proveedores de recursos registrados (requeridos y opcionales).
      4. (Opcional, -ConsultarCuota) Consulta de SOLO LECTURA de cuota: nivel de cuota de la suscripción
         (quotaTiers) y uso/límite por modelo en la región (Usages API).
      5. Imprime los comandos de consulta de cuota para ejecutarlos manualmente.
    Solo registra proveedores si se indica -RegistrarProveedores (y respeta -WhatIf / -Confirm).

    NO EJECUTAR EN PRODUCCIÓN. Usar únicamente en la suscripción del laboratorio del evento.
    Este script no fue ejecutado por Microsoft antes de ser entregado; revísalo y pruébalo con -WhatIf.

.PARAMETER SubscriptionId
    Id de la suscripción del laboratorio. Si se omite se usa la suscripción activa de az.

.PARAMETER Region
    Región objetivo de los despliegues (por defecto eastus2).

.PARAMETER ConsultarCuota
    Ejecuta las consultas de cuota (solo lectura vía az rest). Requiere el rol
    "Cognitive Services Usages Reader" a nivel de SUSCRIPCIÓN (a nivel de recurso no funciona).

.PARAMETER RegistrarProveedores
    Registra los proveedores requeridos que falten. Cambia el estado de la suscripción; usar con -WhatIf primero.

.PARAMETER VersionMinimaCli
    Versión mínima de Azure CLI. Por defecto 2.80.0 (docs-oficiales\foundry\how-to\create-projects.md).

.EXAMPLE
    .\00_prerequisitos.ps1 -SubscriptionId "<SUBSCRIPTION-ID>"

.EXAMPLE
    .\00_prerequisitos.ps1 -SubscriptionId "<SUBSCRIPTION-ID>" -ConsultarCuota

.EXAMPLE
    .\00_prerequisitos.ps1 -SubscriptionId "<SUBSCRIPTION-ID>" -RegistrarProveedores -WhatIf

.NOTES
    Fuentes: docs-oficiales\foundry\openai\quotas-limits.md (quotaTiers), docs-oficiales\foundry\openai\how-to\quota.md
    (Usages API), repos\publico-samples\foundry-samples\infrastructure\infrastructure-setup-bicep\deployment-tools\preflight\README.md
    (lista de proveedores). Código de salida: 0 = sin fallos críticos, 1 = hay al menos un FAIL.
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Medium')]
param(
    [string]$SubscriptionId,
    [string]$Region = 'eastus2',
    [switch]$ConsultarCuota,
    [switch]$RegistrarProveedores,
    [version]$VersionMinimaCli = [version]'2.80.0'
)

$ErrorActionPreference = 'Stop'
$script:Fallos = 0

function Write-Resultado {
    param([string]$Estado, [string]$Mensaje)
    $color = switch ($Estado) { 'PASS' { 'Green' } 'WARN' { 'Yellow' } 'FAIL' { 'Red' } default { 'Gray' } }
    Write-Host ("[{0}] {1}" -f $Estado, $Mensaje) -ForegroundColor $color
    if ($Estado -eq 'FAIL') { $script:Fallos++ }
}

function Invoke-AzJson {
    param([string[]]$Argumentos)
    $salida = & az @Argumentos --only-show-errors -o json 2>&1
    if ($LASTEXITCODE -ne 0) { throw ($salida | Out-String) }
    return ($salida | Out-String | ConvertFrom-Json)
}

Write-Host '== BCI Foundry Lab :: prerrequisitos (solo lectura salvo -RegistrarProveedores) ==' -ForegroundColor Cyan
Write-Host 'NO EJECUTAR EN PRODUCCIÓN. Suscripción de laboratorio únicamente.' -ForegroundColor Yellow

# 1. Azure CLI
if (-not (Get-Command az -ErrorAction SilentlyContinue)) {
    Write-Resultado 'FAIL' 'Azure CLI no está instalada. Instálala: https://learn.microsoft.com/cli/azure/install-azure-cli'
    exit 1
}
try {
    $cli = Invoke-AzJson @('version')
    $versionCli = [version]($cli.'azure-cli' -replace '[^0-9\.].*$', '')
    if ($versionCli -ge $VersionMinimaCli) {
        Write-Resultado 'PASS' "Azure CLI $versionCli (mínimo $VersionMinimaCli)"
    } else {
        Write-Resultado 'FAIL' "Azure CLI $versionCli es menor que $VersionMinimaCli. Ejecuta: az upgrade"
    }
} catch {
    Write-Resultado 'FAIL' "No se pudo leer la versión de Azure CLI: $($_.Exception.Message)"
}

# 2. Sesión y suscripción
try {
    if ($SubscriptionId) {
        if ($PSCmdlet.ShouldProcess($SubscriptionId, 'az account set (cambia la suscripción activa de la sesión de CLI)')) {
            & az account set --subscription $SubscriptionId --only-show-errors
            if ($LASTEXITCODE -ne 0) { throw "az account set falló para $SubscriptionId" }
        }
    }
    $cuenta = Invoke-AzJson @('account', 'show')
    Write-Resultado 'PASS' ("Sesión activa: usuario={0}; suscripción={1} ({2}); tenant={3}" -f $cuenta.user.name, $cuenta.name, $cuenta.id, $cuenta.tenantId)
    if ($SubscriptionId -and $cuenta.id -ne $SubscriptionId) {
        Write-Resultado 'WARN' "La suscripción activa ($($cuenta.id)) no coincide con -SubscriptionId ($SubscriptionId). Si usaste -WhatIf es lo esperado."
    }
    $SubscriptionId = $cuenta.id
} catch {
    Write-Resultado 'FAIL' "No hay sesión de Azure CLI válida. Ejecuta 'az login' (o 'az login --use-device-code'). Detalle: $($_.Exception.Message)"
    exit 1
}

# 3. Proveedores de recursos
$requeridos = @(
    'Microsoft.CognitiveServices', 'Microsoft.Search', 'Microsoft.Insights',
    'Microsoft.OperationalInsights', 'Microsoft.Storage', 'Microsoft.MachineLearningServices'
)
$opcionales = @(
    'Microsoft.ContainerRegistry',   # solo demo de agente hospedado
    'Microsoft.DocumentDB',          # solo modo Estándar (Cosmos DB)
    'Microsoft.Network', 'Microsoft.KeyVault', 'Microsoft.ManagedIdentity'
)
$pendientes = @()
foreach ($p in ($requeridos + $opcionales)) {
    $esRequerido = $requeridos -contains $p
    try {
        $estado = (Invoke-AzJson @('provider', 'show', '--namespace', $p)).registrationState
    } catch {
        Write-Resultado 'WARN' "No se pudo consultar el proveedor $p"
        continue
    }
    if ($estado -eq 'Registered') {
        Write-Resultado 'PASS' "Proveedor $p registrado"
    } elseif ($esRequerido) {
        Write-Resultado 'FAIL' "Proveedor requerido $p en estado '$estado' (usa -RegistrarProveedores o: az provider register --namespace $p)"
        $pendientes += $p
    } else {
        Write-Resultado 'WARN' "Proveedor opcional $p en estado '$estado' (necesario solo para el escenario indicado en los comentarios)"
    }
}
if ($RegistrarProveedores -and $pendientes.Count -gt 0) {
    foreach ($p in $pendientes) {
        if ($PSCmdlet.ShouldProcess($p, 'az provider register')) {
            & az provider register --namespace $p --only-show-errors | Out-Null
            Write-Host "Registro solicitado para $p (puede tardar unos minutos)." -ForegroundColor Gray
        }
    }
}

# 4. Comandos de consulta de cuota (se imprimen siempre)
# Principal del Día 1 (gpt-5.6-luna), respaldo y chat del Día 2 (gpt-5-mini), embeddings (día 2) y respaldo opcional de la propuesta original (gpt-4.1-mini)
$modelosObjetivo = @('gpt-5.6-luna', 'gpt-5-mini', 'text-embedding-3-small', 'gpt-4.1-mini')
$urlUsos = "https://management.azure.com/subscriptions/$SubscriptionId/providers/Microsoft.CognitiveServices/locations/$Region/usages?api-version=2024-10-01"
$urlNivel = "https://management.azure.com/subscriptions/$SubscriptionId/providers/Microsoft.CognitiveServices/quotaTiers?api-version=2025-10-01-preview"
Write-Host "`n-- Comandos de consulta de cuota (solo lectura) --" -ForegroundColor Cyan
Write-Host "Nivel de cuota de la suscripción:`n  az rest --method get --url `"$urlNivel`""
Write-Host "Uso y límite por modelo en ${Region}:`n  az rest --method get --url `"$urlUsos`""
Write-Host "Modelos objetivo: $($modelosObjetivo -join ', ') (principal del Día 1 gpt-5.6-luna, 4K TPM por cuenta; respaldo gpt-5-mini; embeddings text-embedding-3-small; gpt-4.1-mini solo propuesta original)"
Write-Host 'Entorno real: 62 cuentas x 4K = 248K TPM de gpt-5.6-luna (37 en GlobalStandard + 25 en DataZoneStandard). La estimación de la guía (sección 5.3, >= 600) corresponde a la propuesta original; mídela en el ensayo.'
Write-Host 'Capacidad desplegable por modelo (Model Capacities API): ver docs-oficiales\foundry\openai\how-to\quota.md'
Write-Host 'Portal: Foundry > Manage > Quota (pestaña TPM). La unidad de capacidad del despliegue son MILES de TPM.'
Write-Host 'Aumentos de cuota: https://aka.ms/oai/stuquotarequest (evaluación individual y por orden de llegada; sin plazo garantizado).'

# 5. Consulta opcional
if ($ConsultarCuota) {
    Write-Host "`n-- Ejecutando consultas de cuota (GET) --" -ForegroundColor Cyan
    try {
        $nivel = Invoke-AzJson @('rest', '--method', 'get', '--url', $urlNivel)
        $nivel.value | ForEach-Object { Write-Host ("Nivel de cuota: {0} (política de actualización: {1})" -f $_.properties.currentTierName, $_.properties.tierUpgradePolicy) }
        Write-Resultado 'PASS' 'Consulta de nivel de cuota realizada'
    } catch {
        Write-Resultado 'WARN' "No se pudo consultar quotaTiers (¿falta Cognitive Services Usages Reader a nivel de suscripción?): $($_.Exception.Message)"
    }
    try {
        $usos = Invoke-AzJson @('rest', '--method', 'get', '--url', $urlUsos)
        $filtrados = $usos.value | Where-Object {
            $n = $_.name.value
            $_.limit -gt 0 -and ($modelosObjetivo | Where-Object { $n -like "*$_*" })
        }
        if ($filtrados) {
            $filtrados | ForEach-Object { Write-Host ("  {0}: {1}/{2}" -f $_.name.localizedValue, $_.currentValue, $_.limit) }
            Write-Resultado 'PASS' "Cuota consultada en $Region (compara con la estimación de la guía, sección 5.3)"
        } else {
            Write-Resultado 'WARN' "No hay líneas de cuota con límite > 0 para los modelos objetivo en ${Region}: solicita cuota antes del evento."
        }
    } catch {
        Write-Resultado 'WARN' "No se pudo consultar Usages API: $($_.Exception.Message)"
    }
}

Write-Host ''
if ($script:Fallos -gt 0) {
    Write-Host "Resultado: $($script:Fallos) verificación(es) crítica(s) fallida(s)." -ForegroundColor Red
    exit 1
}
Write-Host 'Resultado: sin fallos críticos.' -ForegroundColor Green
exit 0

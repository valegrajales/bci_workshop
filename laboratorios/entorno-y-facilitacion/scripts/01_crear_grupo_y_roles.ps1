<#
.SYNOPSIS
    01_crear_grupo_y_roles.ps1 - Asigna roles de Azure RBAC a los grupos Entra del laboratorio BCI Foundry.

.DESCRIPTION
    Aplica (de forma idempotente) la matriz de roles de la guía (guia-entorno-admin-bci.md, sección 6):

      Participantes (grp-bci-foundry-participantes)
        - Foundry User                      -> recurso Foundry (o por proyecto con -AislamientoPorProyecto)
        - Log Analytics Reader              -> workspace de Log Analytics (o Application Insights) para ver trazas (lab del Día 2)
        - Monitoring Reader                 -> Application Insights conectado (complementario; lo cita la doc de agentes hospedados)
        - Monitoring Metrics Publisher      -> Application Insights, SOLO con -AppInsightsSinAuthLocal (autenticación local deshabilitada)
        - Storage Blob Data Contributor     -> cuenta de Storage del proyecto, SOLO si se indica -StorageProyecto (file search del Día 1; verificar en T-1)
        - Search Index Data Reader          -> Azure AI Search
        - Cognitive Services User           -> Document Intelligence
        - Reader (opcional)                 -> grupo de recursos (-ReaderEnGrupoRecursos)

      Instructores (grp-bci-foundry-instructores)
        - Foundry Owner                     -> recurso Foundry
        - Cognitive Services Usages Reader  -> suscripción (ver cuota)
        - Search Service Contributor + Search Index Data Contributor -> Azure AI Search
        - Log Analytics Reader + Monitoring Reader -> workspace / Application Insights
        - Cognitive Services User           -> Document Intelligence (demo en vivo del Día 1)
        - Contributor (opcional)            -> grupo de recursos (-InstructoresContributorEnGrupo)

    Los roles Foundry se asignan por GUID porque fueron renombrados (Azure AI User -> Foundry User, etc.);
    los GUID no cambian (docs-oficiales\foundry\concepts\rbac-foundry.md).
    Opcionalmente crea los grupos Entra (-CrearGrupos). Los recursos opcionales que no se indiquen se omiten.

    NO EJECUTAR EN PRODUCCIÓN. Usar solo en la suscripción del laboratorio. Este script CAMBIA permisos:
    ejecútalo primero con -WhatIf. Requiere Owner, User Access Administrator o Role Based Access Control
    Administrator en los ámbitos indicados. Este script no fue ejecutado por Microsoft antes de su entrega.

.PARAMETER SubscriptionId        Id de la suscripción del laboratorio (obligatorio).
.PARAMETER ResourceGroup         Grupo de recursos del laboratorio (obligatorio).
.PARAMETER FoundryAccountName    Nombre del recurso Foundry (cuenta AIServices) (obligatorio).
.PARAMETER SearchServiceName     Nombre del servicio Azure AI Search (opcional).
.PARAMETER AppInsightsName       Nombre del recurso Application Insights conectado (opcional).
.PARAMETER DocumentIntelligenceName  Nombre del recurso Document Intelligence (opcional).
.PARAMETER LogAnalyticsWorkspaceName  Nombre del workspace de Log Analytics conectado (opcional; si no se indica, Log Analytics Reader se asigna sobre Application Insights).
.PARAMETER StorageProyecto       Nombre de la cuenta de Storage del proyecto (opcional; solo si existe y es visible en el grupo de recursos).
.PARAMETER AppInsightsSinAuthLocal  Asigna Monitoring Metrics Publisher a los participantes (solo si la autenticación local de Application Insights está deshabilitada).
.PARAMETER SpeechName            (Obsoleto: la demo de voz/avatar del Día 1 se eliminó; no es necesario) Nombre del recurso Speech (opcional; solo instructores).
.PARAMETER GrupoParticipantes    Nombre visible del grupo. Por defecto grp-bci-foundry-participantes.
.PARAMETER GrupoInstructores     Nombre visible del grupo. Por defecto grp-bci-foundry-instructores.
.PARAMETER CrearGrupos           Crea los grupos Entra si no existen (requiere permiso de Entra ID para crear grupos).
.PARAMETER AislamientoPorProyecto  No asigna Foundry User al grupo en el recurso; exige -MapaUsuarioProyecto.
.PARAMETER MapaUsuarioProyecto   CSV con columnas ObjectId,Proyecto (ObjectId del usuario en Entra). Asigna Foundry User por proyecto.
.PARAMETER ReaderEnGrupoRecursos Asigna Reader al grupo de participantes sobre el grupo de recursos.
.PARAMETER InstructoresContributorEnGrupo  Asigna Contributor a instructores en el grupo de recursos (solo para demo de agente hospedado).

.EXAMPLE
    .\01_crear_grupo_y_roles.ps1 -SubscriptionId "<SUBSCRIPTION-ID>" -ResourceGroup "rg-bci-foundry-lab-eus2" `
        -FoundryAccountName "<FOUNDRY-RESOURCE>" -SearchServiceName "<SEARCH>" -AppInsightsName "<APPI>" `
        -DocumentIntelligenceName "<DI>" -WhatIf

.NOTES
    Código de salida: 0 = OK, 1 = error de entrada o de resolución de grupos/recursos críticos.
    Las asignaciones de rol pueden tardar unos minutos en propagarse (verificar con la cuenta de prueba).
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
param(
    [Parameter(Mandatory = $true)][string]$SubscriptionId,
    [Parameter(Mandatory = $true)][string]$ResourceGroup,
    [Parameter(Mandatory = $true)][string]$FoundryAccountName,
    [string]$SearchServiceName,
    [string]$AppInsightsName,
    [string]$DocumentIntelligenceName,
    [string]$LogAnalyticsWorkspaceName,
    [string]$StorageProyecto,
    [switch]$AppInsightsSinAuthLocal,
    [string]$SpeechName,
    [string]$GrupoParticipantes = 'grp-bci-foundry-participantes',
    [string]$GrupoInstructores = 'grp-bci-foundry-instructores',
    [switch]$CrearGrupos,
    [switch]$AislamientoPorProyecto,
    [string]$MapaUsuarioProyecto,
    [switch]$ReaderEnGrupoRecursos,
    [switch]$InstructoresContributorEnGrupo
)

$ErrorActionPreference = 'Stop'

# GUID de roles Foundry (docs-oficiales\foundry\concepts\rbac-foundry.md)
$RolFoundryUser = '53ca6127-db72-4b80-b1b0-d745d6d5456d'
$RolFoundryOwner = 'c883944f-8b7b-4483-af10-35834be79c4a'

$resumen = New-Object System.Collections.Generic.List[object]

function Invoke-AzText {
    param([string[]]$Argumentos)
    $salida = & az @Argumentos --only-show-errors 2>&1
    if ($LASTEXITCODE -ne 0) { throw ($salida | Out-String) }
    return ($salida | Out-String).Trim()
}

function Get-IdRecurso {
    param([string]$Nombre, [string]$Tipo)
    if (-not $Nombre) { return $null }
    try {
        return Invoke-AzText @('resource', 'show', '-g', $ResourceGroup, '-n', $Nombre, '--resource-type', $Tipo, '--query', 'id', '-o', 'tsv')
    } catch {
        Write-Warning "No se encontró $Tipo '$Nombre' en $ResourceGroup. Se omiten sus asignaciones. Detalle: $($_.Exception.Message)"
        return $null
    }
}

function Get-IdGrupo {
    param([string]$Nombre)
    try {
        return Invoke-AzText @('ad', 'group', 'show', '--group', $Nombre, '--query', 'id', '-o', 'tsv')
    } catch {
        if ($CrearGrupos) {
            if ($PSCmdlet.ShouldProcess($Nombre, 'az ad group create (grupo de seguridad Entra)')) {
                return Invoke-AzText @('ad', 'group', 'create', '--display-name', $Nombre, '--mail-nickname', $Nombre, '--query', 'id', '-o', 'tsv')
            }
            return $null
        }
        throw "El grupo '$Nombre' no existe. Créalo en Entra ID o usa -CrearGrupos."
    }
}

function Set-Rol {
    param(
        [string]$ObjectId, [string]$TipoPrincipal, [string]$Rol, [string]$Ambito,
        [string]$Etiqueta, [string]$Destino
    )
    if (-not $Ambito) { return }
    if (-not $ObjectId) {
        $resumen.Add([pscustomobject]@{ Destino = $Destino; Rol = $Etiqueta; Ambito = $Ambito; Estado = 'PLANIFICADO (sin ObjectId: -WhatIf o grupo no creado)' })
        return
    }
    $existente = Invoke-AzText @('role', 'assignment', 'list', '--assignee', $ObjectId, '--role', $Rol, '--scope', $Ambito, '--query', '[0].id', '-o', 'tsv')
    if ($existente) {
        $resumen.Add([pscustomobject]@{ Destino = $Destino; Rol = $Etiqueta; Ambito = $Ambito; Estado = 'YA EXISTE' })
        return
    }
    if ($PSCmdlet.ShouldProcess("$Destino -> $Ambito", "az role assignment create --role '$Etiqueta'")) {
        Invoke-AzText @('role', 'assignment', 'create', '--assignee-object-id', $ObjectId, '--assignee-principal-type', $TipoPrincipal,
            '--role', $Rol, '--scope', $Ambito) | Out-Null
        $resumen.Add([pscustomobject]@{ Destino = $Destino; Rol = $Etiqueta; Ambito = $Ambito; Estado = 'CREADA' })
    } else {
        $resumen.Add([pscustomobject]@{ Destino = $Destino; Rol = $Etiqueta; Ambito = $Ambito; Estado = 'SIMULADA (-WhatIf)' })
    }
}

if ($AislamientoPorProyecto -and -not $MapaUsuarioProyecto) {
    throw '-AislamientoPorProyecto requiere -MapaUsuarioProyecto (CSV con ObjectId,Proyecto).'
}
if ($MapaUsuarioProyecto -and -not (Test-Path -LiteralPath $MapaUsuarioProyecto)) {
    throw "No existe el archivo $MapaUsuarioProyecto"
}

Write-Host '== BCI Foundry Lab :: asignación de roles ==' -ForegroundColor Cyan
Write-Host 'NO EJECUTAR EN PRODUCCIÓN. Suscripción de laboratorio únicamente. Usa -WhatIf primero.' -ForegroundColor Yellow

& az account set --subscription $SubscriptionId --only-show-errors
if ($LASTEXITCODE -ne 0) { throw 'No se pudo seleccionar la suscripción. ¿Ejecutaste az login?' }

$idParticipantes = Get-IdGrupo $GrupoParticipantes
$idInstructores = Get-IdGrupo $GrupoInstructores

$ambitoSub = "/subscriptions/$SubscriptionId"
$ambitoRg = "/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroup"
$idFoundry = Get-IdRecurso $FoundryAccountName 'Microsoft.CognitiveServices/accounts'
if (-not $idFoundry) { throw 'El recurso Foundry es obligatorio y no se encontró.' }
$idSearch = Get-IdRecurso $SearchServiceName 'Microsoft.Search/searchServices'
$idAppi = Get-IdRecurso $AppInsightsName 'Microsoft.Insights/components'
$idDi = Get-IdRecurso $DocumentIntelligenceName 'Microsoft.CognitiveServices/accounts'
$idLaw = Get-IdRecurso $LogAnalyticsWorkspaceName 'Microsoft.OperationalInsights/workspaces'
$idStorage = Get-IdRecurso $StorageProyecto 'Microsoft.Storage/storageAccounts'
$ambitoTrazas = if ($idLaw) { $idLaw } else { $idAppi }
$idSpeech = Get-IdRecurso $SpeechName 'Microsoft.CognitiveServices/accounts'

# --- Participantes ---
if (-not $AislamientoPorProyecto) {
    Set-Rol $idParticipantes 'Group' $RolFoundryUser $idFoundry 'Foundry User' 'Participantes'
}
Set-Rol $idParticipantes 'Group' 'Log Analytics Reader' $ambitoTrazas 'Log Analytics Reader' 'Participantes'
Set-Rol $idParticipantes 'Group' 'Monitoring Reader' $idAppi 'Monitoring Reader' 'Participantes'
if ($AppInsightsSinAuthLocal) {
    Set-Rol $idParticipantes 'Group' 'Monitoring Metrics Publisher' $idAppi 'Monitoring Metrics Publisher' 'Participantes'
}
Set-Rol $idParticipantes 'Group' 'Storage Blob Data Contributor' $idStorage 'Storage Blob Data Contributor' 'Participantes'
Set-Rol $idParticipantes 'Group' 'Search Index Data Reader' $idSearch 'Search Index Data Reader' 'Participantes'
Set-Rol $idParticipantes 'Group' 'Cognitive Services User' $idDi 'Cognitive Services User' 'Participantes'
if ($ReaderEnGrupoRecursos) {
    Set-Rol $idParticipantes 'Group' 'Reader' $ambitoRg 'Reader' 'Participantes'
}

# --- Aislamiento por proyecto (opcional) ---
if ($MapaUsuarioProyecto) {
    $filas = Import-Csv -LiteralPath $MapaUsuarioProyecto
    foreach ($fila in $filas) {
        if (-not $fila.ObjectId -or -not $fila.Proyecto) { Write-Warning "Fila incompleta en el CSV: $($fila | ConvertTo-Json -Compress)"; continue }
        $ambitoProyecto = "$idFoundry/projects/$($fila.Proyecto)"
        Set-Rol $fila.ObjectId 'User' $RolFoundryUser $ambitoProyecto 'Foundry User (proyecto)' "Usuario $($fila.ObjectId)"
    }
}

# --- Instructores ---
Set-Rol $idInstructores 'Group' $RolFoundryOwner $idFoundry 'Foundry Owner' 'Instructores'
Set-Rol $idInstructores 'Group' 'Cognitive Services Usages Reader' $ambitoSub 'Cognitive Services Usages Reader' 'Instructores'
Set-Rol $idInstructores 'Group' 'Search Service Contributor' $idSearch 'Search Service Contributor' 'Instructores'
Set-Rol $idInstructores 'Group' 'Search Index Data Contributor' $idSearch 'Search Index Data Contributor' 'Instructores'
Set-Rol $idInstructores 'Group' 'Log Analytics Reader' $ambitoTrazas 'Log Analytics Reader' 'Instructores'
Set-Rol $idInstructores 'Group' 'Monitoring Reader' $idAppi 'Monitoring Reader' 'Instructores'
Set-Rol $idInstructores 'Group' 'Cognitive Services User' $idDi 'Cognitive Services User (DI)' 'Instructores'
Set-Rol $idInstructores 'Group' 'Cognitive Services User' $idSpeech 'Cognitive Services User (Speech)' 'Instructores'
if ($InstructoresContributorEnGrupo) {
    Set-Rol $idInstructores 'Group' 'Contributor' $ambitoRg 'Contributor' 'Instructores'
}

Write-Host "`n-- Resumen --" -ForegroundColor Cyan
$resumen | Format-Table -AutoSize -Wrap | Out-String | Write-Host
Write-Host 'Siguiente paso: probar con una cuenta de prueba que sea SOLO miembro del grupo: python 02_validar_entorno.py ...' -ForegroundColor Gray
exit 0

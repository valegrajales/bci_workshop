#requires -Version 7
<#
.SYNOPSIS
  Asigna el rol Cognitive Services User a cada cuenta (labNN / instNN) sobre SU cuenta Foundry ya aprovisionada.

.DESCRIPTION
  Para el entorno YA desplegado (rg-bci-inst-NN y rg-bci-lab-NN). Los despliegues nuevos con participante.bicep ya incluyen el rol.
  Por cada grupo de recursos:
    1. Busca la cuenta Foundry (AIServices) del RG.
    2. Identifica al usuario dueño del RG: la asignación de Foundry User (53ca6127-...) a un principal de tipo User en el RG
       (la crea participante.bicep). Si no la encuentra, resuelve el UPN labNN/instNN@<TenantDomain> con az ad user show.
    3. Despliega rol-cognitive-services-user.bicep (scope = cuenta Foundry). Mismo nombre de asignación que participante.bicep,
       así que es idempotente: re-ejecutar no duplica ni falla.
    4. Verifica que la asignación exista en el ámbito de la cuenta.
  NO redespliega participante.bicep (eso pisaría el SKU de gpt-5.6-luna repartido por Add-Modelo.ps1). No toca usuarios, TAP ni modelos.

  Requiere: az CLI con sesión en la suscripción, con permiso para crear asignaciones de rol (Owner o User Access Administrator).

  *** NO EJECUTAR EN PRODUCCIÓN. Es para la suscripción de laboratorio. Usar -WhatIf para ver el plan. ***

.PARAMETER Start / Count   Rango de participantes (por defecto 1..58).
.PARAMETER Instructores     Cantidad de cuentas de instructor (inst01..). 0 = solo participantes.
.PARAMETER Paralelo         Despliegues en paralelo.
.PARAMETER WhatIf           Solo muestra el plan (cuenta y principal por RG), sin asignar nada.

.EXAMPLE
  ./Add-RolCognitiveServicesUser.ps1 -WhatIf
  ./Add-RolCognitiveServicesUser.ps1
  ./Add-RolCognitiveServicesUser.ps1 -Start 7 -Count 1 -Instructores 0   # solo lab07
#>
[CmdletBinding()]
param(
  [string]$SubscriptionId = '3cdef987-9108-4358-bb71-366990c966ce',
  [string]$TenantDomain   = 'mngenvmcap219366.onmicrosoft.com',
  [int]$Start = 1,
  [int]$Count = 58,
  [int]$Instructores = 4,
  [int]$Paralelo = 8,
  [switch]$WhatIf
)
$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$template = Join-Path $here 'rol-cognitive-services-user.bicep'
if (-not (Test-Path $template)) { throw "No se encuentra $template (debe estar junto a este script)." }
az account set --subscription $SubscriptionId | Out-Null

$RolFoundryUser = '53ca6127-db72-4b80-b1b0-d745d6d5456d'
$RolCsUser      = 'a97b65f3-24c7-4388-baec-2e87135dc908'

$plan = @()
for ($i = 1; $i -le $Instructores; $i++) { $n = '{0:D2}' -f $i; $plan += [pscustomobject]@{ Rg = "rg-bci-inst-$n"; Upn = "inst$n@$TenantDomain" } }
for ($i = $Start; $i -lt ($Start + $Count); $i++) { $n = '{0:D2}' -f $i; $plan += [pscustomobject]@{ Rg = "rg-bci-lab-$n"; Upn = "lab$n@$TenantDomain" } }
Write-Host ("Cuentas a procesar: {0} (rol Cognitive Services User sobre la cuenta Foundry de cada RG){1}" -f $plan.Count, $(if ($WhatIf) { ' [WHATIF]' } else { '' }))

$res = $plan | ForEach-Object -ThrottleLimit $Paralelo -Parallel {
  $p = $_; $fu = $using:RolFoundryUser; $cs = $using:RolCsUser; $tpl = $using:template; $wi = $using:WhatIf
  $out = [ordered]@{ Rg = $p.Rg; Upn = $p.Upn; Cuenta = ''; PrincipalId = ''; Estado = '' }
  try {
    $acct = az cognitiveservices account list -g $p.Rg --query "[?kind=='AIServices'] | [0].{n:name,id:id}" -o json 2>$null | ConvertFrom-Json
    if (-not $acct) { $out.Estado = 'SIN_CUENTA'; return [pscustomobject]$out }
    $out.Cuenta = $acct.n

    # Dueño del RG: Foundry User asignado a un User directamente en el RG (participante.bicep).
    $rgId = az group show -n $p.Rg --query id -o tsv
    $principal = az role assignment list --scope $rgId --role $fu --query "[?principalType=='User' && scope=='$rgId'] | [0].principalId" -o tsv 2>$null
    if (-not $principal) { $principal = az ad user show --id $p.Upn --query id -o tsv 2>$null }
    if (-not $principal) { $out.Estado = 'SIN_PRINCIPAL'; return [pscustomobject]$out }
    $out.PrincipalId = $principal

    $ya = az role assignment list --scope $acct.id --role $cs --assignee $principal --query "length(@)" -o tsv 2>$null
    if ([int]$ya -gt 0) { $out.Estado = 'YA_ASIGNADO'; return [pscustomobject]$out }
    if ($wi) { $out.Estado = 'WHATIF_ASIGNARIA'; return [pscustomobject]$out }

    az deployment group create -g $p.Rg -n rol-cs-user --template-file $tpl `
      --parameters accountName=$($acct.n) participantObjectId=$principal principalType=User -o none 2>&1 | Out-Null
    if ($LASTEXITCODE -ne 0) {
      $err = az deployment group show -g $p.Rg -n rol-cs-user --query properties.error.details[0].message -o tsv 2>$null
      $out.Estado = "ERROR: $err"; return [pscustomobject]$out
    }
    $ok = az role assignment list --scope $acct.id --role $cs --assignee $principal --query "length(@)" -o tsv 2>$null
    $out.Estado = $(if ([int]$ok -gt 0) { 'ASIGNADO' } else { 'NO_VERIFICADO (replicación; reintentar en 1-2 min)' })
  } catch { $out.Estado = "ERROR: $($_.Exception.Message)" }
  [pscustomobject]$out
}

$res | Sort-Object Rg | Format-Table Rg, Upn, Cuenta, Estado -AutoSize
$res | Group-Object Estado | ForEach-Object { "{0}: {1}" -f $_.Name, $_.Count }
$bad = @($res | Where-Object { $_.Estado -notin @('ASIGNADO', 'YA_ASIGNADO', 'WHATIF_ASIGNARIA') })
if ($bad.Count) { Write-Warning "$($bad.Count) cuentas requieren revisión (ver tabla)."; exit 1 }
'Listo. La propagación de RBAC puede tardar hasta ~10 min: los participantes deben cerrar y volver a abrir sesión en el Studio si ya estaban dentro.'

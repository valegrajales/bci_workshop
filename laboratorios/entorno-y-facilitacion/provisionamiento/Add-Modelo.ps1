#requires -Version 7
<#
.SYNOPSIS
  Despliega un modelo adicional (por defecto gpt-5.6-luna) en las cuentas Foundry ya aprovisionadas (rg-bci-inst-NN y rg-bci-lab-NN).

.DESCRIPTION
  La cuota de gpt-5.6-luna de la suscripción es chica y se reparte en dos bolsas: GlobalStandard y DataZoneStandard.
  Las primeras -GlobalStandardCuentas cuentas (instructores primero y luego participantes en orden) usan GlobalStandard;
  el resto usa DataZoneStandard. Con la cuota disponible el 2026-10-20 (150 K GlobalStandard + 100 K DataZoneStandard):
  37 cuentas x 4 K en GlobalStandard + 25 cuentas x 4 K en DataZoneStandard = 62 cuentas.
  Es idempotente: si el deployment ya existe con la misma configuración, lo deja igual.

  Requiere: az CLI con sesión en la suscripción (Contributor/Owner). No toca usuarios, TAP ni roles.

.PARAMETER ListaCuentas   Rango de participantes (Start/Count) e instructores a procesar.
.PARAMETER WhatIf         Solo muestra el plan.
#>
[CmdletBinding()]
param(
  [string]$SubscriptionId = '3cdef987-9108-4358-bb71-366990c966ce',
  [string]$ModelName = 'gpt-5.6-luna',
  [string]$ModelVersion = '2026-07-09',
  [string]$DeploymentName = '',
  [int]$Capacity = 4,
  [int]$Start = 1,
  [int]$Count = 58,
  [int]$Instructores = 4,
  [int]$GlobalStandardCuentas = 37,
  [int]$Paralelo = 8,
  [switch]$WhatIf
)
$ErrorActionPreference = 'Stop'
if (-not $DeploymentName) { $DeploymentName = $ModelName }
az account set --subscription $SubscriptionId | Out-Null

$rgs = @()
for ($i = 1; $i -le $Instructores; $i++) { $rgs += ('rg-bci-inst-{0:D2}' -f $i) }
for ($i = $Start; $i -lt ($Start + $Count); $i++) { $rgs += ('rg-bci-lab-{0:D2}' -f $i) }

$plan = for ($k = 0; $k -lt $rgs.Count; $k++) {
  [pscustomobject]@{ Rg = $rgs[$k]; Sku = $(if ($k -lt $GlobalStandardCuentas) { 'GlobalStandard' } else { 'DataZoneStandard' }) }
}
$plan | Group-Object Sku | ForEach-Object { "{0}: {1} cuentas x {2} K = {3} K TPM" -f $_.Name, $_.Count, $Capacity, ($_.Count * $Capacity) }
if ($WhatIf) { $plan | Format-Table -AutoSize; return }

$res = $plan | ForEach-Object -ThrottleLimit $Paralelo -Parallel {
  $p = $_; $m = $using:ModelName; $v = $using:ModelVersion; $d = $using:DeploymentName; $c = $using:Capacity
  $acct = az cognitiveservices account list -g $p.Rg --query "[0].name" -o tsv 2>$null
  if (-not $acct) { return [pscustomobject]@{ Rg = $p.Rg; Sku = $p.Sku; Estado = 'SIN_CUENTA' } }
  $out = az cognitiveservices account deployment create -g $p.Rg -n $acct --deployment-name $d --model-name $m --model-version $v --model-format OpenAI --sku-name $p.Sku --sku-capacity $c --query properties.provisioningState -o tsv 2>&1
  [pscustomobject]@{ Rg = $p.Rg; Cuenta = $acct; Sku = $p.Sku; Estado = ($out | Select-Object -Last 1) }
}
$res | Sort-Object Rg | Format-Table -AutoSize
$bad = @($res | Where-Object { $_.Estado -ne 'Succeeded' })
if ($bad.Count) { Write-Warning "$($bad.Count) cuentas no terminaron en Succeeded:"; $bad | Format-Table -AutoSize; exit 1 }
"Listo: $($res.Count) cuentas con $DeploymentName."

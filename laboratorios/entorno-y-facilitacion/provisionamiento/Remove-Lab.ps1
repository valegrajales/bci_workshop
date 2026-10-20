<#
.SYNOPSIS
  Elimina TODO el laboratorio BCI Foundry Training Day: resource groups, usuarios y grupos.

.DESCRIPTION
  Borra los RG con tag Event=bci-foundry-training (y con ellos cuentas Foundry, deployments, presupuestos y roles de RG),
  los usuarios lab* / inst* y los grupos grp-bci-lab-*. Los modelos desplegados dejan de consumir cuota al borrar las cuentas;
  si hace falta, purgar las cuentas Cognitive Services eliminadas (az cognitiveservices account purge).

  *** DESTRUCTIVO. Requiere -Eliminar. Usar -WhatIf para ver qué se borraría. ***
#>
[CmdletBinding()]
param(
  [string]$SubscriptionId = '3cdef987-9108-4358-bb71-366990c966ce',
  [string]$TenantDomain   = 'mngenvmcap219366.onmicrosoft.com',
  [switch]$Eliminar,
  [switch]$WhatIf
)
$ErrorActionPreference = 'Stop'
function Log($m) { Write-Host ("[{0:HH:mm:ss}] {1}" -f (Get-Date), $m) }
az account set --subscription $SubscriptionId | Out-Null

$rgs = az group list --query "[?tags.Event=='bci-foundry-training'].name" -o tsv
Log ("Resource groups a eliminar: {0}" -f (($rgs | Measure-Object).Count))
$rgs | ForEach-Object { Log "  RG $_" }

Import-Module Microsoft.Graph.Authentication
$tok = (python (Join-Path (Split-Path -Parent $MyInvocation.MyCommand.Path) 'graph_auth.py') token) | Select-Object -First 1
if (-not $tok) { throw 'Sin token de Graph. Ejecuta: python graph_auth.py login' }
Connect-MgGraph -AccessToken (ConvertTo-SecureString $tok -AsPlainText -Force) -NoWelcome
$users = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/users?`$filter=startswith(userPrincipalName,'lab') or startswith(userPrincipalName,'inst')&`$select=id,userPrincipalName&`$top=200").value |
  Where-Object { $_.userPrincipalName -match "^(lab|inst)\d\d@$([regex]::Escape($TenantDomain))$" }
Log ("Usuarios a eliminar: {0}" -f $users.Count)
$groups = (Invoke-MgGraphRequest -Method GET -Uri "https://graph.microsoft.com/v1.0/groups?`$filter=startswith(displayName,'grp-bci-lab-')&`$select=id,displayName").value
Log ("Grupos a eliminar: {0}" -f $groups.Count)

if ($WhatIf -or -not $Eliminar) { Log 'Sin cambios (use -Eliminar para ejecutar).'; return }

foreach ($rg in $rgs) { Log "Eliminando $rg"; az group delete -n $rg --yes --no-wait }
foreach ($u in $users) { Invoke-MgGraphRequest -Method DELETE -Uri "https://graph.microsoft.com/v1.0/users/$($u.id)" | Out-Null }
foreach ($g in $groups) { Invoke-MgGraphRequest -Method DELETE -Uri "https://graph.microsoft.com/v1.0/groups/$($g.id)" | Out-Null }
Log 'Eliminación lanzada. Los RG se borran en segundo plano.'


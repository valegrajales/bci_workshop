<#
.SYNOPSIS
  Aprovisiona el laboratorio BCI Foundry Training Day: usuarios Entra + RG por participante + recursos + presupuesto + Temporary Access Pass.

.DESCRIPTION
  Requiere: az CLI con sesión en la suscripción, y Microsoft.Graph.Authentication con sesión activa
  (Connect-MgGraph -Scopes Policy.ReadWrite.AuthenticationMethod,UserAuthenticationMethod.ReadWrite.All,User.ReadWrite.All,Group.ReadWrite.All).
  Crea, por cada participante N: usuario labNN, RG rg-bci-lab-NN, cuenta Foundry + proyecto + deployments (participante.bicep),
  roles (Foundry User + Reader en su RG) y presupuesto con alertas. Genera un Temporary Access Pass (multi-uso) para iniciar sesión
  sin registrar MFA (el tenant exige MFA y bloquea el registro de métodos desde fuera de la red de confianza).
  Las credenciales (UPN + TAP) se escriben en un CSV LOCAL fuera de OneDrive. NO se guardan contraseñas.

  *** NO EJECUTAR EN PRODUCCIÓN. Es para el tenant/suscripción de laboratorio. Usar -WhatIf para ver el plan. ***

.PARAMETER Start / Count     Rango de participantes (por defecto 1..58).
.PARAMETER Instructores       Cantidad de cuentas de instructor (inst01..). Se agregan al grupo de instructores.
.PARAMETER SoloTap            Solo (re)genera los TAP y el CSV; no despliega nada.
.PARAMETER SkipCompartido     No despliega los recursos compartidos (Search/App Insights).
.PARAMETER AjustarMaxTap      Sube maximumLifetimeInMinutes de la política TAP (solo ese campo) al valor de -TapMinutes. Por defecto NO se toca la política (ya está habilitada para todos, máx. 480 min).
.PARAMETER WhatIf             Muestra lo que haría sin cambiar nada.
#>
[CmdletBinding()]
param(
  [string]$SubscriptionId = '3cdef987-9108-4358-bb71-366990c966ce',
  [string]$TenantDomain   = 'mngenvmcap219366.onmicrosoft.com',
  [int]$Start = 1,
  [int]$Count = 58,
  [int]$Instructores = 4,
  [string]$Location = 'eastus2',
  [string]$SearchLocation = '',
  [int]$ChatCapacity = 10,
  [int]$EmbeddingCapacity = 10,
  [int]$BudgetUSD = 10,
  [string]$NotifyEmail = 'Pablo.Braconi@microsoft.com',
  [int]$TapMinutes = 480,
  [datetime]$TapStart = (Get-Date '2026-10-21T06:30:00-03:00'),
  [string]$SecretsDir = (Join-Path $env:USERPROFILE 'bci-lab-secrets'),
  [string]$DeleteAfter = '2026-10-30',
  [switch]$SoloTap,
  [switch]$AjustarMaxTap,
  [switch]$SkipCompartido,
  [switch]$WhatIf
)

$ErrorActionPreference = 'Stop'
$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$tags = @{ Event = 'bci-foundry-training'; Owner = 'pabracon'; DeleteAfter = $DeleteAfter }
function Log($m) { Write-Host ("[{0:HH:mm:ss}] {1}" -f (Get-Date), $m) }
function Graph($method, $uri, $body = $null) {
  if ($WhatIf -and $method -ne 'GET') { Log "WHATIF $method $uri"; return $null }
  if ($body) { return Invoke-MgGraphRequest -Method $method -Uri $uri -Body ($body | ConvertTo-Json -Depth 8) -ContentType 'application/json' }
  return Invoke-MgGraphRequest -Method $method -Uri $uri
}
function New-RandomPassword { -join ((48..57) + (65..90) + (97..122) + (33,35,36,37,42,43,45,61,63,64) | Get-Random -Count 28 | ForEach-Object { [char]$_ }) }

Import-Module Microsoft.Graph.Authentication
# Token de Graph: se obtiene de la caché local de MSAL (python graph_auth.py login una vez) y se renueva cuando hace falta.
function Connect-GraphMsal {
  $tok = $null
  try { $tok = (python (Join-Path $here 'graph_auth.py') token 2>$null) | Select-Object -First 1 } catch { $tok = $null }
  if ($tok) { Connect-MgGraph -AccessToken (ConvertTo-SecureString $tok -AsPlainText -Force) -NoWelcome; return }
  # Alternativa: sesión de Connect-MgGraph ya iniciada con -UseDeviceAuthentication (token en caché local).
  Connect-MgGraph -TenantId 'eeee485f-b8f7-4983-b3dc-d5d97a0ad2bc' -NoWelcome
  if (-not (Get-MgContext)) { throw 'Sin sesión de Graph. Ejecuta: Connect-MgGraph -UseDeviceAuthentication (con los scopes del encabezado) o python graph_auth.py login' }
}
Connect-GraphMsal
$ctx = Get-MgContext
Log "Graph conectado (tenant $($ctx.TenantId))"

# ---------- Grupos ----------
function Ensure-Group($name) {
  $g = (Graph GET "https://graph.microsoft.com/v1.0/groups?`$filter=displayName eq '$name'").value
  if ($g.Count -gt 0) { return $g[0].id }
  Log "Creando grupo $name"
  $r = Graph POST 'https://graph.microsoft.com/v1.0/groups' @{ displayName = $name; mailEnabled = $false; mailNickname = $name; securityEnabled = $true }
  if ($r) { return $r.id } else { return '00000000-0000-0000-0000-000000000000' }
}
$gPart = Ensure-Group 'grp-bci-lab-participantes'
$gInst = Ensure-Group 'grp-bci-lab-instructores'

# ---------- Política TAP: solo se verifica (ya habilitada para todos los usuarios) ----------
$tapUri = 'https://graph.microsoft.com/v1.0/policies/authenticationMethodsPolicy/authenticationMethodConfigurations/TemporaryAccessPass'
$tapCfg = Graph GET $tapUri
Log ("TAP: estado={0}, máx={1} min" -f $tapCfg.state, $tapCfg.maximumLifetimeInMinutes)
if ($tapCfg.state -ne 'enabled') { throw 'La política Temporary Access Pass no está habilitada en el tenant.' }
if ($TapMinutes -gt $tapCfg.maximumLifetimeInMinutes) {
  if ($AjustarMaxTap) {
    Log "Subiendo maximumLifetimeInMinutes a $TapMinutes (solo ese campo)"
    Graph PATCH $tapUri @{ '@odata.type' = '#microsoft.graph.temporaryAccessPassAuthenticationMethodConfiguration'; maximumLifetimeInMinutes = $TapMinutes } | Out-Null
  } else { throw "TapMinutes ($TapMinutes) supera el máximo de la política ($($tapCfg.maximumLifetimeInMinutes)). Usa -AjustarMaxTap o baja -TapMinutes." }
}
az account set --subscription $SubscriptionId | Out-Null
$rows = @()

function Ensure-User($upn, $display, $nick) {
  $u = $null
  try { $u = Graph GET "https://graph.microsoft.com/v1.0/users/$upn`?`$select=id,userPrincipalName" } catch { $u = $null }
  if ($u -and $u.id) { return $u.id }
  Log "Creando usuario $upn"
  $r = Graph POST 'https://graph.microsoft.com/v1.0/users' @{
    accountEnabled = $true; displayName = $display; mailNickname = $nick; userPrincipalName = $upn; usageLocation = 'CL'
    passwordProfile = @{ forceChangePasswordNextSignIn = $false; password = (New-RandomPassword) } }
  if ($r) { return $r.id } else { return '00000000-0000-0000-0000-000000000000' }
}

# ---------- Lista de cuentas ----------
$cuentas = @()
for ($i = $Start; $i -lt ($Start + $Count); $i++) { $cuentas += [pscustomobject]@{ Tipo = 'participante'; Num = '{0:D2}' -f $i; Grupo = $gPart } }
for ($i = 1; $i -le $Instructores; $i++) { $cuentas += [pscustomobject]@{ Tipo = 'instructor'; Num = '{0:D2}' -f $i; Grupo = $gInst } }

# ---------- Usuarios + RG ----------
foreach ($c in $cuentas) {
  $prefix = if ($c.Tipo -eq 'participante') { 'lab' } else { 'inst' }
  $upn = "$prefix$($c.Num)@$TenantDomain"
  $c | Add-Member -NotePropertyName Upn -NotePropertyValue $upn
  $c | Add-Member -NotePropertyName Rg -NotePropertyValue ("rg-bci-$prefix-$($c.Num)")
  if ($SoloTap) { $c | Add-Member -NotePropertyName UserId -NotePropertyValue ((Graph GET "https://graph.microsoft.com/v1.0/users/$upn`?`$select=id").id); continue }
  $uid = Ensure-User $upn "BCI $($prefix.ToUpper()) $($c.Num)" "$prefix$($c.Num)"
  $c | Add-Member -NotePropertyName UserId -NotePropertyValue $uid
  try { Graph POST "https://graph.microsoft.com/v1.0/groups/$($c.Grupo)/members/`$ref" @{ '@odata.id' = "https://graph.microsoft.com/v1.0/directoryObjects/$uid" } | Out-Null } catch { if ($_.Exception.Message -notmatch 'already exist') { Log "Aviso al agregar al grupo: $($_.Exception.Message)" } }
  if ($WhatIf) { Log "WHATIF az group create $($c.Rg) + deployment participante.bicep"; continue }
  $tagArgs = $tags.GetEnumerator() | ForEach-Object { "$($_.Key)=$($_.Value)" }
  az group create -n $c.Rg -l $Location --tags @tagArgs "Cuenta=$upn" -o none
}

if (-not $SoloTap -and -not $WhatIf) {
  # Esperar replicación de los nuevos principals
  Start-Sleep -Seconds 45

  # ---------- Compartido ----------
  if (-not $SkipCompartido) {
    az group create -n rg-bci-lab-compartido -l $Location --tags "Event=bci-foundry-training" "Owner=pabracon" "DeleteAfter=$DeleteAfter" -o none
    Log 'Desplegando recursos compartidos (Search, Log Analytics, App Insights)'
    $searchLoc = if ($SearchLocation) { $SearchLocation } else { $Location }
    az deployment group create -g rg-bci-lab-compartido -n compartido --template-file (Join-Path $here 'compartido.bicep') `
      --parameters participantsGroupObjectId=$gPart instructorsGroupObjectId=$gInst location=$Location searchLocation=$searchLoc -o none
  }

  # ---------- Participantes: despliegues en paralelo ----------
  $emails = @($NotifyEmail)
  foreach ($c in $cuentas) {
    $params = @{ '$schema' = 'https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#'; contentVersion = '1.0.0.0'; parameters = @{
      participantNumber = @{ value = $c.Num }; participantObjectId = @{ value = $c.UserId }; location = @{ value = $Location }
      chatCapacity = @{ value = $ChatCapacity }; embeddingCapacity = @{ value = $EmbeddingCapacity }
      budgetAmount = @{ value = $BudgetUSD }; budgetContactEmails = @{ value = $emails }; tags = @{ value = $tags } } }
    $pf = Join-Path $env:TEMP "lab-params-$($c.Rg).json"
    $params | ConvertTo-Json -Depth 8 | Set-Content $pf -Encoding utf8
    Log "Lanzando despliegue $($c.Rg)"
    az deployment group create -g $c.Rg -n participante --template-file (Join-Path $here 'participante.bicep') --parameters "@$pf" --no-wait -o none
  }
  Log 'Esperando a que terminen los despliegues...'
  foreach ($c in $cuentas) {
    az deployment group wait -g $c.Rg -n participante --created --timeout 3000 2>$null
    $state = az deployment group show -g $c.Rg -n participante --query properties.provisioningState -o tsv
    $c | Add-Member -NotePropertyName Estado -NotePropertyValue $state
    if ($state -eq 'Succeeded') {
      $o = az deployment group show -g $c.Rg -n participante --query properties.outputs -o json | ConvertFrom-Json
      $c | Add-Member -NotePropertyName ProjectEndpoint -NotePropertyValue $o.projectEndpoint.value
    } else { Log "ATENCIÓN: $($c.Rg) terminó en estado $state" }
    Remove-Item (Join-Path $env:TEMP "lab-params-$($c.Rg).json") -ErrorAction SilentlyContinue
  }
}

# ---------- TAP + CSV local ----------
Connect-GraphMsal   # renueva el token (puede haber pasado más de 1 h)
if (-not (Test-Path $SecretsDir)) { New-Item -ItemType Directory -Path $SecretsDir | Out-Null }
$csv = Join-Path $SecretsDir ("credenciales-{0:yyyyMMdd-HHmm}.csv" -f (Get-Date))
foreach ($c in $cuentas) {
  $tap = ''
  if (-not $WhatIf) {
    $old = (Graph GET "https://graph.microsoft.com/v1.0/users/$($c.UserId)/authentication/temporaryAccessPassMethods").value
    foreach ($o in $old) { Graph DELETE "https://graph.microsoft.com/v1.0/users/$($c.UserId)/authentication/temporaryAccessPassMethods/$($o.id)" | Out-Null }
    $r = Graph POST "https://graph.microsoft.com/v1.0/users/$($c.UserId)/authentication/temporaryAccessPassMethods" @{
      lifetimeInMinutes = $TapMinutes; isUsableOnce = $false; startDateTime = $TapStart.ToUniversalTime().ToString('yyyy-MM-ddTHH:mm:ssZ') }
    if ($r) { $tap = $r.temporaryAccessPass }
  }
  $rows += [pscustomobject]@{ Tipo = $c.Tipo; Usuario = $c.Upn; TAP = $tap; RG = $c.Rg; Estado = $c.Estado; ProjectEndpoint = $c.ProjectEndpoint; TapDesde = $TapStart.ToString('s'); TapMinutos = $TapMinutes }
}
if (-not $WhatIf) { $rows | Export-Csv $csv -NoTypeInformation -Encoding utf8; Log "Credenciales (SENSIBLES) en: $csv" }
Log 'Listo.'




#requires -Version 7.0
<#
 Paso 1 de la demo: muestra el esquema del indice (texto, vector, metadatos de seguridad), la configuracion semantica
 y la distribucion de fragmentos por nivel de acceso. Solo lectura. Requiere `az login`, Search Service Contributor
 para leer el esquema y Search Index Data Reader (o Contributor) para consultar documentos, sobre el servicio.
 Uso:  .\scripts\mostrar-indice.ps1 [-Servicio bci-workshop-srch-fjdb] [-Indice normativa-austral]
#>
param(
    [string]$Servicio = "bci-workshop-srch-fjdb",
    [string]$Indice = "normativa-austral",
    [string]$ApiVersion = "2026-08-01-preview"
)
$ErrorActionPreference = "Stop"

$endpoint = "https://$Servicio.search.windows.net"
$token = az account get-access-token --resource https://search.azure.com --query accessToken -o tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($token)) {
    throw "No se pudo obtener un token de Entra ID: revisa Azure CLI y ejecuta 'az login'."
}
$headers = @{ Authorization = "Bearer $token" }

$def = Invoke-RestMethod -Uri "$endpoint/indexes/${Indice}?api-version=$ApiVersion" -Headers $headers -TimeoutSec 60
Write-Host "`nIndice: $($def.name)" -ForegroundColor Cyan
$def.fields | Select-Object name, type, searchable, filterable, retrievable, analyzer, dimensions | Format-Table -AutoSize | Out-Host

$sem = $def.semantic.configurations | Select-Object -First 1
if ($sem) {
    Write-Host "Configuracion semantica: $($sem.name) (titulo: $($sem.prioritizedFields.titleField.fieldName); contenido: $($sem.prioritizedFields.prioritizedContentFields.fieldName -join ', '))"
}

# El campo vector no es "retrievable" (buena practica: no se devuelven 3072 floats por fragmento), por eso no se ve en
# los resultados. Su existencia se demuestra con el tamano del indice vectorial y con una consulta vectorial.
$campoVector = $def.fields | Where-Object { $_.dimensions } | Select-Object -First 1
$vectorizador = $null
if ($campoVector) {
    $perfil = $def.vectorSearch.profiles | Where-Object { $_.name -eq $campoVector.vectorSearchProfile }
    $vectorizador = $def.vectorSearch.vectorizers | Where-Object { $_.name -eq $perfil.vectorizer }
    Write-Host "`nVectores: campo '$($campoVector.name)' ($($campoVector.dimensions) dimensiones, perfil '$($perfil.name)', algoritmo $($perfil.algorithm))" -ForegroundColor Cyan
    if ($vectorizador) {
        Write-Host "Vectorizador del indice: $($vectorizador.name) -> $($vectorizador.azureOpenAIParameters.deploymentId) en $($vectorizador.azureOpenAIParameters.resourceUri)"
    } else {
        Write-Warning "El perfil no tiene vectorizador: el knowledge base NO puede hacer busqueda vectorial (solo texto + semantico)."
    }
} else {
    Write-Host "`nIndice sin campo vectorial: solo texto + semantico."
}
$stats = Invoke-RestMethod -Uri "$endpoint/indexes/${Indice}/stats?api-version=$ApiVersion" -Headers $headers -TimeoutSec 60
Write-Host ("Estadisticas: {0} documentos, indice vectorial {1:N0} KB" -f $stats.documentCount, ($stats.vectorIndexSize / 1KB))

$body = @{ search = "*"; top = 0; count = $true; facets = @("nivel_acceso", "area") } | ConvertTo-Json
$r = Invoke-RestMethod -Method Post -Uri "$endpoint/indexes/$Indice/docs/search?api-version=$ApiVersion" -Headers $headers `
    -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 60
Write-Host "`nFragmentos indexados: $($r.'@odata.count')" -ForegroundColor Cyan
Write-Host "Por nivel_acceso (base del security trimming):"
$r.'@search.facets'.nivel_acceso | ForEach-Object { "  {0,-12} {1}" -f $_.value, $_.count } | Out-Host
Write-Host "Por area:"
$r.'@search.facets'.area | ForEach-Object { "  {0,-14} {1}" -f $_.value, $_.count } | Out-Host

if ($vectorizador) {
    # Solo vectores (sin 'search'): el servicio vectoriza el texto con el vectorizador del indice.
    # Una paráfrasis encuentra viajes/viáticos; no demuestra por sí sola que el knowledge base use vectores.
    $frase = "cuantas noches de hotel puedo pagar con la tarjeta en un viaje por el pais"
    $vb = @{ select = "id,titulo,seccion,nivel_acceso"; top = 3
             vectorQueries = @(@{ kind = "text"; text = $frase; fields = $campoVector.name; k = 3 }) } | ConvertTo-Json -Depth 6
    $vr = Invoke-RestMethod -Method Post -Uri "$endpoint/indexes/$Indice/docs/search?api-version=$ApiVersion" -Headers $headers `
        -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($vb)) -TimeoutSec 60
    Write-Host "`nPrueba vectorial pura: '$frase'" -ForegroundColor Cyan
    if (@($vr.value).Count -eq 0) { throw "La prueba vectorial pura no devolvio resultados." }
    $vr.value | ForEach-Object { "  {0,-11} {1} > {2}   (score vectorial {3:N3})" -f $_.id, $_.titulo, $_.seccion, $_.'@search.score' } | Out-Host
    Write-Host "Esta prueba valida el indice y su vectorizador; no demuestra su uso por el knowledge base."
}

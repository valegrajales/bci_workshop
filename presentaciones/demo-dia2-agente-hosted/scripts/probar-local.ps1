<#
 Prueba local del agente (paso previo a la demo). Requiere el agente corriendo en http://localhost:8088:
   cd src\agente-gastos-hosted ; copia .env.example a .env ; uv run --python 3.13 python main.py
 (o bien:  azd ai agent run)
 Uso:  .\scripts\probar-local.ps1 [-Pregunta "..."] [-Url http://localhost:8088]
#>
param(
    [string]$Pregunta = "Cuanto es mi limite de alojamiento por noche en un viaje internacional a Tokio?",
    [string]$Url = "http://localhost:8088"
)
$ErrorActionPreference = "Stop"

$body = @{ input = $Pregunta; stream = $false } | ConvertTo-Json
$raw = Invoke-WebRequest -UseBasicParsing -Method Post -Uri "$Url/responses" -ContentType "application/json; charset=utf-8" `
    -Body ([Text.Encoding]::UTF8.GetBytes($body))
# La respuesta no declara charset: se decodifica explicitamente como UTF-8 (PowerShell 5.1 usa otra codificacion).
$ms = New-Object System.IO.MemoryStream
$raw.RawContentStream.CopyTo($ms)
$resp = [Text.Encoding]::UTF8.GetString($ms.ToArray()) | ConvertFrom-Json

if ($resp.status -and $resp.status -ne "completed") {
    throw "La respuesta termino con estado '$($resp.status)': $($resp.error | ConvertTo-Json -Compress)"
}

Write-Host "`nPregunta: $Pregunta" -ForegroundColor Cyan
$texto = @()
foreach ($item in $resp.output) {
    if ($item.type -eq "function_call") {
        Write-Host "Tool llamada: $($item.name)  args: $($item.arguments)" -ForegroundColor Yellow
    }
    elseif ($item.type -eq "function_call_output") {
        Write-Host "Tool devolvio: $($item.output)" -ForegroundColor DarkYellow
    }
    elseif ($item.type -eq "message") {
        foreach ($c in $item.content) { if ($c.type -eq "output_text") { $texto += $c.text } }
    }
}
if (-not $texto) { throw "La respuesta no contiene texto del asistente." }
Write-Host "`nRespuesta:`n$($texto -join "`n")" -ForegroundColor Green

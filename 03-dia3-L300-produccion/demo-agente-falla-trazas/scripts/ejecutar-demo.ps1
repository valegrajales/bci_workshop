#requires -Version 7.0
<#
 Pregunta a un agente de la demo y muestra respuesta, llamadas a la tool MCP (argumentos) y citas.
 Uso:  .\scripts\ejecutar-demo.ps1 -Agente normativa-falla
       .\scripts\ejecutar-demo.ps1 -Agente normativa-corregido -Pregunta "..."
#>
param(
    [ValidateSet("normativa-falla", "normativa-corregido")][string]$Agente = "normativa-falla",
    [string]$Pregunta = "¿En cuánto tiempo debo reportar un incidente de seguridad crítico y a quién?",
    [string]$Proyecto = "https://bci-demo.services.ai.azure.com/api/projects/bci-workshop"
)
$ErrorActionPreference = "Stop"
$token = az account get-access-token --resource https://ai.azure.com --query accessToken -o tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($token)) { throw "Ejecuta 'az login' primero." }
$cuerpo = @{ input = $Pregunta; agent_reference = @{ type = "agent_reference"; name = $Agente } } | ConvertTo-Json -Depth 5
$r = Invoke-RestMethod -Method Post -Uri "$Proyecto/openai/v1/responses" -Headers @{ Authorization = "Bearer $token" } `
    -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($cuerpo)) -TimeoutSec 180

Write-Host "`nAgente: $Agente | response_id: $($r.id)" -ForegroundColor Cyan
if ($r.status -ne "completed") { throw "La respuesta no se completo (status=$($r.status)): $($r.error | ConvertTo-Json -Compress) $($r.incomplete_details | ConvertTo-Json -Compress)" }
Write-Host "Pregunta: $Pregunta`n"
foreach ($o in $r.output) {
    if ($o.type -eq "mcp_call") {
        Write-Host "[tool] $($o.name) args: $($o.arguments)" -ForegroundColor Yellow
        if ($o.error) { Write-Host "[tool] error: $($o.error)" -ForegroundColor Red }
    }
    elseif ($o.type -eq "message") {
        Write-Host "[respuesta]" -ForegroundColor Green
        $o.content | Where-Object { $_.type -eq "output_text" } | ForEach-Object { Write-Host $_.text }
    }
}


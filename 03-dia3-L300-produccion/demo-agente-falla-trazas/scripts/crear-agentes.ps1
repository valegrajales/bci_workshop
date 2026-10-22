#requires -Version 7.0
<#
 Crea (cada ejecucion publica una nueva version) los prompt agents de la demo en el proyecto de Foundry:
   normativa-falla      instrucciones defectuosas (la falla de razonamiento a diagnosticar)
   normativa-corregido  instrucciones correctas (contraste)
 Ambos usan la tool MCP del knowledge base de Foundry IQ mediante la conexion de proyecto RemoteTool "kb-normativa-mcp".
 Autenticacion: Microsoft Entra ID (az login), sin llaves. Uso:  .\scripts\crear-agentes.ps1 [-Modelo gpt-6-luna]
#>
param(
    [string]$Proyecto = "https://bci-demo.services.ai.azure.com/api/projects/bci-workshop",
    [string]$Modelo = "gpt-6-luna",
    [string]$Conexion = "kb-normativa-mcp",
    [string]$Search = "https://bci-workshop-srch-fjdb.search.windows.net",
    [string]$KnowledgeBase = "normativa-kb",
    [string]$ApiVersionSearch = "2026-08-01-preview"
)
$ErrorActionPreference = "Stop"
$raiz = Split-Path $PSScriptRoot -Parent

$token = az account get-access-token --resource https://ai.azure.com --query accessToken -o tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($token)) { throw "Ejecuta 'az login' primero." }
$headers = @{ Authorization = "Bearer $token" }

$descripciones = [ordered]@{
    "normativa-falla"     = "DEMO Dia 3: agente con instrucciones defectuosas que usa mal la tool de Foundry IQ."
    "normativa-corregido" = "DEMO Dia 3: agente corregido que descompone consultas y cita fuentes."
}
foreach ($nombre in $descripciones.Keys) {
    $instrucciones = (Get-Content (Join-Path $raiz "agentes\$nombre.txt") -Raw -Encoding utf8).Trim()
    $cuerpo = @{
        description = $descripciones[$nombre]
        definition  = @{
            kind         = "prompt"
            model        = $Modelo
            instructions = $instrucciones
            tools        = @(@{
                    type                  = "mcp"
                    server_label          = "knowledge_base"
                    server_url            = "$Search/knowledgebases/$KnowledgeBase/mcp?api-version=$ApiVersionSearch"
                    require_approval      = "never"
                    allowed_tools         = @("knowledge_base_retrieve")
                    project_connection_id = $Conexion
                })
        }
    } | ConvertTo-Json -Depth 10
    $r = Invoke-RestMethod -Method Post -Uri "$Proyecto/agents/$nombre/versions?api-version=v1" -Headers $headers `
        -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($cuerpo)) -TimeoutSec 120
    Write-Host "Agente '$nombre' listo: version $($r.version) (modelo $Modelo)." -ForegroundColor Green
}

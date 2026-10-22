#requires -Version 7.0
<#
 Crea (o actualiza, es idempotente) el knowledge source y el knowledge base de retrieval agentico sobre el indice
 de normativa. Requiere el indice ya creado y `az login`. Autenticacion: Microsoft Entra ID (sin llaves).
 Roles del usuario en el servicio de Search: Search Service Contributor (+ Search Index Data Reader para consultar).
 El servicio de Search necesita identidad administrada con el rol "Cognitive Services User" sobre la cuenta de Foundry.
 Uso:  .\scripts\crear-knowledge-base.ps1 [-Servicio bci-workshop-srch-fjdb] [-DeploymentChat gpt-5-mini-013161]
#>
param(
    [string]$Servicio = "bci-workshop-srch-fjdb",
    [string]$Indice = "normativa-austral",
    [string]$KnowledgeSource = "normativa-ks",
    [string]$KnowledgeBase = "normativa-kb",
    [string]$RecursoOpenAI = "https://bci-demo.openai.azure.com",
    [string]$DeploymentChat = "gpt-5-mini-013161",
    [string]$ModeloChat = "gpt-5-mini",
    [string]$ApiVersion = "2026-08-01-preview"
)
$ErrorActionPreference = "Stop"

$endpoint = "https://$Servicio.search.windows.net"
$token = az account get-access-token --resource https://search.azure.com --query accessToken -o tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($token)) {
    throw "No se pudo obtener un token de Entra ID: revisa Azure CLI y ejecuta 'az login'."
}
$headers = @{ Authorization = "Bearer $token" }

function Invoke-Search($ruta, $objeto) {
    $json = $objeto | ConvertTo-Json -Depth 10
    Invoke-RestMethod -Method Put -Uri "$endpoint/${ruta}?api-version=$ApiVersion" -Headers $headers `
        -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($json)) -TimeoutSec 120 | Out-Null
}

$campos = "id", "doc_id", "titulo", "seccion", "area", "nivel_acceso", "contenido"
Invoke-Search "knowledgesources/$KnowledgeSource" @{
    name = $KnowledgeSource
    kind = "searchIndex"
    description = "Normativa interna ficticia de Austral Bank"
    searchIndexParameters = @{
        searchIndexName = $Indice
        semanticConfigurationName = "normativa-semantica"
        sourceDataFields = @($campos | ForEach-Object { @{ name = $_ } })
        # Sin searchFields: incluye todos los campos searchable, también el vector si tiene vectorizador.
    }
}
Write-Host "Knowledge source '$KnowledgeSource' listo (indice '$Indice')." -ForegroundColor Green

Invoke-Search "knowledgebases/$KnowledgeBase" @{
    name = $KnowledgeBase
    description = "Normativa interna ficticia de Austral Bank para empleados bancarios"
    retrievalInstructions = "Usa siempre $KnowledgeSource. Descompone las preguntas que combinen temas distintos en subconsultas separadas."
    answerInstructions = "Responde en espanol y de forma concisa. Cita cada afirmacion con [ref_id:N]. Si las fuentes no contienen la informacion, dilo en una frase y no inventes ni sugieras valores."
    outputMode = "answerSynthesis"
    knowledgeSources = @(@{ name = $KnowledgeSource })
    models = @(@{ kind = "azureOpenAI"; azureOpenAIParameters = @{ resourceUri = $RecursoOpenAI; deploymentId = $DeploymentChat; modelName = $ModeloChat } })
    retrievalReasoningEffort = @{ kind = "low" }
}
Write-Host "Knowledge base '$KnowledgeBase' listo (modelo de planificacion: $DeploymentChat)." -ForegroundColor Green

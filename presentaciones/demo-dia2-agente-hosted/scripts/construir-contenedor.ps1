<#
 Construye la imagen del agente para linux/amd64 (requisito de la plataforma de hosted agents).
 Dos modos:
   .\scripts\construir-contenedor.ps1                          # docker build local (requiere Docker Desktop)
   .\scripts\construir-contenedor.ps1 -Registro miacr -Tag v1  # az acr build remoto: no requiere Docker local
 `azd deploy` ya hace el build remoto en ACR; este script sirve para validar la imagen o para desplegar
 con el SDK (create_version + container_configuration.image) sin azd.
#>
param(
    [string]$Registro,
    [string]$Tag = "v1",
    [string]$Imagen = "agente-gastos"
)
$ErrorActionPreference = "Stop"
$src = Join-Path $PSScriptRoot "..\src\agente-gastos-hosted"

if ($Registro) {
    az acr build --registry $Registro --platform linux/amd64 --image "${Imagen}:${Tag}" $src
    if ($LASTEXITCODE -ne 0) { throw "az acr build fallo (codigo $LASTEXITCODE)" }
    Write-Host "Imagen: $Registro.azurecr.io/${Imagen}:${Tag}" -ForegroundColor Green
}
else {
    docker build --platform linux/amd64 -t "${Imagen}:${Tag}" $src
    if ($LASTEXITCODE -ne 0) { throw "docker build fallo (codigo $LASTEXITCODE)" }
    Write-Host "Imagen local: ${Imagen}:${Tag}" -ForegroundColor Green
    Write-Host "Prueba:  docker run --rm -p 8088:8088 -e FOUNDRY_PROJECT_ENDPOINT=... -e AZURE_AI_MODEL_DEPLOYMENT_NAME=... ${Imagen}:${Tag}"
    Write-Host "(dentro del contenedor DefaultAzureCredential necesita credenciales; para la demo usa azd ai agent run)"
}

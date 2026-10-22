#requires -Version 7.0
# Pruebas sin Azure ni dependencias: todas las llamadas externas están simuladas.
$ErrorActionPreference = "Stop"
$scripts = Join-Path $PSScriptRoot "..\scripts"
$script:pruebas = 0
$global:RetrievalDemoPruebas = @{
    FalloToken = $false
    Solicitudes = [Collections.Generic.List[object]]::new()
    Respuesta = $null
    Respuestas = @()
}
$estado = $global:RetrievalDemoPruebas

function az {
    $global:LASTEXITCODE = [int]$global:RetrievalDemoPruebas.FalloToken
    "token-simulado"
}

function Invoke-RestMethod {
    param($Method, $Uri, $Headers, $ContentType, $Body, $TimeoutSec)
    $json = if ($Body -is [byte[]]) { [Text.Encoding]::UTF8.GetString($Body) } else { $Body }
    $global:RetrievalDemoPruebas.Solicitudes.Add([pscustomobject]@{ Method = $Method; Uri = $Uri; Body = $json })
    if ($global:RetrievalDemoPruebas.Respuestas.Count -gt 0) {
        return $global:RetrievalDemoPruebas.Respuestas[$global:RetrievalDemoPruebas.Solicitudes.Count - 1]
    }
    $global:RetrievalDemoPruebas.Respuesta
}

function Nueva-Respuesta([string]$Permitidos = "publico,interno", [string]$Nivel = "interno") {
    @{
        activity = @(@{
            type = "searchIndex"; id = 1; count = 1; knowledgeSourceName = "normativa-ks"
            startedAt = "2026-10-22T00:00:00Z"; completedAt = "2026-10-22T00:00:01Z"
            searchIndexArguments = @{ search = "años"; filter = "search.in(nivel_acceso, '$Permitidos', ',')" }
        })
        response = @(@{ content = @(@{ type = "text"; text = "Se conservan 6 años [ref_id:0]." }) })
        references = @(@{
            type = "searchIndex"; id = "0"; docKey = "NOR-004-01"; rerankerScore = 2
            sourceData = @{ id = "NOR-004-01"; titulo = "Política"; seccion = "Retención"; nivel_acceso = $Nivel; contenido = "Comprobantes: 6 años." }
        })
    }
}

function Ejecutar([string]$Nombre = "consultar", [hashtable]$Argumentos = @{}) {
    $estado.Solicitudes.Clear()
    $salida = ""
    $fallo = $null
    try { $salida = & (Join-Path $scripts "$Nombre.ps1") @Argumentos *>&1 | Out-String }
    catch { $fallo = $_ }
    [pscustomobject]@{ Salida = $salida; Fallo = $fallo }
}

function Comprobar([bool]$Condicion, [string]$Caso) {
    if (-not $Condicion) { throw "FALLÓ: $Caso" }
    $script:pruebas++
}

foreach ($caso in @(
    @{ Nivel = "publico"; Permitidos = "publico" },
    @{ Nivel = "PUBLICO"; Permitidos = "publico" },
    @{ Nivel = "interno"; Permitidos = "publico,interno" },
    @{ Nivel = "INTERNO"; Permitidos = "publico,interno" },
    @{ Nivel = "InTeRnO"; Permitidos = "publico,interno" },
    @{ Nivel = "restringido"; Permitidos = "publico,interno,restringido" },
    @{ Nivel = "RESTRINGIDO"; Permitidos = "publico,interno,restringido" }
)) {
    $estado.Respuesta = Nueva-Respuesta $caso.Permitidos ($caso.Nivel.ToLowerInvariant())
    $r = Ejecutar -Argumentos @{ Nivel = $caso.Nivel; Crudo = $true }
    Comprobar ($null -eq $r.Fallo) "nivel $($caso.Nivel): $($r.Fallo) $($r.Fallo.ScriptStackTrace)"
    $body = $estado.Solicitudes[0].Body | ConvertFrom-Json
    Comprobar ($body.knowledgeSourceParams[0].filterAddOn -ceq "search.in(nivel_acceso, '$($caso.Permitidos)', ',')") "filtro de $($caso.Nivel)"
    Comprobar ($body.messages[0].content[0].text -cmatch "cuántos años") "UTF-8 de $($caso.Nivel)"
    Comprobar (($r.Salida | ConvertFrom-Json).references[0].sourceData.contenido -ceq "Comprobantes: 6 años.") "JSON y acentos de $($caso.Nivel)"
}

foreach ($crudo in @($false, $true)) {
    foreach ($defecto in @("nivel", "metadatos", "filtro", "fuente", "activity", "cita", "fragmento", "identificador", "texto")) {
        $estado.Respuesta = Nueva-Respuesta
        $estado.Respuesta.response[0].content[0].text = "NO_MOSTRAR [ref_id:0]"
        switch ($defecto) {
            nivel { $estado.Respuesta.references[0].sourceData.nivel_acceso = "restringido" }
            metadatos { $estado.Respuesta.references[0].sourceData.Remove("nivel_acceso") }
            filtro { $estado.Respuesta.activity[0].searchIndexArguments.filter = "" }
            fuente { $estado.Respuesta.activity[0].knowledgeSourceName = "otra-fuente" }
            activity { $estado.Respuesta.activity = @() }
            cita { $estado.Respuesta.response[0].content[0].text = "NO_MOSTRAR [ref_id:999]" }
            fragmento { $estado.Respuesta.references[0].sourceData.contenido = "" }
            identificador { $estado.Respuesta.references[0].sourceData.id = "otro-id" }
            texto { $estado.Respuesta.response = @() }
        }
        $r = Ejecutar -Argumentos @{ Crudo = $crudo }
        Comprobar ($null -ne $r.Fallo) "rechazar $defecto, crudo=$crudo"
        Comprobar ($r.Salida -notmatch "NO_MOSTRAR") "no imprimir datos rechazados ($defecto, crudo=$crudo)"
    }
}

$estado.Respuesta = Nueva-Respuesta
$estado.Respuesta.response[0].content += @{ type = "text"; text = "SEGUNDA_PARTE [ref_id:0]" }
$r = Ejecutar
Comprobar ($null -eq $r.Fallo -and $r.Salida -match "SEGUNDA_PARTE") "leer todos los bloques de texto"

$estado.Respuesta = Nueva-Respuesta
$estado.Respuesta.response[0].content[0].text = "Respuesta sin marcadores."
$r = Ejecutar
Comprobar ($null -eq $r.Fallo -and $r.Salida -match "NO son citas verificadas") "no confundir referencias de apoyo con citas"

$estado.Respuesta = Nueva-Respuesta
$segunda = Nueva-Respuesta
$segunda.activity[0].id = 2
$estado.Respuesta.activity += $segunda.activity[0]
$r = Ejecutar
Comprobar ($null -eq $r.Fallo -and $r.Salida -match "activity\): True") "detectar intervalos solapados"

foreach ($nombre in @("consultar", "mostrar-indice", "crear-knowledge-base")) {
    $estado.FalloToken = $true
    $r = Ejecutar $nombre
    Comprobar ($null -ne $r.Fallo -and $estado.Solicitudes.Count -eq 0) "detener $nombre ante fallo de Azure CLI aunque haya stdout"
}
$estado.FalloToken = $false
$estado.Respuesta = @{}
$r = Ejecutar "crear-knowledge-base"
Comprobar ($null -eq $r.Fallo -and $estado.Solicitudes.Count -eq 2) "simular los dos PUT de preparación sin red"
Comprobar (($estado.Solicitudes[0].Body | ConvertFrom-Json).searchIndexParameters.searchIndexName -ceq "normativa-austral") "nombre del índice"
Comprobar (($estado.Solicitudes[1].Body | ConvertFrom-Json).models[0].azureOpenAIParameters.deploymentId -ceq "gpt-5-mini-013161") "despliegue del planificador"
Comprobar (($estado.Solicitudes[0].Body | ConvertFrom-Json).searchIndexParameters.PSObject.Properties.Name -notcontains "searchFields") "no excluir los campos vectoriales de la fuente"

foreach ($modo in @("sin-vectores", "sin-vectorizador", "con-vectorizador", "vector-vacio")) {
    $def = @{
        name = "prueba"
        fields = @(@{ name = "contenido"; type = "Edm.String"; searchable = $true })
    }
    if ($modo -ne "sin-vectores") {
        $def.fields += @{ name = "vector"; dimensions = 3072; vectorSearchProfile = "perfil" }
        $def.vectorSearch = @{ profiles = @(@{ name = "perfil"; algorithm = "hnsw" }); vectorizers = @() }
        if ($modo -in @("con-vectorizador", "vector-vacio")) {
            $def.vectorSearch.profiles[0].vectorizer = "openai"
            $def.vectorSearch.vectorizers += @{
                name = "openai"
                azureOpenAIParameters = @{ deploymentId = "text-embedding-3-large"; resourceUri = "https://prueba.openai.azure.com" }
            }
        }
    }
    $estado.Respuestas = @(
        $def,
        @{ documentCount = 46; vectorIndexSize = 1703936 },
        @{ "@odata.count" = 46; "@search.facets" = @{ nivel_acceso = @(); area = @() } },
        @{ value = if ($modo -eq "vector-vacio") { @() } else { @(@{ id = "NOR-002-01"; titulo = "Viajes"; seccion = "Nacionales"; "@search.score" = 0.67 }) } }
    )
    $r = Ejecutar "mostrar-indice"
    if ($modo -eq "vector-vacio") {
        Comprobar ($null -ne $r.Fallo) "rechazar una prueba vectorial sin resultados"
    } else {
        Comprobar ($null -eq $r.Fallo) "mostrar índice $modo sin errores: $($r.Fallo)"
    }
    if ($modo -in @("con-vectorizador", "vector-vacio")) {
        Comprobar ($estado.Solicitudes.Count -eq 4) "consultar vectores y estadísticas"
        $vb = $estado.Solicitudes[3].Body | ConvertFrom-Json
        Comprobar ($vb.PSObject.Properties.Name -notcontains "search") "la prueba vectorial no lleva búsqueda de texto"
        Comprobar ($vb.vectorQueries[0].kind -ceq "text" -and $vb.vectorQueries[0].fields -ceq "vector") "usar el vectorizador del campo"
        if ($modo -eq "con-vectorizador") {
            Comprobar ($r.Salida -match "no demuestra su uso por el knowledge base") "no atribuir la prueba del índice al KB"
        }
    } else {
        Comprobar ($estado.Solicitudes.Count -eq 3) "no consultar vectores en $modo"
    }
    if ($modo -eq "sin-vectores") {
        Comprobar ($r.Salida -match "sin campo vectorial" -and $r.Salida -notmatch "WARNING|ADVERTENCIA") "plan B sin advertencia de vectorizador ausente"
    }
}
$estado.Respuestas = @()

Remove-Variable RetrievalDemoPruebas -Scope Global
Write-Host "OK: $script:pruebas comprobaciones locales; ninguna llamada a Azure."

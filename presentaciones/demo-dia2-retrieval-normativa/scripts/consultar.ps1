#requires -Version 7.0
<#
 Pasos 2-4 de la demo: hace una pregunta al knowledge base (retrieval agentico) y muestra
   - las subconsultas que planifico el modelo y se ejecutaron en paralelo contra el indice,
   - el filtro de seguridad aplicado (lo construye este script a partir del nivel del usuario simulado, NUNCA el modelo),
   - la respuesta con citas y los fragmentos exactos citados.
 Requiere `az login` y el rol Search Index Data Reader (o Contributor) sobre el servicio.
 Uso:  .\scripts\consultar.ps1 [-Pregunta "..."] [-Nivel publico|interno|restringido] [-Crudo]
#>
param(
    [ValidateNotNullOrEmpty()]
    [string]$Pregunta = "¿Cuál es el límite de gasto por noche en un viaje nacional y por cuántos años debo conservar los comprobantes de la rendición?",
    [ValidateSet("publico", "interno", "restringido")]
    [string]$Nivel = "interno",
    [string]$Servicio = "bci-workshop-srch-fjdb",
    [string]$KnowledgeBase = "normativa-kb",
    [string]$KnowledgeSource = "normativa-ks",
    [string]$ApiVersion = "2026-08-01-preview",
    [switch]$Crudo
)
$ErrorActionPreference = "Stop"

# Mismo criterio que normativa.construir_filtro_acceso del laboratorio: un nivel ve su nivel y los inferiores.
$Nivel = $Nivel.ToLowerInvariant()
$niveles = "publico", "interno", "restringido"
$permitidos = $niveles[0..([array]::IndexOf($niveles, $Nivel))]
$filtro = "search.in(nivel_acceso, '$($permitidos -join ',')', ',')"

$endpoint = "https://$Servicio.search.windows.net"
$token = az account get-access-token --resource https://search.azure.com --query accessToken -o tsv
if ($LASTEXITCODE -ne 0 -or [string]::IsNullOrWhiteSpace($token)) {
    throw "No se pudo obtener un token de Entra ID: revisa Azure CLI y ejecuta 'az login'."
}
$headers = @{ Authorization = "Bearer $token" }

$body = @{
    messages = @(@{ role = "user"; content = @(@{ type = "text"; text = $Pregunta }) })
    includeActivity = $true
    knowledgeSourceParams = @(@{
        knowledgeSourceName = $KnowledgeSource
        kind = "searchIndex"
        includeReferences = $true
        includeReferenceSourceData = $true
        alwaysQuerySource = $true
        filterAddOn = $filtro
    })
} | ConvertTo-Json -Depth 10

$r = Invoke-RestMethod -Method Post -Uri "$endpoint/knowledgebases/$KnowledgeBase/retrieve?api-version=$ApiVersion" `
    -Headers $headers -ContentType "application/json; charset=utf-8" -Body ([Text.Encoding]::UTF8.GetBytes($body)) -TimeoutSec 180

$plan = @($r.activity | Where-Object { $_.type -eq "modelQueryPlanning" })
$subconsultas = @($r.activity | Where-Object { $_.type -eq "searchIndex" })
$refs = @($r.references | Where-Object { $null -ne $_ })
$fuera = @($refs | Where-Object {
    $_.type -ne "searchIndex" -or $permitidos -notcontains $_.sourceData.nivel_acceso
})
$sinFiltro = @($subconsultas | Where-Object {
    $_.knowledgeSourceName -ne $KnowledgeSource -or $_.searchIndexArguments.filter -cne $filtro
})
# Validar ANTES de mostrar cualquier respuesta, también en modo -Crudo.
if ($subconsultas.Count -eq 0 -or $sinFiltro.Count -gt 0 -or $fuera.Count -gt 0) {
    throw "No se puede verificar el recorte de seguridad: se oculta toda la respuesta. Revisa activity, filtros y niveles de las referencias."
}

$respuesta = (@($r.response | ForEach-Object { $_.content } |
    Where-Object { $_.type -eq "text" } | ForEach-Object { $_.text }) -join "`n")
if ([string]::IsNullOrWhiteSpace($respuesta)) { throw "El knowledge base no devolvió una respuesta de texto." }
$citados = @([regex]::Matches($respuesta, "\[ref_id:([^\]\r\n]+)\]") |
    ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique)
$ids = @($refs | ForEach-Object { "$($_.id)" })
if (@($citados | Where-Object { $ids -cnotcontains $_ }).Count -gt 0) {
    throw "La respuesta cita referencias inexistentes: se oculta para no presentar citas no verificables."
}
if (@($refs | Where-Object {
    -not $_.docKey -or $_.sourceData.id -cne $_.docKey -or
    [string]::IsNullOrWhiteSpace($_.sourceData.contenido)
}).Count -gt 0) {
    throw "Hay referencias sin identificador o fragmento verificable: se oculta la respuesta."
}
if ($Crudo) { $r | ConvertTo-Json -Depth 20; return }

Write-Host "`nPregunta : $Pregunta" -ForegroundColor Cyan
Write-Host "Usuario  : nivel '$Nivel'  ->  filtro: $filtro" -ForegroundColor Cyan

if ($plan) { Write-Host ("`nPlanificacion del modelo: {0} ms, {1} tokens de entrada" -f $plan[0].elapsedMs, $plan[0].inputTokens) }
Write-Host "Subconsultas ejecutadas contra el indice: $($subconsultas.Count)" -ForegroundColor Yellow
$intervalos = @(foreach ($s in $subconsultas) {
    Write-Host ("  [{0}] fragmentos: {1,-3} consulta: {2}" -f $s.id, $s.count, $s.searchIndexArguments.search)
    Write-Host "      filtro: $($s.searchIndexArguments.filter)"
    if ($s.startedAt -and $s.completedAt) {
        $inicio = [datetimeoffset]$s.startedAt
        $fin = [datetimeoffset]$s.completedAt
        Write-Host ("      intervalo UTC: {0:HH:mm:ss.fff} - {1:HH:mm:ss.fff}" -f $inicio.UtcDateTime, $fin.UtcDateTime)
        [pscustomobject]@{ Inicio = $inicio; Fin = $fin }
    }
})
$solapadas = $false
for ($i = 0; $i -lt $intervalos.Count; $i++) {
    for ($j = $i + 1; $j -lt $intervalos.Count; $j++) {
        if ($intervalos[$i].Inicio -lt $intervalos[$j].Fin -and $intervalos[$j].Inicio -lt $intervalos[$i].Fin) {
            $solapadas = $true
        }
    }
}
Write-Host "Paralelismo (intervalos solapados en activity): $solapadas"

Write-Host "`nRespuesta:" -ForegroundColor Green
Write-Host $respuesta

# Fragmentos exactos usados: referencias citadas como [ref_id:N]
if ($citados.Count -eq 0) {
    Write-Warning "La respuesta no trae marcadores [ref_id:N]: no se puede verificar qué fragmentos usó. Repite la pregunta."
    Write-Host "`nReferencias recuperadas de apoyo (NO son citas verificadas):" -ForegroundColor DarkYellow
    $citados = @($refs | Sort-Object { [double]$_.rerankerScore } -Descending |
        Select-Object -First 3 | ForEach-Object { "$($_.id)" })
} else {
    Write-Host "`nCitas devueltas (fragmentos citados en la respuesta):" -ForegroundColor Green
}
foreach ($id in $citados) {
    $ref = $refs | Where-Object { "$($_.id)" -ceq $id } | Select-Object -First 1
    $d = $ref.sourceData
    Write-Host ("`n[ref_id:{0}] {1}  |  {2} > {3}  |  nivel: {4}  |  score semantico: {5:N2}" -f $id, $ref.docKey, $d.titulo, $d.seccion, $d.nivel_acceso, $ref.rerankerScore) -ForegroundColor Yellow
    Write-Host $d.contenido
}
Write-Host ("`nReferencias recuperadas: {0}; con nivel fuera del permiso del usuario: {1}" -f $refs.Count, $fuera.Count) -ForegroundColor Cyan

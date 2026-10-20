<#
.SYNOPSIS
    03_limpieza.ps1 - Elimina el grupo de recursos del laboratorio BCI Foundry después del evento.

.DESCRIPTION
    Por seguridad, SIN -ConfirmarEliminacion el script solo LISTA lo que se eliminaría (modo informativo).
    Con -ConfirmarEliminacion además exige escribir el nombre exacto del grupo de recursos (o pasarlo con
    -ConfirmarNombreGrupo) y verifica la etiqueta evento=bci-foundry-training-2026-10 para evitar borrar un
    grupo equivocado (se puede omitir con -OmitirVerificacionEtiqueta, con precaución).

    Tras eliminar, lista las cuentas de Cognitive Services en borrado temporal (soft-delete: 48 h según
    repos\publico-samples\foundry-samples\infrastructure\infrastructure-setup-bicep\deployment-tools\cleanup\README.md)
    y, con -Purgar, las purga para liberar nombres de recurso y dominios personalizados (requiere permisos
    de Contributor en la suscripción; verificar).

    NO EJECUTAR EN PRODUCCIÓN. Operación DESTRUCTIVA e IRREVERSIBLE. Solo para el grupo de recursos del
    laboratorio, DESPUÉS de exportar trazas/evidencias y confirmar con el organizador y el administrador de BCI.
    Este script no fue ejecutado por Microsoft antes de su entrega. Respeta -WhatIf / -Confirm.

.PARAMETER SubscriptionId           Id de la suscripción (obligatorio).
.PARAMETER ResourceGroup            Grupo de recursos a eliminar (obligatorio).
.PARAMETER ConfirmarEliminacion     Bandera explícita requerida para eliminar de verdad.
.PARAMETER ConfirmarNombreGrupo     Nombre del grupo de recursos repetido (si no, se pide por teclado).
.PARAMETER EtiquetaEvento           Valor esperado de la etiqueta 'evento'. Por defecto bci-foundry-training-2026-10.
.PARAMETER OmitirVerificacionEtiqueta  No exige la etiqueta del evento.
.PARAMETER Purgar                   Purga las cuentas Cognitive Services en soft-delete que pertenecían al grupo.
.PARAMETER SinEsperar               Usa --no-wait en la eliminación (no se podrá listar/purgar en la misma ejecución).

.EXAMPLE
    # Solo informar (no elimina)
    .\03_limpieza.ps1 -SubscriptionId "<SUBSCRIPTION-ID>" -ResourceGroup "rg-bci-foundry-lab-eus2"
.EXAMPLE
    # Simulación completa
    .\03_limpieza.ps1 -SubscriptionId "<SUBSCRIPTION-ID>" -ResourceGroup "rg-bci-foundry-lab-eus2" -ConfirmarEliminacion -WhatIf
.EXAMPLE
    # Eliminación real + purga
    .\03_limpieza.ps1 -SubscriptionId "<SUBSCRIPTION-ID>" -ResourceGroup "rg-bci-foundry-lab-eus2" -ConfirmarEliminacion -Purgar
#>
[CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'High')]
param(
    [Parameter(Mandatory = $true)][string]$SubscriptionId,
    [Parameter(Mandatory = $true)][string]$ResourceGroup,
    [switch]$ConfirmarEliminacion,
    [string]$ConfirmarNombreGrupo,
    [string]$EtiquetaEvento = 'bci-foundry-training-2026-10',
    [switch]$OmitirVerificacionEtiqueta,
    [switch]$Purgar,
    [switch]$SinEsperar
)

$ErrorActionPreference = 'Stop'

function Invoke-AzJson {
    param([string[]]$Argumentos)
    $salida = & az @Argumentos --only-show-errors -o json 2>&1
    if ($LASTEXITCODE -ne 0) { throw ($salida | Out-String) }
    $texto = ($salida | Out-String).Trim()
    if (-not $texto) { return $null }
    return $texto | ConvertFrom-Json
}

Write-Host '== BCI Foundry Lab :: limpieza ==' -ForegroundColor Cyan
Write-Host 'NO EJECUTAR EN PRODUCCIÓN. Operación destructiva e irreversible.' -ForegroundColor Yellow

& az account set --subscription $SubscriptionId --only-show-errors
if ($LASTEXITCODE -ne 0) { throw 'No se pudo seleccionar la suscripción. ¿Ejecutaste az login?' }

$grupo = Invoke-AzJson @('group', 'show', '--name', $ResourceGroup)
if (-not $grupo) { throw "No se encontró el grupo de recursos $ResourceGroup" }

$valorEtiqueta = $null
if ($grupo.tags) { $valorEtiqueta = $grupo.tags.evento }
if (-not $OmitirVerificacionEtiqueta -and $valorEtiqueta -ne $EtiquetaEvento) {
    throw "El grupo '$ResourceGroup' no tiene la etiqueta evento=$EtiquetaEvento (valor actual: '$valorEtiqueta'). Revisa el nombre o usa -OmitirVerificacionEtiqueta."
}

$recursos = Invoke-AzJson @('resource', 'list', '--resource-group', $ResourceGroup, '--query', '[].{nombre:name,tipo:type}')
Write-Host "`nRecursos en $ResourceGroup (ubicación: $($grupo.location)):" -ForegroundColor Cyan
if ($recursos) { $recursos | Format-Table -AutoSize | Out-String | Write-Host } else { Write-Host '(vacío)' }

$bloqueos = Invoke-AzJson @('lock', 'list', '--resource-group', $ResourceGroup)
if ($bloqueos -and @($bloqueos).Count -gt 0) {
    Write-Warning 'Hay bloqueos (locks) en el grupo o en sus recursos; la eliminación fallará hasta retirarlos.'
}

if (-not $ConfirmarEliminacion) {
    Write-Host 'Modo informativo: NO se eliminó nada. Para eliminar agrega -ConfirmarEliminacion (y prueba antes con -WhatIf).' -ForegroundColor Yellow
    exit 0
}

if (-not $ConfirmarNombreGrupo) {
    $ConfirmarNombreGrupo = Read-Host "Escribe el nombre exacto del grupo de recursos ($ResourceGroup) para confirmar"
}
if ($ConfirmarNombreGrupo -cne $ResourceGroup) {
    throw 'El nombre escrito no coincide con el grupo de recursos. Operación cancelada.'
}

$argumentosEliminar = @('group', 'delete', '--name', $ResourceGroup, '--yes')
if ($SinEsperar) { $argumentosEliminar += '--no-wait' }

if ($PSCmdlet.ShouldProcess($ResourceGroup, 'az group delete (elimina TODOS los recursos del grupo)')) {
    & az @argumentosEliminar --only-show-errors
    if ($LASTEXITCODE -ne 0) { throw 'La eliminación del grupo de recursos falló.' }
    Write-Host "Eliminación solicitada para $ResourceGroup." -ForegroundColor Green
} else {
    Write-Host '(-WhatIf) No se eliminó nada.' -ForegroundColor Yellow
}

if ($SinEsperar) {
    Write-Host 'Se usó -SinEsperar: vuelve a ejecutar el script más tarde para listar/purgar cuentas en soft-delete.' -ForegroundColor Gray
    exit 0
}

Write-Host "`nCuentas de Cognitive Services en borrado temporal (48 h) de este grupo:" -ForegroundColor Cyan
$eliminadas = Invoke-AzJson @('cognitiveservices', 'account', 'list-deleted')
$delGrupo = @($eliminadas | Where-Object { $_.id -match "/resourceGroups/$([regex]::Escape($ResourceGroup))/" })
if ($delGrupo.Count -eq 0) {
    Write-Host '(ninguna listada; verificar en el portal de Azure las cuentas eliminadas de Cognitive Services)'
} else {
    $delGrupo | Select-Object name, location | Format-Table -AutoSize | Out-String | Write-Host
    foreach ($cuenta in $delGrupo) {
        if ($Purgar) {
            if ($PSCmdlet.ShouldProcess($cuenta.name, 'az cognitiveservices account purge')) {
                & az cognitiveservices account purge --name $cuenta.name --resource-group $ResourceGroup --location $cuenta.location --only-show-errors
                if ($LASTEXITCODE -ne 0) { Write-Warning "No se pudo purgar $($cuenta.name) (¿permisos de Contributor en la suscripción?)." }
            }
        } else {
            Write-Host "Para reutilizar el nombre '$($cuenta.name)' antes de 48 h, purga con -Purgar." -ForegroundColor Gray
        }
    }
}
Write-Host 'Verifica también: grupos Entra del evento, asignaciones de rol huérfanas y alertas de presupuesto (guía, sección 12).' -ForegroundColor Gray
exit 0

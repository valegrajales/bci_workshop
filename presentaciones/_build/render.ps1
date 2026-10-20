param([string]$Pptx, [string]$OutDir, [int]$Width = 1600)
$ErrorActionPreference = 'Stop'
New-Item -ItemType Directory -Force $OutDir | Out-Null
Get-ChildItem $OutDir -Filter 'slide-*.png' | Remove-Item -Force
$ppt = New-Object -ComObject PowerPoint.Application
$pres = $ppt.Presentations.Open($Pptx, -1, 0, 0)   # ReadOnly, Untitled=false, WithWindow=false
$h = [int]($Width * 9 / 16)
$i = 0
foreach ($s in $pres.Slides) {
  $i++
  $f = Join-Path $OutDir ("slide-{0:D2}.png" -f $i)
  $s.Export($f, 'PNG', $Width, $h)
}
$pres.Close()
"exported $i slides to $OutDir"

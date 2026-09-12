[CmdletBinding()]
param([string]$TargetPath)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..')).Path
$generatorPath = Join-Path $PSScriptRoot 'sync-structure.py'
& (Join-Path $PSScriptRoot 'invoke-python.ps1') -PythonArguments @($generatorPath)
if ($LASTEXITCODE -ne 0) { throw 'Structure generation failed.' }
$repoHtmlPath = Join-Path $repoRoot 'system/repository/navigation/STRUCTURE.html'
if (-not [string]::IsNullOrWhiteSpace($TargetPath)) {
    $targetFullPath = [System.IO.Path]::GetFullPath($TargetPath)
    if ($targetFullPath -ne [System.IO.Path]::GetFullPath($repoHtmlPath)) {
        [System.IO.Directory]::CreateDirectory((Split-Path -Parent $targetFullPath)) | Out-Null
        Copy-Item -LiteralPath $repoHtmlPath -Destination $targetFullPath -Force
    }
}

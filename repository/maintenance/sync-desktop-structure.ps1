[CmdletBinding()]
param(
    [string]$TargetPath
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$generatorPath = Join-Path $PSScriptRoot 'generate-structure-html.ps1'
$repoHtmlPath = Join-Path $repoRoot 'STRUCTURE.html'

function Get-Sha256 {
    param([Parameter(Mandatory = $true)][string]$Path)

    $stream = [System.IO.File]::OpenRead($Path)
    $sha256 = [System.Security.Cryptography.SHA256]::Create()
    try {
        return ([System.BitConverter]::ToString($sha256.ComputeHash($stream))).Replace('-', '')
    }
    finally {
        $sha256.Dispose()
        $stream.Dispose()
    }
}

if ([string]::IsNullOrWhiteSpace($TargetPath)) {
    $desktopSetting = (Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders').Desktop
    $desktopPath = [Environment]::ExpandEnvironmentVariables($desktopSetting)
    $baseName = 'GitHub' + [char]0x4ED3 + [char]0x5E93 + [char]0x5B8C + [char]0x6574 + [char]0x7ED3 + [char]0x6784
    $TargetPath = Join-Path $desktopPath ($baseName + '.html')
}

$targetDirectory = Split-Path -Parent ([System.IO.Path]::GetFullPath($TargetPath))
if (-not (Test-Path -LiteralPath $targetDirectory -PathType Container)) {
    throw "Desktop target directory does not exist: $targetDirectory"
}

if (-not (Test-Path -LiteralPath $generatorPath -PathType Leaf)) {
    throw "Missing HTML generator: $generatorPath"
}

& $generatorPath -TargetPath $repoHtmlPath
& $generatorPath -TargetPath $TargetPath

$repoHash = Get-Sha256 -Path $repoHtmlPath
$desktopHash = Get-Sha256 -Path $TargetPath
if ($desktopHash -ne $repoHash) {
    throw "Desktop HTML does not match repository STRUCTURE.html: $TargetPath"
}

# The Markdown desktop mirror was replaced by the interactive HTML viewer.
$legacyMarkdownPath = [System.IO.Path]::ChangeExtension($TargetPath, '.md')
if (Test-Path -LiteralPath $legacyMarkdownPath -PathType Leaf) {
    Remove-Item -LiteralPath $legacyMarkdownPath -Force
}

Write-Host "Desktop structure HTML synchronized: $TargetPath"
Write-Host "SHA-256: $desktopHash"

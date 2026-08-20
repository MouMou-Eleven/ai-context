[CmdletBinding()]
param(
    [string]$TargetPath
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$sourcePath = Join-Path $repoRoot 'STRUCTURE.md'

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
    $targetFileName = 'GitHub' + [char]0x4ED3 + [char]0x5E93 + [char]0x5B8C + [char]0x6574 + [char]0x7ED3 + [char]0x6784 + '.md'
    $TargetPath = Join-Path $desktopPath $targetFileName
}

$targetDirectory = Split-Path -Parent $TargetPath

if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
    throw "Missing source structure file: $sourcePath"
}

if (-not (Test-Path -LiteralPath $targetDirectory -PathType Container)) {
    throw "Desktop target directory does not exist: $targetDirectory"
}

$sourceHash = Get-Sha256 -Path $sourcePath
$targetHash = $null
if (Test-Path -LiteralPath $TargetPath -PathType Leaf) {
    $targetHash = Get-Sha256 -Path $TargetPath
}

if ($sourceHash -ne $targetHash) {
    $temporaryPath = Join-Path $targetDirectory ('.github-structure-sync-' + [guid]::NewGuid().ToString('N') + '.tmp')
    try {
        [System.IO.File]::WriteAllBytes($temporaryPath, [System.IO.File]::ReadAllBytes($sourcePath))
        Move-Item -LiteralPath $temporaryPath -Destination $TargetPath -Force
    }
    finally {
        if (Test-Path -LiteralPath $temporaryPath) {
            Remove-Item -LiteralPath $temporaryPath -Force
        }
    }
}

$finalHash = Get-Sha256 -Path $TargetPath
if ($finalHash -ne $sourceHash) {
    throw "Desktop structure file hash does not match STRUCTURE.md: $TargetPath"
}

Write-Host "Desktop structure synchronized: $TargetPath"
Write-Host "SHA-256: $finalHash"

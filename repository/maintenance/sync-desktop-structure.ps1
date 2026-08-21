[CmdletBinding()]
param(
    [string]$TargetPath,
    [switch]$Strict
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

if (-not (Test-Path -LiteralPath $generatorPath -PathType Leaf)) {
    throw "Missing HTML generator: $generatorPath"
}

# Repository generation is mandatory. Desktop mirroring is recoverable and must
# never block a commit merely because Windows or the desktop drive is unavailable.
& $generatorPath -TargetPath $repoHtmlPath

try {
    if ([string]::IsNullOrWhiteSpace($TargetPath)) {
        $desktopSetting = (Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders').Desktop
        $desktopPath = [Environment]::ExpandEnvironmentVariables($desktopSetting)
        $baseName = 'GitHub' + [char]0x4ED3 + [char]0x5E93 + [char]0x5B8C + [char]0x6574 + [char]0x7ED3 + [char]0x6784
        $TargetPath = Join-Path $desktopPath ($baseName + '.html')
    }

    $targetFullPath = [System.IO.Path]::GetFullPath($TargetPath)
    $targetDirectory = Split-Path -Parent $targetFullPath
    $targetRoot = [System.IO.Path]::GetPathRoot($targetFullPath)

    if ([string]::IsNullOrWhiteSpace($targetRoot) -or -not (Test-Path -LiteralPath $targetRoot -PathType Container)) {
        throw "Desktop target drive is unavailable: $targetRoot"
    }

    if (-not (Test-Path -LiteralPath $targetDirectory -PathType Container)) {
        [System.IO.Directory]::CreateDirectory($targetDirectory) | Out-Null
    }

    $syncSucceeded = $false
    $lastSyncError = $null
    foreach ($attempt in 1..4) {
        try {
            & $generatorPath -TargetPath $targetFullPath
            $syncSucceeded = $true
            break
        }
        catch {
            $lastSyncError = $_
            if ($attempt -lt 4) {
                Start-Sleep -Milliseconds (100 * [math]::Pow(3, $attempt - 1))
            }
        }
    }

    if (-not $syncSucceeded) {
        throw "Desktop HTML remained unavailable after four attempts: $($lastSyncError.Exception.Message)"
    }

    $repoHash = Get-Sha256 -Path $repoHtmlPath
    $desktopHash = Get-Sha256 -Path $targetFullPath
    if ($desktopHash -ne $repoHash) {
        throw "Desktop HTML does not match repository STRUCTURE.html: $targetFullPath"
    }

    # The Markdown desktop mirror was replaced by the interactive HTML viewer.
    $legacyMarkdownPath = [System.IO.Path]::ChangeExtension($targetFullPath, '.md')
    if (Test-Path -LiteralPath $legacyMarkdownPath -PathType Leaf) {
        try {
            Remove-Item -LiteralPath $legacyMarkdownPath -Force
        }
        catch {
            Write-Warning "Could not remove the legacy Markdown mirror: $($_.Exception.Message)"
        }
    }

    Write-Host "Desktop structure HTML synchronized: $targetFullPath"
    Write-Host "SHA-256: $desktopHash"
}
catch {
    if ($Strict) {
        throw
    }

    Write-Warning "Desktop structure sync deferred: $($_.Exception.Message)"
    Write-Host "Repository STRUCTURE.html is current; a later Git hook or manual sync will retry the desktop mirror."
    return
}

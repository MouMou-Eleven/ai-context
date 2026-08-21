[CmdletBinding()]
param(
    [string]$TargetPath
)

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$sourcePath = Join-Path $repoRoot 'STRUCTURE.md'
$templatePath = Join-Path $PSScriptRoot 'structure-viewer.template.html'

function Get-Utf8Text {
    param([Parameter(Mandatory = $true)][string]$Path)
    return [System.Text.Encoding]::UTF8.GetString([System.IO.File]::ReadAllBytes($Path))
}

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
    $TargetPath = Join-Path $repoRoot 'STRUCTURE.html'
}

if (-not (Test-Path -LiteralPath $sourcePath -PathType Leaf)) {
    throw "Missing structure source: $sourcePath"
}

if (-not (Test-Path -LiteralPath $templatePath -PathType Leaf)) {
    throw "Missing HTML template: $templatePath"
}

$structureText = Get-Utf8Text -Path $sourcePath
$treeMatch = [regex]::Match($structureText, '(?s)```text\s*\r?\n(.*?)\r?\n```')
if (-not $treeMatch.Success) {
    throw 'STRUCTURE.md does not contain the expected text tree block.'
}

$treeText = $treeMatch.Groups[1].Value.TrimEnd()
$treeBase64 = [Convert]::ToBase64String([System.Text.Encoding]::UTF8.GetBytes($treeText))
$sourceHash = Get-Sha256 -Path $sourcePath
$dateMatch = [regex]::Match($structureText, '\*[^\r\n]*?([0-9]{4}-[0-9]{2}-[0-9]{2})\*\s*$')
$confirmedDate = if ($dateMatch.Success) { $dateMatch.Groups[1].Value } else { 'unknown' }

$template = Get-Utf8Text -Path $templatePath
$html = $template.Replace('__STRUCTURE_DATA_BASE64__', $treeBase64)
$html = $html.Replace('__SOURCE_SHA256__', $sourceHash)
$html = $html.Replace('__CONFIRMED_DATE__', $confirmedDate)

$targetDirectory = Split-Path -Parent ([System.IO.Path]::GetFullPath($TargetPath))
if (-not (Test-Path -LiteralPath $targetDirectory -PathType Container)) {
    [System.IO.Directory]::CreateDirectory($targetDirectory) | Out-Null
}

$utf8NoBom = [System.Text.UTF8Encoding]::new($false)
$existing = $null
if (Test-Path -LiteralPath $TargetPath -PathType Leaf) {
    $existing = Get-Utf8Text -Path $TargetPath
}

if ($existing -ne $html) {
    $temporaryPath = Join-Path $targetDirectory ('.structure-html-' + [guid]::NewGuid().ToString('N') + '.tmp')
    try {
        [System.IO.File]::WriteAllText($temporaryPath, $html, $utf8NoBom)
        Move-Item -LiteralPath $temporaryPath -Destination $TargetPath -Force
    }
    finally {
        if (Test-Path -LiteralPath $temporaryPath) {
            Remove-Item -LiteralPath $temporaryPath -Force
        }
    }
}

Write-Host "Structure HTML generated: $TargetPath"
Write-Host "Source SHA-256: $sourceHash"

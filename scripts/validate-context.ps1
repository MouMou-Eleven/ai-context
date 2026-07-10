[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

function Get-RelativePath {
    param([Parameter(Mandatory = $true)][string]$Path)

    $fullPath = [System.IO.Path]::GetFullPath($Path)
    if ($fullPath.StartsWith($repoRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $fullPath.Substring($repoRoot.Length).TrimStart('\', '/') -replace '\\', '/'
    }
    return $fullPath
}

function Add-ValidationError {
    param([Parameter(Mandatory = $true)][string]$Message)
    $errors.Add($Message)
}

function Test-IndexCoverage {
    param(
        [Parameter(Mandatory = $true)][string]$Directory,
        [Parameter(Mandatory = $true)][string]$IndexFile
    )

    $directoryPath = Join-Path $repoRoot $Directory
    $indexPath = Join-Path $repoRoot $IndexFile
    if (-not (Test-Path -LiteralPath $indexPath)) {
        Add-ValidationError "Missing index: $IndexFile"
        return
    }

    $indexContent = Get-Content -Raw -Encoding UTF8 -LiteralPath $indexPath
    Get-ChildItem -LiteralPath $directoryPath -Force | Where-Object {
        $_.Name -notin @('README.md') -and -not $_.Name.StartsWith('.')
    } | ForEach-Object {
        $needle = if ($_.PSIsContainer) { "$($_.Name)/" } else { $_.Name }
        if (-not $indexContent.Contains($needle)) {
            Add-ValidationError "Index '$IndexFile' does not reference '$Directory/$needle'"
        }
    }
}

Push-Location $repoRoot
try {
    $requiredFiles = @(
        'AGENTS.md',
        'README.md',
        'llms.txt',
        'STRUCTURE.md',
        'identity.md',
        'current.md',
        'preferences.md',
        'open-questions.md',
        'projects/README.md',
        'knowledge/README.md',
        'history/README.md',
        'references/README.md'
    )

    foreach ($file in $requiredFiles) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $file))) {
            Add-ValidationError "Missing required file: $file"
        }
    }

    $projectsIndex = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'projects/README.md')
    Get-ChildItem -LiteralPath (Join-Path $repoRoot 'projects') -Directory | ForEach-Object {
        $projectName = $_.Name
        $projectReadme = Join-Path $_.FullName 'README.md'
        if (-not (Test-Path -LiteralPath $projectReadme)) {
            Add-ValidationError "Project '$projectName' has no README.md"
        }
        if (-not $projectsIndex.Contains("$projectName/")) {
            Add-ValidationError "projects/README.md does not reference '$projectName/'"
        }
    }

    Get-ChildItem -LiteralPath (Join-Path $repoRoot 'projects') -Directory -Recurse |
        Where-Object { $_.Name -eq 'revisions' } |
        ForEach-Object {
            $revisionIndex = Join-Path $_.FullName 'README.md'
            if (-not (Test-Path -LiteralPath $revisionIndex)) {
                Add-ValidationError "Revision directory '$(Get-RelativePath $_.FullName)' has no README.md"
                return
            }

            $content = Get-Content -Raw -Encoding UTF8 -LiteralPath $revisionIndex
            Get-ChildItem -LiteralPath $_.FullName -File -Filter '*.md' |
                Where-Object { $_.Name -ne 'README.md' } |
                ForEach-Object {
                    if (-not $content.Contains($_.Name)) {
                        Add-ValidationError "Revision index '$(Get-RelativePath $revisionIndex)' does not reference '$($_.Name)'"
                    }
                }
        }

    $managedIndexes = @(
        @{ Directory = 'projects'; Index = 'projects/README.md' },
        @{ Directory = 'knowledge'; Index = 'knowledge/README.md' },
        @{ Directory = 'history'; Index = 'history/README.md' },
        @{ Directory = 'references'; Index = 'references/README.md' },
        @{ Directory = 'scripts'; Index = 'scripts/README.md' }
    )

    Get-ChildItem -LiteralPath (Join-Path $repoRoot 'projects') -Directory | ForEach-Object {
        $relative = Get-RelativePath $_.FullName
        $managedIndexes += @{ Directory = $relative; Index = "$relative/README.md" }
    }

    $managedIndexes += @(
        @{ Directory = 'knowledge/ai-programming'; Index = 'knowledge/ai-programming/README.md' },
        @{ Directory = 'knowledge/ai-programming/miaoda'; Index = 'knowledge/ai-programming/miaoda/README.md' },
        @{ Directory = 'knowledge/ai-video'; Index = 'knowledge/ai-video/README.md' },
        @{ Directory = 'references/video-chunked-upload'; Index = 'references/video-chunked-upload/README.md' }
    )

    foreach ($item in $managedIndexes) {
        Test-IndexCoverage -Directory $item.Directory -IndexFile $item.Index
    }

    $markdownFiles = Get-ChildItem -LiteralPath $repoRoot -Recurse -File -Filter '*.md' |
        Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' }

    foreach ($file in $markdownFiles) {
        $content = Get-Content -Raw -Encoding UTF8 -LiteralPath $file.FullName
        $matches = [regex]::Matches($content, '\[[^\]]*\]\(([^)]+)\)')
        foreach ($match in $matches) {
            $target = $match.Groups[1].Value.Trim().Trim('<', '>')
            if ($target -match '^(https?://|mailto:|#|[A-Za-z]:[/\\])') {
                continue
            }

            $pathPart = ($target -split '#', 2)[0]
            if ([string]::IsNullOrWhiteSpace($pathPart)) {
                continue
            }

            $decoded = [Uri]::UnescapeDataString($pathPart)
            $resolved = Join-Path $file.DirectoryName $decoded
            if (-not (Test-Path -LiteralPath $resolved)) {
                Add-ValidationError "Broken link in '$(Get-RelativePath $file.FullName)': $target"
            }
        }

        if ($file.Name -eq 'README.md' -and $file.Length -gt 16384) {
            $warnings.Add("Large README may slow routing: $(Get-RelativePath $file.FullName) ($($file.Length) bytes)")
        }
    }

    Write-Host "Context validation scanned $($markdownFiles.Count) Markdown files."
    foreach ($warning in $warnings) {
        Write-Warning $warning
    }

    if ($errors.Count -gt 0) {
        Write-Host "Validation failed with $($errors.Count) error(s):" -ForegroundColor Red
        foreach ($validationError in $errors) {
            Write-Host "- $validationError" -ForegroundColor Red
        }
        exit 1
    }

    Write-Host 'Validation passed: required entries, indexes, projects, revisions, and relative links are consistent.' -ForegroundColor Green
    exit 0
}
finally {
    Pop-Location
}

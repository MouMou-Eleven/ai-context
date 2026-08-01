[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

function Get-RelativePath {
    param([Parameter(Mandatory = $true)][string]$Path)

    $fullPath = [System.IO.Path]::GetFullPath($Path)
    $rootWithSeparator = $repoRoot.TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar
    if ($fullPath.StartsWith($rootWithSeparator, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $fullPath.Substring($rootWithSeparator.Length) -replace '\\', '/'
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
    if (-not (Test-Path -LiteralPath $directoryPath -PathType Container)) {
        Add-ValidationError "Missing managed directory: $Directory"
        return
    }
    if (-not (Test-Path -LiteralPath $indexPath -PathType Leaf)) {
        Add-ValidationError "Missing index: $IndexFile"
        return
    }

    $indexContent = Get-Content -Raw -Encoding UTF8 -LiteralPath $indexPath
    Get-ChildItem -LiteralPath $directoryPath -Force | Where-Object {
        $_.Name -ne 'README.md' -and -not $_.Name.StartsWith('.')
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
        'README.md',
        'AGENTS.md',
        'llms.txt',
        'STRUCTURE.md',
        'personal/README.md',
        'personal/identity.md',
        'personal/current-focus.md',
        'personal/open-questions.md',
        'expression/README.md',
        'projects/README.md',
        'projects/ai-training/README.md',
        'projects/microcourse/README.md',
        'knowledge/README.md',
        'repository/README.md',
        'repository/versioned-knowledge-policy.md',
        'history/README.md'
    )

    foreach ($file in $requiredFiles) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $file) -PathType Leaf)) {
            Add-ValidationError "Missing required file: $file"
        }
    }

    $prohibitedRootEntries = @(
        'identity.md',
        'current.md',
        'preferences.md',
        'open-questions.md',
        'references',
        'scripts'
    )
    foreach ($entry in $prohibitedRootEntries) {
        if (Test-Path -LiteralPath (Join-Path $repoRoot $entry)) {
            Add-ValidationError "Deprecated root entry still exists: $entry"
        }
    }

    $rootReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'README.md')
    foreach ($directory in @('personal', 'expression', 'projects', 'knowledge', 'repository', 'history')) {
        if (-not $rootReadme.Contains("$directory/")) {
            Add-ValidationError "README.md does not reference top-level directory '$directory/'"
        }
    }

    $projectsIndex = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'projects/README.md')
    Get-ChildItem -LiteralPath (Join-Path $repoRoot 'projects') -Directory | ForEach-Object {
        $projectName = $_.Name
        $projectReadme = Join-Path $_.FullName 'README.md'
        if (-not (Test-Path -LiteralPath $projectReadme -PathType Leaf)) {
            Add-ValidationError "Project or work area '$projectName' has no README.md"
        }
        if (-not $projectsIndex.Contains("$projectName/")) {
            Add-ValidationError "projects/README.md does not reference '$projectName/'"
        }
    }

    $trainingReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'projects/ai-training/README.md')
    $microcourseReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'projects/microcourse/README.md')
    if (-not $trainingReadme.Contains('../microcourse/')) {
        Add-ValidationError "AI training README must state that microcourse work is outside its scope"
    }
    if (-not $microcourseReadme.Contains('../ai-training/')) {
        Add-ValidationError "Microcourse README must state its peer-level boundary with AI training"
    }

    Get-ChildItem -LiteralPath (Join-Path $repoRoot 'projects') -Directory -Recurse |
        Where-Object { $_.Name -eq 'revisions' } |
        ForEach-Object {
            $revisionIndex = Join-Path $_.FullName 'README.md'
            if (-not (Test-Path -LiteralPath $revisionIndex -PathType Leaf)) {
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

    $managedDirectories = @('personal', 'expression', 'projects', 'knowledge', 'repository', 'history')
    Get-ChildItem -LiteralPath $repoRoot -Directory -Recurse | ForEach-Object {
        $readme = Join-Path $_.FullName 'README.md'
        if (Test-Path -LiteralPath $readme -PathType Leaf) {
            $relativeDirectory = Get-RelativePath $_.FullName
            if ($relativeDirectory -notmatch '(^|/)\.git($|/)') {
                $managedDirectories += $relativeDirectory
            }
        }
    }
    $managedDirectories | Sort-Object -Unique | ForEach-Object {
        Test-IndexCoverage -Directory $_ -IndexFile "$_/README.md"
    }

    Get-ChildItem -LiteralPath (Join-Path $repoRoot 'projects') -File -Recurse -Filter 'version-features.md' |
        ForEach-Object {
            $productDirectory = $_.DirectoryName
            $productReadme = Join-Path $productDirectory 'README.md'
            if (-not (Test-Path -LiteralPath $productReadme -PathType Leaf)) {
                Add-ValidationError "Dynamic product directory '$(Get-RelativePath $productDirectory)' has no README.md"
                return
            }

            $productContent = Get-Content -Raw -Encoding UTF8 -LiteralPath $productReadme
            $versionContent = Get-Content -Raw -Encoding UTF8 -LiteralPath $_.FullName
            if (-not $productContent.Contains('versioned-knowledge-policy.md')) {
                Add-ValidationError "Dynamic product README '$(Get-RelativePath $productReadme)' does not reference version governance"
            }
            if (-not $versionContent.Contains('Status: historical reference, not current capability.')) {
                Add-ValidationError "Version file '$(Get-RelativePath $_.FullName)' is not clearly marked as history"
            }
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

    Write-Host 'Validation passed: hierarchy, indexes, project boundaries, revisions, dynamic knowledge, and relative links are consistent.' -ForegroundColor Green
    exit 0
}
finally {
    Pop-Location
}

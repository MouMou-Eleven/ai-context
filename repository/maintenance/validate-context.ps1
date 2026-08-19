[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$errors = [System.Collections.Generic.List[string]]::new()
$warnings = [System.Collections.Generic.List[string]]::new()

function Get-RepoRelativePath {
    param([Parameter(Mandatory = $true)][string]$Path)

    $fullPath = [System.IO.Path]::GetFullPath($Path)
    $prefix = $repoRoot.TrimEnd('\', '/') + [System.IO.Path]::DirectorySeparatorChar
    if ($fullPath.StartsWith($prefix, [System.StringComparison]::OrdinalIgnoreCase)) {
        return $fullPath.Substring($prefix.Length) -replace '\\', '/'
    }
    return $fullPath
}

function Add-ValidationError {
    param([Parameter(Mandatory = $true)][string]$Message)
    $errors.Add($Message)
}

Push-Location $repoRoot
try {
    $requiredFiles = @(
        '.gitattributes',
        '.gitignore',
        'README.md',
        'AGENTS.md',
        'llms.txt',
        'STRUCTURE.md',
        'personal/README.md',
        'personal/profile.md',
        'personal/business-overview.md',
        'personal/credentials.md',
        'personal/growth-path.md',
        'personal/capabilities.md',
        'brain/README.md',
        'brain/thinking-and-decisions.md',
        'brain/business-cognition.md',
        'brain/ai-expression/README.md',
        'brain/ai-expression/cross-domain-rules.md',
        'brain/ai-expression/oral-expression/README.md',
        'brain/ai-expression/written-expression/README.md',
        'brain/ai-expression/experience/README.md',
        'brain/ai-expression/chinese-datasets/README.md',
        'work/README.md',
        'work/design/README.md',
        'work/ai/README.md',
        'work/ai/programming/README.md',
        'work/ai/training/README.md',
        'work/ai/video/README.md',
        'work/ai/publishing/README.md',
        'work/ai/self-media/README.md',
        'work/other/README.md',
        'repository/README.md',
        'repository/environment/README.md',
        'repository/versioned-knowledge-policy.md',
        'history/README.md'
    )

    foreach ($file in $requiredFiles) {
        if (-not (Test-Path -LiteralPath (Join-Path $repoRoot $file) -PathType Leaf)) {
            Add-ValidationError "Missing required file: $file"
        }
    }

    foreach ($deprecatedDirectory in @('expression', 'knowledge', 'projects')) {
        $deprecatedPath = Join-Path $repoRoot $deprecatedDirectory
        if (Test-Path -LiteralPath $deprecatedPath) {
            $legacyFiles = @(Get-ChildItem -LiteralPath $deprecatedPath -Recurse -File -Force)
            if ($legacyFiles.Count -gt 0) {
                Add-ValidationError "Deprecated top-level directory still contains files: $deprecatedDirectory/"
            }
        }
    }

    if (Test-Path -LiteralPath (Join-Path $repoRoot 'brain/personal-expression.md')) {
        Add-ValidationError 'Legacy personal-expression.md still exists; current Chinese expression rules belong under brain/ai-expression/.'
    }

    $rootReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'README.md')
    $agents = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'AGENTS.md')
    $llms = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'llms.txt')
    $structure = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'STRUCTURE.md')
    foreach ($directory in @('personal', 'brain', 'work', 'repository', 'history')) {
        if (-not $rootReadme.Contains("$directory/")) {
            Add-ValidationError "README.md does not reference top-level directory '$directory/'"
        }
        if (-not $structure.Contains("$directory/")) {
            Add-ValidationError "STRUCTURE.md does not reference top-level directory '$directory/'"
        }
    }

    foreach ($routingFile in @(
        @{ Name = 'AGENTS.md'; Content = $agents },
        @{ Name = 'llms.txt'; Content = $llms }
    )) {
        if (-not $routingFile.Content.Contains('brain/ai-expression/README.md')) {
            Add-ValidationError "$($routingFile.Name) does not define the AI expression default entry."
        }
        if (-not $routingFile.Content.Contains('brain/ai-expression/cross-domain-rules.md')) {
            Add-ValidationError "$($routingFile.Name) does not define the default cross-domain Chinese quality rules."
        }
        if (-not $routingFile.Content.Contains('brain/ai-expression/experience/README.md')) {
            Add-ValidationError "$($routingFile.Name) does not define the default AI expression experience index."
        }
    }

    if (-not $structure.Contains('ai-expression/')) {
        Add-ValidationError 'STRUCTURE.md does not include the AI expression hierarchy.'
    }

    $requiredWorkDirectories = @(
        'work/design/ppt-design',
        'work/design/poster-fold-design',
        'work/design/book-design',
        'work/design/microcourse-mg-animation',
        'work/design/ae-promo-video',
        'work/design/ai-design',
        'work/ai/programming/tools',
        'work/ai/programming/experience',
        'work/ai/programming/projects',
        'work/ai/training/experience',
        'work/ai/training/outlines',
        'work/ai/training/materials',
        'work/ai/training/projects',
        'work/ai/video/common',
        'work/ai/video/types',
        'work/ai/video/tools',
        'work/ai/video/projects',
        'work/ai/publishing/projects',
        'work/ai/self-media/titles',
        'work/ai/self-media/articles',
        'work/ai/self-media/video-scripts',
        'work/ai/self-media/live-sales',
        'work/ai/self-media/experience'
    )

    foreach ($directory in $requiredWorkDirectories) {
        $readme = Join-Path $repoRoot "$directory/README.md"
        if (-not (Test-Path -LiteralPath $readme -PathType Leaf)) {
            Add-ValidationError "Managed work directory has no README.md: $directory/"
        }
    }

    $trainingReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'work/ai/training/README.md')
    $selfMediaReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'work/ai/self-media/README.md')
    $publishingReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'work/ai/publishing/README.md')
    $microcourseReadme = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'work/design/microcourse-mg-animation/README.md')
    if (-not $trainingReadme.Contains('../self-media/')) {
        Add-ValidationError 'AI training README must state its boundary with self-media.'
    }
    if (-not $selfMediaReadme.Contains('../training/')) {
        Add-ValidationError 'AI self-media README must state its boundary with AI training.'
    }
    if (-not $microcourseReadme.Contains('../../ai/training/')) {
        Add-ValidationError 'Microcourse README must link to the separate AI training area.'
    }

    foreach ($domainReadme in @(
        @{ Name = 'AI training'; Content = $trainingReadme },
        @{ Name = 'AI self-media'; Content = $selfMediaReadme },
        @{ Name = 'AI publishing'; Content = $publishingReadme }
    )) {
        if (-not $domainReadme.Content.Contains('brain/ai-expression/')) {
            Add-ValidationError "$($domainReadme.Name) README must compose its rules with the AI expression base layer."
        }
    }

    $markdownFiles = Get-ChildItem -LiteralPath $repoRoot -Recurse -File -Filter '*.md' |
        Where-Object { $_.FullName -notmatch '[\\/]\.git[\\/]' }

    foreach ($file in $markdownFiles) {
        $content = Get-Content -Raw -Encoding UTF8 -LiteralPath $file.FullName
        $links = [regex]::Matches($content, '\[[^\]]*\]\(([^)]+)\)')
        foreach ($link in $links) {
            $target = $link.Groups[1].Value.Trim().Trim('<', '>')
            if ($target -match '^(https?://|mailto:|#|[A-Za-z]:[/\\])') {
                continue
            }

            $pathPart = ($target -split '#', 2)[0]
            if ([string]::IsNullOrWhiteSpace($pathPart)) {
                continue
            }

            $resolved = Join-Path $file.DirectoryName ([Uri]::UnescapeDataString($pathPart))
            if (-not (Test-Path -LiteralPath $resolved)) {
                Add-ValidationError "Broken link in '$(Get-RepoRelativePath $file.FullName)': $target"
            }
        }
    }

    $textFiles = Get-ChildItem -LiteralPath $repoRoot -Recurse -File |
        Where-Object {
            $_.FullName -notmatch '[\\/]\.git[\\/]' -and
            $_.Extension -in @('.md', '.txt', '.ps1', '.ts')
        }

    foreach ($file in $textFiles) {
        $content = Get-Content -Raw -Encoding UTF8 -LiteralPath $file.FullName
        $secretPattern = "(?im)^\s*(api[_-]?key|token|password|cookie)\s*[:=]\s*[\x22\x27]?[A-Za-z0-9_\-]{16,}"
        if ($content -match $secretPattern) {
            Add-ValidationError "Possible secret in '$(Get-RepoRelativePath $file.FullName)'"
        }
    }

    $duplicateGroups = Get-ChildItem -LiteralPath $repoRoot -Recurse -File |
        Where-Object {
            $_.FullName -notmatch '[\\/]\.git[\\/]' -and
            $_.Length -gt 0 -and
            $_.Name -ne 'README.md'
        } |
        Get-FileHash -Algorithm SHA256 |
        Group-Object Hash |
        Where-Object Count -gt 1

    foreach ($group in $duplicateGroups) {
        $paths = ($group.Group.Path | ForEach-Object { Get-RepoRelativePath $_ }) -join ', '
        $warnings.Add("Exact duplicate content: $paths")
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

    Write-Host 'Validation passed: hierarchy, boundaries, links, deprecated paths, and sensitive-data checks are consistent.' -ForegroundColor Green
    exit 0
}
finally {
    Pop-Location
}

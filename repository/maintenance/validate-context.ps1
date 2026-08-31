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

Push-Location $repoRoot
try {
    $requiredFiles = @(
        '.gitattributes',
        '.gitignore',
        'README.md',
        'AGENTS.md',
        'llms.txt',
        'STRUCTURE.md',
        'STRUCTURE.html',
        'personal/README.md',
        'personal/profile.md',
        'personal/business-overview.md',
        'personal/credentials.md',
        'personal/growth-path.md',
        'personal/capabilities.md',
        'brain/README.md',
        'brain/cognition/README.md',
        'brain/cognition/thinking-and-decisions.md',
        'brain/cognition/business-cognition.md',
        'brain/ai-expression/README.md',
        'brain/ai-expression/cross-domain-rules.md',
        'brain/ai-expression/oral-expression/README.md',
        'brain/ai-expression/written-expression/README.md',
        'brain/ai-expression/experience/README.md',
        'brain/ai-expression/chinese-datasets/README.md',
        'brain/ai-expression/chinese-datasets/grammar-and-error-checklist.md',
        'work/README.md',
        'work/design/README.md',
        'work/ai/README.md',
        'work/ai/programming/README.md',
        'work/ai/training/README.md',
        'work/ai/video/README.md',
        'work/ai/publishing/README.md',
        'work/ai/self-media/README.md',
        'work/other/README.md',
        'work/other/commercial/README.md',
        'work/other/commercial/experience/README.md',
        'work/other/commercial/experience/content-demand-and-conversion.md',
        'work/other/commercial/experience/external-deliverable-language.md',
        'repository/README.md',
        'repository/environment/README.md',
        'repository/versioned-knowledge-policy.md',
        'repository/maintenance/generate-structure-html.ps1',
        'repository/maintenance/structure-viewer.template.html',
        'repository/maintenance/sync-desktop-structure.ps1',
        'repository/maintenance/git-hooks/pre-commit',
        'repository/maintenance/git-hooks/post-commit',
        'repository/maintenance/git-hooks/post-merge',
        'repository/maintenance/git-hooks/post-checkout',
        'repository/maintenance/git-hooks/post-rewrite',
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

    foreach ($legacyCognitionFile in @('brain/thinking-and-decisions.md', 'brain/business-cognition.md')) {
        if (Test-Path -LiteralPath (Join-Path $repoRoot $legacyCognitionFile)) {
            Add-ValidationError "Legacy cognition file still exists at the brain root: $legacyCognitionFile"
        }
    }

    if (Test-Path -LiteralPath (Join-Path $repoRoot 'work/ai/commercial')) {
        Add-ValidationError 'Commercial delivery still exists under work/ai/; the current location is work/other/commercial/.'
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
        if (-not $routingFile.Content.Contains('brain/ai-expression/chinese-datasets/grammar-and-error-checklist.md')) {
            Add-ValidationError "$($routingFile.Name) does not define the default Chinese grammar and error checklist."
        }
        if (-not $routingFile.Content.Contains('brain/cognition/README.md')) {
            Add-ValidationError "$($routingFile.Name) does not define the current cognition entry."
        }
        if (-not $routingFile.Content.Contains('work/other/commercial/experience/content-demand-and-conversion.md')) {
            Add-ValidationError "$($routingFile.Name) does not define the cross-industry content demand and conversion method."
        }
    }

    if (-not $structure.Contains('ai-expression/')) {
        Add-ValidationError 'STRUCTURE.md does not include the AI expression hierarchy.'
    }

    if (-not $agents.Contains('publish-policy: direct-main-no-pr')) {
        Add-ValidationError 'AGENTS.md does not define the user-confirmed direct-to-main publishing rule.'
    }

    foreach ($routingFile in @(
        @{ Name = 'AGENTS.md'; Content = $agents },
        @{ Name = 'llms.txt'; Content = $llms },
        @{ Name = 'README.md'; Content = $rootReadme }
    )) {
        if (-not $routingFile.Content.Contains('work/other/commercial/')) {
            Add-ValidationError "$($routingFile.Name) does not route commercial delivery through work/other/commercial/."
        }
    }

    $desktopStructureBaseName = 'GitHub' + [char]0x4ED3 + [char]0x5E93 + [char]0x5B8C + [char]0x6574 + [char]0x7ED3 + [char]0x6784
    try {
        $desktopSetting = (Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders').Desktop
        $desktopDirectory = [Environment]::ExpandEnvironmentVariables($desktopSetting)
        $desktopStructureFileName = $desktopStructureBaseName + '.html'
        $desktopStructurePath = Join-Path $desktopDirectory $desktopStructureFileName
        $legacyDesktopMarkdownPath = Join-Path $desktopDirectory ($desktopStructureBaseName + '.md')
        if (Test-Path -LiteralPath $desktopDirectory -PathType Container) {
            if (-not (Test-Path -LiteralPath $desktopStructurePath -PathType Leaf)) {
                $warnings.Add("Desktop structure mirror is currently missing and will be recreated by the next sync: $desktopStructurePath")
            }
            else {
                $repoHtmlHash = Get-Sha256 -Path (Join-Path $repoRoot 'STRUCTURE.html')
                $desktopStructureHash = Get-Sha256 -Path $desktopStructurePath
                if ($repoHtmlHash -ne $desktopStructureHash) {
                    Add-ValidationError "Desktop structure mirror is not synchronized: $desktopStructurePath"
                }
            }
            if (Test-Path -LiteralPath $legacyDesktopMarkdownPath -PathType Leaf) {
                Add-ValidationError "Legacy desktop Markdown mirror still exists: $legacyDesktopMarkdownPath"
            }
        }
        else {
            $warnings.Add("Desktop directory is currently unavailable; repository validation continued: $desktopDirectory")
        }
    }
    catch {
        $warnings.Add("Desktop mirror check was skipped because Windows desktop discovery failed: $($_.Exception.Message)")
    }

    $sourceStructureHash = Get-Sha256 -Path (Join-Path $repoRoot 'STRUCTURE.md')
    $generatedHtml = Get-Content -Raw -Encoding UTF8 -LiteralPath (Join-Path $repoRoot 'STRUCTURE.html')
    if (-not $generatedHtml.Contains($sourceStructureHash)) {
        Add-ValidationError 'STRUCTURE.html was not generated from the current STRUCTURE.md content.'
    }

    $treeMatch = [regex]::Match($structure, '(?s)```text\s*\r?\n(.*?)\r?\n```')
    if (-not $treeMatch.Success) {
        Add-ValidationError 'STRUCTURE.md does not contain the expected complete tree block.'
    }
    else {
        $documentedPaths = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
        $pathByDepth = [System.Collections.Generic.Dictionary[int, string]]::new()
        foreach ($treeLine in ($treeMatch.Groups[1].Value -split '\r?\n')) {
            # Unicode escapes keep the box-drawing parser stable when Windows PowerShell 5.1
            # reads this UTF-8-without-BOM script.
            $branchMatch = [regex]::Match($treeLine, '^((?:(?:\u2502   |    ))*)(?:\u251C\u2500\u2500 |\u2514\u2500\u2500 )(.+)$')
            if (-not $branchMatch.Success) {
                continue
            }

            $depth = [int]($branchMatch.Groups[1].Value.Length / 4) + 1
            $name = ($branchMatch.Groups[2].Value.Trim() -split '\s{2,}', 2)[0].TrimEnd('/')
            $parentPath = if ($depth -eq 1) { '' } else { $pathByDepth[$depth - 1] }
            $documentedPath = if ([string]::IsNullOrWhiteSpace($parentPath)) { $name } else { "$parentPath/$name" }
            $pathByDepth[$depth] = $documentedPath
            $null = $documentedPaths.Add($documentedPath)
        }

        $vendorSnapshotRoots = [System.Collections.Generic.List[string]]::new()
        $skillRepositoryRoot = Join-Path $repoRoot 'work/ai/programming/experience/skill-repository'
        if (Test-Path -LiteralPath $skillRepositoryRoot -PathType Container) {
            $skillDirectories = @(Get-ChildItem -LiteralPath $skillRepositoryRoot -Directory -Force)
            foreach ($skillDirectory in $skillDirectories) {
                $skillReadmePath = Join-Path $skillDirectory.FullName 'README.md'
                $skillMetadataPath = Join-Path $skillDirectory.FullName 'upstream.json'
                if (-not (Test-Path -LiteralPath $skillReadmePath -PathType Leaf)) {
                    Add-ValidationError "Skill repository entry has no README.md: $(Get-RepoRelativePath $skillDirectory.FullName)/"
                }
                if (-not (Test-Path -LiteralPath $skillMetadataPath -PathType Leaf)) {
                    Add-ValidationError "Skill repository entry has no upstream.json: $(Get-RepoRelativePath $skillDirectory.FullName)/"
                    continue
                }

                try {
                    $skillMetadata = Get-Content -Raw -Encoding UTF8 -LiteralPath $skillMetadataPath | ConvertFrom-Json
                }
                catch {
                    Add-ValidationError "Skill repository metadata is invalid JSON: $(Get-RepoRelativePath $skillMetadataPath)"
                    continue
                }

                if ([string]::IsNullOrWhiteSpace([string]$skillMetadata.id) -or
                    [string]::IsNullOrWhiteSpace([string]$skillMetadata.storageMode) -or
                    [string]::IsNullOrWhiteSpace([string]$skillMetadata.sourcePath)) {
                    Add-ValidationError "Skill repository metadata is missing id, storageMode, or sourcePath: $(Get-RepoRelativePath $skillMetadataPath)"
                    continue
                }

                $skillSourcePath = Join-Path $skillDirectory.FullName ([string]$skillMetadata.sourcePath)
                if (-not (Test-Path -LiteralPath $skillSourcePath -PathType Container)) {
                    Add-ValidationError "Skill repository sourcePath does not exist: $(Get-RepoRelativePath $skillSourcePath)"
                    continue
                }

                if ([string]$skillMetadata.storageMode -eq 'full-repository-snapshot') {
                    if ([string]::IsNullOrWhiteSpace([string]$skillMetadata.upstreamRepository) -or
                        [string]::IsNullOrWhiteSpace([string]$skillMetadata.commit) -or
                        [string]::IsNullOrWhiteSpace([string]$skillMetadata.defaultBranch)) {
                        Add-ValidationError "Full Skill snapshot metadata is missing upstreamRepository, defaultBranch, or commit: $(Get-RepoRelativePath $skillMetadataPath)"
                    }

                    $relativeSnapshotRoot = (Get-RepoRelativePath $skillSourcePath).TrimEnd('/')
                    if (-not $documentedPaths.Contains($relativeSnapshotRoot)) {
                        Add-ValidationError "STRUCTURE.md is missing full Skill snapshot root: $relativeSnapshotRoot"
                    }
                    $vendorSnapshotRoots.Add($relativeSnapshotRoot)
                }
            }
        }

        $actualFiles = Get-ChildItem -LiteralPath $repoRoot -Recurse -File -Force |
            Where-Object { $_.FullName -notmatch '[\\/]\.git(?:[\\/]|$)' }
        foreach ($fileEntry in $actualFiles) {
            $relativeFile = Get-RepoRelativePath $fileEntry.FullName
            $isVendorSnapshotFile = $false
            foreach ($snapshotRoot in $vendorSnapshotRoots) {
                if ($relativeFile.StartsWith("$snapshotRoot/", [System.StringComparison]::OrdinalIgnoreCase)) {
                    $isVendorSnapshotFile = $true
                    break
                }
            }
            if ($isVendorSnapshotFile) {
                continue
            }

            if (-not $documentedPaths.Contains($relativeFile)) {
                Add-ValidationError "STRUCTURE.md is missing repository entry: $relativeFile"
            }

            $parentDirectory = $fileEntry.Directory
            while ($null -ne $parentDirectory -and $parentDirectory.FullName -ne $repoRoot) {
                $relativeDirectory = Get-RepoRelativePath $parentDirectory.FullName
                if (-not $documentedPaths.Contains($relativeDirectory)) {
                    Add-ValidationError "STRUCTURE.md is missing repository directory: $relativeDirectory"
                }
                $parentDirectory = $parentDirectory.Parent
            }
        }
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
        'work/ai/programming/experience/skill-repository',
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
        'work/ai/self-media/experience',
        'work/other/commercial',
        'work/other/commercial/experience'
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

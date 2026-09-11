[CmdletBinding()]
param()

$ErrorActionPreference = 'Stop'
$validatorPath = Join-Path $PSScriptRoot 'validate-context.py'
& (Join-Path $PSScriptRoot 'invoke-python.ps1') -PythonArguments @($validatorPath)
exit $LASTEXITCODE

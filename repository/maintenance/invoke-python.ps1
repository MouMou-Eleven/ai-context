[CmdletBinding()]
param([Parameter(Mandatory = $true)][string[]]$PythonArguments)

$ErrorActionPreference = 'Stop'
$env:PYTHONUTF8 = '1'
foreach ($candidate in @('python', 'python3', 'py')) {
    $commands = @(Get-Command $candidate -CommandType Application -ErrorAction SilentlyContinue)
    $prefix = if ($candidate -eq 'py') { @('-3') } else { @() }
    foreach ($command in $commands) {
        & $command.Source @prefix -c 'import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)' 2>$null
        if ($LASTEXITCODE -ne 0) { continue }
        & $command.Source @prefix -B @PythonArguments
        exit $LASTEXITCODE
    }
}
throw 'A working Python 3.10+ runtime is required for context maintenance.'

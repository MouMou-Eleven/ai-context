"""Validate the exact Git index snapshot; never stage or modify user files."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
from context_common import ROOT, clean_git_environment, git


def check_staged(root=ROOT):
    root = Path(root).resolve()
    if git(root, 'ls-files', '--unmerged', inherit_repository_env=True):
        print('Unmerged index entries prevent validation.', file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory(prefix='ai-context-index-') as folder:
        snapshot = Path(folder)
        git(root, 'checkout-index', '--all', '--force', '--prefix=' + snapshot.as_posix().rstrip('/') + '/', inherit_repository_env=True)
        validator = snapshot / 'repository/maintenance/validate-context.py'
        if not validator.is_file():
            print('Stage the portable validator before using this hook.', file=sys.stderr)
            return 1
        env = dict(clean_git_environment(), PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
        # All validation inputs and executable checks come from the exported index.
        result = subprocess.run([sys.executable, '-B', str(validator), '--root', str(snapshot)], cwd=snapshot, env=env)
        if result.returncode:
            print('Staged snapshot failed. Regenerate outputs, review, and explicitly stage matching inputs and outputs.', file=sys.stderr)
            return result.returncode
        return subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', str(snapshot / 'repository/maintenance/tests'), '-v'], cwd=snapshot, env=env).returncode


if __name__ == '__main__':
    raise SystemExit(check_staged())

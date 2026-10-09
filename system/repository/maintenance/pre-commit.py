"""Validate the exact Git index snapshot; never stage or modify user files."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
from context_common import ROOT, clean_git_environment, git


def behind_upstream(root):
    """Refuse commits from a clone that is behind GitHub: old clones carry old rules."""
    try:
        subprocess.run(['git', '-C', str(root), 'fetch', '--quiet'], timeout=20,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except (OSError, subprocess.SubprocessError):
        pass
    result = subprocess.run(['git', '-C', str(root), 'rev-list', '--count', 'HEAD..@{upstream}'],
                            capture_output=True, text=True)
    return int(result.stdout.strip()) if result.returncode == 0 and result.stdout.strip().isdigit() else 0


def check_staged(root=ROOT):
    root = Path(root).resolve()
    behind = behind_upstream(root)
    if behind:
        print(f'本地仓库落后 GitHub {behind} 个提交。先 git pull，再按最新规则重新确认写入位置后提交。', file=sys.stderr)
        return 1
    if git(root, 'ls-files', '--unmerged', inherit_repository_env=True):
        print('Unmerged index entries prevent validation.', file=sys.stderr)
        return 1
    with tempfile.TemporaryDirectory(prefix='ai-context-index-') as folder:
        snapshot = Path(folder)
        git(root, 'checkout-index', '--all', '--force', '--prefix=' + snapshot.as_posix().rstrip('/') + '/', inherit_repository_env=True)
        validator = snapshot / 'system/repository/maintenance/validate-context.py'
        if not validator.is_file():
            print('Stage the portable validator before using this hook.', file=sys.stderr)
            return 1
        env = dict(clean_git_environment(), PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='1')
        # All validation inputs and executable checks come from the exported index.
        result = subprocess.run([sys.executable, '-B', str(validator), '--root', str(snapshot)], cwd=snapshot, env=env)
        if result.returncode:
            print('Staged snapshot failed. Regenerate outputs, review, and explicitly stage matching inputs and outputs.', file=sys.stderr)
            return result.returncode
        return subprocess.run([sys.executable, '-B', '-m', 'unittest', 'discover', '-s', str(snapshot / 'system/repository/maintenance/tests'), '-v'], cwd=snapshot, env=env).returncode


if __name__ == '__main__':
    raise SystemExit(check_staged())

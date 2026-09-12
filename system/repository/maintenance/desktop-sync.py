"""Best-effort Windows desktop mirror without changing system/repository files."""
import hashlib
import os
from pathlib import Path
import tempfile
from context_common import ROOT


def sync():
    if os.name != 'nt':
        return
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders') as key:
            desktop = Path(os.path.expandvars(winreg.QueryValueEx(key, 'Desktop')[0]))
        if not desktop.is_dir():
            raise OSError('Windows desktop is unavailable')
        target = desktop / 'GitHub仓库完整结构.html'
        data = (ROOT / 'system/repository/navigation/STRUCTURE.html').read_bytes()
        if target.is_file() and target.read_bytes() == data:
            return
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=desktop, prefix='.ai-context-', suffix='.tmp', delete=False) as handle:
                temporary = Path(handle.name)
                handle.write(data)
            os.replace(temporary, target)
            if hashlib.sha256(target.read_bytes()).digest() != hashlib.sha256(data).digest():
                raise OSError('Desktop mirror hash differs')
        finally:
            if temporary and temporary.exists():
                temporary.unlink()
        print('Desktop structure mirror synchronized.')
    except (OSError, ImportError) as exc:
        print(f'Desktop mirror deferred: {exc}')


if __name__ == '__main__':
    sync()

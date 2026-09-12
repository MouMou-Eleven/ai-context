"""Shared standard-library helpers for working trees and exported Git indexes."""
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[3]
MAINTENANCE = 'system/repository/maintenance'
NAVIGATION = 'system/repository/navigation'

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, 'reconfigure'):
        stream.reconfigure(encoding='utf-8')


def load_module(name, root=ROOT):
    spec = importlib.util.spec_from_file_location(name.replace('-', '_'), root / MAINTENANCE / (name + '.py'))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def clean_git_environment():
    env = dict(os.environ)
    try:
        local_names = subprocess.check_output(['git', 'rev-parse', '--local-env-vars'], stderr=subprocess.DEVNULL).decode('ascii').splitlines()
    except (FileNotFoundError, subprocess.CalledProcessError):
        local_names = ['GIT_DIR', 'GIT_WORK_TREE', 'GIT_INDEX_FILE', 'GIT_PREFIX', 'GIT_COMMON_DIR', 'GIT_OBJECT_DIRECTORY', 'GIT_ALTERNATE_OBJECT_DIRECTORIES']
    for name in local_names:
        env.pop(name, None)
    return env


def git(root, *args, inherit_repository_env=False):
    env = None if inherit_repository_env else clean_git_environment()
    return subprocess.check_output(['git', '-c', 'safe.directory=' + str(root), '-C', str(root), *args], env=env)


def repo_files(root=ROOT):
    root = Path(root).resolve()
    try:
        if not (root / '.git').exists():
            raise FileNotFoundError('Exported snapshot has no Git metadata')
        data = subprocess.check_output(['git', '-c', 'safe.directory=' + str(root), '-C', str(root),
                                        'ls-files', '-z', '--cached', '--others', '--exclude-standard'], stderr=subprocess.DEVNULL,
                                       env=clean_git_environment())
        names = {s.decode('utf-8') for s in data.split(b'\0') if s}
        return sorted(name for name in names if (root / name).is_file() and '__pycache__' not in Path(name).parts and Path(name).suffix not in {'.pyc', '.pyo'})
    except (subprocess.CalledProcessError, FileNotFoundError):
        return sorted(p.relative_to(root).as_posix() for p in root.rglob('*')
                      if p.is_file() and '.git' not in p.relative_to(root).parts
                      and '__pycache__' not in p.relative_to(root).parts and p.suffix not in {'.pyc', '.pyo'})


def read_json(path):
    """Read JSON source without applying a schema; callers own structured parsing."""
    return Path(path).read_text(encoding='utf-8-sig')


def snapshot_roots(root=ROOT):
    results = []
    base = root / 'work/domains/other/skills'
    for path in base.glob('*/upstream.json'):
        try:
            data = json.loads(read_json(path))
            if data.get('origin') == 'third-party' and data.get('storageMode') == 'full-repository-snapshot':
                source = (path.parent / data['sourcePath']).resolve()
                if source.is_relative_to(root.resolve()):
                    results.append(source.relative_to(root.resolve()).as_posix())
        except (ValueError, KeyError, TypeError):
            continue
    return results


def within(name, prefix):
    return name == prefix or name.startswith(prefix + '/')


def without_code(text):
    return re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', text)


def markdown_targets(text):
    text = without_code(text)
    text = re.sub(r'`[^`\n]+`', '', text)
    results = []
    # Balance destination parentheses, so report(v2).md is not truncated at its first closing bracket.
    for match in re.finditer(r'\[[^\]\n]*\]\(', text):
        start = match.end()
        if start < len(text) and text[start] == '<':
            end = text.find('>', start + 1)
            if end >= 0:
                results.append(text[start + 1:end])
            continue
        depth, escaped, destination = 0, False, []
        for character in text[start:]:
            if escaped:
                destination.append(character)
                escaped = False
                continue
            if character == '\\':
                escaped = True
                continue
            if character == '(':
                depth += 1
            elif character == ')':
                if depth == 0:
                    break
                depth -= 1
            elif character.isspace() and depth == 0:
                break
            destination.append(character)
        if destination:
            results.append(''.join(destination))
    results.extend(match.group(1).strip('<>') for match in re.finditer(r'(?m)^\s*\[[^\]]+\]:\s*(<[^>]+>|\S+)', text))
    return results


def resolve_target(root, source, target):
    if target.startswith('#') or re.match(r'^[a-zA-Z][\w+.-]*:', target):
        return None
    part = unquote(urlsplit(target).path)
    if not part:
        return None
    candidate = (root / part.lstrip('/') if part.startswith('/') else source.parent / part).resolve()
    return candidate


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding='utf-8', newline='\n')

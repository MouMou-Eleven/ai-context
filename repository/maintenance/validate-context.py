"""Validate repository facts, navigation, indexes and generated artifacts without writes."""
import argparse
from collections import defaultdict
from datetime import date
import hashlib
import json
from pathlib import Path
import re
from context_common import ROOT, load_module, markdown_targets, read_json, repo_files, resolve_target, snapshot_roots, within


def check_links(root, files):
    errors = []
    for name in files:
        if Path(name).suffix.lower() not in {'.md', '.txt'}:
            continue
        path = root / name
        for target in markdown_targets(path.read_text(encoding='utf-8-sig')):
            resolved = resolve_target(root, path, target)
            if resolved is None:
                continue
            if not resolved.is_relative_to(root):
                errors.append(f'Link escapes repository: {name}: {target}')
            elif not resolved.exists():
                errors.append(f'Broken link: {name}: {target}')
    return errors


def check_indexes(root, files):
    errors = []
    vendor = snapshot_roots(root)
    readmes = {name: (root / name).read_text(encoding='utf-8-sig') for name in files if Path(name).name == 'README.md'}
    for name in files:
        if any(within(name, prefix) for prefix in vendor):
            continue
        path = Path(name)
        if path.name == 'README.md':
            parent = path.parent.parent
        else:
            parent = path.parent
        owner = None
        while True:
            candidate = (parent / 'README.md').as_posix()
            if candidate in readmes and candidate != name:
                owner = candidate
                break
            if parent == Path('.'):
                break
            parent = parent.parent
        if owner is None:
            if name != 'README.md':
                errors.append(f'No owning README: {name}')
            continue
        text = readmes[owner]
        owner_dir = Path(owner).parent
        relative = path.relative_to(owner_dir).as_posix()
        # Existing trees/backtick indexes are valid indexes, but exact file names are required.
        indexed = any(resolve_target(root, root / owner, target) == (root / name).resolve()
                      for target in markdown_targets(text))
        if not indexed:
            for token in re.findall(r'`([^`\n]+)`', text):
                normalized = token.strip('./').replace('\\', '/')
                if normalized == relative or normalized == name:
                    indexed = True
                    break
                if path.name == 'README.md' and normalized.rstrip('/') == relative.removesuffix('/README.md'):
                    indexed = True
                    break
        if not indexed:
            if path.name == 'README.md':
                branch = relative.removesuffix('/README.md')
                indexed = bool(re.search(r'(?m)(?:├── |└── )' + re.escape(branch) + r'/(?:\s|$)', text))
            else:
                indexed = bool(re.search(r'(?m)(?:├── |└── )' + re.escape(relative) + r'(?:\s|$)', text))
        if not indexed:
            errors.append(f'Unindexed file: {name} (owner: {owner})')
    return errors


def check_skills(root):
    errors = []
    base = root / 'work/ai/programming/experience/skill-repository'
    for folder in sorted(base.iterdir()) if base.exists() else []:
        if not folder.is_dir():
            continue
        label = folder.relative_to(root).as_posix()
        if not (folder / 'README.md').is_file():
            errors.append(f'Skill wrapper missing README: {label}')
        path = folder / 'upstream.json'
        try:
            data = json.loads(read_json(path))
        except (OSError, ValueError):
            errors.append(f'Skill metadata missing or invalid: {label}/upstream.json')
            continue
        for field in ['id', 'storageMode', 'sourcePath', 'origin', 'documentationReviewedAt']:
            if not isinstance(data.get(field), str) or not data[field].strip():
                errors.append(f'Skill metadata requires {field}: {label}')
        if data.get('schemaVersion') != 1 or data.get('id') != folder.name:
            errors.append(f'Skill schemaVersion/id mismatch: {label}')
        for field in ['syncedAt', 'documentationReviewedAt']:
            try:
                date.fromisoformat(data.get(field, ''))
            except (ValueError, TypeError):
                errors.append(f'Skill requires ISO date {field}: {label}')
        if data.get('origin') not in {'internal', 'third-party'}:
            errors.append(f'Skill origin must be internal or third-party: {label}')
        if data.get('storageMode') not in {'skill-snapshot', 'full-repository-snapshot'}:
            errors.append(f'Unknown Skill storageMode: {label}')
        for field in ['capabilities', 'useWhen', 'notFor', 'runtimeRequirements']:
            if not isinstance(data.get(field), list) or not data[field] or not all(isinstance(x, str) and x.strip() for x in data[field]):
                errors.append(f'Skill metadata requires nonempty {field}: {label}')
        source = (folder / data.get('sourcePath', '')).resolve()
        if not source.is_relative_to(folder.resolve()) or not source.is_dir():
            errors.append(f'Skill sourcePath is missing or outside wrapper: {label}')
        elif data.get('storageMode') == 'skill-snapshot' and not (source / 'SKILL.md').is_file():
            errors.append(f'Skill source entry is missing: {label}/{data.get("sourcePath")}/SKILL.md')
        elif data.get('storageMode') == 'full-repository-snapshot' and not any(source.rglob('SKILL.md')):
            errors.append(f'Full Skill snapshot contains no SKILL.md entry: {label}')
        if data.get('origin') == 'internal':
            if data.get('authorship') != 'self-developed' or not data.get('maintainer'):
                errors.append(f'Internal Skill needs self-developed authorship and maintainer: {label}')
            revision = data.get('workflowRevision')
            if not isinstance(revision, int) or isinstance(revision, bool) or revision <= 0:
                errors.append(f'Internal Skill needs a positive workflowRevision: {label}')
        if data.get('origin') == 'third-party':
            if not re.match(r'^https://[^\s]+$', str(data.get('upstreamRepository', ''))):
                errors.append(f'Third-party Skill needs upstream URL: {label}')
            for field in ['license', 'defaultBranch', 'commit']:
                if not data.get(field):
                    errors.append(f'Third-party Skill needs {field}: {label}')
            if not re.fullmatch(r'[0-9a-fA-F]{40}', str(data.get('commit', ''))):
                errors.append(f'Third-party Skill commit must identify exact snapshot: {label}')
        for runtime_path in data.get('requiredRuntimePaths', []):
            runtime = (source / runtime_path).resolve()
            if not runtime.is_relative_to(source) or not runtime.exists():
                errors.append(f'Skill runtime path is missing: {label}/{runtime_path}')
    return errors


def check_registries(root):
    errors = []
    for filename, key in [('routes.json', 'routes'), ('projects.json', 'projects')]:
        path = root / 'repository/navigation' / filename
        try:
            data = json.loads(read_json(path))
        except (OSError, ValueError) as exc:
            errors.append(f'Invalid navigation registry {filename}: {exc}')
            continue
        if data.get('schemaVersion') != 1 or not isinstance(data.get(key), list):
            errors.append(f'Invalid registry schema: {filename}')
            continue
        ids = [item.get('id') for item in data[key]]
        if len(set(ids)) != len(ids) or not all(ids):
            errors.append(f'Duplicate or missing registry id: {filename}')
        if key == 'routes':
            for required_id in ['cognition', 'commercial', 'training', 'community', 'external-training', 'bug-lesson', 'feishu-book']:
                if required_id not in ids:
                    errors.append(f'Required routing boundary is missing: {required_id}')
        paths = list(data.get('readFirst', []))
        for item in data[key]:
            paths.append(item.get('entry', ''))
            if key == 'routes' and (not item.get('matchAny') or not isinstance(item.get('priority'), int)):
                errors.append(f'Route missing matchAny/priority: {item.get("id")}')
            paths.extend(d.get('path', '') for d in item.get('dependencies', []))
        for overlay in data.get('overlays', []):
            paths.extend(overlay.get('paths', []))
        for value in paths:
            target = (root / value).resolve()
            if not value or not target.is_relative_to(root) or not target.is_file():
                errors.append(f'Registry path missing or outside repository: {filename}: {value}')
    return errors


def check_policy(root, files):
    errors = []
    policy = json.loads(read_json(root / 'repository/maintenance/validation-policy.json'))
    for name in policy['requiredFiles']:
        if not (root / name).is_file():
            errors.append(f'Missing required file: {name}')
    for name in policy['managedDirectories']:
        if not (root / name / 'README.md').is_file():
            errors.append(f'Managed directory missing README: {name}')
    for name in policy['deprecatedPaths']:
        if any(within(item, name) for item in files):
            errors.append(f'Deprecated path still contains files: {name}')
    for name in ['README.md', 'STRUCTURE.md']:
        text = (root / name).read_text(encoding='utf-8-sig') if (root / name).exists() else ''
        for directory in ['personal', 'brain', 'work', 'repository', 'history']:
            if directory + '/' not in text:
                errors.append(f'{name} omits top-level directory {directory}/')
    for name in ['AGENTS.md', 'llms.txt']:
        text = (root / name).read_text(encoding='utf-8-sig') if (root / name).exists() else ''
        if 'brain/ai-expression/README.md' not in text:
            errors.append(f'{name} omits Chinese expression short entry')
    agents = (root / 'AGENTS.md').read_text(encoding='utf-8-sig') if (root / 'AGENTS.md').exists() else ''
    if 'publish-policy: direct-main-no-pr' not in agents:
        errors.append('AGENTS.md omits confirmed publishing policy')
    boundaries = {
        'work/ai/training/README.md': ['../self-media/', 'brain/ai-expression/'],
        'work/ai/self-media/README.md': ['../training/', 'brain/ai-expression/'],
        'work/ai/publishing/README.md': ['brain/ai-expression/'],
        'work/design/microcourse-mg-animation/README.md': ['../../ai/training/'],
    }
    for name, required in boundaries.items():
        text = (root / name).read_text(encoding='utf-8-sig') if (root / name).exists() else ''
        for token in required:
            if token not in text:
                errors.append(f'Domain boundary missing: {name}: {token}')
    return errors


def check_sensitive_and_duplicates(root, files):
    errors, warnings = [], []
    hashes = defaultdict(list)
    pattern = re.compile(r'''(?im)^\s*(api[_-]?key|token|password|cookie)\s*[:=]\s*["']?[A-Za-z0-9_\-]{16,}''')
    for name in files:
        path = root / name
        data = path.read_bytes()
        if path.suffix.lower() in {'.md', '.txt', '.ps1', '.ts', '.py', '.json', '.yaml', '.yml'}:
            if pattern.search(data.decode('utf-8', errors='replace')):
                errors.append(f'Possible secret: {name}')
        if data and path.name != 'README.md':
            hashes[hashlib.sha256(data).digest()].append(name)
    vendors = snapshot_roots(root)
    vendor_counts = defaultdict(int)
    for names in hashes.values():
        if len(names) > 1:
            same_vendor = next((prefix for prefix in vendors if all(within(name, prefix) for name in names)), None)
            if same_vendor:
                vendor_counts[same_vendor] += 1
            else:
                warnings.append('Exact duplicate content: ' + ', '.join(names))
    for prefix, count in vendor_counts.items():
        warnings.append(f'External snapshot contains {count} exact-duplicate groups: {prefix}; preserved upstream structure, not deduplicated.')
    return errors, warnings


def validate(root=ROOT):
    root = Path(root).resolve()
    files = repo_files(root)
    errors, warnings = [], []
    for checker in [check_policy, check_links, check_indexes]:
        errors.extend(checker(root, files))
    errors.extend(check_skills(root))
    errors.extend(check_registries(root))
    secret_errors, duplicate_warnings = check_sensitive_and_duplicates(root, files)
    errors.extend(secret_errors)
    warnings.extend(duplicate_warnings)
    for module in ['sync-navigation', 'sync-structure']:
        try:
            stale = load_module(module, root).sync(check=True, root=root)
            errors.extend(f'Generated artifact is stale: {name}; run {module}.py' for name in stale)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append(f'Cannot check generated artifacts ({module}): {exc}')
    return {'files': len(files), 'errors': sorted(set(errors)), 'warnings': warnings}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    try:
        result = validate(args.root)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        result = {'files': 0, 'errors': [f'Validation could not complete: {exc}'], 'warnings': []}
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f'Context validation scanned {result["files"]} files.')
        for level in ['errors', 'warnings']:
            for message in result[level]:
                print(f'{level[:-1].upper()}: {message}')
        print(f'{len(result["errors"])} error(s), {len(result["warnings"])} warning(s).')
    raise SystemExit(1 if result['errors'] else 0)

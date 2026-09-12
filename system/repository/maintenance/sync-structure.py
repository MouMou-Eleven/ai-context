"""Generate human knowledge navigation and the complete repository file tree."""
import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
from context_common import ROOT, read_json, repo_files, snapshot_roots, within, write_text


def description(root, path, catalog):
    if path in catalog:
        return catalog[path]
    target = root / path
    heading_file = target / 'README.md' if target.is_dir() else target
    if heading_file.suffix == '.md' and heading_file.is_file():
        heading = re.search(r'^#\s+(.+)$', heading_file.read_text(encoding='utf-8-sig'), re.M)
        if heading:
            return heading.group(1).strip()[:100]
    return {'json': '结构化配置与索引', 'py': '跨平台维护或执行脚本', 'ps1': 'Windows 兼容入口',
            'yml': '自动化配置', 'yaml': '自动化配置', 'txt': '文本资料', 'md': '说明与资料',
            'html': '可交互页面', 'png': '图片素材', 'jpg': '图片素材', 'docx': '原始文档'}.get(target.suffix.lstrip('.'), '目录入口' if target.is_dir() else '资料与资源')


def build_tree(root, files, catalog):
    folded = snapshot_roots(root)
    tree = {}
    for name in files:
        parts = name.split('/')
        cursor = tree
        for i, part in enumerate(parts):
            cursor = cursor.setdefault(part, {'children': {}, 'folder': i < len(parts) - 1})['children']
    lines = ['ai-context/']
    preferred = ['README.md', 'AGENTS.md', 'llms.txt', 'personal', 'brain', 'work', 'system']

    def render(children, prefix='', parent=''):
        keys = sorted(children, key=lambda key: (preferred.index(key) if not parent and key in preferred else len(preferred), key.casefold()))
        for i, name in enumerate(keys):
            node = children[name]
            path = '/'.join(filter(None, [parent, name]))
            label = name + ('/' if node['folder'] else '')
            desc = description(root, path, catalog)
            if path in folded:
                count = sum(within(item, path) for item in files)
                desc = f'上游完整快照，共 {count} 个文件；展开可核查内部层级'
            lines.append(prefix + ('└── ' if i == len(keys) - 1 else '├── ') + label + '  ' + desc)
            render(node['children'], prefix + ('    ' if i == len(keys) - 1 else '│   '), path)
    render(tree)
    return '\n'.join(lines)


def build_knowledge(root, files, metadata):
    """Derive the human view from actual content, without a second manual tree."""
    catalog = metadata.get('descriptions', {})
    labels = metadata.get('knowledgeLabels', {})
    roots = ['personal', 'brain', 'work', 'system']
    root_labels = dict(zip(roots, ['个人信息', '建委大脑', '工作领域与项目', 'AI协作与维护']))
    hidden = []
    for path in (root / 'work/domains/other/skills').glob('*/upstream.json'):
        data = json.loads(read_json(path))
        hidden.append((path.parent / data['sourcePath']).relative_to(root).as_posix())
    tree = {}
    visible_extensions = {'.md', '.txt', '.docx', '.pdf'}
    for name in files:
        parts = name.split('/')
        if parts[0] not in roots or any(within(name, prefix) for prefix in hidden):
            continue
        if Path(name).suffix.lower() not in visible_extensions or Path(name).name in {'llms.txt', 'STRUCTURE.md', 'AGENTS.md'}:
            continue
        if 'raw' in parts or 'git-hooks' in parts or any(part.startswith('.') for part in parts):
            continue
        cursor = tree
        folders = parts[:-1]
        for i, part in enumerate(folders):
            path = '/'.join(folders[:i + 1])
            cursor = cursor.setdefault(part, {'path': path, 'children': {}, 'folder': True})['children']
        if parts[-1] != 'README.md':
            cursor[parts[-1]] = {'path': name, 'children': {}, 'folder': False}

    def convert(node):
        path = node['path']
        folder = node['folder']
        entry = path + '/README.md' if folder else path
        if not (root / entry).is_file():
            entry = ''
        raw_desc = description(root, path, catalog)
        label = root_labels.get(path) or labels.get(path)
        if not label:
            heading_path = root / entry if entry else None
            heading = re.search(r'^#\s+(.+)$', heading_path.read_text(encoding='utf-8-sig'), re.M) if heading_path and heading_path.suffix == '.md' else None
            label = heading.group(1).strip() if heading else raw_desc
            label = re.sub(r'^[A-Za-z][A-Za-z -]*\s*[—–]\s*', '', label)
            label = re.sub(r'^\*+|\*+$', '', label)
        desc = re.sub(r'^[一二三四五六七八九十]+级目录[：:]\s*', '', raw_desc)
        children = list(node['children'].values())
        order = metadata.get('knowledgeOrder', {}).get(path, [])
        children.sort(key=lambda item: (order.index(Path(item['path']).name) if Path(item['path']).name in order else len(order), item['path'].casefold()))
        return {'label': label, 'path': path, 'entry': entry, 'kind': 'folder' if folder else 'document',
                'description': '' if desc == label else desc, 'children': [convert(item) for item in children]}
    return {'label': 'AI Context', 'path': '', 'entry': 'README.md', 'kind': 'folder',
            'description': '建委的长期协作上下文', 'children': [convert(tree[key]) for key in roots if key in tree]}


def outputs(root=ROOT):
    root = Path(root).resolve()
    metadata = json.loads(read_json(root / 'system/repository/maintenance/structure-descriptions.json'))
    files = repo_files(root)
    current_paths = set(files)
    for name in files:
        current_paths.update(parent.as_posix() for parent in Path(name).parents if parent != Path('.'))
    metadata['descriptions'] = {name: text for name, text in metadata['descriptions'].items() if name in current_paths}
    metadata['knowledgeLabels'] = {name: text for name, text in metadata.get('knowledgeLabels', {}).items() if name in current_paths}
    metadata['descriptions']['llms.txt'] = '兼容调用的极短指针，完整任务指南位于系统导航'
    original = (root / 'system/repository/navigation/STRUCTURE.md').read_text(encoding='utf-8-sig')
    tree = build_tree(root, files, metadata['descriptions'])
    match = re.search(r'```text\s*\n.*?\n```', original, re.S)
    if not match:
        raise ValueError('system/repository/navigation/STRUCTURE.md has no text tree block')
    markdown = original[:match.start()] + '```text\n' + tree + '\n```' + original[match.end():]
    markdown = re.sub(r'\*([^\n*]*?)[0-9]{4}-[0-9]{2}-[0-9]{2}\*\s*$', lambda m: '*' + m.group(1) + metadata['confirmedDate'] + '*\n', markdown)
    template = (root / 'system/repository/maintenance/structure-viewer.template.html').read_text(encoding='utf-8-sig')
    html = template.replace('__STRUCTURE_DATA_BASE64__', base64.b64encode(tree.encode('utf-8')).decode('ascii'))
    knowledge = json.dumps(build_knowledge(root, files, metadata), ensure_ascii=False, separators=(',', ':'))
    html = html.replace('__KNOWLEDGE_DATA_BASE64__', base64.b64encode(knowledge.encode('utf-8')).decode('ascii'))
    html = html.replace('__SOURCE_SHA256__', hashlib.sha256(markdown.encode('utf-8')).hexdigest().upper())
    html = html.replace('__CONFIRMED_DATE__', metadata['confirmedDate'])
    return {'system/repository/navigation/STRUCTURE.md': markdown, 'system/repository/navigation/STRUCTURE.html': html,
            'system/repository/maintenance/structure-descriptions.json': json.dumps(metadata, ensure_ascii=False, indent=2) + '\n'}


def sync(check=False, root=ROOT):
    changed = []
    for name, expected in outputs(root).items():
        path = root / name
        if not path.exists() or path.read_text(encoding='utf-8-sig') != expected:
            changed.append(name)
            if not check:
                write_text(path, expected)
    return changed


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    changed = sync(args.check, args.root.resolve())
    print(('Stale: ' if args.check else 'Updated: ') + ', '.join(changed) if changed else 'Structure and HTML are synchronized.')
    raise SystemExit(1 if args.check and changed else 0)

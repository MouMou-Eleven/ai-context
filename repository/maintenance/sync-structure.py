"""Generate the complete repository tree and existing interactive HTML viewer."""
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
        collapsed = next((prefix for prefix in folded if within(name, prefix)), None)
        visible = collapsed or name
        parts = visible.split('/')
        cursor = tree
        for i, part in enumerate(parts):
            cursor = cursor.setdefault(part, {'children': {}, 'folder': i < len(parts) - 1 or collapsed is not None})['children']
    lines = ['ai-context/']
    preferred = ['README.md', 'AGENTS.md', 'llms.txt', 'STRUCTURE.md', 'STRUCTURE.html', 'personal', 'brain', 'work', 'repository', 'history']

    def render(children, prefix='', parent=''):
        keys = sorted(children, key=lambda key: (preferred.index(key) if not parent and key in preferred else len(preferred), key.casefold()))
        for i, name in enumerate(keys):
            node = children[name]
            path = '/'.join(filter(None, [parent, name]))
            label = name + ('/' if node['folder'] else '')
            desc = description(root, path, catalog)
            if path in folded:
                count = sum(within(item, path) for item in files)
                desc += f'；上游完整快照，共 {count} 个文件，内部层级按需查看'
            lines.append(prefix + ('└── ' if i == len(keys) - 1 else '├── ') + label + '  ' + desc)
            render(node['children'], prefix + ('    ' if i == len(keys) - 1 else '│   '), path)
    render(tree)
    return '\n'.join(lines)


def outputs(root=ROOT):
    root = Path(root).resolve()
    metadata = json.loads(read_json(root / 'repository/maintenance/structure-descriptions.json'))
    files = repo_files(root)
    current_paths = set(files)
    for name in files:
        current_paths.update(parent.as_posix() for parent in Path(name).parents if parent != Path('.'))
    metadata['descriptions'] = {name: text for name, text in metadata['descriptions'].items() if name in current_paths}
    metadata['descriptions']['llms.txt'] = '任务路由与必要依赖的最小读取入口'
    if 'brain/ai-expression/chinese-datasets/grammar-and-error-checklist.md' in current_paths:
        metadata['descriptions']['brain/ai-expression/chinese-datasets/grammar-and-error-checklist.md'] = '按需读取的中文语法与病句详查'
    original = (root / 'STRUCTURE.md').read_text(encoding='utf-8-sig')
    tree = build_tree(root, files, metadata['descriptions'])
    match = re.search(r'```text\s*\n.*?\n```', original, re.S)
    if not match:
        raise ValueError('STRUCTURE.md has no text tree block')
    markdown = original[:match.start()] + '```text\n' + tree + '\n```' + original[match.end():]
    markdown = re.sub(r'\*([^\n*]*?)[0-9]{4}-[0-9]{2}-[0-9]{2}\*\s*$', lambda m: '*' + m.group(1) + metadata['confirmedDate'] + '*\n', markdown)
    template = (root / 'repository/maintenance/structure-viewer.template.html').read_text(encoding='utf-8-sig')
    html = template.replace('__STRUCTURE_DATA_BASE64__', base64.b64encode(tree.encode('utf-8')).decode('ascii'))
    html = html.replace('__SOURCE_SHA256__', hashlib.sha256(markdown.encode('utf-8')).hexdigest().upper())
    html = html.replace('__CONFIRMED_DATE__', metadata['confirmedDate'])
    return {'STRUCTURE.md': markdown, 'STRUCTURE.html': html,
            'repository/maintenance/structure-descriptions.json': json.dumps(metadata, ensure_ascii=False, indent=2) + '\n'}


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

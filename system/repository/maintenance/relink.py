"""Rewrite repository references after files or folders move.

Usage: python relink.py OLD=NEW [OLD=NEW ...] [--dry-run]

Each OLD/NEW is a repository-relative path (file or folder). The script updates
relative Markdown links in every tracked text file and exact repository paths in
JSON/Python/Markdown text, so moves never leave broken references behind.
It does not move files; run `git mv` first.
"""
import os
import re
import sys
from pathlib import Path

from context_common import ROOT, repo_files

TEXT = {'.md', '.json', '.py', '.txt', '.html', '.yml', '.yaml', '.ps1'}
LINK = re.compile(r'(\]\()([^)\s]+)(\))')


def mapping_for(path, moves):
    """Return the new repository path for an old one, or None if unaffected."""
    for old, new in moves:
        if path == old:
            return new
        if path.startswith(old + '/'):
            return new + path[len(old):]
    return None


def rewrite_links(text, owner_old, owner_new, moves):
    def fix(match):
        target = match.group(2)
        if re.match(r'^[a-z]+:', target) or target.startswith('#'):
            return match.group(0)
        path_part, sep, anchor = target.partition('#')
        if not path_part:
            return match.group(0)
        absolute = os.path.normpath(os.path.join(os.path.dirname(owner_old), path_part)).replace('\\', '/')
        moved = mapping_for(absolute, moves) or absolute
        relative = os.path.relpath(moved, os.path.dirname(owner_new) or '.').replace('\\', '/')
        if path_part.endswith('/') and not relative.endswith('/'):
            relative += '/'
        if path_part.startswith('./') and not relative.startswith('.'):
            relative = './' + relative
        new_target = relative + (sep + anchor if sep else '')
        return match.group(1) + new_target + match.group(3)
    return LINK.sub(fix, text)


def rewrite_plain(text, moves):
    for old, new in sorted(moves, key=lambda m: -len(m[0])):
        text = re.sub(r'(?<![\w./-])' + re.escape(old) + r'(?=[/"\'`\s,)\]]|$)', new, text)
    return text


def main(argv):
    dry = '--dry-run' in argv
    moves = [tuple(a.split('=', 1)) for a in argv if '=' in a]
    if not moves:
        print(__doc__)
        return 2
    changed = []
    # Only files Git actually saw renamed are relocated; files already living in
    # the destination folder keep their own location for link resolution.
    import subprocess
    status = subprocess.run(['git', '-C', str(ROOT), 'diff', '--cached', '--name-status', '-M', 'HEAD'],
                            capture_output=True, text=True, encoding='utf-8').stdout
    renamed = {}
    for line in status.splitlines():
        parts = line.split('\t')
        if parts and parts[0].startswith('R') and len(parts) == 3:
            renamed[parts[2]] = parts[1]
    for name in repo_files(ROOT):
        path = ROOT / name
        if path.suffix.lower() not in TEXT or '/source/' in name or '/skill/' in name:
            continue
        original = path.read_text(encoding='utf-8-sig')
        # A moved file's own links were written relative to its old location.
        old_name = renamed.get(name, name)
        text = original
        if path.suffix.lower() in {'.md', '.html'}:
            text = rewrite_links(text, old_name, name, moves)
        text = rewrite_plain(text, moves)
        if text != original:
            changed.append(name)
            if not dry:
                path.write_text(text, encoding='utf-8', newline='\n')
    print(('Would change' if dry else 'Changed') + f' {len(changed)} file(s):')
    for name in changed:
        print('  ' + name)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

"""Report whether the repository is due for an upgrade.

Reads system/repository/usage-log.md and system/repository/observations.md
(formats in system/repository/evolution.md) and applies the content-based
triggers written there. Standard library only; never writes files.

  python -B system/repository/maintenance/evolution-status.py          # human readable
  python -B system/repository/maintenance/evolution-status.py --json   # machine readable
  python -B system/repository/maintenance/evolution-status.py --hook   # Claude Code SessionStart: prints
                                                                        # hookSpecificOutput only when due
"""
import argparse
from collections import defaultdict
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
LOG = 'system/repository/usage-log.md'
OBSERVATIONS = 'system/repository/observations.md'
MARKER = re.compile(r'<!--\s*last-upgrade:\s*(\d{4}-\d{2}-\d{2})\s*-->')
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
LINK_TARGET = re.compile(r'\]\(([^)\s]+)\)')
FAILURE_TYPE = re.compile(r'(?<![A-Za-z])[ABC](?![A-Za-z])')

# Default thresholds; evolution.md explains them and says when to adjust.
ROUTINE_LOG_ROWS = 20
REPEATED_B = 2
MISSED_READS = 2
PROJECTS_FOR_PROMOTION = 2

for stream in (sys.stdout, sys.stderr):
    if hasattr(stream, 'reconfigure'):
        stream.reconfigure(encoding='utf-8')


def table_rows(text, heading):
    """Cells of the first Markdown table after a '## heading' line."""
    lines = text.split('\n')
    start = next((i for i, line in enumerate(lines) if line.strip() == '## ' + heading), None)
    if start is None:
        return []
    rows, header_seen = [], False
    for line in lines[start + 1:]:
        stripped = line.strip()
        if stripped.startswith('## '):
            break
        if not stripped.startswith('|'):
            continue
        cells = [cell.strip() for cell in stripped.strip('|').split('|')]
        if set(stripped) <= set('|-: '):
            header_seen = True
            continue
        if not header_seen:
            continue
        rows.append(cells)
    return rows


def normalise_target(target):
    target = target.split('?')[0]
    target = re.sub(r'^(\.\./)+', '', target)
    return target.lstrip('./')


def read(root, name):
    path = Path(root) / name
    return path.read_text(encoding='utf-8') if path.exists() else ''


def status(root=ROOT):
    """Triggers 1-3 count every row still in the tables (handled rows are deleted at an
    upgrade, unhandled ones stay and keep counting); trigger 4 counts rows dated on or
    after the last upgrade."""
    root = Path(root)
    log_text = read(root, LOG)
    marker = MARKER.search(log_text)
    last = marker.group(1) if marker else '0000-00-00'
    entries, warnings = [], []
    for cells in table_rows(log_text, '日志'):
        if len(cells) < 6 or not DATE.match(cells[0]):
            warnings.append(f'使用日志有一行没被计数（日期要写成 YYYY-MM-DD，至少 6 列）：{" | ".join(cells)[:60]}')
            continue
        entries.append({'date': cells[0], 'types': set(FAILURE_TYPE.findall(cells[4])),
                        'rules': sorted({normalise_target(t) for t in LINK_TARGET.findall(cells[5])})})
    recent = [entry for entry in entries if entry['date'] >= last]
    reasons = []
    if len(recent) >= ROUTINE_LOG_ROWS:
        reasons.append(f'上次升级（{last}）以来已记 {len(recent)} 条使用日志，该做一次例行复盘')
    b_hits = defaultdict(list)
    for entry in entries:
        if 'B' in entry['types']:
            for rule in entry['rules']:
                b_hits[rule].append(entry['date'])
    for rule, dates in sorted(b_hits.items()):
        if len(dates) >= REPEATED_B:
            reasons.append(f'{rule} 读了仍被违反 {len(dates)} 次（B 类），写法管不住，要改成检查动作')
    missed = [entry for entry in entries if 'A' in entry['types']]
    if len(missed) >= MISSED_READS:
        reasons.append(f'有 {len(missed)} 次该读的经验没读到（A 类），入口或任务表要改')
    groups = defaultdict(set)
    for cells in table_rows(read(root, OBSERVATIONS), '观察'):
        if len(cells) < 8 or not DATE.match(cells[0]):
            warnings.append(f'观察记录有一行没被计数（日期要写成 YYYY-MM-DD，8 列）：{" | ".join(cells)[:60]}')
            continue
        if cells[7].startswith('待定') and cells[2]:
            groups[cells[2]].add(cells[1])
    for category, projects in sorted(groups.items()):
        if len(projects) >= PROJECTS_FOR_PROMOTION:
            reasons.append(f'观察“{category}”已在 {len(projects)} 个项目出现（{"、".join(sorted(projects))}），可以考虑升成通用规则')
    return {'lastUpgrade': last, 'entries': len(entries), 'entriesSinceUpgrade': len(recent),
            'due': bool(reasons), 'reasons': reasons, 'warnings': warnings}


def reminder(result):
    return ('仓库该升级了：' + '；'.join(result['reasons']) +
            '。按 system/repository/evolution.md 的“升级怎么做”处理；在升级完成前，每次回复末尾用一句话提醒建委。')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--hook', action='store_true')
    args = parser.parse_args()
    result = status(args.root)
    if args.hook:
        if result['due']:
            print(json.dumps({'hookSpecificOutput': {'hookEventName': 'SessionStart',
                                                     'additionalContext': reminder(result)}}, ensure_ascii=False))
    elif args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(reminder(result) if result['due'] else
              f'仓库暂不需要升级：上次升级 {result["lastUpgrade"]}，之后已记 {result["entriesSinceUpgrade"]} 条使用日志。')
        for warning in result['warnings']:
            print('注意：' + warning)

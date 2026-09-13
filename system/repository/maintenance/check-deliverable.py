"""Read-only learner-facing draft lint. No finding is not semantic approval."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style'}:
            self.hidden += 1
        if tag in {'p', 'h1', 'h2', 'h3', 'h4', 'li', 'tr', 'callout', 'title'}:
            self.parts.append('\n')
        if tag in {'td', 'th'}:
            self.parts.append(' | ')

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}:
            self.hidden = max(0, self.hidden - 1)
        if tag in {'p', 'h1', 'h2', 'h3', 'h4', 'li', 'tr', 'callout', 'title'}:
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


PATTERNS = [
    ('teaching-time', r'(?:两|二|2)\s*(?:个)?小时(?:怎么|如何)(?:去)?讲|授课时间安排|讲课时间规划|(?:时间|时长)分配表'),
    ('instructor-cue', r'现场重点看什么|现场使用建议|讲师(?:提醒|备注|提示|动作)|课堂要看什么|演示准备|转场提醒'),
    ('meta-instruction', r'先把结论(?:讲|放)在前面|每讲一个能力.{0,12}挑一条|不要从头到尾连续播'),
]


def inspect(content, profile='learner', markup=False):
    if markup:
        parser = VisibleText()
        parser.feed(content)
        content = ''.join(parser.parts)
    if not content.strip():
        raise ValueError('No visible draft text; provide the actual deliverable, not an empty export.')
    findings = []
    if profile == 'learner':
        for number, line in enumerate(content.splitlines(), 1):
            for rule, pattern in PATTERNS:
                match = re.search(pattern, line)
                if match:
                    findings.append({'rule': rule, 'textLine': number, 'match': match.group(),
                                     'excerpt': line[max(0, match.start()-35):match.end()+90],
                                     'action': '核对是否为讲师指令；是则移出学员正文。引用、反例或用户明确要求需逐项说明。'})
    return findings


def check(path, profile='learner'):
    data = Path(path).read_bytes()
    content = data.decode('utf-8-sig')
    findings = inspect(content, profile, Path(path).suffix.lower() in {'.xml', '.html', '.htm'})
    return {'artifact': str(path), 'sha256': hashlib.sha256(data).hexdigest(), 'profile': profile,
            'status': 'needs_revision_or_review' if findings else 'no_pattern_found_requires_semantic_review',
            'findings': findings, 'approved': False,
            'note': 'textLine为抽取正文行号；需核对原稿。未检测事实、媒体、目标位置或语义完整性；不得据此宣称交付合格。'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('artifact', type=Path)
    parser.add_argument('--profile', choices=['learner', 'instructor', 'general'], default='learner')
    args = parser.parse_args()
    try:
        result = check(args.artifact, args.profile)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(1 if result['findings'] else 0)
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({'status': 'unreadable', 'approved': False, 'error': str(exc)}, ensure_ascii=False))
        raise SystemExit(2)

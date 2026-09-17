"""Read-only audience and optional Word layout checks; no finding is not approval."""
import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import zipfile
from xml.etree import ElementTree as ET

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

PROPOSAL_PATTERNS = [
    ('internal-design', r'以公开真实材料为基础|以可核验的工作成果为落点|本方案为课程设计文件|两场授课的分工|两位讲师在课前|各配置的内容边界|整体时长联动'),
    ('internal-procedure', r'每个案例使用同一条操作路径|现场不预设AI一定出错|若当次输出正确|讲师(?:提醒|备注|提示|动作)|(?:课前|演示)彩排|预录流程|操作路径|输入.{0,8}处理.{0,8}输出.{0,8}人工复核位置'),
    ('internal-evidence', r'公开政策与案例来源|案例与演示的证据范围|工具依据与使用说明|原文中的事项|应当保留的判断边界|清单记载'),
    ('proposal-url', r'https?://[^\s<>]+|www\.[^\s<>]+'),
]

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'


def docx_content(data, layout=None):
    """Extract visible paragraphs, including split runs, tables, headers and footers."""
    import io
    with zipfile.ZipFile(io.BytesIO(data)) as package:
        document = ET.fromstring(package.read('word/document.xml'))
        roots = [document]
        for name in sorted(package.namelist()):
            if re.fullmatch(r'word/(?:header|footer)\d+\.xml', name):
                roots.append(ET.fromstring(package.read(name)))
        content = '\n'.join(''.join(node.text or '' for node in p.iter(W+'t'))
                            for root in roots for p in root.iter(W+'p'))
        extra = []
        for name in package.namelist():
            if name.startswith('word/') and name.endswith('.rels'):
                for rel in ET.fromstring(package.read(name)):
                    if rel.get('Type', '').endswith('/hyperlink') and rel.get('TargetMode') == 'External':
                        extra.append({'rule': 'proposal-hyperlink', 'match': rel.get('Target', ''),
                                      'action': '对外方案不默认携带网站链接；核对是否为用户明确要求。'})
        layout_findings = []
        if layout:
            styles = ET.fromstring(package.read('word/styles.xml'))
            by_id = {s.get(W+'styleId'): s for s in styles.findall(W+'style')}

            def inherited(style_id, child, seen=None):
                seen = set() if seen is None else seen
                if style_id in seen or style_id not in by_id:
                    return None
                seen.add(style_id)
                style = by_id[style_id]
                found = style.find(child)
                if found is not None:
                    return found.get(W+'val')
                base = style.find(W+'basedOn')
                return inherited(base.get(W+'val'), child, seen) if base is not None else None

            titles = []
            for p in document.iter(W+'p'):
                style = p.find(W+'pPr/'+W+'pStyle')
                sid = style.get(W+'val') if style is not None else ''
                sname = inherited(sid, W+'name') or ''
                if sid == 'Title' or sname.lower() in {'title', '标题'}:
                    titles.append(p)
                    jc = p.find(W+'pPr/'+W+'jc')
                    align = jc.get(W+'val') if jc is not None else inherited(sid, W+'pPr/'+W+'jc')
                    if align != 'center':
                        layout_findings.append({'rule': 'word-title-center', 'action': '政企Word主标题应居中；检查段落与样式继承。'})
            if not titles:
                layout_findings.append({'rule': 'word-title-missing', 'action': '未识别原生Title主标题；人工确认主标题样式及居中。'})
        return content, extra, layout_findings


def inspect(content, profile='learner', markup=False):
    if markup:
        parser = VisibleText()
        parser.feed(content)
        content = ''.join(parser.parts)
    if not content.strip():
        raise ValueError('No visible draft text; provide the actual deliverable, not an empty export.')
    findings = []
    if profile in {'learner', 'external-proposal'}:
        for number, line in enumerate(content.splitlines(), 1):
            for rule, pattern in (PATTERNS if profile == 'learner' else PROPOSAL_PATTERNS):
                match = re.search(pattern, line)
                if match:
                    findings.append({'rule': rule, 'textLine': number, 'match': match.group(),
                                     'excerpt': line[max(0, match.start()-35):match.end()+90],
                                     'action': ('核对是否为讲师指令；是则移出学员正文。引用、反例或用户明确要求需逐项说明。' if profile == 'learner' else '核对是否为内部设计或来源说明；对外方案应写课程主题、应用场景与学习价值。引用或用户明确要求需逐项复核。')})
    return findings


def check(path, profile='learner', layout=None):
    data = Path(path).read_bytes()
    suffix = Path(path).suffix.lower()
    extra, layout_findings = [], []
    if suffix == '.docx':
        content, extra, layout_findings = docx_content(data, layout)
    else:
        if layout:
            raise ValueError('Word layout checking requires a .docx artifact.')
        content = data.decode('utf-8-sig')
    findings = inspect(content, profile, suffix in {'.xml', '.html', '.htm'})
    if profile == 'external-proposal':
        findings.extend(extra)
    findings.extend(layout_findings)
    return {'artifact': str(path), 'sha256': hashlib.sha256(data).hexdigest(), 'profile': profile,
            'status': 'needs_revision_or_review' if findings else 'no_pattern_found_requires_semantic_review',
            'findings': findings, 'approved': False,
            'note': 'textLine为抽取正文行号；需核对原稿。未检测事实、媒体、目标位置或语义完整性；不得据此宣称交付合格。'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('artifact', type=Path)
    parser.add_argument('--profile', choices=['learner', 'instructor', 'general', 'external-proposal'], default='learner')
    parser.add_argument('--layout', choices=['gov-enterprise-word'])
    args = parser.parse_args()
    try:
        result = check(args.artifact, args.profile, args.layout)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(1 if result['findings'] else 0)
    except (OSError, UnicodeError, ValueError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(json.dumps({'status': 'unreadable', 'approved': False, 'error': str(exc)}, ensure_ascii=False))
        raise SystemExit(2)

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
from urllib.parse import urlsplit, parse_qs

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

COMPETITION_PATTERNS = [
    ('fill-in-prompt', r'(?:请|由|待|需|交由|留给).{0,12}(?:填写|填报|补充|补填|确认后填)|(?:真实参与者|客户|老师|教师|申报单位).{0,8}(?:确认|填写|补充)|此处(?:填写|留空)|（?待定）?$'),
    ('ghostwriting', r'代做|代写|代填|代为(?:制作|开发|填写)|由(?:我们|开发者|技术人员)(?:代|帮)'),
    ('over-clarification', r'尚未(?:在|经|进行|完成).{0,12}(?:课堂|学校|真实|实际).{0,6}(?:验证|试用|应用|评估)|(?:有待|还需|仍需|需要进一步).{0,8}(?:验证|检验|评估)|仅为(?:模拟|测试|演示)|均为(?:模拟|测试)数据|不代表(?:真实|实际)|不能(?:据此)?(?:说明|证明|宣称)'),
    ('narration-written', r'^我问[，,]|(?:先|再)看(?:正常|一个|下)?.{0,4}[：:。]|如下所示|综上所述|值得注意的是|其中[，,]'),
    ('audience-mismatch', r'给(?:老师|教师)看|教师(?:可|请)自行|老师自己(?:再)?填'),
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
        if layout == 'gov-enterprise-word':
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
        if layout == 'tianjin-contest-word':
            layout_findings.extend(contest_layout(package, document))
        link_findings = tianjin_review_links(content)
        main_relationships = {}
        if 'word/_rels/document.xml.rels' in package.namelist():
            main_relationships = {r.get('Id'): r.get('Target', '') for r in ET.fromstring(package.read('word/_rels/document.xml.rels'))}
        relationship_ns = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
        for hyperlink in document.iter(W+'hyperlink'):
            displayed = ''.join(t.text or '' for t in hyperlink.iter(W+'t')).strip()
            target = main_relationships.get(hyperlink.get(relationship_ns+'id'), '')
            if displayed.startswith('https://aiagent.tjtc.edu.cn/chat-temp/') and target != displayed:
                link_findings.append({'rule': 'contest-review-link-target', 'match': displayed,
                                      'action': 'Word显示的评审地址与实际超链接目标不同；两者都应逐字匹配平台复制的完整链接。'})
        for name in package.namelist():
            if name.startswith('word/') and name.endswith(('.xml', '.rels')):
                root = ET.fromstring(package.read(name))
                for node in root.iter():
                    for value in node.attrib.values():
                        link_findings.extend(tianjin_review_links(value))
                    if node.tag in (W+'instrText', W+'fldSimple') and node.text:
                        link_findings.extend(tianjin_review_links(node.text))
        # Deduplicate links found in visible text and their backing relationship.
        seen = set()
        for finding in link_findings:
            key = (finding['rule'], finding['match'])
            if key not in seen:
                seen.add(key)
                extra.append(finding)
        return content, extra, layout_findings


def contest_layout(package, document):
    """Tianjin contest Word rules: 黑体 headings without theme fonts, centered captions, team table."""
    findings = []
    styles = ET.fromstring(package.read('word/styles.xml'))
    by_id = {s.get(W+'styleId'): s for s in styles.findall(W+'style')}

    def chain(sid):
        seen = []
        while sid in by_id and sid not in seen:
            seen.append(sid)
            base = by_id[sid].find(W+'basedOn')
            sid = base.get(W+'val') if base is not None else None
        return [by_id[x] for x in seen]

    def fonts(node):
        f = node.find(W+'rPr/'+W+'rFonts') if node is not None else None
        return dict((k.split('}')[1], v) for k, v in f.attrib.items()) if f is not None else {}

    def heading(p):
        st = p.find(W+'pPr/'+W+'pStyle')
        sid = st.get(W+'val') if st is not None else ''
        names = [(s.find(W+'name').get(W+'val') if s.find(W+'name') is not None else '').lower() for s in chain(sid)]
        return sid, any(n == 'title' or n.startswith('heading') or n.startswith('标题') for n in names)

    reported = set()
    in_table = {id(x) for t in document.iter(W+'tbl') for x in t.iter(W+'p')}
    for p in document.iter(W+'p'):
        text = ''.join(t.text or '' for t in p.iter(W+'t')).strip()
        if not text:
            continue
        sid, is_heading = heading(p)
        if is_heading:
            for style in chain(sid):
                f = fonts(style)
                if any(k.endswith('Theme') or k == 'cstheme' for k in f if k != 'cstheme') or (f and not f.get('ascii')):
                    key = style.get(W+'styleId')
                    if key not in reported:
                        reported.add(key)
                        findings.append({'rule': 'contest-heading-theme-font', 'match': key,
                                         'action': '标题样式仍用主题字体（显示为Cambria/Calibri等英文字体）；样式与每个run的ascii/hAnsi/eastAsia都显式设为黑体。'})
            for r in p.iter(W+'r'):
                f = fonts(r)
                bad = [v for k, v in f.items() if k in ('ascii', 'hAnsi', 'eastAsia') and v != '黑体']
                if bad or any(k in ('asciiTheme', 'hAnsiTheme', 'eastAsiaTheme') for k in f):
                    findings.append({'rule': 'contest-heading-font', 'match': text[:30],
                                     'action': '标题文字的中西文字体都应为黑体，不能是主题字体或Times New Roman。'})
                    break
        if id(p) not in in_table and re.match(r'^(?:图|表)\s*\d{1,2}(?!\d)', text) and len(text) < 120:
            jc = p.find(W+'pPr/'+W+'jc')
            align = jc.get(W+'val') if jc is not None else None
            if align is None:
                for style in chain(sid):
                    j = style.find(W+'pPr/'+W+'jc')
                    if j is not None:
                        align = j.get(W+'val')
                        break
            if align != 'center':
                findings.append({'rule': 'contest-caption-center', 'match': text[:30], 'action': '图注、表注应居中。'})
    findings.extend(contest_structure(document, chain, heading, in_table))
    for table in document.iter(W+'tbl'):
        rows = [[''.join(t.text or '' for t in c.iter(W+'t')).strip() for c in r.findall(W+'tc')] for r in table.findall(W+'tr')]
        if not rows or '姓名' not in rows[0]:
            continue
        head = rows[0]
        duty = [i for i, h in enumerate(head) if h in ('职责', '分工', '工作内容', '实际贡献', '主要贡献')]
        for row in rows[1:]:
            if any(i < len(row) and not row[i] for i in duty):
                findings.append({'rule': 'contest-team-duty-blank', 'match': ' | '.join(row),
                                 'action': '团队表只有姓名留空；职责和工作内容按作品实际分工写好。'})
                break
    return findings


def contest_structure(document, chain, heading, in_table):
    """Alignment, numbering, spacing and filled project-name rules shared by contest documents."""
    findings = []
    hanzi_gap = re.compile(r'[一-鿿][ 　]+[一-鿿]')
    caption = re.compile(r'^(?:图|表)\s*\d')

    def style_name(style):
        name = style.find(W+'name')
        return (name.get(W+'val') if name is not None else '').lower()

    def align(p, sid):
        jc = p.find(W+'pPr/'+W+'jc')
        if jc is not None:
            return jc.get(W+'val')
        for style in chain(sid):
            j = style.find(W+'pPr/'+W+'jc')
            if j is not None:
                return j.get(W+'val')
        return None

    def indented(p, sid):
        for node in [p] + chain(sid):
            ind = node.find(W+'pPr/'+W+'ind')
            if ind is not None and any(ind.get(W+k) not in (None, '0') for k in ('firstLine', 'firstLineChars')):
                return True
        return False

    paragraphs = []
    for p in document.iter(W+'p'):
        text = ''.join(t.text or '' for t in p.iter(W+'t')).strip()
        st = p.find(W+'pPr/'+W+'pStyle')
        sid = st.get(W+'val') if st is not None else ''
        paragraphs.append((p, text, sid, id(p) in in_table, p.find('.//'+W+'drawing') is not None))
    body = [x for x in paragraphs if not x[3]]
    filled = [x for x in body if x[1]]
    report = bool(filled) and '技术说明与验证报告' in filled[0][1]
    if report:
        for p, text, sid, _, _ in filled[:2]:
            if len(text) < 80 and align(p, sid) != 'center':
                findings.append({'rule': 'contest-title-center', 'match': text[:30], 'action': '主标题和副标题行居中。'})
    unindented, blanks, pending = 0, 0, 0
    for index, (p, text, sid, _, drawing) in enumerate(body):
        if not text and not drawing:
            pending += 1
            continue
        blanks, pending = blanks + pending, 0
        is_heading = heading(p)[1]
        level_one = any(style_name(s) == 'heading 1' for s in chain(sid))
        if report and level_one and not re.match(r'^(?:[一二三四五六七八九十]+、|附)', text):
            findings.append({'rule': 'contest-heading-number', 'match': text[:30], 'action': '一级标题用“一、二、三……”编号。'})
        if re.match(r'^(?:[一二三四五六七八九十]+|\d+)[ 　]+\S', text):
            findings.append({'rule': 'contest-number-punctuation', 'match': text[:30], 'action': '编号后用顿号或点号，不用空格。'})
        if hanzi_gap.search(text) and not caption.match(text):
            findings.append({'rule': 'contest-space-separator', 'match': text[:30], 'action': '汉字之间不用空格分隔：并列用顿号，前后两部分用冒号或逗号。'})
        if caption.match(text) and hanzi_gap.search(re.sub(r'^(?:图|表)\s*\d+\s*', '', text)):
            findings.append({'rule': 'contest-space-separator', 'match': text[:30], 'action': '图注编号后空一格，标题内部用冒号或逗号，不再用空格分隔。'})
        if text == '项目详细介绍' or text == '项目名称：':
            findings.append({'rule': 'contest-project-name-blank', 'match': text, 'action': '作品内容的空要填项目名称（写在原下划线上）；只有人员身份字段留空。'})
        if (report and not is_heading and not drawing and len(text) > 40 and not caption.match(text)
                and align(p, sid) != 'center' and not indented(p, sid)):
            unindented += 1
    for p, text, sid, inside, _ in paragraphs:
        if inside and hanzi_gap.search(text):
            findings.append({'rule': 'contest-space-separator', 'match': text[:30], 'action': '表格里的并列词也用顿号，不用空格。'})
    if unindented:
        findings.append({'rule': 'contest-body-indent', 'match': f'{unindented}段', 'action': '正文段落首行缩进2字、两端对齐。'})
    if report and blanks >= 3:
        findings.append({'rule': 'contest-empty-spacing', 'match': f'{blanks}个空段落', 'action': '用段前段后控制间距，删除用来撑间距的空段落。'})
    return findings


def tianjin_review_links(content):
    """Check full Tianjin temporary URLs without claiming platform access was tested."""
    findings = []
    for match in re.finditer(r'https://aiagent\.tjtc\.edu\.cn/chat-temp/[^\s<>"\u0027，。；（）)\]}]+', content):
        url = match.group().replace('&amp;', '&')
        values = parse_qs(urlsplit(url).query).get('appid', [])
        if len(values) != 1 or not re.fullmatch(r'\d+-\d+', values[0]):
            findings.append({'rule': 'contest-review-link-appid', 'match': url,
                             'action': '天津临时评审链接必须保留平台复制的完整查询参数及唯一appid；回读登录可用未勾选、有效期为空，并在未登录状态验证。'})
    return findings


def inspect(content, profile='learner', markup=False):
    if markup:
        parser = VisibleText()
        parser.feed(content)
        content = ''.join(parser.parts)
    if not content.strip():
        raise ValueError('No visible draft text; provide the actual deliverable, not an empty export.')
    findings = []
    if profile in {'learner', 'external-proposal', 'competition'}:
        table = {'learner': PATTERNS, 'external-proposal': PROPOSAL_PATTERNS, 'competition': COMPETITION_PATTERNS}[profile]
        for number, line in enumerate(content.splitlines(), 1):
            for rule, pattern in table:
                match = re.search(pattern, line)
                if match:
                    findings.append({'rule': rule, 'textLine': number, 'match': match.group(),
                                     'excerpt': line[max(0, match.start()-35):match.end()+90],
                                     'action': {'learner': '核对是否为讲师指令；是则移出学员正文。引用、反例或用户明确要求需逐项说明。',
                                                'external-proposal': '核对是否为内部设计或来源说明；对外方案应写课程主题、应用场景与学习价值。引用或用户明确要求需逐项复核。',
                                                'competition': '评审成品只写给评委看：删掉填写提示、代做字样和非必须的澄清；“存在不足”栏目按字数要求简要写。'}[profile]})
    if profile == 'competition':
        findings.extend(tianjin_review_links(content))
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
        findings.extend(f for f in extra if f['rule'] == 'proposal-hyperlink')
    if profile == 'competition':
        for f in extra:
            if f['rule'].startswith('contest-review-link') and not any(x['rule'] == f['rule'] and x.get('match') == f.get('match') for x in findings):
                findings.append(f)
    findings.extend(layout_findings)
    return {'artifact': str(path), 'sha256': hashlib.sha256(data).hexdigest(), 'profile': profile,
            'status': 'needs_revision_or_review' if findings else 'no_pattern_found_requires_semantic_review',
            'findings': findings, 'approved': False,
            'note': 'textLine为抽取正文行号；需核对原稿。未检测事实、媒体、目标位置或语义完整性；不得据此宣称交付合格。'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('artifact', type=Path)
    parser.add_argument('--profile', choices=['learner', 'instructor', 'general', 'external-proposal', 'competition'], default='learner')
    parser.add_argument('--layout', choices=['gov-enterprise-word', 'tianjin-contest-word'])
    args = parser.parse_args()
    try:
        result = check(args.artifact, args.profile, args.layout)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        raise SystemExit(1 if result['findings'] else 0)
    except (OSError, UnicodeError, ValueError, KeyError, zipfile.BadZipFile, ET.ParseError) as exc:
        print(json.dumps({'status': 'unreadable', 'approved': False, 'error': str(exc)}, ensure_ascii=False))
        raise SystemExit(2)

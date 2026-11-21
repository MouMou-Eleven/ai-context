"""Content rules that keep the repository maintainable by any AI.

Each rule has one home (see ingestion-workflow.md#一条规则只有一个家默认); these checks
block the most common ways that home gets bypassed.

Red lines are only set by Jianwei (AGENTS.md, step 3). validation-policy.json "redlineBudget"
records, per file, how many red-line marks each file had after the 2026-11-13 review. A file
with more marks than its budget (or a new file with any) is blocked, so a red line cannot be
moved or swapped in silently. Lower a count when red lines are removed; raise it only after
Jianwei confirms a new one.

Retired sayings (system/repository/retired-rules.md) must not come back into rule files: the
current text holds only the new rule, the register keeps the trace, and this check blocks the
detection words of a retired rule from reappearing outside history sections.

AGENTS.md is loaded whole by every tool; Codex stops loading project instructions at 32 KiB,
so the entry is kept under AGENTS_MAX_BYTES.
"""
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path

BRAIN_LINE_LIMIT = 220
AGENTS_CELL_LIMIT = 130
AGENTS_MAX_BYTES = 30000
RETIRED = 'system/repository/retired-rules.md'
RETIRED_EXEMPT = {RETIRED, 'system/repository/observations.md', 'system/repository/usage-log.md',
                  'system/repository/evolution.md'}
HISTORY_HEADING = re.compile(r'^## .*(来源|来历|来源与状态|修订记录)\s*$')
# Words just before a retired saying that mark it as superseded (而不是 X / 以前的 X / 替换掉错写的 X) ...
SUPERSEDED_BEFORE = re.compile(r'不是|不再|不要求|不用|替换掉|以前的|错写的|退役的|旧的')
# ... or just after it (X 已被取代 / X 已经拆进对照表).
SUPERSEDED_AFTER = re.compile(r'^[”」』"]?(已被|已经被|被)?(取代|退役|废弃|拆进|并进|并入|改掉|改成|替换)|^[”」』"]?已经?(拆进|并进|并入|退役|取消|改掉)')
SUPERSEDED_AFTER_NEAR = re.compile(r'被纠正|被推翻|被取代|已退役')
NEARBY = 6
SIMILARITY_LIMIT = 0.6
MIN_PARAGRAPH_HANZI = 50
POLICY = Path(__file__).with_name('validation-policy.json')

LOCAL_PATH = re.compile(r'(?<![\w/.])(?:[A-Za-z]:[\\/][^\s`)|，。]*|/c/Users/[^\s`)|，。]*|~/[^\s`)|，。]*)')
GENERATED = re.compile(r'<!-- generated[^>]*start -->[\s\S]*?<!-- generated[^>]*end -->')
FENCE = re.compile(r'```[\s\S]*?```')
LINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')
HANZI = re.compile(r'[一-鿿]')
REDLINE_MARK = re.compile(r'（红线|\*\*红线|红线\*\*|\| 红线 \||^#+ .*红线', re.M)


def visible(text):
    """What a reader sees: link targets, emphasis and code ticks removed."""
    return re.sub(r'[*`]', '', LINK.sub(r'\1', text)).strip()


def prose(text):
    return FENCE.sub('', GENERATED.sub('', text))


def is_case(name):
    return Path(name).name.startswith('case-')


def vendored(name):
    return any(part in ('source', 'skill', 'revisions') for part in Path(name).parts)


def rule_layer(name):
    if not name.endswith('.md') or vendored(name) or is_case(name):
        return False
    if name == 'AGENTS.md' or name.startswith('brain/') or name.startswith('work/domains/'):
        return True
    return name.startswith('system/') and not name.startswith(('system/repository/navigation/', 'system/repository/maintenance/'))


def redline_marks(text):
    return len(REDLINE_MARK.findall(prose(text)))


def redline_scope(name):
    """Every Markdown file a reader may take a rule from: methods, cases, projects, entries."""
    return (name.endswith('.md') and not vendored(name)
            and not name.startswith(('system/repository/navigation/', 'system/repository/maintenance/')))


def redline_budget():
    import json
    return json.loads(POLICY.read_text(encoding='utf-8')).get('redlineBudget', {})


def redline_counts(root, files):
    root = Path(root)
    counts = {}
    for name in files:
        if redline_scope(name):
            n = redline_marks((root / name).read_text(encoding='utf-8', errors='replace'))
            if n:
                counts[name] = n
    return counts


def local_paths(text):
    return LOCAL_PATH.findall(prose(text))


def long_brain_lines(text):
    return [(n, len(visible(line))) for n, line in enumerate(text.splitlines(), 1) if len(visible(line)) > BRAIN_LINE_LIMIT]


def long_agents_cells(text):
    found = []
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith('|') and not set(line) <= set('|-: '):
            for cell in line.strip().strip('|').split('|'):
                if len(visible(cell)) > AGENTS_CELL_LIMIT:
                    found.append((n, len(visible(cell))))
    return found


def paragraphs(text):
    for block in re.split(r'\n\s*\n|\n(?=[-|*>]|\d+\.)', LINK.sub(r'\1', prose(text))):
        hanzi = ''.join(HANZI.findall(block))
        if len(hanzi) >= MIN_PARAGRAPH_HANZI:
            yield block.strip(), {hanzi[i:i + 4] for i in range(len(hanzi) - 3)}


def similar_paragraphs(texts):
    """texts: {name: text}. Returns (similarity, name_a, name_b, excerpt) across different files."""
    items = [(name, block, shingles) for name, text in texts.items() for block, shingles in paragraphs(text)]
    index = defaultdict(list)
    for i, (_, _, shingles) in enumerate(items):
        for s in shingles:
            index[s].append(i)
    shared = defaultdict(int)
    for members in index.values():
        if len(members) <= 40:
            for a, b in combinations(members, 2):
                if items[a][0] != items[b][0]:
                    shared[(a, b)] += 1
    found = []
    for (a, b), count in shared.items():
        score = count / min(len(items[a][2]), len(items[b][2]))
        if score >= SIMILARITY_LIMIT:
            found.append((round(score, 2), items[a][0], items[b][0], items[a][1][:40].replace('\n', ' ')))
    return sorted(found, reverse=True)


def retired_terms(text):
    """{detection word: old saying} from the 退役表 in retired-rules.md."""
    terms, in_table = {}, False
    for line in text.splitlines():
        if line.startswith('## '):
            in_table = line.strip() == '## 退役表'
            continue
        if not in_table or not line.startswith('|') or set(line) <= set('|-: '):
            continue
        cells = [cell.strip() for cell in line.strip().strip('|').split('|')]
        # A row Jianwei took back (退役日期 cell notes 要回) no longer blocks its words.
        if len(cells) >= 3 and cells[0] != '退役日期' and '要回' not in cells[0]:
            for word in re.findall(r'`([^`]+)`', cells[2]):
                terms[word] = cells[1][:30]
    return terms


def retired_hits(text, terms):
    """Uses of a retired saying outside a level-2 history section (来源 / 来历 …, until the next
    level-2 heading). A use is allowed only when the words right around it say it was superseded."""
    hits, exempt = [], False
    for line in prose(text).splitlines():
        if line.startswith('## '):
            exempt = bool(HISTORY_HEADING.match(line))
            continue
        if exempt or line.startswith('#'):
            continue
        for word, old in terms.items():
            start = line.find(word)
            while start != -1:
                before = line[max(0, start - NEARBY):start]
                after = line[start + len(word):start + len(word) + NEARBY]
                if not (SUPERSEDED_BEFORE.search(before) or SUPERSEDED_AFTER.search(after)
                        or SUPERSEDED_AFTER_NEAR.search(after)):
                    hits.append((word, old))
                    break
                start = line.find(word, start + 1)
    return hits


def check(root, files, budget=None):
    root = Path(root)
    budget = redline_budget() if budget is None else budget
    errors = []
    texts = {}
    for name in files:
        if not name.endswith('.md'):
            continue
        text = (root / name).read_text(encoding='utf-8', errors='replace')
        if name.startswith('work/domains/') and not is_case(name) and not vendored(name):
            for hit in local_paths(text)[:3]:
                errors.append(f'本机路径写进了领域方法，应移到案例或项目: {name}: {hit}')
        if name.startswith('brain/'):
            for line, length in long_brain_lines(text):
                errors.append(f'大脑条目过长（{length}字>{BRAIN_LINE_LIMIT}），只留原则并链接执行细节: {name}:{line}')
        if name == 'AGENTS.md':
            size = len(text.encode('utf-8'))
            if size > AGENTS_MAX_BYTES:
                errors.append(f'AGENTS.md 有 {size} 字节，超过 {AGENTS_MAX_BYTES}：Codex 读到 32 KiB 就不再往下读，细则移到链接的入口里')
            for line, length in long_agents_cells(text):
                errors.append(f'AGENTS任务表单元格过长（{length}字>{AGENTS_CELL_LIMIT}），细则放进链接的入口: AGENTS.md:{line}')
        if rule_layer(name):
            texts[name] = text
    register = root / RETIRED
    terms = retired_terms(register.read_text(encoding='utf-8')) if register.is_file() else {}
    for name, text in sorted(texts.items()):
        if name in RETIRED_EXEMPT:
            continue
        for word, old in retired_hits(text, terms):
            errors.append(f'已退役的说法又出现了（“{word}”，旧说法：{old}），正文按退役表里“现在以哪里为准”的写法改: {name}')
    for score, a, b, excerpt in similar_paragraphs(texts):
        errors.append(f'同一规则写在两处（相似度{score}），只保留一处正文、另一处改为链接: {a} <> {b}: {excerpt}')
    for name, n in sorted(redline_counts(root, files).items()):
        if n > budget.get(name, 0):
            errors.append(f'红线标记增加（{name}：{budget.get(name, 0)}处→{n}处）：新的红线只有建委能定，AI 写的规则请标默认；建委确认过的新红线，同时改 validation-policy.json 的 redlineBudget')
    return errors

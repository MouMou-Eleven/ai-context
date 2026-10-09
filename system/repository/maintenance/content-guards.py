"""Content rules that keep the repository maintainable by any AI.

Each rule has one home (see ingestion-workflow.md#一条规则只有一个家红线); these checks
block the most common ways that home gets bypassed.
"""
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path

BRAIN_LINE_LIMIT = 220
AGENTS_CELL_LIMIT = 130
SIMILARITY_LIMIT = 0.6
MIN_PARAGRAPH_HANZI = 50

LOCAL_PATH = re.compile(r'(?<![\w/.])(?:[A-Za-z]:[\\/][^\s`)|，。]*|/c/Users/[^\s`)|，。]*|~/[^\s`)|，。]*)')
GENERATED = re.compile(r'<!-- generated[^>]*start -->[\s\S]*?<!-- generated[^>]*end -->')
FENCE = re.compile(r'```[\s\S]*?```')
LINK = re.compile(r'\[([^\]]*)\]\([^)]*\)')
HANZI = re.compile(r'[一-鿿]')


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


def check(root, files):
    root = Path(root)
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
            for line, length in long_agents_cells(text):
                errors.append(f'AGENTS任务表单元格过长（{length}字>{AGENTS_CELL_LIMIT}），细则放进链接的入口: AGENTS.md:{line}')
        if rule_layer(name):
            texts[name] = text
    for score, a, b, excerpt in similar_paragraphs(texts):
        errors.append(f'同一规则写在两处（相似度{score}），只保留一处正文、另一处改为链接: {a} <> {b}: {excerpt}')
    return errors

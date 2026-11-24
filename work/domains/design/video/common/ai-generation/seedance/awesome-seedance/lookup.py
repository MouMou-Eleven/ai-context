"""Read a selected template or exact case from the pinned local snapshot, without network."""
import argparse
from copy import deepcopy
import json
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / 'source'


def read_json(name):
    return json.loads((SOURCE / name).read_text(encoding='utf-8'))


def template_record(template_id):
    data = read_json('data/style-library.json')
    local = read_json('data/templates-local.json')
    templates = {t['id']: deepcopy(t) for t in data['templates']}
    for key, override in local.get('overrides', {}).items():
        if key not in templates:
            continue
        for field, value in override.items():
            if isinstance(value, dict) and isinstance(templates[key].get(field), dict):
                templates[key][field].update(value)
            else:
                templates[key][field] = value
    templates.update({t['id']: t for t in local.get('templates', [])})
    if template_id not in templates:
        raise ValueError('未找到模板ID：' + template_id)
    return templates[template_id]


def lookup(case=None, template=None):
    data = read_json('data/cases.json')
    cases = {c['slug']: c for c in data['cases']}
    result = {'evidenceBoundary': '上游快照报告，不是本次生成或建委实测；空复测不代表失败或成功。',
              'snapshot': json.loads((SOURCE.parent / 'upstream.json').read_text(encoding='utf-8'))['commit']}
    if case:
        if case not in cases:
            raise ValueError('未找到案例slug：' + case)
        result['case'] = cases[case]
    elif template:
        t = template_record(template)
        result['template'] = t
        # Preserve the upstream anchor order; popularity is not a claim of reproducibility.
        anchors = t.get('exampleCases', [])
        result['anchorCases'] = [cases[s] for s in anchors if s in cases][:2]
        result['missingAnchorSlugs'] = [s for s in anchors if s not in cases]
        result['note'] = '锚点最多两条；其余按template.exampleCases逐条查。先比实际输入与复测条件，不按热度认定适用。'
    else:
        raise ValueError('必须指定case或template')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--case', help='案例链接末尾的精确slug')
    group.add_argument('--template', help='模板文件名，不含.md')
    args = parser.parse_args()
    try:
        print(json.dumps(lookup(args.case, args.template), ensure_ascii=False, indent=2))
    except ValueError as error:
        parser.error(str(error))

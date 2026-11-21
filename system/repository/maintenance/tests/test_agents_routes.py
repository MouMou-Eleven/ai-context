"""AGENTS.md (what every AI reads) and routes.json (its machine copy) must not drift apart.

Before 2026-11-21 the two had silently diverged: run with the old routes.json, 15 of the 34 AGENTS
rows that list files missed some of them for a real task (e.g. a courseware for a publicity post skipped the role scenarios).
"""
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import MAINTENANCE, ROOT, load_module

validator = load_module('validate-context')
ROUTES = 'system/repository/navigation/routes.json'


class AgentsRoutes(unittest.TestCase):
    def test_repository_has_no_drift(self):
        self.assertEqual(validator.check_agents_routes(ROOT), [])

    def test_every_row_is_parsed(self):
        rows = validator.agents_task_rows((ROOT / 'AGENTS.md').read_text(encoding='utf-8'))
        self.assertGreater(len(rows), 25)
        self.assertIn('work/domains/training/experience/role-specific-scenarios.md',
                      next(v for k, v in rows.items() if k.startswith('写培训**课件**'))[0])
        self.assertIn('work/domains/training/README.md', next(v for k, v in rows.items() if k.startswith('写培训**课件**'))[1])

    def drift(self, edit_agents=None, edit_routes=None):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / MAINTENANCE, root / MAINTENANCE, ignore=shutil.ignore_patterns('__pycache__', 'tests'))
            (root / ROUTES).parent.mkdir(parents=True)
            agents = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
            routes = json.loads((ROOT / ROUTES).read_text(encoding='utf-8'))
            if edit_agents:
                agents = edit_agents(agents)
            if edit_routes:
                edit_routes(routes)
            (root / 'AGENTS.md').write_text(agents, encoding='utf-8')
            (root / ROUTES).write_text(json.dumps(routes, ensure_ascii=False), encoding='utf-8')
            return validator.check_agents_routes(root)

    def test_new_agents_row_without_example_is_blocked(self):
        row = '| 写招聘启事 | [宣传写法](work/domains/self-media/marketing-copy/reader-question-led-promotion.md) |\n'
        errors = self.drift(edit_agents=lambda t: t.replace('| 公众号 / 图文文章 |', row + '| 公众号 / 图文文章 |', 1))
        self.assertTrue(any('写招聘启事' in e and '没有示例任务' in e for e in errors))

    def test_file_added_to_agents_but_not_routes_is_blocked(self):
        extra = '[审美标尺](work/domains/design/common/design-principles/taste-benchmarks.md)'
        errors = self.drift(edit_agents=lambda t: t.replace('| [教程写法](work/domains/training/experience/tutorial-writing.md)',
                                                          '| ' + extra + ' + [教程写法](work/domains/training/experience/tutorial-writing.md)', 1))
        self.assertTrue(any('taste-benchmarks.md' in e and '读不到' in e for e in errors))

    def test_renamed_row_leaves_stale_example(self):
        errors = self.drift(edit_routes=lambda r: r['agentsRowExamples'].update({'已经删掉的一行': ['随便一句']}))
        self.assertTrue(any('已经删掉的一行' in e for e in errors))


if __name__ == '__main__':
    unittest.main()

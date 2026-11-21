"""Content guards must block the ways a rule's single home gets bypassed."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import ROOT, load_module, repo_files

guards = load_module('content-guards')
RULE = '写入仓库前先搜索同一件事有没有已有正文，有就改那一处，不要在入口、领域说明和大脑里各写一遍，否则几个月后几处说法会互相矛盾。'


class Guards(unittest.TestCase):
    def test_repository_passes(self):
        self.assertEqual(guards.check(ROOT, repo_files(ROOT)), [])

    def test_local_path_in_method_is_caught(self):
        self.assertTrue(guards.local_paths('模板在 `F:\桌面文件\模板.pptx`，先实测。'))
        self.assertFalse(guards.local_paths('模板先实测，例：见[案例](case-a.md)。'))

    def test_long_brain_line_is_caught(self):
        self.assertTrue(guards.long_brain_lines('- ' + '原则' * 150))
        self.assertFalse(guards.long_brain_lines('- **短原则。** 执行见[链接](../x.md)。'))

    def test_long_agents_cell_is_caught(self):
        self.assertTrue(guards.long_agents_cells('| 任务 | ' + '细则' * 80 + ' |'))
        self.assertFalse(guards.long_agents_cells('| 任务 | [入口](a.md) |'))

    def test_same_rule_in_two_files_is_caught(self):
        reworded = RULE.replace('写入仓库前', '往仓库写之前').replace('否则', '不然')
        self.assertTrue(guards.similar_paragraphs({'a.md': RULE, 'b.md': reworded}))
        self.assertFalse(guards.similar_paragraphs({'a.md': RULE, 'b.md': '规则见[写入规范](x.md)。'}))

    def test_retired_saying_is_caught_outside_history(self):
        register = (ROOT / guards.RETIRED).read_text(encoding='utf-8')
        terms = guards.retired_terms(register)
        self.assertIn('五问法', terms)
        self.assertTrue(guards.retired_hits('## 课上怎么讲\n\n先用五问法把要求说清楚。', terms))
        # 说明它已被取代的句子、来历小节里的记录，都不算复活
        self.assertFalse(guards.retired_hits('## 课上怎么讲\n\n以前的五问法已经拆进对照表。', terms))
        self.assertFalse(guards.retired_hits('## 来源与状态\n\n- 第 3 课用了五问法。', terms))

    def test_agents_entry_stays_under_codex_limit(self):
        size = len((ROOT / 'AGENTS.md').read_text(encoding='utf-8').encode('utf-8'))
        self.assertLessEqual(size, guards.AGENTS_MAX_BYTES)


if __name__ == '__main__':
    unittest.main()

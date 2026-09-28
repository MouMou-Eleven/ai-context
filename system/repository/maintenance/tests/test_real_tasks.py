"""Regression: real tasks from 建委 (2026-09-28) must reach the experience that answers them.

Each case was a real failure before the restructure. The router mirrors the AGENTS.md
task table; if either drifts, these tests fail.
"""
import sys
from pathlib import Path
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import ROOT, load_module

router = load_module('context-route')
TR = 'work/domains/training/'
CM = 'work/domains/other/commercial/'
VOICE = 'system/expression/voice-samples.md'


class RealTasks(unittest.TestCase):
    def reads(self, task):
        return router.resolve(task, 'auto')['read']

    def test_bank_office_courseware(self):
        read = self.reads('帮我写一份给银行员工的AI办公培训课件，3小时')
        for path in [TR + 'experience/jianwei-training-style.md', VOICE,
                     TR + 'experience/demo-driven-course-design.md', TR + 'topics.md']:
            self.assertIn(path, read)

    def test_training_promotion_article_combines_domains(self):
        read = self.reads('写一篇公众号文章，宣传我下个月的AI培训，既要有干货又要招生')
        self.assertIn('work/domains/self-media/marketing-copy/reader-question-led-promotion.md', read)
        self.assertIn(TR + 'topics.md', read)
        self.assertIn(VOICE, read)

    def test_training_proposal_is_creation_and_reads_proposal_method(self):
        result = router.resolve('给济南某企业出一份AI培训方案', 'auto')
        self.assertEqual(result['intent'], 'create')
        self.assertIn(CM + 'experience/external-proposal-design.md', result['read'])
        self.assertIn(CM + 'experience/external-deliverable-language.md', result['read'])
        self.assertIn(TR + 'topics.md', result['read'])

    def test_miaoda_payment_reads_workflow_and_topic(self):
        read = self.reads('用秒哒做一个带支付的小程序')
        self.assertIn('work/domains/development/tools/miaoda/workflow.md', read)
        self.assertIn('work/domains/development/tools/miaoda/topics/payment.md', read)
        self.assertFalse(any('lark' in p for p in read))

    def test_promo_storyboard_reads_seedance(self):
        read = self.reads('帮我做一个企业宣传片的分镜和提示词')
        self.assertIn('work/domains/design/video/common/seedance/README.md', read)
        self.assertIn('work/domains/design/video/common/seedance/practical-workflow.md', read)

    def test_every_agents_table_link_exists(self):
        import re
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)#:]+\.md)\)', text):
            self.assertTrue((ROOT / target).is_file(), target)


if __name__ == '__main__':
    unittest.main()

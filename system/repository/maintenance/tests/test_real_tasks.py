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
        self.assertIn(TR + 'experience/external-proposal-design.md', result['read'])
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

    def test_training_sink_reads_ai_training_project(self):
        read = router.resolve('这些是培训的经验，沉淀到培训板块', 'write')['read']
        self.assertIn('work/projects/ai-training/README.md', read)
        self.assertIn('system/repository/ingestion-workflow.md', read)

    def test_roadshow_reads_competition_rules(self):
        read = self.reads('准备OPC比赛路演PPT')
        self.assertIn(CM + 'experience/competition-and-investor-materials.md', read)

    def test_sales_talk_and_nonprofit_reach_commercial_map(self):
        self.assertIn(CM + 'README.md', self.reads('和企业客户谈单的沟通话术'))
        self.assertIn(CM + 'README.md', self.reads('给公益组织写一份AI培训方案'))

    def test_brain_auto_distill_rule_has_one_home(self):
        home = (ROOT / 'system/repository/ingestion-workflow.md').read_text(encoding='utf-8')
        self.assertIn('### 建委大脑自动提炼', home)
        for rel in ['AGENTS.md', 'brain/README.md']:
            text = (ROOT / rel).read_text(encoding='utf-8')
            self.assertIn('ingestion-workflow.md#建委大脑自动提炼', text, rel)
            self.assertNotIn('先查重，已有就不写', text, rel)

    def test_courseware_beautify_is_ppt_design_not_training(self):
        for task in ['给这份课件做美化', '这份培训课件的排版重新设计一下', '幻灯片美化']:
            result = router.resolve(task, 'create')
            self.assertEqual(result['selectedCandidate'], 'ppt', task)
            self.assertIn('work/domains/design/graphic/ppt/ai-assisted-design/workflow.md', result['read'], task)
            self.assertNotIn(TR + 'experience/jianwei-training-style.md', result['read'], task)
        self.assertEqual(router.resolve('帮我写一份给银行员工的AI办公培训课件', 'create')['selectedCandidate'], 'training')

    def test_roadshow_is_commercial_and_speech_is_training(self):
        for task in ['写一份创赛路演演讲稿', '准备项目答辩的路演稿']:
            result = router.resolve(task, 'create')
            self.assertEqual(result['selectedCandidate'], 'commercial', task)
            self.assertIn(CM + 'experience/competition-and-investor-materials.md', result['read'], task)
            self.assertNotIn('question-meaning-example-sharing', [m['id'] for m in result['methods']], task)
        speech = router.resolve('准备一场关于AI的主题演讲', 'create')
        self.assertEqual(speech['selectedCandidate'], 'training')
        self.assertIn('question-meaning-example-sharing', [m['id'] for m in speech['methods']])

    def test_generic_contest_video_is_not_chuangsai(self):
        self.assertNotEqual(router.resolve('做一个比赛宣传片', 'create')['selectedCandidate'], 'competition-video')
        self.assertEqual(router.resolve('做一个AI大赛的参赛视频', 'create')['selectedCandidate'], 'video')
        self.assertEqual(router.resolve('做一个创赛宣传片', 'create')['selectedCandidate'], 'competition-video')

    def test_lecturer_intro_is_personal_not_training(self):
        for task in ['写一份讲师介绍', '写个人简介']:
            result = router.resolve(task, 'create')
            self.assertEqual(result['selectedCandidate'], 'personal', task)
            self.assertIn('brain/preferences.md', result['read'], task)

    def test_tutorial_and_article_genres_load_writing_methods_for_any_topic(self):
        self.assertIn(TR + 'experience/tutorial-writing.md', self.reads('把PPT设计流程写成保姆级教程'))
        self.assertIn('work/domains/self-media/articles/README.md', router.resolve('写一篇公众号文章介绍我的AI做PPT方法', 'create')['read'])

    def test_expression_source_anchors_resolve(self):
        text = (ROOT / 'system/expression/corrections.md').read_text(encoding='utf-8')
        for heading in ['## 来源表', '### 外部表达参考', '## 好材料怎样提炼成可用方法']:
            self.assertIn('\n' + heading + '\n', text)
        for code in ['| T1 |', '| G1 |', '| O2 |', '| F8 |']:
            self.assertIn(code, text)

    def test_every_agents_table_link_exists(self):
        import re
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)#:]+\.md)\)', text):
            self.assertTrue((ROOT / target).is_file(), target)


if __name__ == '__main__':
    unittest.main()

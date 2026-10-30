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

    def test_hands_on_video_reads_code_video_without_saying_code(self):
        # 2026-10-30: 建委 asks for edits in plain words; the AI still works in code.
        cv = 'work/domains/design/common/code-driven-video/README.md'
        for task in ['帮我剪一下这个视频', '在这个视频上给我做个科技感的效果', '给这段视频加字幕和标题',
                     '把这几个镜头剪成30秒宣传片', '这个创赛视频帮我做一下片头和转场', '微课视频加个动画效果']:
            self.assertIn(cv, self.reads(task), task)
        self.assertEqual(router.resolve('把这几个镜头剪成30秒宣传片', 'create')['selectedCandidate'], 'enterprise-video')
        self.assertEqual(router.resolve('这个创赛视频帮我做一下片头和转场', 'create')['selectedCandidate'], 'competition-video')
        for task in ['帮我写一段Seedance视频提示词', '写一个企业宣传片的即梦提示词', '帮我设计一张海报']:
            self.assertNotIn(cv, self.reads(task), task)

    def test_teacher_courseware_is_design_and_own_courseware_is_training(self):
        for task in ['最近承接了一个语文课件的订单', '给老师做一份三年级数学课件', '帮老师美化一下课件']:
            self.assertEqual(router.resolve(task, 'create')['selectedCandidate'], 'ppt', task)
        self.assertEqual(router.resolve('最近承接了一个精品课的订单，有指定模板', 'create')['selectedCandidate'], 'microcourse')
        for task in ['给山东高速做AI办公培训，准备培训课件和演示用的Excel文件', '最近承接了一个企业AI培训，先写培训大纲']:
            self.assertEqual(router.resolve(task, 'create')['selectedCandidate'], 'training', task)

    def test_wancai_and_education_mg_are_microcourse(self):
        for task in ['最近需要做一个教育类的万彩微课', '做一个教育类的MG动画']:
            self.assertEqual(router.resolve(task, 'create')['selectedCandidate'], 'microcourse', task)
        self.assertNotEqual(router.resolve('做一个企业MG动画宣传', 'create')['selectedCandidate'], 'microcourse')

    def test_graphic_design_principles_trigger_for_all_graphic_work(self):
        base = 'work/domains/design/common/design-principles/'
        for task in ['帮我设计一张活动海报', '做一份PPT', '设计一本画册的内页版式']:
            result = router.resolve(task, 'create')
            self.assertIn('graphic-design-principles', [m['id'] for m in result['methods']], task)
            self.assertIn(base + 'README.md', result['read'], task)
        self.assertIn(base + 'color.md', self.reads('这张海报配色不好看，帮我改改'))
        self.assertIn(base + 'mood.md', router.resolve('做一份企业介绍PPT，要有高级感', 'create')['read'])
        self.assertNotIn('graphic-design-principles', [m['id'] for m in router.resolve('写一份银行员工的AI办公培训课件', 'create')['methods']])

    def test_template_courseware_is_not_premium_course(self):
        result = router.resolve('给老师美化一份课件，有学校的模板', 'create')
        self.assertEqual(result['selectedCandidate'], 'ppt')
        self.assertIn('ai-assisted-ppt-design', [m['id'] for m in result['methods']])
        premium = router.resolve('最近承接了一个精品课的订单，要录课合成', 'create')
        self.assertIn('premium-course-production', [m['id'] for m in premium['methods']])
        self.assertIn('work/domains/design/graphic/ppt/ai-assisted-design/workflow.md', premium['read'])

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

    def test_tianjin_contest_math_regeneration_reaches_format_rules(self):
        """2026-10-29: another AI read the repo and still used theme fonts and blank team tables."""
        ED = 'work/domains/development/industry-cases/education/'
        read = self.reads('看我的GitHub仓库，重新生成一份天津智能体比赛数学的申报书和技术说明与验证报告')
        for path in [ED + 'tianjin-agent-contest/README.md', ED + 'tianjin-agent-contest/submission-package.md',
                     ED + 'tianjin-agent-contest/document-format.md', CM + 'experience/competition-and-investor-materials.md']:
            self.assertIn(path, read)
        video = self.reads('帮我写天津大赛赛道二演示视频的逐字稿并录屏')
        self.assertIn(ED + 'tianjin-agent-contest/demo-video.md', video)

    def test_tianjin_platform_and_subject_integration(self):
        ED = 'work/domains/development/industry-cases/education/'
        read = self.reads('在天津平台上给客户搭一个英语智能体')
        for path in [ED + 'tianjin-agent-contest/platform/capabilities.md', ED + 'tianjin-agent-contest/platform/build-sop.md',
                     ED + 'subject-integration/classroom-agent-design.md']:
            self.assertIn(path, read)
        generic = self.reads('用扣子做一个科学课的教育智能体')
        self.assertIn(ED + 'subject-integration/classroom-agent-design.md', generic)
        self.assertNotIn(ED + 'tianjin-agent-contest/document-format.md', generic)

    def test_every_agents_table_link_exists(self):
        import re
        text = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)#:]+\.md)\)', text):
            self.assertTrue((ROOT / target).is_file(), target)


if __name__ == '__main__':
    unittest.main()


class DesignAndContestTasks(unittest.TestCase):
    """建委 2026-10-30：设计经验躺在平面目录用不上、"好看"没人翻译；比赛视频经验只留在比赛目录。"""
    DP = 'work/domains/design/common/design-principles/'
    CV = 'work/domains/design/common/code-driven-video/'

    def reads(self, task):
        return router.resolve(task, 'auto')['read']

    def test_video_beautify_reads_shared_principles_and_vocabulary(self):
        read = self.reads('把这个视频包装得好看一点，要有科技感')
        for path in [self.CV + 'README.md', self.DP + 'README.md', self.DP + 'aesthetic-vocabulary.md']:
            self.assertIn(path, read)

    def test_generic_screen_edit_does_not_pull_contest_rules(self):
        # 比赛视频的专属做法只留在比赛目录；普通录屏剪辑不能读到天津的要求。
        read = self.reads('帮我剪一下这个智能体演示录屏，加框选标注')
        self.assertIn(self.CV + 'README.md', read)
        self.assertFalse(any('tianjin' in p for p in read))

    def test_tianjin_demo_video_reads_contest_video_method(self):
        read = self.reads('天津大赛的演示视频，帮我剪辑一下')
        self.assertIn('work/domains/development/industry-cases/education/tianjin-agent-contest/demo-video.md', read)

    def test_website_redesign_reads_design_principles(self):
        read = self.reads('给网站首页改版，要更有设计感')
        self.assertIn('work/domains/development/experience/frontend-ui-quality-standards.md', read)
        self.assertIn(self.DP + 'README.md', read)

    def test_poster_not_premium_reads_vocabulary(self):
        self.assertIn(self.DP + 'aesthetic-vocabulary.md', self.reads('这个海报不够高级，帮我改改'))


class DeliverableAutoTriggers(unittest.TestCase):
    """建委 2026-10-31：顺带要交 Word、要出画面时自动用规范，不等他提；比赛模板优先。"""
    FMT = 'work/domains/other/commercial/delivery-formats/gov-enterprise-word.md'
    DP = 'work/domains/design/common/design-principles/README.md'

    def reads(self, task):
        return router.resolve(task, 'auto')['read']

    def test_word_for_government_school_enterprise_reads_delivery_format(self):
        for task in ['帮我写一份项目总结报告，用Word交付给区教育局', '给这个企业客户出一份合作方案的Word文档',
                     '把这个智能体的使用说明整理成Word交给学校']:
            self.assertIn(self.FMT, self.reads(task), task)

    def test_contest_template_word_does_not_take_business_format(self):
        self.assertNotIn(self.FMT, self.reads('重写天津大赛数学作品的申报书Word'))

    def test_any_visual_deliverable_reads_design_principles(self):
        for task in ['做一个介绍我们产品的PPT', '给智能体比赛做个流程图', '给课程做个招生海报']:
            self.assertIn(self.DP, self.reads(task), task)

    def test_lookup_does_not_trigger_deliverable_rules(self):
        read = self.reads('看一下仓库里有哪些PPT经验')
        self.assertNotIn(self.FMT, read)

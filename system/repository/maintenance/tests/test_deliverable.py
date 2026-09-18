import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import load_module

checker = load_module('check-deliverable')
router = load_module('context-route')


class DeliverableChecks(unittest.TestCase):
    def test_cadre_training_keeps_project_and_practical_method(self):
        result = router.resolve('修改济南市总工会AI培训方案，实操先工具全景后场景', 'create')
        self.assertEqual(result['selectedCandidate'], 'external-training')
        self.assertIn('work/projects/external-training/jinan-cadre-ai/README.md', result['read'])
        self.assertIn('work/domains/training/experience/demo-driven-course-design.md', result['read'])
        self.assertIn('work/domains/other/commercial/experience/external-proposal-design.md',result['read'])
        self.assertEqual(checker.inspect('提示词设计与任务表达：讲解提示词构成、优化工具与效果比较。', 'external-proposal'), [])
        result = router.resolve('只查济南市总工会培训方案位置', 'read')
        self.assertIn('work/projects/external-training/jinan-cadre-ai/README.md', result['read'])
        self.assertNotIn('work/domains/training/experience/demo-driven-course-design.md', result['read'])

    def test_external_proposal_rejected_fragments(self):
        fragments = ['以公开真实材料为基础，以可核验的工作成果为落点。',
                     '本方案为课程设计文件', '两场授课的分工', '各配置的内容边界',
                     '整体时长联动', '每个案例使用同一条操作路径',
                     '现场不预设AI一定出错。若当次输出正确，继续检查。',
                     '公开政策与案例来源', '案例与演示的证据范围', '工具依据与使用说明',
                     '原文中的事项', '应当保留的判断边界', 'https://example.org/policy']
        for fragment in fragments:
            self.assertTrue(checker.inspect(fragment, 'external-proposal'), fragment)
            self.assertEqual(checker.inspect(fragment, 'instructor'), [])

    def test_external_proposal_legitimate_content_is_not_banned(self):
        text = '组织单位：济南市总工会\n培训时长：3小时，实操1.5—2小时\n讲师：黄宏伟、杨建委\n课程介绍：政策研读、群众诉求分析、信息脱敏与安全使用。'
        self.assertEqual(checker.inspect(text, 'external-proposal'), [])

    def test_docx_split_runs_hidden_links_and_inherited_title_alignment(self):
        ns = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'proposal.docx'
            def make(align='center', text='培训方案', hyperlink=False, title=True):
                with zipfile.ZipFile(path, 'w') as z:
                    style = '<w:pStyle w:val="Title"/>' if title else ''
                    z.writestr('word/document.xml', f'<w:document xmlns:w="{ns}"><w:body><w:p><w:pPr>{style}</w:pPr><w:r><w:t>{text[:2]}</w:t></w:r><w:r><w:t>{text[2:]}</w:t></w:r></w:p></w:body></w:document>')
                    z.writestr('word/styles.xml', f'<w:styles xmlns:w="{ns}"><w:style w:styleId="Base"><w:pPr><w:jc w:val="{align}"/></w:pPr></w:style><w:style w:styleId="Title"><w:basedOn w:val="Base"/></w:style></w:styles>')
                    if hyperlink:
                        z.writestr('word/_rels/document.xml.rels', '<Relationships><Relationship Type="test/hyperlink" Target="https://example.org" TargetMode="External"/></Relationships>')
            make()
            self.assertEqual(checker.check(path,'external-proposal','gov-enterprise-word')['findings'], [])
            make('left','两场授课的分工',True)
            rules = {x['rule'] for x in checker.check(path,'external-proposal','gov-enterprise-word')['findings']}
            self.assertEqual(rules, {'internal-design','proposal-hyperlink','word-title-center'})
            make(title=False)
            self.assertEqual(checker.check(path,'external-proposal','gov-enterprise-word')['findings'][0]['rule'], 'word-title-missing')
            path.write_bytes(b'not a docx')
            with self.assertRaises(zipfile.BadZipFile):
                checker.check(path, 'external-proposal')

    def test_proposal_routes_include_audience_and_format_methods(self):
        result = router.resolve('写AI培训方案给组织方，Word格式', 'create')
        for name in ['experience/external-proposal-design.md', 'delivery-formats/gov-enterprise-word.md']:
            self.assertIn('work/domains/other/commercial/'+name, result['read'])
        for task in ['给讲师写内部备课稿', '写内部培训方案', '只查培训方案位置']:
            result = router.resolve(task, 'read' if task.startswith('只查') else 'create')
            self.assertNotIn('work/domains/other/commercial/experience/external-proposal-design.md',result['read'])

    def test_original_failure_excerpt_is_detected(self):
        # Actual headings/callout fragments from the 2026-09-13 draft; no model facts.
        text = '<h1>两小时怎么讲：先给结果，再用案例证明</h1><h1>先把结论讲在前面</h1><table><tr><th>现场重点看什么</th></tr></table><callout><p>现场使用建议：不要从头到尾连续播。</p></callout>'
        findings = checker.inspect(text, markup=True)
        self.assertEqual(len(findings), 5)
        self.assertEqual({f['rule'] for f in findings}, {'teaching-time', 'meta-instruction', 'instructor-cue'})

    def test_student_exercise_and_role_facts_are_not_banned(self):
        self.assertEqual(checker.inspect('请用10分钟完成练习。\n讲师账号和学员账号的权限不同。\n普通人也可能是调查对象。\n本次课程总时长两小时。'), [])

    def test_explicit_instructor_draft_is_not_learner_linted(self):
        self.assertEqual(checker.inspect('讲师提醒：先检查投影。两小时怎么讲', 'instructor'), [])

    def test_quoted_counterexample_remains_a_review_signal(self):
        findings = checker.inspect('错误示例：“现场重点看什么”不适合作为本页表头。')
        self.assertTrue(findings)
        self.assertIn('引用', findings[0]['action'])

    def test_split_xml_text_and_entities_are_checked(self):
        self.assertTrue(checker.inspect('<p>讲师<b>提醒</b>&#xff1a;播放视频</p>', markup=True))
        self.assertEqual(checker.inspect('<p>练习</p><img alt="讲师提醒" src="private-token"/>', markup=True), [])

    def test_empty_or_script_only_is_not_success(self):
        for content, markup in [('', False), ('<script>讲师提醒</script>', True)]:
            with self.assertRaises(ValueError):
                checker.inspect(content, markup=markup)

    def test_hash_changes_and_no_findings_never_mean_approval(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory)/'draft.md'
            path.write_text('先比较两种操作的结果。', encoding='utf-8')
            first = checker.check(path)
            self.assertFalse(first['approved'])
            self.assertIn('semantic_review', first['status'])
            self.assertEqual(first['sha256'], hashlib.sha256(path.read_bytes()).hexdigest())
            path.write_text('讲师提醒：先比较结果。', encoding='utf-8')
            second = checker.check(path)
            self.assertNotEqual(first['sha256'], second['sha256'])
            self.assertTrue(second['findings'])

    def test_share_material_routes_to_training_not_just_a_keyword_index(self):
        for task in ['整理模型分享资料，讲两个小时', '写分享内容供学员阅读', '修改讲课文档']:
            result = router.resolve(task, 'create')
            self.assertEqual(result['selectedCandidate'], 'training')
            self.assertIn('work/domains/training/experience/jianwei-training-style.md', result['read'])
            self.assertIn('system/repository/execution-checks.md', result['read'])

    def test_general_delivery_checks_apply_across_domains(self):
        for task in ['做企业宣传片', '开发网站', '写商业计划书', '修改飞书书稿', '写朋友圈']:
            result = router.resolve(task, 'create')
            self.assertIn('system/repository/execution-checks.md', result['read'])
        result = router.resolve('查培训资料位置', 'read')
        self.assertNotIn('system/repository/execution-checks.md', result['read'])

    def test_sharing_a_post_does_not_become_classroom_creation(self):
        result = router.resolve('把分享资料写成朋友圈宣传', 'create')
        self.assertEqual(result['selectedCandidate'], 'self-media')
        self.assertNotIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_promotion_reads_method_and_project_without_teacher_draft_rules(self):
        for task in ['给会员社群写介绍页，讲解AI编程课程有什么价值',
                     '重写会员社群报名页', '给会员社群写宣传文章',
                     '给会员社群的对外宣传的文档换个写法',
                     '给会员社群写直播销售话术']:
            result = router.resolve(task, 'create')
            self.assertEqual(result['selectedCandidate'], 'self-media', task)
            self.assertIn('work/domains/self-media/marketing-copy/reader-question-led-promotion.md', result['read'])
            self.assertIn('work/projects/paid-community-course/README.md', result['read'])
            self.assertNotIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_teaching_promotion_as_a_subject_still_uses_training(self):
        result = router.resolve('给会员社群写一节教学课件，教大家怎样写产品介绍页', 'create')
        self.assertEqual(result['selectedCandidate'], 'community')
        self.assertIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_plain_articles_and_pure_teaching_do_not_load_sales_questions(self):
        for task in ['写一篇AI自媒体科普文章', '写AI培训文给学员，纯教学不招生',
                     '给讲师写内部备课稿', '只查会员社群报名页的位置']:
            intent = 'read' if task.startswith('只查') else 'create'
            result = router.resolve(task, intent)
            self.assertNotIn('work/domains/self-media/marketing-copy/reader-question-led-promotion.md', result['read'], task)

    def test_literal_folder_names_find_domain_and_keep_execution_checks(self):
        for folder, expected in [('self-media', 'self-media'), ('training', 'training')]:
            result = router.resolve(f'参考 work/domains/{folder} 写新内容', 'create')
            self.assertEqual(result['selectedCandidate'], expected)
            self.assertIn('system/repository/execution-checks.md', result['read'])

    def test_generic_promotion_does_not_invent_community_facts(self):
        result = router.resolve('写产品介绍和购买顾虑的推广文章', 'create')
        self.assertEqual(result['selectedCandidate'], 'self-media')
        self.assertIn('work/domains/self-media/marketing-copy/reader-question-led-promotion.md', result['read'])
        self.assertNotIn('work/projects/paid-community-course/README.md', result['read'])

    def test_question_marks_and_no_patterns_do_not_certify_reader_value(self):
        # Rejected opening from the actual promotion draft. It contains no learner-lint pattern.
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'promotion.md'
            path.write_text('你想做的事，能不能不再卡在“我不会”这一步？', encoding='utf-8')
            result = checker.check(path)
            self.assertEqual(result['findings'], [])
            self.assertFalse(result['approved'])
            self.assertIn('semantic_review', result['status'])


if __name__ == '__main__':
    unittest.main()

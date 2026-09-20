"""Natural requests, deeper discovery, boundaries and complete-source evidence."""
import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import ROOT, load_module, write_text
from context_retrieval import checked_scope, discover, enrich, infer_intent, source_pack

router = load_module('context-route')


class TaskRetrieval(unittest.TestCase):
    def test_natural_requests_choose_work_not_repository_maintenance(self):
        for task in ['参考我的GitHub仓库，帮我做一个客户预约小程序',
                     '参考仓库，给我做一个自动整理表格的脚本']:
            result = router.resolve(task, 'auto')
            self.assertEqual(result['selectedCandidate'], 'programming')
            self.assertEqual(result['intent'], 'create')
            self.assertIn('work/domains/development/experience/README.md', result['read'])
            self.assertNotIn('system/repository/ingestion-workflow.md', result['read'])

    def test_vague_request_needs_goal_not_exact_path(self):
        result = enrich(ROOT, router.resolve('看我的GitHub仓库', 'auto'))
        self.assertIsNone(result['selectedCandidate'])
        self.assertTrue(result['needsTaskDescription'])
        self.assertEqual(result['discovery'], [])
        self.assertEqual(router.resolve('修复仓库路由')['selectedCandidate'], 'system/repository')

    def test_article_goes_into_channel_without_training_or_sales_facts(self):
        result = router.resolve('参考仓库，写一篇公众号文章', 'auto')
        self.assertIn('work/domains/self-media/articles/README.md', result['read'])
        self.assertFalse(any('/training/' in p or '/paid-community-course/' in p for p in result['read']))
        self.assertNotIn('work/domains/self-media/marketing-copy/reader-question-led-promotion.md', result['read'])

    def test_project_promotion_reads_deeper_facts_without_teaching_methods(self):
        result = router.resolve('给会员社群写一篇课程宣传文章', 'auto')
        self.assertIn('work/projects/paid-community-course/positioning-and-vision.md', result['read'])
        self.assertIn('work/projects/paid-community-course/course-materials-index.md', result['read'])
        self.assertNotIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_unknown_vocabulary_is_search_review_not_missing_user_goal(self):
        result = enrich(ROOT, router.resolve('帮我整理客户预约的数据去重方案', 'auto'))
        self.assertTrue(result['needsRouteReview'])
        self.assertFalse(result['needsTaskDescription'])

    def test_miaoda_reads_upload_rules_without_loading_legacy_source(self):
        result = enrich(ROOT, router.resolve('用秒哒开发一个大视频上传页面', 'auto'))
        self.assertIn('work/domains/development/tools/miaoda/experience/patterns/large-video-upload.md', result['read'])
        self.assertIn('work/domains/development/tools/miaoda/experience/prompts/uploads.md', result['read'])
        self.assertTrue(any('large-video-upload.md' in h['path'] for h in result['discovery']))
        self.assertFalse(any('/reference-materials/' in p or '/yancut-ai/' in p for p in result['read']))

    def test_scope_enables_subdirectory_lookup_without_overriding_deliverable(self):
        result = router.resolve('帮我改这篇文章', 'auto', scope='work/domains/self-media')
        self.assertEqual(result['selectedCandidate'], 'self-media')
        self.assertIn('work/domains/self-media/articles/README.md', result['read'])
        result = router.resolve('给会员社群写朋友圈宣传', 'auto', scope='work/domains/training')
        self.assertEqual(result['selectedCandidate'], 'self-media')
        self.assertNotIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_training_audience_is_a_delivery_gate_not_route_success(self):
        for task, expected in [('帮我做一份培训分享资料，讲两小时', 'learner'),
                               ('写培训讲师内部备课稿', 'instructor'),
                               ('写一份提交组织方的培训方案', 'external-proposal')]:
            result = enrich(ROOT, router.resolve(task, 'auto'))
            self.assertEqual(result['deliverableCheck']['profile'], expected)
            self.assertFalse(result['completionGate']['readyToDeliver'])
            self.assertEqual(result['readingStatus'], 'planned-not-read')
        self.assertEqual(infer_intent('查会员社群课程进度'), 'read')


class DiscoveryEvidence(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()

    def test_new_method_is_searchable_without_new_registry(self):
        path = 'work/domains/development/experience/sheet-validation.md'
        write_text(self.root / path, '# 表格重复数据校验\n\n导入前检查重复记录与空值。\n')
        hits = discover(self.root, '表格导入重复记录怎么办', ['work/domains/development'])
        self.assertEqual(hits[0]['path'], path)
        self.assertEqual(hits[0]['status'], 'candidate-not-read')
        self.assertEqual((self.root / path).read_text(encoding='utf-8').splitlines()[hits[0]['line']-1], hits[0]['excerpt'])

    def test_history_raw_and_inactive_method_are_not_active_search_results(self):
        active = 'work/domains/training/experience/current.md'
        paths = [active, 'work/domains/training/revisions/old.md',
                 'work/domains/training/raw/sample.md', 'work/domains/training/experience/retired.md']
        for p in paths:
            write_text(self.root / p, '# 学员视角检查\n学员标题与表头。\n')
        hits = discover(self.root, '学员视角检查', ['work/domains/training'], excluded_paths=[paths[-1]])
        self.assertEqual([h['path'] for h in hits], [active])

    def test_scope_cannot_escape_or_reference_missing_paths(self):
        for value in ['../', 'absent']:
            with self.assertRaises(ValueError):
                checked_scope(self.root, value)

    def test_pack_hash_and_budget_never_claim_unread_content_is_complete(self):
        write_text(self.root / 'a.md', '# Rule\nA real rule.\n')
        result = {'read': ['a.md', 'missing.md']}
        pack = source_pack(self.root, result)
        self.assertEqual(pack['sources'][0]['sha256'], hashlib.sha256((self.root / 'a.md').read_bytes()).hexdigest())
        self.assertEqual(pack['sources'][1]['status'], 'missing')
        self.assertFalse(pack['allPlannedSourcesIncluded'])
        limited = source_pack(self.root, {'read': ['a.md']}, 1)
        self.assertNotIn('content', limited['sources'][0])
        self.assertFalse(limited['allPlannedSourcesIncluded'])
        full = source_pack(self.root, {'read': ['a.md']})
        self.assertTrue(full['allPlannedSourcesIncluded'])
        self.assertEqual(full['sources'][0]['content'], '# Rule\nA real rule.\n')


if __name__ == '__main__':
    unittest.main()

"""Method discovery and lifecycle checks; these do not grade generated prose."""
import copy
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import ROOT, load_module, write_text

router = load_module('context-route')
navigation = load_module('sync-navigation')
validator = load_module('validate-context')
CATALOG = 'system/repository/navigation/routes.json'
TECHNICAL = 'problem-driven-explanation'
PROMOTION = 'reader-question-promotion'
VIDEO_WORKBENCH = 'interactive-video-production-workbench'
TRAINING_STYLE = 'work/domains/training/experience/jianwei-training-style.md'
BOOK_STYLE = 'work/projects/feishu-efficient-office/writing-style-analysis.md'


def method_ids(result):
    return {method['id'] for method in result['methods']}


class MethodRouting(unittest.TestCase):
    def test_frontend_feedback_routes_for_web_and_miaoda(self):
        for task in ['修改网站移动端UI，导航与分享需要重新排版','秒哒网站改版，修复响应式界面','前端UI设计与手机适配']:
            self.assertIn('frontend-ui-quality', method_ids(router.resolve(task, 'create')))
        self.assertNotIn('frontend-ui-quality', method_ids(router.resolve('网站纯后端数据库迁移', 'create')))

    def test_training_explanation_needs_no_author_name(self):
        result = router.resolve('给企业培训写课件，向小白解释大模型幻觉', 'create')
        self.assertEqual(method_ids(result), {TECHNICAL})
        self.assertIn(TRAINING_STYLE, result['read'])

    def test_self_media_explanation_does_not_inherit_teacher_style(self):
        result = router.resolve('给自媒体写文章，解释API概念', 'create')
        self.assertEqual(method_ids(result), {TECHNICAL})
        self.assertNotIn(TRAINING_STYLE, result['read'])

    def test_book_explanation_keeps_project_editorial_rules(self):
        result = router.resolve('为飞书高效办公书稿解释权限的概念', 'create')
        self.assertEqual(result['selectedCandidate'], 'feishu-book')
        self.assertEqual(method_ids(result), {TECHNICAL})
        self.assertIn(BOOK_STYLE, result['read'])
        self.assertNotIn(TRAINING_STYLE, result['read'])

    def test_promotion_does_not_activate_explanation_just_for_ai(self):
        result = router.resolve('给AI会员社群写对外宣传文档', 'create')
        self.assertEqual(method_ids(result), {PROMOTION})
        self.assertIn('work/projects/paid-community-course/README.md', result['read'])

    def test_commercial_explanation_is_optional(self):
        result = router.resolve('商业计划书中解释服务器的概念', 'create')
        self.assertEqual(method_ids(result), {TECHNICAL})
        self.assertEqual(method_ids(router.resolve('写一份商业计划书', 'create')), set())

    def test_read_and_exact_editing_do_not_restructure_content(self):
        task = '飞书高效办公书稿解释权限概念'
        self.assertFalse(router.resolve(task, 'read')['methods'])
        for guard in ['只接受修订', '逐字保留', '不要改写']:
            with self.subTest(guard=guard):
                result = router.resolve(task + '，' + guard, 'write')
                self.assertFalse(result['methods'])
                self.assertIn(BOOK_STYLE, result['read'])

    def test_pure_teaching_excludes_promotion(self):
        result = router.resolve('给培训学员写纯教学课件，解释API，不涉及招生', 'create')
        self.assertEqual(method_ids(result), {TECHNICAL})

    def test_video_workbench_routes_to_video_method(self):
        result = router.resolve('制作微课时做一个交互式分镜工作台，能逐段试听和复制提示词', 'create')
        self.assertEqual(result['selectedCandidate'], 'microcourse')
        self.assertIn(VIDEO_WORKBENCH, method_ids(result))
        self.assertIn('work/domains/design/video/common/interactive-production-workbench.md', result['read'])
        self.assertNotIn('work/domains/other/skills/jianwei-ai-learning-community-workbench/README.md', result['read'])

    def test_professional_ai_workbench_does_not_activate_video_method(self):
        result = router.resolve('为教师设计一个日常AI工作台', 'create')
        self.assertEqual(result['selectedCandidate'], 'workbench')
        self.assertNotIn(VIDEO_WORKBENCH, method_ids(result))


class MethodRegistry(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.catalog = json.loads((ROOT / CATALOG).read_text(encoding='utf-8-sig'))
        self.method = next(method for method in self.catalog['methodRules'] if method['id'] == TECHNICAL)
        paths = set(self.catalog['readFirst'])
        for route in self.catalog['routes']:
            paths.add(route['entry'])
            paths.update(item['path'] for item in route.get('dependencies', []))
        for overlay in self.catalog.get('overlays', []) + self.catalog.get('genreRules', []):
            paths.update(overlay['paths'])
        for method in self.catalog['methodRules']:
            paths.update([method['path'], method['evidence'], *method['entryPoints']])
        paths.update(['work/projects/README.md', 'work/projects/cases/README.md', 'work/projects/archive/README.md'])
        for path in paths:
            write_text(self.root / path, '# Fixture\n')
        projects = [{'id': path.parent.name, 'name': path.parent.name, 'domain': 'Fixture',
                     'entry': path.relative_to(self.root).as_posix()}
                    for path in (self.root / 'work/projects').glob('*/README.md')
                    if path.parent.name not in {'archive', 'cases'}]
        cases = [{'id': path.stem, 'name': path.stem, 'domain': 'Fixture',
                  'entry': path.relative_to(self.root).as_posix()}
                 for path in (self.root / 'work/projects/cases').glob('*.md')
                 if path.name != 'README.md']
        write_text(self.root / 'system/repository/navigation/projects.json',
                   json.dumps({'schemaVersion': 1, 'projects': projects, 'cases': cases}))
        self.save()

    def save(self):
        write_text(self.root / CATALOG, json.dumps(self.catalog, ensure_ascii=False))

    def test_valid_registry_and_candidate_retirement(self):
        self.assertEqual(validator.check_registries(self.root), [])
        for status in ['candidate', 'retired']:
            self.method['status'] = status
            self.save()
            result = router.resolve('给培训写课件，解释API概念', 'create', repo_root=self.root)
            self.assertNotIn(TECHNICAL, method_ids(result))

    def test_new_method_works_by_registration_without_code_change(self):
        extra = copy.deepcopy(self.method)
        extra.update(id='new-example', label='New example', whenAll=[['对照'], ['选项']],
                     path='work/domains/training/experience/comparison-example.md')
        self.catalog['methodRules'].append(extra)
        write_text(self.root / extra['path'], '# Example body that must not be copied into entries\n')
        self.save()
        result = router.resolve('给培训写对照选项说明', 'create', repo_root=self.root)
        self.assertEqual(method_ids(result), {'new-example'})
        outputs = navigation.outputs(self.root)
        self.assertIn('[New example]', outputs[extra['entryPoints'][0]])
        self.assertNotIn('Example body that must not be copied', outputs[extra['entryPoints'][0]])

    def test_generation_removes_withdrawn_relationships_and_retired_method(self):
        navigation.sync(root=self.root)
        former_entry = self.method['entryPoints'].pop(0)
        self.save()
        navigation.sync(root=self.root)
        self.assertNotIn(self.method['label'], (self.root / former_entry).read_text(encoding='utf-8'))
        remaining_entry = self.method['entryPoints'][0]
        self.method['status'] = 'retired'
        self.save()
        navigation.sync(root=self.root)
        self.assertNotIn(self.method['label'], (self.root / remaining_entry).read_text(encoding='utf-8'))
        self.assertEqual(navigation.sync(check=True, root=self.root), [])

    def test_bad_method_metadata_is_rejected_without_crashing(self):
        cases = [
            ('evidence', None, 'Method needs evidence'),
            ('evidence', '../outside.md', 'outside repository'),
            ('selectedAny', ['nonexistent'], 'unknown route'),
            ('intents', ['read'], 'creative intents'),
            ('whenAll', [], 'trigger conditions'),
            ('entryPoints', ['AGENTS.md'], 'README files'),
            ('confirmedAt', 'not-a-date', 'ISO confirmedAt'),
            ('id', [], 'Duplicate or missing method id'),
        ]
        original = copy.deepcopy(self.method)
        for field, value, message in cases:
            with self.subTest(field=field, value=value):
                self.method.clear()
                self.method.update(copy.deepcopy(original))
                self.method[field] = value
                self.save()
                self.assertTrue(any(message in error for error in validator.check_registries(self.root)))

    def test_malformed_method_collection_has_clear_error(self):
        for value, message in [(None, 'must be a list'), ([None], 'must be an object')]:
            self.catalog['methodRules'] = value
            self.save()
            self.assertTrue(any(message in error for error in validator.check_registries(self.root)))


if __name__ == '__main__':
    unittest.main()

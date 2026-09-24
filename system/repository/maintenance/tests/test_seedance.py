"""Video generation routing, selective reading and evidence-preserving extraction."""
import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import ROOT, load_module, write_text
from context_retrieval import source_pack

router = load_module('context-route')
validator = load_module('validate-context')
BASE = 'work/domains/design/video/common/awesome-seedance'
SKILL = BASE + '/source/agents/skills/seedance-prompt-library/SKILL.md'
spec = importlib.util.spec_from_file_location('seedance_lookup', ROOT / BASE / 'lookup.py')
lookup = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lookup)


class SeedanceRouting(unittest.TestCase):
    def test_implicit_product_prompt_reads_one_specific_template(self):
        result = router.resolve('参考仓库，给产品广告写一段AI视频提示词', 'auto')
        self.assertIn(SKILL, result['read'])
        self.assertIn(BASE + '/source/docs/templates/zh/product-commercial-shotlist.md', result['read'])
        self.assertNotIn(BASE + '/source/docs/templates/zh/horror-suspense.md', result['read'])
        self.assertNotIn(BASE + '/source/data/cases.json', result['read'])
        self.assertNotIn(BASE + '/source/agents/skills/seedance-prompt-library/references/style-library.md', result['read'])
        pack = source_pack(ROOT, result, 60000)
        self.assertTrue(any(s['path'].endswith('/product-commercial-shotlist.md') and s.get('content') for s in pack['sources']))

    def test_microcourse_keeps_primary_identity_and_existing_experience(self):
        result = router.resolve('为教师微课写AI生成镜头提示词，人物参考图要保持角色一致', 'auto')
        self.assertEqual(result['selectedCandidate'], 'microcourse')
        self.assertIn(BASE + '/source/docs/templates/zh/character-reference-lock.md', result['read'])
        self.assertIn('work/domains/design/video/common/tools/seedance/practical-workflow.md', result['read'])
        self.assertNotIn('work/projects/paid-community-course/README.md', result['read'])

    def test_explicit_and_directory_scoped_invocation(self):
        for task, scope in [('调用awesome-seedance', None), ('用Seedance做一段猫咪短片', None),
                            ('给产品广告写视频提示词', 'work/domains/design/video/common')]:
            with self.subTest(task=task):
                self.assertIn(SKILL, router.resolve(task, 'auto', scope=scope)['read'])

    def test_neighboring_tasks_and_preserved_prompts_do_not_activate(self):
        for task in ['用AE制作企业宣传片，只改字幕', '用Remotion做参数化MG动画',
                     '写一篇介绍Seedance的公众号文章', '写一篇介绍AI生成视频的文章',
                     '只写口播文案，谈谈AI视频', '查看awesome-seedance有哪些案例',
                     '用秒哒开发视频上传功能', '修改视频提示词文档，保留原提示词',
                     '为教师微课制作分镜，不用AI生成', '调用awesome-seedance，只查来源']:
            with self.subTest(task=task):
                self.assertNotIn(SKILL, router.resolve(task, 'auto')['read'])

    def test_storyboard_reads_specialist_and_cases_only_when_adopted(self):
        result = router.resolve('给分镜网格转视频写即梦视频提示词', 'auto')
        self.assertIn(BASE + '/source/agents/skills/seedance-storyboard-grid-to-video/SKILL.md', result['read'])
        self.assertIn(BASE + '/source/agents/skills/seedance-storyboard-grid-to-video/references/cases.md', result['read'])
        self.assertNotIn(SKILL, router.resolve('只查分镜网格转视频案例', 'auto')['read'])

    def test_conditional_reference_schema_and_missing_path_are_validated(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            data = json.loads((ROOT / 'system/repository/navigation/routes.json').read_text(encoding='utf-8'))
            method = next(m for m in data['methodRules'] if m['id'] == 'awesome-seedance')
            method['readWhen'] = [{'whenAny': ['广告'], 'paths': ['missing-template.md']}, {'whenAny': [], 'paths': []}, 'bad']
            write_text(root / 'system/repository/navigation/routes.json', json.dumps(data))
            write_text(root / 'system/repository/navigation/projects.json', json.dumps({'schemaVersion': 1, 'projects': []}))
            errors = validator.check_registries(root)
            self.assertTrue(any('missing-template.md' in e for e in errors))
            self.assertTrue(any('readWhen needs nonempty whenAny' in e for e in errors))
            self.assertTrue(any('readWhen entry must be an object' in e for e in errors))


class SeedanceEvidence(unittest.TestCase):
    def test_degraded_case_keeps_original_verdict_and_provenance(self):
        result = lookup.lookup(case='seedance-25-diner-frozen-time-rewind')['case']
        original = next(c for c in lookup.read_json('data/cases.json')['cases'] if c['slug'] == result['slug'])
        self.assertEqual(result, original)
        self.assertEqual(result['retests'][0]['verdict'], 'degraded')
        self.assertTrue(result['sourceUrl'].startswith('https://'))

    def test_untested_case_is_not_upgraded(self):
        case = next(c for c in lookup.read_json('data/cases.json')['cases'] if not c.get('retests'))
        self.assertEqual(lookup.lookup(case=case['slug'])['case'], case)

    def test_selected_templates_include_real_bounded_anchors(self):
        for template in ['product-commercial-shotlist', 'storyboard-grid-to-video']:
            result = lookup.lookup(template=template)
            self.assertEqual(result['template']['id'], template)
            self.assertGreater(len(result['anchorCases']), 0)
            self.assertLessEqual(len(result['anchorCases']), 2)
            self.assertEqual(result['missingAnchorSlugs'], [])
            self.assertTrue(all(c['promptFull'] for c in result['anchorCases']))

    def test_unknown_identifier_fails_instead_of_substituting(self):
        with self.assertRaises(ValueError):
            lookup.lookup(case='not-a-real-case')
        with self.assertRaises(ValueError):
            lookup.lookup(template='../../unrelated')


if __name__ == '__main__':
    unittest.main()

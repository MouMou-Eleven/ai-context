import json
import os
from pathlib import Path
import subprocess
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

MAINTENANCE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(MAINTENANCE))
from context_common import ROOT, clean_git_environment, git, load_module, markdown_targets, write_text

validator = load_module('validate-context')
router = load_module('context-route')
structure = load_module('sync-structure')
hook = load_module('pre-commit')
navigation = load_module('sync-navigation')


class Routes(unittest.TestCase):
    def test_named_tool_cannot_replace_member_course_context(self):
        for tool in ['Remotion动效', '秒哒']:
            result = router.resolve('给会员社群写一节' + tool + '课程', 'create')
            self.assertEqual(result['selectedCandidate'], 'community')
            self.assertIn('work/domains/training/experience/jianwei-training-style.md', result['read'])
            self.assertTrue(any('/development/' in path or 'system/skills/' in path for path in result['read']))

    def test_external_training_keeps_tool_as_dependency(self):
        for tool in ['秒哒', 'Origin科研图']:
            result = router.resolve('给企业培训讲' + tool, 'create')
            self.assertEqual(result['selectedCandidate'], 'external-training')
            self.assertFalse(any('paid-community-course' in path for path in result['read']))
            self.assertTrue(any('/development/' in path or 'system/skills/' in path for path in result['read']))

    def test_remotion_microcourse_retains_design_ownership(self):
        result = router.resolve('给教师用Remotion做MG微课', 'create')
        self.assertEqual(result['selectedCandidate'], 'microcourse')
        self.assertTrue(any('jianwei-ai-community-remotion-video' in path for path in result['read']))
        self.assertFalse(any('/training/' in path for path in result['read']))

    def test_enrollment_poster_reads_project_and_design_without_course_rules(self):
        result = router.resolve('给会员社群做招生海报', 'create')
        self.assertEqual(result['selectedCandidate'], 'poster')
        self.assertIn('work/projects/paid-community-course/README.md', result['read'])
        self.assertFalse(any('/training/experience/' in path for path in result['read']))

    def test_explicit_noncommunity_training_excludes_community(self):
        result = router.resolve('不是会员社群，给企业培训写课程', 'create')
        self.assertFalse(any('paid-community-course' in path for path in result['read']))

    def test_business_analysis_capability_and_image_environment_are_routed(self):
        result = router.resolve('拆解同行并做渠道选择', 'read')
        self.assertEqual(result['selectedCandidate'], 'business-analysis')
        image_result = router.resolve('生成图片做视觉概念', 'create')
        self.assertIn('system/environment/image-generation.md', image_result['read'])

    def test_bug_course_is_external_even_when_old_community_label_is_present(self):
        result = router.resolve('查会员社群里别让 Bug 打败你这课')
        self.assertEqual(result['selectedCandidate'], 'bug-lesson')
        self.assertFalse(any('paid-community-course' in path for path in result['read']))

    def test_course_number_never_establishes_community_identity(self):
        result = router.resolve('第6课是什么课程')
        self.assertNotEqual(result['selectedCandidate'], 'community')
        self.assertFalse(any('paid-community-course' in path for path in result['read']))

    def test_course_number_query_uses_materials_and_marks_series_unresolved(self):
        for task in ['查第6课', '第十二节在哪里', '找第 103 课资料']:
            result = router.resolve(task, 'read')
            self.assertEqual(result['selectedCandidate'], 'course-number')
            self.assertTrue(result['courseSeriesUnresolved'])
            self.assertIn('work/domains/training/materials/README.md', result['read'])
            self.assertIn('work/domains/training/attribution-and-updates.md', result['read'])
            self.assertFalse(any('/training/experience/' in path or 'paid-community-course' in path for path in result['read']))

    def test_status_query_does_not_load_training_writing_rules(self):
        result = router.resolve('会员社群课程进度', 'read')
        self.assertFalse(any('/training/experience/' in path for path in result['read']))

    def test_create_course_loads_training_methods(self):
        result = router.resolve('写企业培训课件', 'create')
        self.assertIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_design_automatically_reads_ai_video_dependency(self):
        result = router.resolve('做MG动画微课，AI生成镜头和视频提示词', 'create')
        self.assertIn('work/domains/design/video/education/README.md', result['read'])
        self.assertIn('work/domains/design/video/README.md', result['read'])

    def test_ai_video_automatically_reads_design_dependency(self):
        result = router.resolve('AI视频素材交给AE后期合成', 'create')
        self.assertIn('work/domains/design/video/README.md', result['read'])
        self.assertIn('work/domains/design/video/common/ae-production.md', result['read'])

    def test_pure_teaching_does_not_activate_sales(self):
        result = router.resolve('培训纯教学案例演示，不涉及招生与销售', 'create')
        self.assertFalse(any('/commercial/' in path or '/self-media/' in path for path in result['read']))

    def test_chinese_output_and_repository_writes_are_independent(self):
        for intent in ['read', 'create', 'write']:
            result = router.resolve('修改并沉淀企业培训课件', intent, produces_chinese=True, writes_repository=True)
            self.assertIn('system/expression/README.md', result['read'])
            self.assertIn('system/repository/ingestion-workflow.md', result['read'])
        result = router.resolve('只移动文件', 'write', produces_chinese=False)
        self.assertNotIn('system/expression/README.md', result['read'])
        self.assertIn('system/repository/ingestion-workflow.md', result['read'])

    def test_simple_chinese_reply_uses_short_card_without_all_genres(self):
        result = router.resolve('查个人简介', 'read')
        self.assertIn('system/expression/README.md', result['read'])
        self.assertNotIn('system/expression/genres.md', result['read'])
        self.assertFalse(any('/oral-expression/' in path or '/written-expression/' in path for path in result['read']))

    def test_mg_is_a_technique_not_automatic_teacher_ownership(self):
        for task, expected in [('做企业MG动画宣传片', 'enterprise-video'), ('做MG动画', 'video')]:
            result = router.resolve(task, 'create')
            self.assertEqual(result['selectedCandidate'], expected)
            self.assertFalse(any('/education/' in path or 'paid-community-course' in path for path in result['read']))

    def test_generic_book_request_does_not_invent_feishu_project(self):
        result = router.resolve('帮我写书稿', 'create')
        self.assertFalse(any('/feishu-efficient-office/' in path for path in result['read']))
        self.assertIn('system/expression/genres.md', result['read'])

    def test_genre_selection_does_not_load_all_modes(self):
        result = router.resolve('写一份自然口播稿', 'create')
        self.assertIn('system/expression/oral-expression/README.md', result['read'])
        self.assertNotIn('system/expression/written-expression/README.md', result['read'])

    def test_member_course_promotion_is_self_media_with_project_facts(self):
        result = router.resolve('给会员课程写朋友圈宣传', 'create')
        self.assertEqual(result['selectedCandidate'], 'self-media')
        self.assertIn('work/projects/paid-community-course/README.md', result['read'])
        self.assertIn('personal/expression-preferences.md', result['read'])
        self.assertFalse(any('/training/experience/' in path for path in result['read']))

    def test_channel_output_and_training_fact_boundaries(self):
        tasks = [
            ('给会员社群做海报', 'create', 'poster', 'work/projects/paid-community-course/README.md'),
            ('为外训写朋友圈宣传', 'create', 'self-media', 'work/projects/external-training/README.md'),
            ('会员社群状态查询', 'read', 'community', 'work/projects/paid-community-course/README.md'),
        ]
        for task, intent, selected, project in tasks:
            result = router.resolve(task, intent)
            self.assertEqual(result['selectedCandidate'], selected)
            self.assertIn(project, result['read'])
            self.assertFalse(any('/training/experience/' in path for path in result['read']))
        result = router.resolve('不属于会员课程，为外训写朋友圈宣传', 'create')
        self.assertNotIn('work/projects/paid-community-course/README.md', result['read'])

    def test_teaching_how_to_make_a_post_still_reads_teaching_methods(self):
        result = router.resolve('给会员课程备课，教会员写朋友圈宣传', 'create')
        self.assertEqual(result['selectedCandidate'], 'community')
        self.assertIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_ae_matches_chinese_boundaries_without_matching_unrelated_words(self):
        result = router.resolve('用AE做企业MG宣传片', 'create')
        self.assertEqual(result['selectedCandidate'], 'enterprise-video')
        self.assertIn('work/domains/design/video/common/ae-production.md', result['read'])
        for task in ['为SAE产品做企业宣传片', '做AEROSPACE企业宣传片', '分析AEs数据']:
            result = router.resolve(task, 'create')
            self.assertNotIn('ae', [item['id'] for item in result['candidates']])

    def test_classroom_material_does_not_force_written_genre(self):
        result = router.resolve('修改并沉淀企业培训课件', 'write')
        self.assertIn('work/domains/training/experience/jianwei-training-style.md', result['read'])
        self.assertIn('system/expression/genres.md', result['read'])
        self.assertNotIn('system/expression/written-expression/README.md', result['read'])
        result = router.resolve('写一份企业培训课件朗读稿', 'create')
        self.assertIn('system/expression/oral-expression/README.md', result['read'])
        self.assertNotIn('system/expression/written-expression/README.md', result['read'])


class ContentValidation(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name).resolve()

    def tearDown(self):
        self.tmp.cleanup()

    def write(self, name, text):
        write_text(self.root / name, text)

    def test_broken_link_is_error_but_fenced_examples_are_not_links(self):
        self.write('README.md', '[missing](missing.md)\n```md\n[example](not-real.md)\n```\n')
        errors = validator.check_links(self.root, ['README.md'])
        self.assertEqual(len(errors), 1)
        self.assertIn('missing.md', errors[0])

    def test_link_with_balanced_parentheses(self):
        self.write('report(v2).md', '# Report\n')
        self.write('README.md', '[report](./report(v2).md)\n')
        self.assertEqual(validator.check_links(self.root, ['README.md']), [])

    def test_link_outside_repo_is_rejected(self):
        self.write('README.md', '[escape](../outside.md)\n')
        self.assertTrue(validator.check_links(self.root, ['README.md']))

    def test_file_requires_nearest_readme_index(self):
        self.write('README.md', '[area](area/README.md)\n')
        self.write('area/README.md', '# Area\n')
        self.write('area/lesson.md', '# Lesson\n')
        names = ['README.md', 'area/README.md', 'area/lesson.md']
        self.assertTrue(any('lesson.md' in item for item in validator.check_indexes(self.root, names)))
        self.write('area/README.md', '[lesson](lesson.md)\n')
        self.assertEqual(validator.check_indexes(self.root, names), [])

    def test_invalid_registry_path_is_rejected(self):
        self.write('system/repository/navigation/routes.json', json.dumps({'schemaVersion': 1, 'routes': [{'id': 'bad', 'entry': 'absent.md', 'matchAny': ['x'], 'priority': 1}]}))
        self.write('system/repository/navigation/projects.json', json.dumps({'schemaVersion': 1, 'projects': []}))
        self.assertTrue(any('absent.md' in item for item in validator.check_registries(self.root)))

    def test_new_case_requires_registration(self):
        self.write('system/repository/navigation/routes.json', json.dumps({'schemaVersion': 1, 'routes': []}))
        self.write('system/repository/navigation/projects.json', json.dumps({'schemaVersion': 1, 'projects': [], 'cases': []}))
        self.write('work/projects/cases/new-case.md', '# New case\n')
        self.assertTrue(any('missing registry entry: work/projects/cases/new-case.md' in item for item in validator.check_registries(self.root)))

    def test_skill_requires_capability_and_authorship_metadata(self):
        base = 'system/skills/sample/'
        self.write(base + 'README.md', '# Skill\n')
        self.write(base + 'skill/SKILL.md', '# Skill source\n')
        self.write(base + 'upstream.json', json.dumps({'schemaVersion': 1, 'id': 'sample', 'origin': 'internal', 'sourcePath': 'skill', 'storageMode': 'skill-snapshot', 'documentationReviewedAt': '2026-09-12'}))
        errors = validator.check_skills(self.root)
        self.assertTrue(any('capabilities' in item for item in errors))
        self.assertTrue(any('authorship' in item for item in errors))
        self.assertTrue(any('syncedAt' in item for item in errors))
        self.assertTrue(any('workflowRevision' in item for item in errors))

    def test_git_helper_does_not_reuse_another_repository_environment(self):
        original = self.root / 'original'
        fixture = self.root / 'fixture'
        original.mkdir()
        fixture.mkdir()
        git(original, 'init', '-q')
        write_text(original / 'original.txt', 'original')
        git(original, 'add', '.')
        original_tree = git(original, 'write-tree')
        with patch.dict(os.environ, {'GIT_DIR': str(original / '.git'), 'GIT_WORK_TREE': str(original), 'GIT_INDEX_FILE': str(original / '.git/index')}):
            git(fixture, 'init', '-q')
            self.assertTrue((fixture / '.git').is_dir())
            write_text(fixture / 'fixture.txt', 'fixture')
            git(fixture, 'add', '.')
            self.assertEqual(git(original, 'write-tree'), original_tree)
            self.assertNotIn('GIT_DIR', clean_git_environment())

    def test_hook_runtime_probe_selects_a_working_interpreter(self):
        shell = shutil.which('sh')
        if shell is None and shutil.which('git'):
            guess = Path(shutil.which('git')).resolve().parents[1] / 'bin/sh.exe'
            if guess.is_file():
                shell = str(guess)
        if shell is None:
            self.skipTest('Git POSIX shell is not available')
        result = subprocess.run([shell, str(MAINTENANCE / 'git-hooks/run-python'), '-c', 'import sys; print(sys.version_info >= (3, 10))'], capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.strip(), 'True')

    def test_tree_and_html_drift_are_both_detected(self):
        self.write('system/repository/navigation/STRUCTURE.md', '# Structure\n```text\nai-context/\n```\n*确认：2026-09-12*\n')
        self.write('system/repository/navigation/STRUCTURE.html', 'old')
        self.write('system/repository/maintenance/structure-descriptions.json', json.dumps({'schemaVersion': 1, 'confirmedDate': '2026-09-12', 'descriptions': {}}))
        self.write('system/repository/maintenance/structure-viewer.template.html', '__STRUCTURE_DATA_BASE64__ __KNOWLEDGE_DATA_BASE64__ __SOURCE_SHA256__ __CONFIRMED_DATE__')
        structure.sync(root=self.root)
        self.assertEqual(structure.sync(check=True, root=self.root), [])
        self.write('new.md', '# New material\n')
        self.assertEqual(set(structure.sync(check=True, root=self.root)), {'system/repository/navigation/STRUCTURE.md', 'system/repository/navigation/STRUCTURE.html'})
        structure.sync(root=self.root)
        self.write('system/repository/navigation/STRUCTURE.html', 'tampered')
        self.assertEqual(structure.sync(check=True, root=self.root), ['system/repository/navigation/STRUCTURE.html'])

    def test_knowledge_view_has_four_roots_without_readme_or_skill_sources(self):
        files = ['personal/README.md', 'brain/README.md', 'work/README.md', 'system/README.md',
                 'work/projects/cases/README.md', 'work/projects/cases/demo.md', 'system/skills/demo/README.md',
                 'system/skills/demo/upstream.json', 'system/skills/demo/skill/SKILL.md', 'system/repository/maintenance/check.py']
        for name in files:
            self.write(name, '# Test\n')
        self.write('system/skills/demo/upstream.json', json.dumps({'sourcePath': 'skill'}))
        tree = structure.build_knowledge(self.root, files, {})
        self.assertEqual([node['path'] for node in tree['children']], ['personal', 'brain', 'work', 'system'])
        paths = []
        def collect(node):
            paths.append(node['path'])
            for child in node['children']:
                collect(child)
        collect(tree)
        self.assertIn('work/projects/cases/demo.md', paths)
        self.assertIn('system/skills/demo', paths)
        self.assertFalse(any(path.endswith('README.md') or '/skill/' in path or path.endswith('.py') for path in paths))

    def test_related_asset_generation_uses_registry_and_removes_old_rows(self):
        self.write('system/repository/navigation/routes.json', json.dumps({'routes': []}))
        registry = {'projects': [], 'cases': [{'id': 'demo', 'name': 'Demo', 'domain': 'Design', 'entry': 'work/projects/cases/demo.md', 'domainEntries': ['work/domains/design/README.md']}]}
        self.write('system/repository/navigation/projects.json', json.dumps(registry))
        for name in ['personal/business-overview.md', 'work/projects/README.md', 'work/projects/cases/README.md', 'work/projects/archive/README.md', 'work/domains/design/README.md']:
            self.write(name, '# Entry\n')
        navigation.sync(root=self.root)
        path = self.root / 'work/domains/design/README.md'
        self.assertIn('[Demo](../../projects/cases/demo.md)', path.read_text(encoding='utf-8'))
        registry['cases'][0]['domainEntries'] = []
        self.write('system/repository/navigation/projects.json', json.dumps(registry))
        navigation.sync(root=self.root)
        self.assertNotIn('[Demo]', path.read_text(encoding='utf-8'))

    def test_staged_snapshot_ignores_unstaged_repairs_and_does_not_stage(self):
        git(self.root, 'init', '-q')
        git(self.root, 'config', 'core.autocrlf', 'false')
        self.write('value.txt', 'bad')
        self.write('system/repository/maintenance/validate-context.py', "from pathlib import Path\nraise SystemExit(0 if Path('value.txt').read_text() == 'good' else 1)\n")
        self.write('system/repository/maintenance/tests/test_empty.py', 'import unittest\n')
        git(self.root, 'add', '.')
        index_before = git(self.root, 'write-tree')
        self.write('value.txt', 'good')
        self.write('system/repository/maintenance/validate-context.py', 'raise SystemExit(0)\n')
        self.assertNotEqual(hook.check_staged(self.root), 0)
        self.assertEqual(git(self.root, 'write-tree'), index_before)
        self.assertEqual((self.root / 'value.txt').read_text(), 'good')


if __name__ == '__main__':
    unittest.main()

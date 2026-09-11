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


class Routes(unittest.TestCase):
    def test_named_tool_cannot_replace_member_course_context(self):
        for tool in ['Remotion动效', '秒哒']:
            result = router.resolve('给会员社群写一节' + tool + '课程', 'create')
            self.assertEqual(result['selectedCandidate'], 'community')
            self.assertIn('work/ai/training/experience/jianwei-training-style.md', result['read'])
            self.assertTrue(any('/programming/' in path for path in result['read']))

    def test_external_training_keeps_tool_as_dependency(self):
        for tool in ['秒哒', 'Origin科研图']:
            result = router.resolve('给企业培训讲' + tool, 'create')
            self.assertEqual(result['selectedCandidate'], 'external-training')
            self.assertFalse(any('paid-community-course' in path for path in result['read']))
            self.assertTrue(any('/programming/' in path for path in result['read']))

    def test_remotion_microcourse_retains_design_ownership(self):
        result = router.resolve('给教师用Remotion做MG微课', 'create')
        self.assertEqual(result['selectedCandidate'], 'microcourse')
        self.assertTrue(any('jianwei-ai-community-remotion-video' in path for path in result['read']))
        self.assertFalse(any('/training/' in path for path in result['read']))

    def test_enrollment_poster_reads_project_and_design_without_course_rules(self):
        result = router.resolve('给会员社群做招生海报', 'create')
        self.assertEqual(result['selectedCandidate'], 'poster')
        self.assertIn('work/ai/training/projects/paid-community-course/README.md', result['read'])
        self.assertFalse(any('/training/experience/' in path for path in result['read']))

    def test_explicit_noncommunity_training_excludes_community(self):
        result = router.resolve('不是会员社群，给企业培训写课程', 'create')
        self.assertFalse(any('paid-community-course' in path for path in result['read']))

    def test_business_analysis_capability_and_image_environment_are_routed(self):
        result = router.resolve('拆解同行并做渠道选择', 'read')
        self.assertEqual(result['selectedCandidate'], 'business-analysis')
        image_result = router.resolve('生成图片做视觉概念', 'create')
        self.assertIn('repository/environment/image-generation.md', image_result['read'])

    def test_bug_course_is_external_even_when_old_community_label_is_present(self):
        result = router.resolve('查会员社群里别让 Bug 打败你这课')
        self.assertEqual(result['selectedCandidate'], 'bug-lesson')
        self.assertFalse(any('paid-community-course' in path for path in result['read']))

    def test_course_number_never_establishes_community_identity(self):
        result = router.resolve('第6课是什么课程')
        self.assertNotEqual(result['selectedCandidate'], 'community')
        self.assertFalse(any('paid-community-course' in path for path in result['read']))

    def test_status_query_does_not_load_training_writing_rules(self):
        result = router.resolve('会员社群课程进度', 'read')
        self.assertFalse(any('/training/experience/' in path for path in result['read']))

    def test_create_course_loads_training_methods(self):
        result = router.resolve('写企业培训课件', 'create')
        self.assertIn('work/ai/training/experience/jianwei-training-style.md', result['read'])

    def test_design_automatically_reads_ai_video_dependency(self):
        result = router.resolve('做MG动画微课，AI生成镜头和视频提示词', 'create')
        self.assertIn('work/design/microcourse-mg-animation/README.md', result['read'])
        self.assertIn('work/ai/video/README.md', result['read'])

    def test_ai_video_automatically_reads_design_dependency(self):
        result = router.resolve('AI视频素材交给AE后期合成', 'create')
        self.assertIn('work/ai/video/README.md', result['read'])
        self.assertIn('work/design/ae-promo-video/README.md', result['read'])

    def test_pure_teaching_does_not_activate_sales(self):
        result = router.resolve('培训纯教学案例演示，不涉及招生与销售', 'create')
        self.assertFalse(any('/commercial/' in path or '/self-media/' in path for path in result['read']))


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
        self.write('repository/navigation/routes.json', json.dumps({'schemaVersion': 1, 'routes': [{'id': 'bad', 'entry': 'absent.md', 'matchAny': ['x'], 'priority': 1}]}))
        self.write('repository/navigation/projects.json', json.dumps({'schemaVersion': 1, 'projects': []}))
        self.assertTrue(any('absent.md' in item for item in validator.check_registries(self.root)))

    def test_skill_requires_capability_and_authorship_metadata(self):
        base = 'work/ai/programming/experience/skill-repository/sample/'
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
        self.write('STRUCTURE.md', '# Structure\n```text\nai-context/\n```\n*确认：2026-09-12*\n')
        self.write('STRUCTURE.html', 'old')
        self.write('repository/maintenance/structure-descriptions.json', json.dumps({'schemaVersion': 1, 'confirmedDate': '2026-09-12', 'descriptions': {}}))
        self.write('repository/maintenance/structure-viewer.template.html', '__STRUCTURE_DATA_BASE64__ __SOURCE_SHA256__ __CONFIRMED_DATE__')
        structure.sync(root=self.root)
        self.assertEqual(structure.sync(check=True, root=self.root), [])
        self.write('new.md', '# New material\n')
        self.assertEqual(set(structure.sync(check=True, root=self.root)), {'STRUCTURE.md', 'STRUCTURE.html'})
        structure.sync(root=self.root)
        self.write('STRUCTURE.html', 'tampered')
        self.assertEqual(structure.sync(check=True, root=self.root), ['STRUCTURE.html'])

    def test_staged_snapshot_ignores_unstaged_repairs_and_does_not_stage(self):
        git(self.root, 'init', '-q')
        git(self.root, 'config', 'core.autocrlf', 'false')
        self.write('value.txt', 'bad')
        self.write('repository/maintenance/validate-context.py', "from pathlib import Path\nraise SystemExit(0 if Path('value.txt').read_text() == 'good' else 1)\n")
        self.write('repository/maintenance/tests/test_empty.py', 'import unittest\n')
        git(self.root, 'add', '.')
        index_before = git(self.root, 'write-tree')
        self.write('value.txt', 'good')
        self.write('repository/maintenance/validate-context.py', 'raise SystemExit(0)\n')
        self.assertNotEqual(hook.check_staged(self.root), 0)
        self.assertEqual(git(self.root, 'write-tree'), index_before)
        self.assertEqual((self.root / 'value.txt').read_text(), 'good')


if __name__ == '__main__':
    unittest.main()

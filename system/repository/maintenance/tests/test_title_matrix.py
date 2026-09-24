"""Title capability activation, boundary isolation and domain-owned snapshots."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import ROOT, load_module, repo_files, skill_metadata_paths, snapshot_roots, write_text
from context_retrieval import discover, source_pack

router = load_module('context-route')
validator = load_module('validate-context')
structure = load_module('sync-structure')
BASE = 'work/domains/self-media/titles/title-matrix'
SKILL = BASE + '/source/skills/title-matrix/SKILL.md'


class TitleRouting(unittest.TestCase):
    def test_implicit_article_reads_skill_without_user_naming_it(self):
        for task in ['参考仓库写一篇公众号文章，介绍我整理素材的方法',
                     '写一篇自媒体文章解释API概念', '写小红书图文笔记']:
            with self.subTest(task=task):
                result = router.resolve(task, 'auto')
                self.assertIn(SKILL, result['read'])
                self.assertIn(BASE + '/README.md', result['read'])
                self.assertIn(BASE + '/upstream.json', result['read'])
                self.assertIn(BASE + '/source/skills/title-matrix/references/platforms.md', result['read'])
                self.assertNotIn('work/projects/paid-community-course/README.md', result['read'])

    def test_explicit_generation_diagnosis_and_review(self):
        for task in ['使用title-matrix生成六个标题', '帮我起标题', '帮我诊断这个标题',
                     '这几个自媒体标题选哪个', '用标题矩阵写视频号发布标题',
                     '使用title-matrix，评审这三个候选']:
            with self.subTest(task=task):
                self.assertIn(SKILL, router.resolve(task, 'auto')['read'])

    def test_protected_edits_and_nonmedia_titles_do_not_load_skill(self):
        for task in ['写公众号文章，保留原标题', '公众号只改正文', '公众号文章只改错字',
                     '查title-matrix的来源', '给合同起标题', '给学员课件拟标题',
                     '给飞书高效办公书稿修改章节标题', '给项目方案起标题',
                     '帮我备课，教会员写公众号标题', '写公众号文章，不需要标题']:
            with self.subTest(task=task):
                self.assertNotIn(SKILL, router.resolve(task, 'auto')['read'])

    def test_title_does_not_replace_promotion_structure_or_project_facts(self):
        result = router.resolve('给会员社群写公众号宣传文章并起标题', 'auto')
        self.assertEqual(result['selectedCandidate'], 'self-media')
        self.assertIn(SKILL, result['read'])
        self.assertIn('work/projects/paid-community-course/README.md', result['read'])
        self.assertIn('work/domains/self-media/marketing-copy/reader-question-led-promotion.md', result['read'])
        self.assertNotIn('work/domains/training/experience/jianwei-training-style.md', result['read'])

    def test_scope_only_article_still_discovers_and_reads_title_skill(self):
        result = router.resolve('帮我写这篇文章', 'auto', scope='work/domains/self-media/articles')
        self.assertIn(SKILL, result['read'])
        pack = source_pack(ROOT, result, 150000)
        self.assertTrue(any(e['path'] == SKILL and e.get('content', '').startswith('---') for e in pack['sources']))


class DomainSkillSnapshot(unittest.TestCase):
    def test_domain_wrapper_is_validated_and_source_not_in_default_discovery(self):
        self.assertIn(ROOT / BASE / 'upstream.json', skill_metadata_paths(ROOT))
        self.assertIn(BASE + '/source', snapshot_roots(ROOT))
        self.assertEqual(validator.check_skills(ROOT), [])
        hits = discover(ROOT, '公众号标题矩阵', ['work/domains/self-media'], limit=50)
        self.assertTrue(any(h['path'] == BASE + '/README.md' for h in hits))
        self.assertFalse(any('/title-matrix/source/' in h['path'] for h in hits))

    def test_daily_navigation_keeps_domain_entry_and_hides_vendor_internals(self):
        files = repo_files(ROOT)
        tree = structure.build_knowledge(ROOT, files, {})
        def flatten(node):
            return [node['path']] + [path for child in node['children'] for path in flatten(child)]
        paths = flatten(tree)
        self.assertIn(BASE, paths)
        self.assertFalse(any(path.startswith(BASE + '/source') for path in paths))

    def test_missing_domain_runtime_reference_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            metadata = json.loads((ROOT / BASE / 'upstream.json').read_text(encoding='utf-8'))
            write_text(root / BASE / 'upstream.json', json.dumps(metadata))
            write_text(root / BASE / 'README.md', '# Title capability\n')
            write_text(root / SKILL, '# Skill\n')
            errors = validator.check_skills(root)
            self.assertTrue(any('references/platforms.md' in e for e in errors))

    def test_invalid_method_companion_path_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp).resolve()
            data = json.loads((ROOT / 'system/repository/navigation/routes.json').read_text(encoding='utf-8'))
            method = next(m for m in data['methodRules'] if m['id'] == 'title-matrix')
            method['readWith'] = ['absent-title-reference.md']
            write_text(root / 'system/repository/navigation/routes.json', json.dumps(data))
            write_text(root / 'system/repository/navigation/projects.json', json.dumps({'schemaVersion': 1, 'projects': []}))
            self.assertTrue(any('absent-title-reference.md' in e for e in validator.check_registries(root)))


if __name__ == '__main__':
    unittest.main()

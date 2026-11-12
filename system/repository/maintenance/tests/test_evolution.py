"""The evolution loop (system/repository/evolution.md) must fire on content, not dates,
and new red lines must not slip in without Jianwei."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from context_common import MAINTENANCE, ROOT, load_module, repo_files

evolution = load_module('evolution-status')
guards = load_module('content-guards')

LOG_HEAD = '''# 仓库使用日志

<!-- last-upgrade: 2026-11-13 -->

## 历次升级

| 日期 | 做了什么 |
|---|---|
| 2026-11-13 | 第八轮整改 |

## 日志

| 日期 | 任务 | 读了 | 结果 | 失败类型 | 涉及规则 | 说明 |
|---|---|---|---|---|---|---|
| 2026-11-13 | 升级当天 | AGENTS | 待反馈 | 待反馈 | — | 不计入 |
'''
OBS_HEAD = '''# 观察记录

## 观察

| 日期 | 项目 | 类别 | 好/不好 | 建委原话 | 对应成品 | 改了什么、改后建委怎么说 | 状态 |
|---|---|---|---|---|---|---|---|
'''
RULE = '[同一画面一份素材只出现一次](../../work/domains/design/video/promo/competition/ae-template-layout.md)'


def row(date, kind='无', rule='—'):
    return f'| {date} | 某单 | ae-template-layout | 返工 1 轮 | {kind} | {rule} | 原话 |\n'


def obs(date, project, category, state='待定'):
    return f'| {date} | {project} | {category} | 不好 | 原话 | 成品 v1 | 改法 | {state} |\n'


class Evolution(unittest.TestCase):
    def status(self, log_rows='', obs_rows=''):
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'system/repository'
            base.mkdir(parents=True)
            (base / 'usage-log.md').write_text(LOG_HEAD + log_rows, encoding='utf-8')
            (base / 'observations.md').write_text(OBS_HEAD + obs_rows, encoding='utf-8')
            return evolution.status(tmp)

    def test_quiet_after_upgrade(self):
        result = self.status(row('2026-11-14'), obs('2026-11-14', '甲项目', '画面饱满'))
        self.assertFalse(result['due'])
        self.assertEqual(result['entriesSinceUpgrade'], 1)

    def test_rows_on_or_before_last_upgrade_do_not_count(self):
        result = self.status(''.join(row('2026-11-12', 'B', RULE) for _ in range(3)))
        self.assertFalse(result['due'])
        self.assertEqual(result['entriesSinceUpgrade'], 0)

    def test_twenty_entries_trigger_routine_review(self):
        result = self.status(''.join(row(f'2026-12-{d:02d}') for d in range(1, 21)))
        self.assertTrue(result['due'])
        self.assertIn('20 条使用日志', result['reasons'][0])

    def test_same_rule_broken_twice_after_reading(self):
        result = self.status(row('2026-11-20', 'B', RULE) + row('2026-11-25', 'B、C', RULE))
        self.assertTrue(result['due'])
        self.assertTrue(any('ae-template-layout.md' in r and 'B 类' in r for r in result['reasons']))

    def test_one_b_is_not_enough(self):
        self.assertFalse(self.status(row('2026-11-20', 'B', RULE))['due'])

    def test_two_missed_reads(self):
        result = self.status(row('2026-11-20', 'A') + row('2026-11-21', 'A'))
        self.assertTrue(any('A 类' in r for r in result['reasons']))

    def test_same_category_in_two_projects(self):
        result = self.status(obs_rows=obs('2026-11-14', '甲项目', '画面饱满') + obs('2026-11-20', '乙项目', '画面饱满'))
        self.assertTrue(result['due'])
        self.assertIn('画面饱满', result['reasons'][0])

    def test_same_project_twice_or_handled_rows_do_not_promote(self):
        same = obs('2026-11-14', '甲项目', '节奏') + obs('2026-11-15', '甲项目', '节奏')
        handled = obs('2026-11-14', '甲项目', '配色') + obs('2026-11-20', '乙项目', '配色', '已晋升 → 链接')
        self.assertFalse(self.status(obs_rows=same + handled)['due'])

    def test_hook_is_silent_when_not_due_and_valid_json_when_due(self):
        script = ROOT / MAINTENANCE / 'evolution-status.py'
        with tempfile.TemporaryDirectory() as tmp:
            base = Path(tmp) / 'system/repository'
            base.mkdir(parents=True)
            (base / 'usage-log.md').write_text(LOG_HEAD, encoding='utf-8')
            (base / 'observations.md').write_text(OBS_HEAD, encoding='utf-8')
            quiet = subprocess.run([sys.executable, '-B', str(script), '--hook', '--root', tmp],
                                   capture_output=True, text=True, encoding='utf-8')
            self.assertEqual((quiet.returncode, quiet.stdout), (0, ''))
            (base / 'usage-log.md').write_text(LOG_HEAD + row('2026-11-20', 'A') + row('2026-11-21', 'A'), encoding='utf-8')
            due = subprocess.run([sys.executable, '-B', str(script), '--hook', '--root', tmp],
                                 capture_output=True, text=True, encoding='utf-8')
            payload = json.loads(due.stdout)
            self.assertEqual(payload['hookSpecificOutput']['hookEventName'], 'SessionStart')
            self.assertIn('仓库该升级了', payload['hookSpecificOutput']['additionalContext'])

    def test_real_log_and_observations_parse(self):
        result = evolution.status(ROOT)
        self.assertRegex(result['lastUpgrade'], r'^\d{4}-\d{2}-\d{2}$')
        self.assertNotEqual(result['lastUpgrade'], '0000-00-00')

    def test_agents_links_the_loop(self):
        agents = (ROOT / 'AGENTS.md').read_text(encoding='utf-8')
        for target in ('system/repository/evolution.md', 'system/repository/usage-log.md',
                       'system/repository/observations.md', 'evolution-status.py'):
            self.assertIn(target, agents)


class RedlineBudget(unittest.TestCase):
    def test_marks_are_counted(self):
        self.assertEqual(guards.redline_marks('## 一、先确认平台（红线）\n\n- **红线**：不编造。'), 2)
        self.assertEqual(guards.redline_marks('## 一、先确认平台（默认）\n\n```text\n红线：提示词里的\n```'), 0)

    def test_new_red_line_is_blocked(self):
        files = repo_files(ROOT)
        self.assertEqual([e for e in guards.check(ROOT, files) if '红线标记' in e], [])
        blocked = guards.check(ROOT, files, redline_budget=guards.REDLINE_BUDGET - 1)
        self.assertTrue(any('红线标记' in e and '建委' in e for e in blocked))


if __name__ == '__main__':
    unittest.main()

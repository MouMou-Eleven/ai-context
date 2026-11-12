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
        self.assertEqual(result['entriesSinceUpgrade'], 2)

    def test_unhandled_rows_from_before_the_upgrade_still_count(self):
        result = self.status(row('2026-11-01', 'B', RULE) + row('2026-11-20', 'B', RULE))
        self.assertTrue(any('B 类' in r for r in result['reasons']))
        self.assertEqual(result['entriesSinceUpgrade'], 2)  # 2026-11-20 and the upgrade-day row

    def test_routine_review_counts_only_since_the_upgrade(self):
        old = ''.join(row(f'2026-10-{d:02d}') for d in range(1, 21))
        self.assertFalse(self.status(old)['due'])

    def test_failure_type_letters_must_stand_alone(self):
        result = self.status(row('2026-11-20', 'N/A') + row('2026-11-21', 'NA'))
        self.assertFalse(result['due'])

    def test_same_link_twice_in_one_row_counts_once(self):
        self.assertFalse(self.status(row('2026-11-20', 'B', RULE + '、' + RULE))['due'])

    def test_malformed_dates_are_reported(self):
        result = self.status(row('2026-11-3', 'A') + row('2026-11-04', 'A'))
        self.assertFalse(result['due'])
        self.assertTrue(result['warnings'])

    def test_twenty_entries_trigger_routine_review(self):
        self.assertFalse(self.status(''.join(row(f'2026-12-{d:02d}') for d in range(1, 19)))['due'])
        result = self.status(''.join(row(f'2026-12-{d:02d}') for d in range(1, 20)))  # + upgrade-day row = 20
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
        self.assertGreater(result['entries'], 0, '使用日志的“## 日志”表没解析出行，标题或表格格式可能改坏了')
        self.assertEqual(result['warnings'], [])
        observed = evolution.table_rows((ROOT / evolution.OBSERVATIONS).read_text(encoding='utf-8'), '观察')
        self.assertTrue(observed and all(len(cells) == 8 for cells in observed), '观察表没解析出 8 列的行')

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
        budget = guards.redline_budget()
        self.assertEqual([e for e in guards.check(ROOT, files) if '红线标记' in e], [])
        self.assertEqual(guards.redline_counts(ROOT, files), budget, '红线减少后请同步调低 redlineBudget')
        name = 'AGENTS.md'
        moved = dict(budget, **{name: budget[name] - 1})
        blocked = guards.check(ROOT, files, budget=moved)
        self.assertTrue(any('红线标记' in e and name in e and '建委' in e for e in blocked))

    def test_red_lines_in_projects_and_cases_are_counted(self):
        self.assertTrue(guards.redline_scope('work/projects/README.md'))
        self.assertTrue(guards.redline_scope('work/domains/design/case-a.md'))
        self.assertFalse(guards.redline_scope('system/repository/revisions/2026-11-13-x.md'))


if __name__ == '__main__':
    unittest.main()

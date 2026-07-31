# 2026-08-01 Codex 项目信任配置修复

> 设备：台式电脑1
> 项目：`C:\Users\Administrator\Documents\Codex\2026-07-13\new-chat`
> 触发提示：Codex 配置页要求把当前目录添加为 trusted project，否则不加载项目级 config、hooks 和 exec policies。

## 一、根因

活动 `%USERPROFILE%/.codex/config.toml` 中缺少当前项目的 `[projects.'...']` 信任段。历史配置备份中存在其他项目的同类 `trust_level = "trusted"` 条目，说明字段受当前 Codex 版本支持；本次不是网络故障，也不是插件包丢失。

本机另有 `%USERPROFILE%/.codex/plugin-persistence-guard.ps1` 每 3 秒维护插件和 marketplace 注册，但原脚本没有维护项目信任段。外部供应商/配置同步重写 `config.toml` 后，项目信任项可能再次消失，从而造成同一提示反复出现。

## 二、本次修复

1. 备份活动 `config.toml` 和插件持久化守护脚本，备份仅保存在本机，不进入 GitHub。
2. 在活动配置中加入：

```toml
[projects.'c:\users\administrator\documents\codex\2026-07-13\new-chat']
trust_level = "trusted"
```

3. 将同一项目段加入 `plugin-persistence-guard.ps1` 的必要配置块，避免后续配置同步再次删除。
4. 仅重启插件持久化守护进程以加载新规则；没有重启 Codex、CC Switch 或 Clash。

## 三、验证

- `codex doctor` 报告 `config.toml parse ok`，识别当前 cwd 为 `new-chat`，活动 provider 本地端点可达。
- 跨过多个 3 秒守护循环后，项目段和 `trust_level = "trusted"` 仍存在。
- `codex plugin list` 识别 Browser、Chrome、Computer Use、Visualize、GitHub、Build Web Apps、Product Design，以及 Documents、PDF、Spreadsheets、Presentations 等插件为 `installed, enabled`。
- 插件 marketplace 快照和 `.codex-plugin` 文件存在；因此截图中的插件加载问题与项目未信任有关，不是插件安装文件丢失。
- Codex、CC Switch、Clash 进程均保持响应。

## 四、后续口径

1. 再出现同一提示时，先检查活动 `config.toml` 是否仍有当前项目段，再检查守护脚本和守护进程；不要先重装所有插件。
2. 项目信任只应添加明确由建委维护的目录，不要把下载目录或未知仓库批量设为 trusted。
3. 当前已打开的 Codex 配置页可能保留旧提示；新任务或下次正常打开项目时应读取新配置。活动任务期间不要为了刷新提示强制重启 Codex。
4. `codex doctor` 还报告少量历史 rollout/状态数据库索引不一致；它与本次信任提示无直接关系，不应在没有备份和单独授权时删除历史会话数据。

本修订不包含 API Key、Token、Cookie、完整认证配置或局域网信息。

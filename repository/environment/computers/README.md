# 电脑环境档案

> 本目录按设备保存建委的电脑环境、长期故障记录和已验证处理边界。处理电脑、网络、VPN、Codex 或本地工具问题时，必须先确认设备并读取对应入口，不能只凭当前对话或通用经验操作。

## 设备索引

| 设备名称 | 状态 | 最近核验 | 首读入口 |
|---|---|---|---|
| 台式电脑1 | 在用 | 2026-07-23 | [`desktop-1/README.md`](./desktop-1/README.md) |

## AI 使用规则

1. 先确认当前操作的是哪台电脑；没有确认时不要套用其他设备的端口、路径或修复方案。
2. 先读设备 README 的“当前有效状态”和“操作禁区”，再按需读取专题文件。
3. 正在执行 Codex 任务时，先做只读诊断。不要直接重启 Codex、CC Switch、Clash、切换节点或重载配置。
4. 修改前备份，修改后验证实际运行态；不能只看配置文件就断言已经生效。
5. 仓库只记录排障所需信息，不保存 API Key、Token、Cookie、局域网地址、网关、MAC 地址或机器真实主机名。
6. 新增设备时使用新的独立目录和 README，不得混写到“台式电脑1”。

## 文件索引

- [`desktop-1/README.md`](./desktop-1/README.md)：台式电脑1当前入口、配置摘要和操作边界。
- [`desktop-1/network-and-codex.md`](./desktop-1/network-and-codex.md)：网络、Clash、CC Switch、Codex 上下文与插件排障细节。
- [`desktop-1/history.md`](./desktop-1/history.md)：台式电脑1已清洗的关键修复与变化摘要。
- [`windows-junction-migration.md`](./windows-junction-migration.md)：本机 AppData Junction 迁移、安全清理和卸载边界。

*文件最后整理：2026-07-23；设备事实最后核验：2026-07-23*

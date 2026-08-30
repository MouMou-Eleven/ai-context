# 台式电脑1

> 当前设备名称：**台式电脑1**。这是本机电脑问题的首读入口。网络、VPN、Codex、CC Switch、Codex++、插件和 Windows 环境相关任务都应先读本文件。

## 当前有效状态

| 项目 | 已核验状态 |
|---|---|
| 操作系统 | Windows 11 Pro，x64，build 26200 |
| 处理器 | Intel Core i5-12600KF |
| 内存 | 约 32 GB |
| 主网络 | 有线网卡；局域网地址不入库 |
| Codex CLI | 0.142.5 |
| Codex 桌面应用 | 26.715.9757.0 x64 |
| CC Switch | 3.18.0 |
| Clash for Windows | 0.20.16.3-ikuuu，规则模式 |
| Codex++ | 1.2.41；供应商自动切换当前关闭 |
| 磁盘状态 | C、D、E、F 均为 NTFS，2026-08-30 核验为 Healthy；C 盘清理后可用约 54.99 GiB |
| Codex 会话存储 | `sessions` 与 `archived_sessions` 当前仍在 C 盘普通目录；已部署并验证 SYSTEM 开机迁移任务，等待下一次重新启动正式迁移到 F 盘 |

截至 2026-07-23，本机 Codex 活动请求链路为：

```text
Codex -> CC Switch 本地端口 127.0.0.1:15721 -> 当前外部供应商
                  |
                  +-> 外部 HTTPS 按 Clash 规则决定代理路径
```

本地 `127.0.0.1` 已绕过系统代理，Codex 到 CC Switch 的本地通信不经过 Clash。WinHTTP 为直连；Windows 用户代理由 Clash 使用 `127.0.0.1:7890`。

## 2026-07-23 已修复

- 找到 Codex 频繁压缩的直接原因：自定义插件持久化脚本每 3 秒强制写入 `model_context_window = 128000` 和 `model_auto_compact_token_limit = 64000`。
- 已从 `%USERPROFILE%/.codex/plugin-persistence-guard.ps1` 删除这两个强制项，并重启该脚本自身；没有重启 Codex、CC Switch 或 Clash。
- 连续跨过多个脚本循环后，活动 `config.toml` 未再出现 `64K/128K` 数值，现由 Codex 模型目录决定上下文与自动压缩阈值。
- 火绒阻止的是 Codex 重写“启动”目录中的插件守护 VBS，不是项目文件写入。现有 VBS 和守护进程仍可工作，不需要关闭火绒。
- 当前已安装并由守护脚本维护的插件共 8 个：Browser、Chrome、Computer Use、Visualize、GitHub、Build Web Apps、Creative Production、Product Design。

详见 [`network-and-codex.md`](./network-and-codex.md)。

## 操作禁区

1. Codex 正在执行任务时，不要重启 Codex、CC Switch、Clash，不要切换节点或重载 Clash 配置。
2. 不要再次向插件持久化脚本加入 `model_context_window` 或 `model_auto_compact_token_limit`。
3. 不要同时开启 Codex++ 的供应商自动切换与 CC Switch 的供应商管理，避免多个工具争抢 `config.toml` 和 `auth.json`。
4. 不要因火绒拦截一条启动项写入就关闭整体防护；先核对被拦截的具体目标。
5. 修改 Clash 后必须同时检查“持久配置文件”和“当前内核运行规则”；文件存在不代表运行内核已加载。
6. 不要把供应商密钥、Token、Cookie 或完整认证文件写入本仓库。
7. 统计 C 盘目录时必须跳过 Junction 和其他 ReparsePoint；微信 `xwechat` 当前真实数据在 F 盘，不能重复算作 C 盘占用。
8. 不要从正在执行的 Codex 任务中迁移 `.codex\sessions` 或反复安排注销触发。会话迁移只能在 Codex 完全退出后的独立 Windows 维护窗口执行。

## 后续排障顺序

1. 确认 Codex、CC Switch、Clash 进程和监听端口是否仍在。
2. 查看 CC Switch 日志中的上游状态码，区分本地代理故障、供应商故障和请求体过大。
3. 查看活动 `%USERPROFILE%/.codex/config.toml` 是否被外部工具写入异常上下文限制。
4. 查看 Clash 当前运行模式、当前节点、规则命中和实际 `/rules` 运行态。
5. 只有在安全窗口才重载 Clash 或重启相关工具，并在操作后验证 Codex 会话可继续。

## 文件索引

- [`network-and-codex.md`](./network-and-codex.md)：本次网络与 Codex 稳定性排查、官方上下文核验、Clash 规则和插件持久化。
- [`disk-cleanup-and-codex-storage.md`](./disk-cleanup-and-codex-storage.md)：磁盘清理固定路径、Junction 统计陷阱、Codex 空间增长原因及会话迁移方案。
- [`history.md`](./history.md)：关键修复、失效故障与配置变化摘要。

## 2026-08-30 磁盘清理与 Codex 存储核验

- C 盘在线验收阶段从约 39.38 GiB 可用增加到约 54.99 GiB，真实净增约 15.61 GiB；剪映、Edge、AE、npm、显卡和临时缓存均按进程与路径边界清理。
- 删除 22 份数据库中已经不存在的 Codex 备份，释放约 1.892 GiB；仍被索引的聊天、归档聊天和 2 份备份完整保留。
- 2026-08-30 核验时，221 个被索引的 Codex 会话文件约 25.40 GiB。长会话快速增长的主要原因是上下文压缩记录反复携带截图和 base64 图片数据。
- 微信 `%APPDATA%\Tencent\xwechat` 已是指向 `F:\AppData_Migrated\XWeChat` 的 Junction。扫描显示的约 16.58 GiB 不占 C 盘。
- Codex 可以使用 Junction 实现“C 盘保留数据库和入口，F 盘保存会话文件”；本次失败的是活动任务退出后的执行生命周期，不是 Junction 原理。当前没有部分迁移，数据安全。
- 已注册 `CodexSessionMigration-ToF-Boot` 系统级开机任务，并以 `NT AUTHORITY\SYSTEM` 身份完成一次安全干运行：权限、C/F 盘访问、日志和 Codex 运行阻断均已验证。下次正常重新启动后自动执行；成功或硬失败都会留下 JSON 状态并停用任务，不会形成反复开机循环。
- 上次真实重启中，Codex++ 的登录自动启动在哈希校验末段拉起了 ChatGPT，迁移因此安全延迟而非失败。现已临时安装 `CodexPlusPlusMigrationGate.ps1`，等待迁移结果后恢复原 `CodexPlusPlusWatcher` 启动命令，专门消除这个启动竞态。
- 另外确认启动文件夹中还有同名 `CodexPlusPlusWatcher.lnk` 直接启动 Codex++；该快捷方式已临时隔离并登记，迁移后原样恢复，避免第二条启动链绕过闸门。

完整路径、保留项、失败路线和下一次迁移步骤见 [`disk-cleanup-and-codex-storage.md`](./disk-cleanup-and-codex-storage.md)。

## 2026-07-24 最新网络核验

- `chatgptshare.com` 当前解析为 `154.26.186.65`，本机直连和 Clash 代理到该地址的 80/443 均失败；GitHub、Google 等对照站点正常。当前结论是目标站源服务器不可用，不再把它当成本机 Clash 故障反复切节点。
- 运行时规则尾部为“漏网之鱼 -> 主选择组”，不是直连；持久配置里的专用域名规则尚未进入当前内核，需等无活动任务的安全窗口再重载验证。

## 2026-08-01 Codex 配置修复

- 已为 `new-chat` 项目补回 `trust_level = "trusted"`，解决 Codex 不加载项目级 config、hooks 和 exec policies 的提示。
- 已将该信任段纳入插件持久化守护脚本，防止供应商/配置同步重写 `config.toml` 后再次丢失。
- `codex doctor` 确认配置解析正常，`codex plugin list` 确认当前插件均为已安装并启用；本次不是网络故障或插件包丢失。
- 变化摘要见 [`history.md`](./history.md)。

## 待处理

- 新增的部分站点规则已经写入 Clash 持久配置，但在 2026-07-23 检查时，当前运行内核尚未全部加载。为避免中断正在执行的 Codex 任务，当时未强制重载；应在无活动任务的安全窗口重载后逐条验证。
- 如果插件再次在重启后消失，先检查守护脚本与启动 VBS 是否在运行，再查火绒日志；不要直接重复安装全部插件。

*文件最后整理：2026-08-30；设备事实最后核验：2026-08-30*

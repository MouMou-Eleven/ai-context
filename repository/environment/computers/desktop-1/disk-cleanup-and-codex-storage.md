# 台式电脑1：磁盘清理与 Codex 存储基线

> 本文件保存 2026-08-30 实机清理后可长期复用的路径、判断方法、清理边界和 Codex 会话迁移结论。后续再次清理台式电脑1时，先读本文件，再做当次只读扫描；不要从全盘无差别搜索重新开始，也不要把历史大小当成当前大小。

## 一、2026-08-30 实机结果

### 磁盘状态

| 盘符 | 容量 | 清理后可用 | 可用比例 | 文件系统与健康状态 |
|---|---:|---:|---:|---|
| C | 290.54 GiB | 54.99 GiB | 18.9% | NTFS，Healthy |
| D | 331.00 GiB | 268.61 GiB | 81.2% | NTFS，Healthy |
| E | 331.10 GiB | 79.10 GiB | 23.9% | NTFS，Healthy |
| F | 1907.73 GiB | 1584.06 GiB | 83.0% | NTFS，Healthy |

本轮可在线验收阶段，C 盘空闲空间从约 39.38 GiB 增加到约 54.99 GiB，真实净增约 15.61 GiB。各类文件按逻辑大小合计删除约 16.00 GiB；两者不完全相等，是因为清理期间 Codex、浏览器和其他应用仍在写入少量新缓存和审计记录。判断清理效果必须以卷的 `SizeRemaining` 或 `Get-PSDrive C` 为准，不能只累加文件大小。

### 本次明确释放的主要空间

| 类别 | 已删除 | 处理边界 |
|---|---:|---|
| 剪映 Cache、CEF 缓存、ShaderCache 和日志 | 约 8.31 GiB | 保留 Projects、ComponentStore、SupplysStore 和 Resources |
| Edge 可重建缓存 | 约 3.65 GiB | 保留密码、Cookie、历史、书签、扩展、IndexedDB 和网站持久数据 |
| Adobe / AE 媒体缓存 | 约 0.017 GiB | 保留 Motion Graphics Templates 和工程文件 |
| 已删除但仍残留的 Codex 备份 | 约 1.892 GiB | 22 份数据库中已不存在的备份被删除；2 份仍有索引的备份保留 |
| npm 内容下载缓存 | 约 2.002 GiB | 只清 `_cacache`；正在运行 MCP 使用的 `_npx` 保留 |
| 旧 NVIDIA 缓存、用户临时文件 | 约 0.130 GiB | 只删超过 7 天且未锁定的可重建文件 |

同一轮早期还清理过 Bun、VS Code、uv、pip、Wink、ima.copilot、WorkBuddy 等可重建缓存约 5.72 GiB，以及已核验安装版本和文件哈希的旧安装包约 0.25 GiB。这部分发生在上表的 39.38 GiB 起点之前，不应再次加入 15.61 GiB 的净增数字。

## 二、以后优先扫描的固定位置

### A 类：满足运行条件后可以直接清理

| 工具 | 精确位置或识别规则 | 运行条件 | 不得触碰 |
|---|---|---|---|
| 剪映专业版 | `%LOCALAPPDATA%\JianyingPro\User Data\Cache`、`CEF\Cache`、`CEF\ShaderCache`、`Log` | 剪映和 CapCut 相关进程均未运行 | `Projects`、`ComponentStore`、`SupplysStore`、`Resources`、用户草稿和导出文件 |
| Adobe / AE | `%APPDATA%\Adobe\Common\Media Cache`、`Media Cache Files`、`Peak Files` | `AfterFX.exe` 未运行 | `Motion Graphics Templates`、`.aep`、插件、素材和工程目录 |
| Edge | 各 Profile 下的 `Cache`、`Code Cache`、`GPUCache`、`ShaderCache`、`Service Worker\CacheStorage`，以及顶层 `component_crx_cache`、`Crashpad` | 先判断是否有可见窗口；只有后台进程时才停止独立 `msedge.exe`。不要停止 `msedgewebview2.exe` | `Cookies`、`Login Data`、`History`、`Bookmarks`、`Extensions`、`IndexedDB`、`Local Storage`、`Web Data` |
| npm | `%LOCALAPPDATA%\npm-cache\_cacache` 和旧日志 | 没有 `npm install/update/ci/cache`；进程命令行未引用 `_cacache` | `_npx`。本机多个 MCP 服务直接从 `_npx` 运行，删除会中断 Codex 工具 |
| NVIDIA | `%LOCALAPPDATA%\NVIDIA\DXCache`、`GLCache` 中超过 7 天的普通文件 | 删除失败或被占用时保留，不强杀显卡相关进程 | 驱动、控制面板、CUDA 运行库和 Program Files 下组件 |
| 用户临时目录 | `%LOCALAPPDATA%\Temp` 中超过 7 天的普通文件 | 跳过近期、锁定和 ReparsePoint 文件 | 不能按扩展名推断用户资料；不递归穿透 Junction |
| Codex 已删除备份 | `%USERPROFILE%\.codex-session-delete\backups` | 每个文件都必须先读取 `session_id`，再与 `%USERPROFILE%\.codex\state_5.sqlite` 的 `threads.id` 比对 | 数据库仍有索引、元数据无法读取、路径异常或文件发生变化的备份 |

### B 类：清理前必须重新确认

- 微信主资料路径是 `E:\微信\缓存\xwechat_files`。聊天文件、图片、视频和 PDF 需要按用户最新要求区分自动缓存与主动保存内容；不能只根据扩展名批量删除。
- `%APPDATA%\Tencent\xwechat` 当前是指向 `F:\AppData_Migrated\XWeChat` 的 Junction。扫描时看到的约 16.58 GiB 属于 F 盘，不占 C 盘。清理这里不会增加 C 盘空间，只能释放 F 盘；只考虑两个月前的 `Cache`、`Temp`、`CacheStorage` 和旧日志。
- Camtasia 9 本轮未在 C 盘常见 AppData 路径发现有效缓存。以后可以扫描明确的 Temp、Recovery 和录屏临时目录，但必须保留 `.trec`、`.camproj`、`.tscproj` 以及用户录屏。
- 安装包只有在已安装版本、安装路径、文件版本和哈希均核对后才能删除。不能根据 `.exe`、`.msi`、`.zip` 扩展名批量处理。
- Windows、Program Files 和 ProgramData 下的内容需要先确认组件归属。不要把 `Package Cache`、驱动组件、Windows Update、Defender、网络组件或安全软件数据当普通缓存。

### C 类：禁止自动清理

- 用户用中文自行建立和分类的文档、课程、项目、素材、录屏和下载目录。
- `.codex\sessions`、`.codex\archived_sessions` 中仍被 `state_5.sqlite` 索引的会话。
- `.cc-switch`、Clash / VPN、代理配置、防火墙、火绒和其他安全或网络环境文件。
- Codex 的 `auth.json`、`config.toml`、状态数据库、插件注册、skills 和仍在使用的 MCP 运行目录。
- 剪映项目、Adobe 工程、浏览器账号与持久数据、微信聊天正文和主动保存附件。

## 三、磁盘扫描中最容易误判的三个问题

### 1. Junction 会制造“C 盘仍占用十几 GiB”的假象

普通的 `Get-ChildItem -Recurse` 可能沿 Junction 进入 F 盘，把目标文件算到 C 盘目录树中。2026-08-30 首轮统计因此把 `xwechat` 的 16.58 GiB 列在 C 盘 AppData 下；检查 `Get-Item.LinkType` 后确认它实际位于 F 盘。

后续统计必须同时满足：

1. 先检查待扫描根目录及其子目录的 `Attributes`、`LinkType` 和 `Target`。
2. 不进入 `ReparsePoint`；可使用 `-Attributes !ReparsePoint`，或用自建目录栈明确跳过重解析点。
3. 最终以卷空闲空间变化验收，目录统计只用于定位。

### 2. 候选大小不等于真实净释放

长时间清理时，Codex、浏览器、日志和软件后台进程仍会写入新文件。报告必须同时给出：

- 删除候选的逻辑大小。
- 删除成功的文件大小和数量。
- 清理前后 `SizeRemaining` 的真实差值。
- 锁定、变化、权限不足和保留项。

### 3. 正在运行的程序可能把“缓存目录”当运行目录

本机 npm 的 `_npx` 中直接运行多个 MCP 服务。它虽然位于 `npm-cache` 下，但不能按缓存整目录删除。以后必须同时检查 `Win32_Process.ExecutablePath` 和 `CommandLine`，再决定目录是否只是可重建缓存。

## 四、Codex 空间增长的实机结论

### 当前存储结构

2026-08-30 复核时：

- `.codex\sessions` 与 `.codex\archived_sessions` 中共有 221 个被数据库索引的 JSONL 文件，合计约 25.40 GiB。
- 另有 5 个未被索引的孤儿文件，但总计不足 0.0002 GiB，没有清理价值。
- `state_5.sqlite` 中的 `rollout_path` 仍以 C 盘 `.codex\sessions` 和 `.codex\archived_sessions` 路径登记。
- `.codex-session-delete\backups` 中 22 份无索引备份已经删除；2 份仍有索引的备份约 0.0069 GiB，已保留。

### 为什么长会话会快速变大

最大的会话文件约 5.88 GB。逐行分析发现，多个超过 100 MB 的 `compacted` 记录反复携带 `data:image`、`image_url`、`screenshot` 和 base64 图片数据。第二大文件也出现相同模式。

因此，本机 Codex 会话快速膨胀的主要机制不是普通文本聊天，而是长时间、图片密集型任务在上下文压缩过程中重复保存图片数据。将会话迁移到 F 盘可以解决 C 盘容量压力，但不会阻止会话继续增长。以后仍应：

- 大量截图任务完成后及时开启新任务，避免一个会话无限增长。
- 清理时只删除数据库明确不存在的会话或备份。
- 不因 JSONL 修改时间较旧就推断它已经废弃。

## 五、Codex 会话能否“C 盘保留入口，F 盘保存真实数据”

### 结论：可以，当前只是尚未安全完成

目标结构可以设计为：

```text
C:\Users\Administrator\.codex\state_5.sqlite        保留在 C 盘，继续保存任务索引
C:\Users\Administrator\.codex\sessions             Junction 入口
    -> F:\AppData_Migrated\Codex\sessions           会话真实文件
C:\Users\Administrator\.codex\archived_sessions    Junction 入口
    -> F:\AppData_Migrated\Codex\archived_sessions  归档会话真实文件
```

数据库中的 `rollout_path` 不需要改成 F 盘路径。它继续访问原 C 盘路径，Windows 文件系统通过 Junction 转到 F 盘。因此，这正是“索引保留在 C 盘、聊天记录实际存到 F 盘”的实现方式。

不建议迁移整个 `.codex`。状态数据库、配置、认证、插件和 skills 留在 C 盘，风险更低；只迁移体积最大的 `sessions` 和 `archived_sessions`。

### 为什么 2026-08-30 没有完成

迁移必须在 Codex 完全停止写入会话文件后完成。本次从活动 Codex 任务中尝试了直接子进程、WMI、Explorer 代理和脱离 Windows Job 的进程。即使进程报告 `InAnyJob=False`，Codex 关闭后仍被桌面应用的任务生命周期追踪终止。之后注册的 HKCU RunOnce 在用户注销并重新登录后也没有触发，日志和迁移状态文件均不存在。

已确认：

- 没有发生部分迁移。
- `sessions` 和 `archived_sessions` 仍是 C 盘普通目录，不是 Junction。
- 会话数据没有丢失。
- 失败点是活动任务无法可靠留下一个在 Codex 退出后继续运行的迁移进程，不是 Junction 技术本身不可用。

不要再重复同一套“让当前 Codex 任务关闭自己后继续迁移”的做法，也不要再次要求用户反复注销。

### 下一次应使用的安全执行方式

只能在 Codex 之外的独立 Windows 维护窗口执行，例如：

1. 先准备经过审计的离线脚本和回滚脚本。
2. 用户正常退出 Codex，确认 `codex.exe`、`codex-code-mode-host.exe`、`codex-plus-plus.exe` 及相关写入进程全部结束。
3. 从独立 PowerShell 窗口或开机前已注册的 Windows 计划任务运行迁移；不要让执行进程从活动 Codex 任务派生。
4. 将两个源目录镜像复制到 F 盘，校验文件数、总字节数和关键文件哈希。
5. 再次确认没有 Codex 进程，将 C 盘源目录改名为临时回滚副本，创建两个 Junction 并验证 `LinkType = Junction`、`Target` 正确。
6. 启动 Codex，核验任务列表、现有聊天、归档聊天、新消息写入和新建任务都正常。
7. 验证通过后才删除 C 盘临时回滚副本；失败则移除 Junction 并恢复原目录。

迁移前后都要记录 C、F 盘空闲空间，且 F 盘目标必须纳入备份。F 盘掉线或目标目录损坏时，Codex 通过 C 盘入口也无法访问会话数据。

### 2026-08-30 已部署并验证的开机迁移任务

为避免再次依赖当前 Codex 任务退出后的子进程，已经部署一份独立于 Codex 的 Windows 系统级计划任务：

| 项目 | 已核验值 |
|---|---|
| 计划任务 | `CodexSessionMigration-ToF-Boot` |
| 运行身份 | `NT AUTHORITY\SYSTEM`，最高权限 |
| 触发方式 | Windows 开机 `AtStartup`；`StartWhenAvailable = true` |
| 并发与时限 | `IgnoreNew`；最长运行 4 小时 |
| 正式脚本 | `C:\ProgramData\CodexSessionMigration\Invoke-CodexSessionMigration.ps1` |
| 脚本 SHA-256 | `F33860952DBD3CE2015C2C0EB7CED5B9FAEF83D93FD692072AA7B417F8E6C2F6` |
| 审计目录 | `C:\ProgramData\CodexSessionMigration` |
| 预检结果 | `PreflightPassed`；源会话约 25.402 GiB，F 盘可用约 1583.99 GiB |

最终任务已经在 Codex 仍运行时由任务计划程序手动启动过一次。它确实以 `SYSTEM` 身份运行，能够访问 C、F 盘并写入状态和日志；检测到真实 Codex 写入进程后返回 `DeferredCodexRunning`，没有复制、改名、创建 Junction 或删除任何文件，任务仍保持启用。这个测试证明了开机任务的独立启动链路，不再依赖 Codex 退出后留下的子进程。

正式开机执行采用以下事务边界：

1. 先写 `boot-triggered.json` 和 `migration.log`，避免无声失败。
2. 校验 C、F 盘均为固定 NTFS 卷，校验 F 盘所有权标记、源目录形态和空间余量。
3. 使用 `robocopy /E` 增量复制，不使用会删除目标文件的 `/MIR`。目标端多出的 20 个文件、约 0.434383 GiB 会移动到 `F:\AppData_Migrated\Codex\orphan-quarantine\<runId>`，不会直接删除。
4. 对每一个源文件和目标文件按相对路径做 SHA-256 一致性校验；校验完成后再次检查 Codex 写入进程。
5. 原 C 盘目录先原子改名为带 runId 的回滚副本，再建立两个 Junction，并通过 C 盘入口进行写入穿透测试。
6. 任一步失败都只移除指向核准 F 盘目标的 Junction，并恢复 C 盘原目录；成功验证后才删除 C 盘回滚副本。
7. 成功写 `success.json` 并停用自身；不可恢复的失败写 `failure.json` 并停用自身，避免反复开机循环。只有“Codex 仍在写入”这一可恢复状态会保留任务，等待下次安全开机。

首次正式执行只需要正常“重新启动”Windows，并在开机后暂时不要手动打开 Codex。约 25.4 GiB 数据需要逐文件哈希，可能持续数分钟。验收时检查 `success.json`、两个 C 盘入口的 `LinkType = Junction`、目标均指向 F 盘、任务已经停用以及 C 盘真实空闲空间增加；不能只看脚本是否消失或单一目录大小。

### 2026-08-30 重启验收与自动启动竞态修复

第一次真实重启已经证明 `AtStartup` 任务确实被触发，并完成了 C/F 两侧复制和完整 SHA-256 校验；但登录后的 `CodexPlusPlusWatcher` 自动启动了 `F:\Codex++\codex-plus-plus.exe`，随后拉起 `ChatGPT.exe`。任务在最后切换前检测到这些写入进程，按设计留下源目录并记录 `DeferredCodexStartedDuringHash`，因此没有完成 Junction，也没有损坏或删除会话。

为消除这个已确认的竞态，已部署一次性的 Codex++ 启动闸门：

- `C:\ProgramData\CodexSessionMigration\CodexPlusPlusMigrationGate.ps1` 在用户登录时等待 `success.json` 或 `failure.json`。
- 原 `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\CodexPlusPlusWatcher` 命令已精确备份为 `"F:\Codex++\codex-plus-plus.exe" --debug-port 9229`，当前值临时指向闸门。
- 迁移成功、硬失败或 4 小时 15 分钟超时后，闸门都会恢复原命令；恢复后才启动原 Codex++。如果启动项在等待期间被用户改动，闸门不会覆盖用户的新值。
- 闸门不改 Codex 配置、会话数据库、网络、Clash、火绒或 Codex++ 本体。它只影响这一次尚未完成迁移的登录启动顺序。

更新后的正式脚本使用 2026-08-30 已完整验证的两份清单作为基线。文件路径、字节数或 UTC 修改时间未变的文件复用已验证 SHA-256；有任何变化的文件才重新计算 C/F 两份哈希，无法找到完整基线时仍退回全量校验。这样保留可审计的一致性检查，同时避免再次用约 9 分钟全量读盘给自动启动留下竞态窗口。

本次更新后的安装结果为 `InstalledAndDryRunVerified`，SYSTEM 干运行仍为 `DeferredCodexRunning` 且任务返回码为 0；源目录仍为普通目录，正式迁移尚未发生。运行脚本 SHA-256 为 `F7D562ED400D1C48334B7D8A4C99E2A087834BE2E86837E2B2361E3D9339AA21`，闸门脚本 SHA-256 为 `E1619AB63D7D42C28C2BFA999DD68EF26527BDA087CA5ACF3130C2C6BD8B61CB`。

## 六、以后执行电脑清理的固定流程

1. 读取本文件和设备 README，确认仍是台式电脑1。
2. 获取四个卷的容量、空闲空间、文件系统和健康状态。
3. 扫描时跳过 Junction 和其他 ReparsePoint，先处理已知 A 类路径。
4. 检查相关程序的进程、可执行路径和命令行；不在不安全窗口强关 Codex、网络工具或安全软件。
5. 生成候选清单，区分可直接清理、需用户确认、禁止自动清理。
6. 删除时只使用固定根目录、`LiteralPath` 和逐文件验证；不使用跨 Junction 的通配符递归删除。
7. 对 Codex 备份逐个比对 `state_5.sqlite`，对安装包核对版本和哈希。
8. 清理后再次读取四个卷的真实空闲空间，复核应用进程、Junction、保留文件和失败项。
9. 把新增的稳定路径、误判原因和安全边界更新到本文件；一次性日志和聊天内容不入库。

## 七、相关资料

- [`README.md`](./README.md)：台式电脑1当前入口和操作禁区。
- [`network-and-codex.md`](./network-and-codex.md)：Codex、CC Switch、Clash 与插件排障。
- [`../windows-junction-migration.md`](../windows-junction-migration.md)：已经验证成功的 Windows AppData Junction 迁移方法与卸载边界。
- [`history.md`](./history.md)：本机关键变化摘要。

*文件建立：2026-08-30；设备事实最后核验：2026-08-30*

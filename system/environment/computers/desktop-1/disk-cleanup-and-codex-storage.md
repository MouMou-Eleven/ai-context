# 台式电脑1：磁盘清理与 Codex 存储基线

> 本文件保存 2026-08-30 实机清理后可长期复用的路径、判断方法、清理边界和 Codex 会话迁移结论。后续再次清理台式电脑1时，先读本文件，再做当次只读扫描；不要从全盘无差别搜索重新开始，也不要把历史大小当成当前大小。

## 2026-09-24 复用入口：先分清会话、工作产物和应用缓存

**触发**：建委说“删掉 Codex 对话后文件还在”“C/E 盘又满了”或要求四盘清理时，先按本节定位，再读取下方 A/B/C 分类。**不适用**：软件打不开、网络异常、硬件故障排查；不要为释放空间改动系统、网络或运行组件。

### 三种存储不能混为一谈

| 类型 | 当前真实位置与判断 | 清理闸门 |
|---|---|---|
| Codex 当前／归档聊天 | `C:\Users\Administrator\.codex\sessions` 和 `archived_sessions` 均为 Junction，实际目标是 `F:\AppData_Migrated\Codex\` 下对应目录；`state_5.sqlite` 索引留 C 盘 | 不能因 C 盘入口可见就再迁移或删除会话；先核对 Junction 目标与数据库索引 |
| Codex 任务生成的工作产物 | `C:\Users\Administrator\Documents\Codex\<日期>\<任务>` 是独立文件夹；删除聊天不会联动清理这些文件 | 数据库缺少 `threads.cwd` 只表示“未找到直接索引”，**不证明废弃**；须核查项目内容、进程、链接和建委逐项目授权 |
| 应用可重建缓存 | 下表精确根目录；大小会重新增长 | 先确认软件已停、目录没有重解析点，逐文件删除并记录实际卷空闲变化；不能清整个应用目录 |

本轮只读扫描发现 `Documents\Codex` 下 178 个工作目录，普通文件逻辑量约 25.92 GiB；111 个没有被当前 `threads.cwd` 直接索引，合计约 7.05 GiB，**不是自动删除清单**。建委明确批准编号 1、2、3、4、6 后，才删除以下五个精确根目录；编号 5 `2026-09-02\new-chat` 保留：

| 批准项 | 已清理精确相对路径（共同前缀 `C:\Users\Administrator\Documents\Codex\`） | 删除普通文件逻辑量 |
|---|---|---:|
| 1 | `2026-09-20\c\outputs` | 0.266 GiB；37 个文件已删，播放器占用使空文件夹暂留 |
| 2 | `2026-09-20\c\work` | 0.294 GiB |
| 3 | `2026-07-04\new-chat-2` | 0.953 GiB |
| 4 | `2026-07-11\new-chat` | 0.653 GiB |
| 6 | `2026-08-13\new-chat` | 0.433 GiB |

合计删除约 2.600 GiB 逻辑普通文件；两个工作目录内的 762 个重解析链接只移除链接本身，未进入其目标。删除前 C 盘可用 39.046 GiB，五项删除后即时读数 41.339 GiB。后续清缓存、Windows 搜索索引写入和活动应用写入会让卷读数波动，**不能把 2.600 GiB 当成最终净释放**。

本轮其他已执行项：AE 精确缓存删除 2710 个 `.aecache`（逻辑 22.39 GiB）；360 浏览器无可见窗口且建委再次确认已保存并关闭后，结束其专属后台进程，删除 `CacheStorage` 的 3729 个文件（逻辑 1.94 GiB）；剪映关闭后清 `User Data\Cache` 的 17,862 个普通文件（逻辑 1.176 GiB），3 个被锁的 `trayCloudDraft\ec_sdk*` 文件和 1 个异常尾空格路径保留。没有动剪映草稿根目录、浏览器持久数据、AE 工程。观察到 C 盘空间在 Windows Search 大量短时写入时下探、随后回升；不为追逐瞬时读数关闭或清理 Search。

| 卷 | 清理前可用 | 本轮最终复读可用 | 净变化 |
|---|---:|---:|---:|
| C | 39.046 GiB | 43.872 GiB | +4.826 GiB |
| D | 272.111 GiB | 272.111 GiB | 未清理 |
| E | 64.774 GiB | 89.082 GiB | +24.308 GiB |
| F | 1565.901 GiB | 1565.894 GiB | 未清理；少量活动写入 |

卷空闲量是当次时间点的观测值，清理期间应用、搜索索引会继续写入；不能把这些数字当成未来可用空间保证。C 盘还有 Claude 虚拟机、正在写入的 Codex 应用数据及可能用于恢复的 PowerPoint 临时文件等大项，均没有因“容量大”而删。D/F 主要是系统分页文件、迁移数据和用户资料，本轮没有得到安全且值得清理的自动删除项。

### 下次最快的定位顺序与停手条件

1. 记录 C/D/E/F 的 `SizeRemaining`、程序进程、扫描时间。扫描器必须跳过 `ReparsePoint`，按卷看真实占用；目录逻辑量不等于卷已用量，权限拒绝范围要记下来。
2. C 盘先看 `Documents\Codex` 已获批准的旧任务产物、`%LOCALAPPDATA%\JianyingPro\User Data\Cache`、用户 Temp 中超过 7 天的普通文件、npm `_cacache`；`_npx` 是本机 MCP 运行目录，不能当下载缓存清。`AppData\Roaming\Codex\web` 在本轮仍有当日写入，不得因为名字含 Codex 就删除。
3. E 盘先量 AE 的 `E:\Ae2020\缓存\Adobe\After Effects\17.0\Disk Cache - PC-20240618ZHAK.noindex` 下 `.aecache`，再量 `E:\360极速浏览器\360ChromeX\Chrome\User Data\Default\Service Worker\CacheStorage`。这两项会再生：本轮分别重新增长到约 22.39 GiB（2710 个 `.aecache`）和 1.94 GiB（3729 个文件）；AfterFX、360 均退出后只清各自精确缓存文件，浏览器账号／历史／书签／网站持久数据保留。
4. D/F 先看卷空闲与顶层占用；本轮 D 可用约 272.11 GiB、F 可用约 1565.90 GiB，没有容量紧迫。D 的 `pagefile.sys` 是系统分页文件，F 的 `AppData_Migrated` 含 Codex 和微信迁移数据，都不可当“旧文件”删。
5. 微信、剪映草稿、PowerPoint 恢复文件、安装包、录屏和用户中文分类目录，即使大也先列简短候选供确认；没有来源证据时不能称微信 PDF 是自动下载。若程序重新启动、文件被锁、路径异常或候选变化，停在该项，不强杀 Codex／系统／网络组件。
6. 清理后复读四卷可用空间、Junction 目标、关键程序运行状态及失败项。若净变化反常，先查活动写入者；本轮看到 `SearchIndexer.exe` 短时大量写入后空间回升，不因此清理或关闭 Windows Search。

本次四盘顶层只读扫描显示：C 主要是用户目录约 141.99 GiB、Windows 约 38.60 GiB 和程序目录；E 主要是微信约 77.02 GiB、剪映约 41.59 GiB，均含真实资料／草稿；D 主要是 38 GiB 系统分页文件和用户资料；F 主要是用户文件与迁移后的应用数据。扫描有读取拒绝项，也可能重复计入硬链接，以上数字只用于定位，不作为精确可释放量。一次性逐文件清单、扫描 JSON 和删除结果留在本机任务工作区，不把私人文件名、聊天正文、Token 上传仓库。

## 2026-09-15 最新复核：迁移已成功，缓存又增长

### 当前事实与证据

- C 盘开始可用 36.30 GiB，E 盘 39.98 GiB；D 盘 279.13 GiB，F 盘 1580.17 GiB。四卷均为 NTFS、Healthy；健康标记不等于完整硬件故障检测。
- `C:\ProgramData\CodexSessionMigration\success.json` 记录 2026-08-31 18:32:21 完成迁移，当时会话合计 23.754781 GiB，C 盘可用 71.911 GiB。2026-09-15 实际核验两处 C 盘 Junction 均指向原定 F 盘路径；当前会话文件合计约 6.29 GiB。
- 旧文档没有回填成功状态。“等待下次重启”只描述 8 月 30 日，不再适用。以后直接查 Junction 和文件实际所在卷，不要重复迁移。
- `.codex-session-delete\backups` 与 `.codex\sessions` 是不同目录。会话迁往 F 盘后，删除工具仍会在 C 盘保存恢复副本；本次发现 8 份无当前索引的删除备份约 5.6511 GiB，其中同一已删除会话有两份各约 2.4382 GiB 的备份。
- 当前数据库有 213 个线程、其中 16 个归档。归档不是删除；官方说明仍可从设置恢复归档聊天，见 [OpenAI 故障排查](https://learn.chatgpt.com/docs/reference/troubleshooting)。本次只按已删除备份的 `session_id` 与实时只读数据库交叉核验，不改会话正文或数据库。
- 微信附件中扫描到 785 份 PDF，合计 3.4132 GiB。建委逐批确认后，删除其中 20 份超过两个月的学科 PDF，共 50.02 MiB；其他附件保留。不能把这次明确名单授权推广为以后无条件删除所有 PDF。
- 清理前已经有 2 个索引指向不存在的 rollout 文件，两者恰有恢复备份；这两份备份保留。缺失并非本轮删除造成，不能为凑释放空间删除最后的可恢复副本。

### 已完成清理与验收（2026-09-15 19:01）

| 卷 | 清理前可用 | 清理后可用 | 净增加 |
|---|---:|---:|---:|
| C | 36.30 GiB | 45.86 GiB | 9.56 GiB |
| E | 39.98 GiB | 94.98 GiB | 55.00 GiB |

合计净增约 64.56 GiB。成功删除 99,333 个普通文件，逻辑大小约 65.53 GiB：C 盘约 10.6339 GiB、E 盘约 54.8974 GiB。主要为 360 缓存 33.22 GiB、AE 21.63 GiB、已删除会话备份 5.65 GiB、npm 2.00 GiB、剪映 1.34 GiB，以及 Figma/WorkBuddy/显卡/pip 缓存和经确认的 20 份微信 PDF。36 个被占用的缓存/日志文件保留；D/F 本轮没有删除。

AE 磁盘缓存和 360 CacheStorage 清理后普通文件数均为 0。现有 Codex 数据库只读完整性检查为 ok，线程仍为 213 个；两个 Junction 和浏览器持久数据保留项分别核验。不以这些检查承诺所有软硬件均经过完整功能测试。

PowerPoint 的 60 份临时恢复文件（6.0047 GiB，最后修改在 2026-04-03 至 2026-05-15）以及剪映回收站 9 个草稿（4.3352 GiB）只生成了候选名单，未取得放弃恢复确认，本轮保留。未来若建委明确确认名单，才按该名单清除。

### 清理前大项明细

| 位置或类别 | 扫描逻辑大小 | 判定 |
|---|---:|---|
| E 盘 360 浏览器 | 41.85 GiB，其中 CacheStorage 32.62 GiB | 大量为飞书站点离线资源缓存；保存工作、退出窗口及后台后清理可重建缓存，保留登录、历史、书签、IndexedDB、Local Storage |
| E 盘 AE | 24.53 GiB，其中 `.aecache` 21.63 GiB | 精确清理 `E:\Ae2020\缓存\Adobe\After Effects\17.0\Disk Cache - PC-20240618ZHAK.noindex` 的 8287 个 `.aecache`；不碰软件本体 |
| E 盘微信 | 72.99 GiB | 主账号消息视频约 23.00 GiB、文件约 20.34 GiB、附件约 14.93 GiB；消息库及附件不当作普通缓存删除 |
| E 盘剪映 | 41.46 GiB | `JianyingPro Drafts` 26.80 GiB，其中云草稿缓存 12.88 GiB、回收草稿 4.33 GiB；素材库 13.21 GiB。可能影响工程，不自动删除 |
| C 盘 Claude-3p | 10.60 GiB | 约 10.04 GiB 为虚拟机包；它是运行环境，不是删除聊天残留 |
| C 盘 Codex 工作目录 | 19.70 GiB | 含视频成品、项目源码和依赖；聊天删除不能证明这些产物废弃 |
| C 盘 PowerPoint | 约 6.00 GiB | 60 个 `.tmp` 可能含恢复内容，即使较旧也先保留，另列审阅清单 |
| C 盘 Camtasia | 录屏目录约 1.34 GiB | 主要为真实 `.trec` 录屏；没有确认到值得整批清理的大录屏缓存 |
| C 盘用户 Temp | 3.50 GiB | 其中约 2.95 GiB 是当天生成的 Visual Studio 安装临时内容，不在当次清理窗口动它 |

### 扫描与权限边界

普通权限扫描 C 盘 1,443,963 个文件、E 盘 867,248 个文件，显式跳过重解析点；分别记录 251 和 10 个读取错误。随后以提升权限的独立只读脚本复核这 261 处，共读到额外约 12.49 GiB，仍有 24 个拒绝访问或锁定错误；没有接管所有权或修改 ACL。

额外大项主要为 WindowsApps 约 7.36 GiB、Windows Search 数据约 2.28 GiB、Codex 沙箱用户约 0.87 GiB、Defender 定义备份约 0.43 GiB，均保留。目录逻辑大小可能因硬链接重复统计，不能与卷使用量直接相加；释放空间以卷前后读数为准。

### 下次清理新增定位规则

1. 先核查迁移后的聊天入口，以及 C 盘独立的删除备份目录；备份须逐文件验证，不把已归档或界面没显示的任务直接判为已删除。
2. E 盘首先测量 360 的 `Default\Service Worker\CacheStorage` 和 AE `.aecache`。前者本次最大几处 origin 来自飞书站点，继续访问会重新下载；后者继续渲染也会重新生成。
3. 用户关闭窗口不代表进程已退出。本次用户保存并关闭后，仍需核对并结束 360 与剪映托盘的专属无窗口后台；不能扩大到 Codex、网络工具或 WebView2。
   清理中途 360 再次出现进程时已暂停剩余删除，建委再次确认关闭后才恢复。脚本增加每秒复查，不能只在整批开始前看一次进程。360 本机历史数据库名为 `360History`，不能因找不到普通 Chrome 的 `History` 文件误报丢失。
4. 清理只使用固定根目录的普通文件清单，逐项校验时间、大小与祖先重解析点，锁定项保留。记录每一项成功和跳过原因，不递归删除整个应用目录。
5. 自动下载来源无法从 PDF 路径或文件时间证明。微信 PDF 按具体清单征求确认，不能用“教学类”文件名替代下载来源证据。
6. 本次不调整任何缓存位置、缓存容量或自动清理频率。需要长期控制时，再明确确认具体软件和设置，尤其不能将整个 `.codex`、浏览器配置或微信资料根目录随意迁移。

一次性目录清单、文件名单和逐项删除日志保存在本机任务目录 `Documents\Codex\2026-07-31\new-chat\outputs\disk-audit-20260915`，不把私人附件名或对话内容提交 GitHub。

本轮第二次 C 盘扫描还观察到另一在执行 AI 项目新建约 447.90 MiB 的 `qa-r27\rebuild\node_modules`，其工作目录累计新增约 472.54 MiB；Windows 目录同期净增约 228.61 MiB，本轮报告及审计目录约 133.81 MiB。因此，清理与新增写入可以同时发生，净释放量不能只按删除清单累计；这些活跃依赖和系统内容未清理。

## 一、2026-08-30 实机结果（历史）

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

### 结论：可以；2026-08-31 已完成，2026-09-15 已复核

以下保留原设计与失败历史。当前完成状态以本页顶部新证据为准，不再运行历史迁移方案。

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

### 当时拟定的安全执行方式（历史，不再执行）

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
- 进一步核验发现用户启动文件夹中的 `Startup\CodexPlusPlusWatcher.lnk` 也直接指向同一命令；它已临时移动到 `C:\ProgramData\CodexSessionMigration\CodexPlusPlusWatcher.lnk.migration-disabled`，原目标、参数和工作目录记录在 `codex-plus-plus-shortcut-backup.json`。它不是删除，迁移结果出来后会原样移回。
- 迁移成功、硬失败或 4 小时 15 分钟超时后，闸门都会恢复原命令；恢复后才启动原 Codex++。如果启动项在等待期间被用户改动，闸门不会覆盖用户的新值。
- 闸门不改 Codex 配置、会话数据库、网络、Clash、火绒或 Codex++ 本体。它只影响这一次尚未完成迁移的登录启动顺序。

更新后的正式脚本使用 2026-08-30 已完整验证的两份清单作为基线。文件路径、字节数或 UTC 修改时间未变的文件复用已验证 SHA-256；有任何变化的文件才重新计算 C/F 两份哈希，无法找到完整基线时仍退回全量校验。这样保留可审计的一致性检查，同时避免再次用约 9 分钟全量读盘给自动启动留下竞态窗口。

本次更新后的安装结果为 `InstalledAndDryRunVerified`，SYSTEM 干运行仍为 `DeferredCodexRunning` 且任务返回码为 0；源目录仍为普通目录，正式迁移尚未发生。运行脚本 SHA-256 为 `F7D562ED400D1C48334B7D8A4C99E2A087834BE2E86837E2B2361E3D9339AA21`，最新闸门脚本 SHA-256 为 `B589CAF388192C2045E322B595FCCDC3F4556BCFECCEC53CCB438CCEFE5796C3`。

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

*文件建立：2026-08-30；存储事实最后核验：2026-09-15*

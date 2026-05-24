# Windows C 盘瘦身：用 NTFS Junction 把 AppData 迁到 F 盘

> 一次性把臃肿的应用数据从 C 盘转移到 F 盘，又不破坏任何软件的运行。
> 实际操作日期：2026-05-24，C 盘释放 57.96 GB。

---

## 一、为什么这么做

我的 C 盘只剩 40 GB 可用，挤的全是常驻应用堆在 AppData 下的本地数据：飞书、企业微信、微信、Cursor、Docker、豆包、WPS、微信解密工具（.vchat）等。

直接卸载会丢配置和聊天记录；改安装路径要重装；移动文件夹应用会找不到数据。**NTFS Junction（目录联接）**是唯一既能搬走数据、又能让应用毫无感知继续运行的办法。

## 二、Junction 是什么

NTFS 文件系统层的"目录重定向"，由 Windows 内核的 reparse point 机制实现：

```
C:\Users\Administrator\AppData\Roaming\LarkShell   ← 这是 Junction（占几百字节）
                       ↓ 内核自动转发
F:\AppData_Migrated\LarkShell                       ← 真实数据在这里
```

应用打开 C: 上的路径时，操作系统在文件系统层把请求重定向到 F:，**应用完全感知不到**。Windows 自己就大量用这个机制（如 `C:\Users\All Users` → `C:\ProgramData`）。

跟快捷方式（.lnk）和符号链接（symlink）的区别：
- 快捷方式：是个文件，需要应用主动识别才能跳转
- 符号链接（symlink）：内核级跳转，但需要管理员权限创建，跨盘要开启开发者模式
- Junction：内核级跳转，**只能指向目录、只在本地盘、无需管理员权限**——最稳

## 三、本次迁移记录

### 迁移清单（按执行顺序）

| 应用 | 原路径 | F 盘目标 | 大小 |
|---|---|---|---|
| DotVchat（微信解密工具数据） | `C:\Users\Administrator\.vchat` | `F:\AppData_Migrated\DotVchat` | 5739.2 MB |
| Cursor | `C:\Users\Administrator\AppData\Roaming\Cursor` | `F:\AppData_Migrated\Cursor` | 5235.4 MB |
| Docker | `C:\Users\Administrator\AppData\Local\Docker` | `F:\AppData_Migrated\Docker` | 4167.6 MB |
| 企业微信 WXWork | `C:\Users\Administrator\AppData\Roaming\Tencent\WXWork` | `F:\AppData_Migrated\WXWork` | 4035 MB |
| 飞书 LarkShell | `C:\Users\Administrator\AppData\Roaming\LarkShell` | `F:\AppData_Migrated\LarkShell` | 15404.6 MB |
| 微信 XWeChat | `C:\Users\Administrator\AppData\Roaming\Tencent\xwechat` | `F:\AppData_Migrated\XWeChat` | 11143.7 MB |
| 豆包 Doubao | `C:\Users\Administrator\AppData\Local\Doubao` | `F:\AppData_Migrated\Doubao` | 7199.5 MB |
| WPS（kingsoft） | `C:\Users\Administrator\AppData\Roaming\kingsoft` | `F:\AppData_Migrated\Kingsoft` | 5375 MB |

**结果**：C 盘 40.87 GB → 98.82 GB，净释放 **57.96 GB**。

### 故意没迁的：`.cursor`

`C:\Users\Administrator\.cursor` 里有 Cursor 扩展的常驻 MCP 服务进程（`mcp-server-windows-x64.exe`），迁移过程中会锁住目录。如果硬迁会导致 VS Code/Cursor 当场崩溃。判断逻辑：迁移前用 `Win32_Process` 扫一遍 `ExecutablePath` 和 `CommandLine`，发现有进程驻留就跳过。

## 四、迁移脚本的关键设计

脚本路径：`C:\tmp\migrate_v2.ps1`（由 PowerShell 跑）。核心思路是**全程不杀进程，发现锁就停**，保证不破坏任何在跑的应用。

每个目录的迁移步骤：

1. **预检锁**：扫 `Win32_Process`，正则匹配 `ExecutablePath` / `CommandLine`，发现有进程驻留就抛错跳过。
2. **统计源**：`Get-DirStats` 算文件数 + 总字节数，作为校验基线。
3. **robocopy /MIR**：镜像复制，`/COPY:DAT /DCOPY:DAT` 保留时间戳和属性，`/MT:8` 多线程。退出码 ≥8 视为失败。
4. **字节级校验**：复制完再算一遍目标统计，文件数和字节数必须**完全一致**才继续。
5. **再次锁检查**：删源之前再扫一遍，防止迁移过程中应用启动占用。
6. **删源 + 建 Junction**：`Remove-Item -Recurse` 删源，`cmd /c mklink /J 源 目标` 建联接，最后 `Get-Item.LinkType` 验证返回 `Junction`。
7. **任一步失败立即停**：循环里 `try/catch`，出错记日志后 `break`，绝不带病推进。

日志路径：`F:\AppData_Migrated\migration.log`（含完整时间戳）。

## 五、后续维护（重要）

### 5.1 关于 `Get-ChildItem -Recurse` 的统计陷阱

PowerShell 的 `Get-ChildItem -Recurse` **默认会跟随 Junction**——你统计 C 盘大小时，它会顺着 Junction 跑去 F 盘把数据再数一遍算到 C 上，让人误以为"迁移没生效"。

**真实占用以这两个为准**：
```powershell
Get-PSDrive C                                          # 看可用空间（最准）
Get-ChildItem C:\ -Recurse -Attributes !ReparsePoint   # 排除重解析点统计
```

### 5.2 卸载软件时的正确顺序

Junction 引入的真正麻烦是卸载可能留"孤儿"——C 盘留下死 Junction，或 F 盘留下没人用的数据。

**安全卸载流程**：
```cmd
# 1. 用应用自带卸载器卸载
# 2. 检查 C 盘 Junction 是否还在
dir /AL C:\Users\Administrator\AppData\Roaming\<app>
# 3. 如果还在，只删 Junction（不加 /s，重要！）
rmdir C:\Users\Administrator\AppData\Roaming\<app>
# 4. 再删 F 盘真实数据
rmdir /s /q F:\AppData_Migrated\<app>
```

**绝对不要做**：
- `del /s /q C:\junction路径\*`——`del /s` 会穿透 Junction，把 F 盘真实数据全删掉（如果是要卸载倒也无所谓，但如果只是清缓存就完蛋了）

### 5.3 备份策略要变

数据现在都集中在 F 盘一块物理盘上，鸡蛋集中在一个篮子。**F 盘必须做定期备份**——外接硬盘 / NAS / 云盘任选，但不能没有。

### 5.4 已知风险点

| 风险 | 触发条件 | 应对 |
|---|---|---|
| Junction 失效 | F 盘掉线/拔出 | F 盘别动，做好备份 |
| 备份软件双倍占用 | 跟随 Junction 把 F 数据当 C 备份 | 备份配置里排除 F 盘目标路径或排除 Junction |
| Windows 大版本升级重置 Junction | 历史上偶发于 Users 下的目录 | 关键 Junction 截图记录，必要时 `mklink /J` 重建即可 |
| 杀软重复扫描 | 部分老杀软跟随 Junction 扫两遍 | 现代 Defender 已正确处理，没事 |

## 六、再次迁移其他软件的步骤模板

未来 C 盘又胀起来时，复用同一套脚本：

1. 编辑 `C:\tmp\migrate_v2.ps1` 的 `$plan` 数组，加新条目：
   ```powershell
   @{ Label="XXX"; Source="C:\...\XXX"; Target="F:\AppData_Migrated\XXX" }
   ```
2. **先关闭对应应用**（脚本会自动检测锁并跳过，但提前关更稳）
3. 用管理员 PowerShell 跑脚本
4. 看 `F:\AppData_Migrated\migration.log` 确认 `[OK]`
5. 启动应用确认无异常

## 七、相关文件

- 迁移脚本：`C:\tmp\migrate_v2.ps1`
- 进程扫描脚本：`C:\tmp\scan_only.ps1`（只扫不杀，迁移前用）
- 迁移日志：`F:\AppData_Migrated\migration.log`
- 索引说明：`F:\AppData_Migrated\README.txt`（迁移脚本自动生成）

---

*记录时间：2026-05-24*
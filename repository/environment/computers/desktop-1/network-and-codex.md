# 台式电脑1：网络、Clash 与 Codex 排障基线

> 本文件记录 2026-07-23 的实机检查结果。它是后续排查基线，不代表外部供应商、VPN 节点或网站状态永久不变。

## 一、问题表现与分类

本机曾连续出现以下几类错误，不能混为同一个“网络不稳定”问题：

| 表现 | 含义 | 已核验判断 |
|---|---|---|
| HTTP 502/503/504，CC Switch local proxy failed | CC Switch 能接到本地请求，但外部供应商连接失败、超时或无可用供应商 | 主要与上游供应商、DNS、节点或长连接稳定性有关 |
| HTTP 413 Payload Too Large | 请求正文超过上游网关限制 | 不是 Clash 错误；本次还叠加了错误的 64K 自动压缩配置 |
| `stream disconnected` / response body decode error | 流式响应中途断开或返回了非预期网页 | 切换全局/直连/节点会中断既有连接，供应商 5xx 页面也会触发 |
| 国内站点正常、个别海外站点一直转圈 | 规则未命中、节点对目标站点不兼容，或目标站点自身异常 | 必须对单域名做 DNS、直连、代理、节点和运行规则对比 |
| 插件重启后减少 | 插件注册未持久化或守护启动被拦截 | 当前有独立守护脚本维护 8 个插件 |

## 二、Codex 上下文与自动压缩

### 官方核验结果

2026-07-23 通过 OpenAI 官方 `openai/codex` 源码和本机 Codex 官方内置模型目录核验：

- 当前官方内置模型的上下文窗口是 `272000` token。
- 有效上下文按 `95%` 计算，为 `258400` token。
- `258400` 十进制 token 约等于 `252.3 Ki token`，口语中常被说成约 `254K`；它与 `64K` 不是同一档。
- 本地显式配置 `model_context_window` 或 `model_auto_compact_token_limit` 会覆盖模型目录默认值。

官方来源：

- [OpenAI Codex `model_info.rs`](https://github.com/openai/codex/blob/6e0455fdc4114ae5d14a88ec966c090208e71e0c/codex-rs/models-manager/src/model_info.rs)
- [OpenAI Codex `context_window.rs`](https://github.com/openai/codex/blob/6e0455fdc4114ae5d14a88ec966c090208e71e0c/codex-rs/core/src/session/context_window.rs)

### 本机为何变成 64K

直接写入源不是官方 Codex。`%USERPROFILE%/.codex/plugin-persistence-guard.ps1` 原先每 3 秒强制维护：

```toml
model_context_window = 128000
model_auto_compact_token_limit = 64000
```

第一次手动删除后几秒内又恢复，守护日志时间与恢复时间一致，从而锁定写入源。脚本已修正为只维护插件注册和必要的输出设置，不再写这两个字段。活动配置经过多轮循环验证，没有再次恢复。

当前保留的相关设置为：

```toml
model_auto_compact_token_limit_scope = "total"
tool_output_token_limit = 12000
```

结论：之前频繁显示“上下文已自动压缩”，根因是本机自定义守护脚本把阈值固定为 64K；清除硬编码后，后续新产生的上下文应回到官方模型目录决定的有效上限。已启动的任务仍可能保留创建时的模型快照，需以新任务验证最终 UI 表现。

## 三、当前代理与供应商链路

### 运行组件

| 组件 | 当前作用 |
|---|---|
| Clash for Windows | 规则模式；Windows 用户代理监听 `127.0.0.1:7890` |
| CC Switch | 本地 Codex 网关监听 `127.0.0.1:15721` |
| Codex++ | 管理器在本次排查时关闭供应商自动切换，不作为活动请求网关 |
| Codex | 请求发往 CC Switch 的本地 `/v1/responses`，再由 CC Switch 转发 |

当前供应商链路经 CC Switch 指向 `https://2api.aiwanwu.cc/v1/responses`。2026-07-23 实测经代理访问该域名和 GitHub 均返回 HTTP 200，CC Switch 近期日志未出现新的 WARN/ERROR。

### 系统代理边界

- Windows 用户代理：`127.0.0.1:7890`。
- 本地地址 `localhost`、`127.*` 绕过代理，所以 Codex 到 CC Switch 的本地连接不应绕进 Clash。
- WinHTTP 为直连。
- 不要在 Windows 系统代理里残留一个已退出代理软件的端口；这会让 CC Switch 的上游请求表现为随机失败。

## 四、Clash 当前配置

### 当前模式和节点

- 模式：规则模式。
- 主选择组：`🔰 选择节点`。
- 2026-07-23 当前节点：`🇭🇰 香港S04 | IEPL`。
- `🐟 漏网之鱼` 指向主选择组。

持久配置位于 Clash 安装目录的 `data/profiles/`，本次活动订阅配置为 `1768329120061.yml`；同时存在 `cfw-settings.yaml` 的解析器/覆写设置。

### 已写入持久配置的定向规则

| 域名 | 目标策略 |
|---|---|
| `minimal.gallery` | 日本 S04 |
| `awwwards.com` | 日本 S04 |
| `chatgptshare.com` | 主选择组 |
| `aiwanwu.cc` | 主选择组 |
| `naiccc.com` | 主选择组 |
| `admin.shareoai.com` | 主选择组 |
| `openai.com`、`chatgpt.com`、`oaistatic.com`、`oaiusercontent.com` | 主选择组 |
| `github.com`、`githubusercontent.com` | 主选择组 |

重要：2026-07-23 通过 Clash 控制器检查运行时 `/rules`，`openai.com` 和 `github.com` 规则已存在，但 `minimal.gallery`、`awwwards.com`、`chatgptshare.com` 等新增规则尚未全部进入当前内核。配置文件已写入不等于当前内核已加载。为不切断正在执行的 Codex 任务，本次没有强制重载 Clash。

### 安全窗口操作

在没有 Codex 活动任务时：

1. 记录当前 Clash 节点和模式。
2. 重载当前订阅配置或重启 Clash 内核。
3. 用控制器 `/rules` 验证上述域名规则已进入运行态。
4. 分别测试 DNS、直连、系统代理和指定节点的 HTTPS。
5. 验证 GitHub、OpenAI/Codex 供应商和常用国内站点均正常，再结束维护。

## 五、插件持久化与火绒

插件持久化由以下文件负责：

- `%USERPROFILE%/.codex/plugin-persistence-guard.ps1`
- `%APPDATA%/Microsoft/Windows/Start Menu/Programs/Startup/CodexPluginPersistenceGuard.vbs`

守护脚本每 3 秒检查插件注册。本次修复只删除其上下文窗口强制设置，没有移除插件维护功能。

火绒日志中的拦截目标是启动目录 VBS 的重写操作。现有 VBS 文件和守护进程仍存在，因此这条拦截不等于 Codex 无法写项目文件。后续若插件再次消失，按以下顺序检查：

1. 守护 PowerShell 进程是否在运行。
2. 启动 VBS 是否存在、内容是否指向正确脚本。
3. 守护日志是否有插件恢复记录。
4. `%USERPROFILE%/.codex/plugins` 的注册状态与实际缓存是否一致。
5. 最后才考虑重新安装插件或为单个已核验文件添加火绒放行。

## 六、2026-07-24 chatgptshare.com 复核

2026-07-24 对 `https://chatgptshare.com/list/?partner=6iwhbhzxFqH` 做了 DNS、直连、Clash 代理和多节点对照：阿里 DNS、Cloudflare DNS、Google DNS 均返回 `154.26.186.65`；本机 TCP 80/443 均失败；Clash 代理 HTTPS 握手失败并返回 502；香港、日本、新加坡、美国、欧洲节点的独立 delay 测试全部失败；Globalping 的 5 个独立公网 HTTP 探针也全部失败。对照测试中 Google 204 和 GitHub 200 正常。

运行时规则最后是 `DomainKeyword . -> 🐟 漏网之鱼` 与 `Match -> 🐟 漏网之鱼`，不是 `DIRECT`。持久 `profileParsersText` 中虽有 `chatgptshare.com -> 🔰 选择节点`，当前运行内核尚未加载这条专用规则；这属于配置同步问题，但不是本次故障主因，因为 catch-all 已经走代理，而目标源站 80/443 本身不可达。

因此本次不切换节点、不重启 Clash、不改 hosts。源站恢复后再做一次 `/rules` 命中和页面验证；若仍失败，再继续检查节点与规则。关键结论见 [`history.md`](./history.md)。

## 七、2026-08-01 项目信任与插件加载修复

Codex 配置页出现“将当前项目添加为 trusted project”提示时，活动 `config.toml` 缺少 `new-chat` 项目段。已补回 `trust_level = "trusted"`，并将该段加入插件持久化守护脚本的必要块，避免后续配置同步再次删除。`codex doctor` 确认 TOML 解析正常，`codex plugin list` 确认插件注册和安装缓存完整。本次不是 Clash 或插件下载故障。

关键结论见 [`history.md`](./history.md)。

## 八、变更和验证边界

- 本次没有重启 Codex、CC Switch 或 Clash，也没有切换节点。
- 修改前已在本机 `.codex` 目录创建配置和脚本备份；备份不进入 GitHub。
- 仓库未记录任何 API Key、Token、Cookie、局域网地址或完整认证文件。
- 外部站点和供应商状态会变化；后续排查必须重新实测，不得把 2026-07-23 的 HTTP 结果当永久事实。

## 九、2026-09-07 GitHub、iKuuu、CFW 与 Clash Verge 复核

### GitHub 故障结论

本次实测不是 GitHub 账户或仓库权限失效：GitHub CLI 仍以 `MouMou-Eleven` 登录，凭据范围满足私有仓库读写；专用 Ed25519 公钥已经注册到 GitHub。网络表现存在明显路径差异：GitHub API 可以直连，GitHub 网页直连超时，而通过 iKuuu 本地代理访问网页和 API 都返回成功。因此，之前 HTTPS push 失败属于 GitHub HTTPS 路径不稳定，不能通过增大 `http.postBuffer` 解决。

`ai-context` 已改用独立 SSH 别名：目标是 `ssh.github.com:443`，只使用 `id_ed25519_ai_context`。SSH 连接前由本地脚本依次探测 iKuuu、Clash for Windows 和 Clash Verge 的常见本地端口，使用当前真正启动的代理；都未启动时回退到 SSH 443 直连。该配置只作用于 GitHub SSH，不会改变浏览器或国内应用的流量路线。

Git 内置 SSH 与 Windows OpenSSH 对 `ProxyCommand` 的调用方式不同。本机 Git 内置 SSH 曾把命令前的 `exec` 交给 PowerShell，导致 `exec is not recognized`。当前仓库已经通过仓库级 `core.sshCommand` 明确使用 Windows OpenSSH。2026-09-07 已依次验证 SSH 账户认证、`git fetch`、`git push --dry-run` 和真实 `git push`，远端 `main` 成功前进到课程复盘提交。

后续处理 GitHub 连接时按以下顺序检查：

1. `ssh -T github-ai-context` 是否返回 GitHub 认证成功。
2. 当前使用的 VPN 客户端是否真的有本地代理端口在监听，不能只看窗口是否打开。
3. `git remote -v` 是否仍为 `git@github-ai-context:...`，仓库级 `core.sshCommand` 是否仍指向 Windows OpenSSH。
4. 先执行 `git fetch` 和 `git push --dry-run`，确认远端无冲突后再真实推送。
5. 不把 GitHub 代理写成全局 Git 代理；固定全局端口会在 iKuuu、CFW 和 Verge 之间切换时变成失效配置，也会影响其他仓库和国内地址。

### Clash for Windows 分流结论

活动订阅本身已经包含 `.cn` 域名和中国大陆 IP 直连规则，尾部未命中流量才进入主选择组。因此，没有证据支持“当前 CFW 把所有国内流量都送到代理节点”。浏览器请求先进入本地 Clash 端口，不等于流量最终经过付费节点；是否消耗节点流量取决于规则最终选择 `DIRECT` 还是代理组。

本次发现的实际异常是持久配置的活动订阅索引为 `-1`，同时 `GitHub -> 主选择组` 中的主选择组被保存为 `DIRECT`。这会让 GitHub 规则虽然存在，却仍然直连并触发超时。现已把活动订阅索引恢复为该订阅，并把主选择组恢复到原先保存的香港 IEPL 节点。修改前已完整备份；为不切断当前 Codex 任务，本次只更新持久配置，没有强制重载 CFW 内核。

不要为了省流量把 CFW 改成全局直连，也不要把所有域名手工列进规则。正确做法是保持规则模式、国内规则指向 `DIRECT`、GitHub/OpenAI 等确需代理的域名指向主选择组，最后才由漏网规则接管未匹配流量。

### Clash Verge 更新与同步

Clash Verge Rev 已通过官方 GitHub Release 对应的 winget 包从 2.3.2 更新到 2.5.2，安装程序哈希验证通过。原配置生成出的基础模式是 `global`，这会让系统代理或 TUN 接管的全部流量进入同一个策略，是本次最明确的额外流量风险。`config.yaml`、`clash-verge.yaml` 和校验配置现已统一改为 `rule`，Mihomo 配置检查通过。

Verge 中原有两个远程订阅均已过期或返回 404，不能继续把它们当成可更新来源。本次没有编造订阅，而是把当前仍可用的 CFW iKuuu 订阅地址和本地配置缓存同步到 Verge，并将其设为活动配置。仓库不保存订阅地址。为避免与正在运行的 iKuuu 和 Codex 链路争抢系统代理或 TUN，本次没有启动 Verge 接管网络；实际启用时仍需在安全窗口核对运行态。

### 切换 VPN 的固定边界

- 同一时间只让一个客户端接管 Windows 系统代理或 TUN；另一个客户端可以保留安装，但不要同时接管。
- 每次切换后确认旧端口没有残留在 Windows 用户代理中，再测试 GitHub 网页、API、SSH 和一个国内站点。
- 国内站点要通过 Clash 的连接详情或控制器确认最终策略为 `DIRECT`，不能只根据“请求经过 127.0.0.1”判断流量被代理。
- 配置文件写入成功不代表运行内核已经加载；重载或启动只能放在没有活动 Codex 会话的维护窗口，并在之后验证真实规则命中。
- 本机备份位于 GitHub 仓库之外，包含本地配置和订阅信息，不得提交到仓库或发送到聊天中。

*文件最后整理：2026-09-07；运行状态最后核验：2026-09-07*

# 2026-08-15 上游核验与 AI 执行安全整合

## 背景

本轮重新核验 OpenCut 主项目，以及 OpenMontage、FableCut、Palmier Pro 三个 AI 剪辑项目。目标不是拼接界面或复制受限代码，而是判断哪些工程设计已经真实存在、能够商业化落地，并以干净实现吸收到言剪 AI。

## 上游判断

### OpenCut

- 最新稳定 release 仍为 `v0.3.0`（2026-04-15），言剪 AI 当前基线没有落后于新的稳定版。
- `main` 相比 `v0.3.0` 已有大量提交，但官方明确说明正在从头重写；Web 改为 Vite + TanStack，桌面端仍处于非常早期阶段，编辑器路由尚未形成可替换的稳定产品。
- 当前决定：继续锁定 `v0.3.0`，不把重写中的 `main` 合入比赛版本。以后只在官方发布新稳定 tag 后建立临时升级分支验证。

来源：

- <https://github.com/OpenCut-app/OpenCut>
- <https://github.com/OpenCut-app/OpenCut/releases/tag/v0.3.0>
- <https://github.com/OpenCut-app/OpenCut/blob/main/README.md>
- <https://github.com/OpenCut-app/OpenCut/blob/main/apps/desktop/README.md>

### OpenMontage

- 项目持续更新提供商、模型和工具，但没有 release 和正式 milestone；公开的未来方向主要是 issue/RFC，不能当作交付承诺。
- 仍存在 Windows 渲染、黑屏、工具能力误报和静默回退等未解决问题。
- License 为 AGPL-3.0，不复制代码。吸收其“能力/提供商注册表”思想，但必须把可用、待配置和待集成状态真实展示给用户，禁止静默降级。

来源：<https://github.com/calesthio/OpenMontage>

### FableCut

- 最新 release 为 `v1.6.0`；近期新增 Claude Code 插件形态，并把应用目录与数据目录分离，说明项目不是纯展示壳。
- 自动字幕、WebCodecs 导出、OTIO 和更多 agent 能力目前仍是 issue，不是已完成路线图；测试覆盖和单文件架构仍不足以直接作为商业底座。
- License 为 MIT。吸收其“基于项目版本生成局部编辑计划”的乐观并发思想，防止旧计划修改已变化的时间线。

来源：

- <https://github.com/ronak-create/FableCut>
- <https://github.com/ronak-create/FableCut/issues>

### Palmier Pro

- 最新 release 为 `v0.7.4`（2026-08-12），近期真实更新包括时间线标记、关键帧轨道、有限长度 mutation receipt 和导出修复。
- 项目仅支持 macOS/Swift；AI 生成服务是闭源付费部分。公开 issue 不是正式 roadmap。
- License 为 GPL-3.0，不复制代码。吸收其“有界执行回执 + 可撤销 agent mutation”思想。

来源：

- <https://github.com/palmier-io/palmier-pro>
- <https://github.com/palmier-io/palmier-pro/releases/tag/v0.7.4>
- <https://github.com/palmier-io/palmier-pro/blob/main/FAQ.md>

## 已整合到言剪 AI

1. 能力预检：每个 AI 计划展示所需能力、提供商和真实状态。OpenCut 本地时间线标为可执行；未完成的转写、停顿检测、声音回写和未配置渲染服务明确标为待接入或待配置。
2. 项目版本锁：AI 请求携带由项目、场景、画布、轨道和元素关键字段生成的轻量项目指纹；执行前再次计算，旧计划遇到新时间线会被拒绝。
3. 有界执行回执：记录计划 ID、前后版本、成功/跳过/待服务/回滚数量和最多 20 个受影响元素 ID，避免回执无限膨胀。
4. 失败回滚：本地可撤销命令执行中出现错误时，自动撤销本轮已经应用的本地修改；远程服务不会被伪装成可回滚本地命令。
5. 紧凑上下文：只向规划器提供选择数量、轨道数量、元素数量、时长、画幅和项目指纹，不上传完整时间线或素材内容。

## 验证结果

- Next.js 生产构建通过。
- 言剪 AI 规划器新增回归测试 5 项，全部通过。
- 浏览器实测：中文首页、创作台、真实剪辑器正常；竖屏计划执行后生成版本回执；再次执行旧计划被拒绝；测试修改已通过撤销恢复。
- `127.0.0.1:3417` 原有两个进程同时监听，导致浏览器命中旧生产版本。本轮已清理冲突并让当前开发服务独占该地址。

## 后续边界

- 不因 OpenCut `main` 提交活跃就提前升级；只跟随稳定 release。
- 不把三项目的 issue 写成言剪 AI 已完成能力。
- AGPL/GPL 项目只作设计与行为参考，不复制源码；MIT 项目也优先采用独立实现，保留清晰来源记录。
- 下一阶段优先补齐转写、停顿检测和声音音频回写中的一个真实闭环，再扩充 AI 命令数量。

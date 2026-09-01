# 言剪 AI 架构与上游兼容策略

> 当前适用：OpenCut v0.3.0 基线；核验日期 2026-09-01。

## 一、分层结构

```text
用户界面
  首页 / 创作台 / 素材库 / 模板 / 项目 / 声音库 / 任务 / 帮助 / 价格
      ↓
言剪 AI 产品层
  中英双语 / AI 对话 / 计划确认 / 个人声音选择 / 粗剪 / 精剪 / 画面包装 / 交付
      ↓
能力适配层
  OpenCut 编辑命令 / Voice provider / Remotion / HyperFrames provider
      ↓
基础设施
  浏览器本地项目 / 模型 API / 声音 API / 独立渲染服务（后两者生产方案待定）
```

## 二、与 OpenCut 的边界

### 尽量复用

- 素材导入、项目数据、画布预览、多轨时间线、属性调整和导出骨架。
- OpenCut 修复的浏览器兼容、媒体处理和编辑器稳定性改进。

### 言剪 AI 自有

- `features/yancut/` 下的品牌、双语、AI 四阶段计划、声音库、包装 provider 和 OpenCut 命令适配。
- `/studio` 产品壳及业务页面。
- `/api/yancut/*` 服务接口。
- `packages/yancut-remotion` 包装模板。

### 兼容原则

1. 不直接重写 OpenCut 核心数据结构；通过适配层调用编辑器能力。
2. 新功能优先放在 YanCut 命名空间，降低上游升级冲突。
3. 修改上游共享文件时保持改动小而明确；每次升级先对比 release 与 changelog。
4. 锁定上游 tag 和 commit，不直接追随不稳定开发分支。
5. 升级顺序：建立临时升级分支 → 合并新 tag → 解决共享文件冲突 → 运行构建、AI 测试、编辑器冒烟测试 → 写修订记录。

## 三、AI 规划与安全

- 模型只返回受 Zod Schema 约束的命令，不允许执行任意代码。
- 不允许模型构造“删除全部元素”命令。
- 缺少声音、标题或其他必要选择时使用 `request_input`，不能擅自编造。
- 模型输出先展示计划，用户确认后再执行。
- 模型不可用或未配置时使用本地规划器，保证演示不完全依赖外网。
- 每份计划绑定项目内容指纹；执行时项目已变化则拒绝旧计划。
- 执行前显示能力预检，不允许把未接入或未配置的服务静默伪装为可用。
- 执行后生成有限长度回执；本地命令中途失败时撤销本轮已应用修改。
- AI 上下文中的播放头和项目时长统一使用秒，写入 OpenCut 时间线时再转换为 ticks。
- 当前可本地执行的专业命令包括：剪气口、生成字幕、倍速与保持音调、淡入淡出关键帧、文字安全区、画幅、音量和可编辑动效包装。
- 新增专业命令包括：真实转场、前景人声驱动 ducking、响度/波形分析、低分辨率预览代理、分段速度曲线和音频/字幕证据驱动的高光切片。

测试环境变量：

- `YANCUT_LLM_BASE_URL`
- `YANCUT_LLM_API_KEY`
- `YANCUT_LLM_MODEL`
- `YANCUT_LLM_REASONING_EFFORT`

任何真实 Key 只进入本地忽略文件或部署平台密钥，不进入 Git。

## 四、声音库与视频包装

- 声音对象同时保存本地展示信息和供应商 voice ID；模型只能使用用户当前明确选择的 voice ID。
- 声音克隆必须增加授权确认、用途说明、删除能力和供应商数据政策提示。
- Remotion 适合 React 组件化、参数稳定的视频包装，当前作为主实现。其 8 类动效语言由 AI 选择，并映射成 OpenCut 中可继续编辑的文字轨、标签和关键帧；用户不再进入独立包装中心。
- Player 预览、CLI 渲染、MP4 下载和任务状态实现仍作为底层渲染能力保留，后续由 AI 计划或统一导出流程调用，不作为与剪辑流程割裂的产品模块。
- 本地渲染通过子进程隔离 Remotion CLI，避免将 bundler/renderer 直接打入 Next.js 路由；生产环境仍需独立渲染服务和任务队列。
- Remotion 队列接口统一返回 `queued/running/completed/failed`、进度、输出地址和可选 `statusUrl`；本地开发使用异步内存队列，云端通过 `YANCUT_REMOTION_RENDER_URL` 切换到外部 worker，前端只依赖轮询合同。
- HyperFrames 适合 HTML/CSS/GSAP 组合方向，但生产调用方式、版本与服务端渲染能力必须重新核验；当前只保留 provider 接口，不声称已经生产可用。

## 五、Recut 参考边界

- 可借鉴：应用/能力/操作模型、稳定素材 ID、任务状态、确认后执行、本地优先与统一操作接口。
- 不直接并入：受其个人非商业许可约束的源码。商业或团队使用需单独授权。
- 对外材料只描述言剪 AI 已实现的产品能力，不写内部来源讨论；许可判断保留在研发记录中。

## 六、Shotcut / MLT 参考边界

- 成熟度判断：Shotcut 是持续维护的跨平台桌面剪辑器，具备多轨、波形、关键帧、字幕、代理、变速、转场、滤镜、批量导出和 MLT XML 等成熟能力，不属于引流空壳。
- 可吸收：专业剪辑任务模型、素材箱与智能分类、轨道和关键帧交互、代理与预览缩放、音频分析、转场/滤镜预设、任务队列和 MLT 的 producer/filter/transition/consumer 分层。
- 当前不直接合并 Shotcut UI/源码：其运行时是 Qt 6 + C++ + MLT/FFmpeg 的桌面架构，与 Next.js 浏览器架构不兼容；仓库为 GPLv3，直接链接或分发修改版会产生明确的许可证义务。
- 可选未来路径：把 MLT 作为独立、可替换的后台渲染工作进程，通过任务合同和 MLT XML/OpenTimelineIO 与网页端交换；是否采用必须先完成部署和许可证评审。
- 相关官方来源：<https://github.com/mltframework/shotcut>、<https://shotcut.org/features/>、<https://shotcut.org/roadmap/>、<https://www.mltframework.org/docs/>。

## 七、Concat 参考边界

- 成熟度判断：Concat 有 React/Tauri/Rust/FFmpeg 真实源码、安装包、持续构建和编辑器测试，不是引流空壳；但项目创建时间短、单一主要贡献者、只有 alpha 预发布，仍属于高活跃工程原型。
- 可吸收：稳定 ID、引擎拥有项目真相、串行命令、一次手势一个撤销步骤、延迟自动保存、临时文件原子替换、模板素材槽位和任务状态。
- 当前不直接合并源码：其 Tauri/Rust 桌面运行时与 Next.js 浏览器架构不兼容；MPL-2.0 文件级 copyleft 及第三方 GPL 依赖需要明确的分发评审。
- 本轮已落地：真实模板槽位和实例化验证、半成品项目回滚、AI 计划串行队列；同时修复 ducking 的 ticks/秒单位错误。
- 相关来源：<https://github.com/jub0t/Concat>、<https://github.com/jub0t/Concat/blob/main/ARCHITECTURE.md>、<https://github.com/jub0t/Concat/releases>、<https://github.com/jub0t/Concat/issues>。

## 八、版本与来源

| 动态事实 | 当前记录 | 来源 | 核验日期 |
|---|---|---|---|
| OpenCut 基线 | v0.3.0 / `f4bd689...` | OpenCut release 与本地 Git | 2026-08-13 |
| OpenCut 最新稳定版 | 仍为 v0.3.0；`main` 正在重写，不作为升级基线 | OpenCut README、release 与 desktop README | 2026-08-15 |
| OpenCut License | MIT | 上游 `LICENSE` | 2026-08-13 |
| 测试中转接口 | OpenAI 兼容 `/v1/chat/completions` | <https://api.shuaiapi.com/llms-full.txt> 与实测 | 2026-08-13 |
| 测试模型 | `gpt-5.6-sol`，reasoning `high` | 用户指定与实测 | 2026-08-13 |
| Recut 参考版本 | 0.1.41；只参考公开架构与交互经验 | Recut 仓库、架构与 LICENSE | 2026-08-31 |
| Remotion 本地版本 | 4.0.506；本地渲染闭环已验证 | 本地依赖与实测 | 2026-08-31 |
| Shotcut 参考状态 | 26.8 系列；GPLv3；Qt 6/C++，依赖 MLT、FFmpeg、Frei0r、SDL | Shotcut GitHub、Features、Roadmap | 2026-08-31 |
| Concat 参考状态 | `v0.2.0-alpha.16`；MPL-2.0；React/Tauri/Rust/FFmpeg；真实但仍是单人主导 alpha | Concat GitHub、Architecture、Releases、Issues、License | 2026-09-01 |
| 言剪 AI 源码仓库 | 私有 `MouMou-Eleven/yancut-ai`；本地 `main` 提交 `e4f2eb2`；远端提交 `7e4e816`；`upstream` 保留 OpenCut | GitHub API、Git Data API、Git 远端核验 | 2026-09-01 |

这些动态事实后续使用前必须重新核验，不能把本表永久当作当前真相。

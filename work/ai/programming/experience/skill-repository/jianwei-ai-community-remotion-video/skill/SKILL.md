---
name: jianwei-ai-community-remotion-video
description: 将任意一句话、脚本、数据、参考图或图文混合需求，导演化为稳定、可读、有记忆点的 Remotion React 动画。自动识别内容结构、画面层级、动效语法和输出比例，生成参数化 Composition，并通过确定性布局、帧驱动运动、参考图保真与跨帧验收适配不同类型输入。专用于 Remotion 视频与动效制作。
metadata:
  short-description: 通用自适应 Remotion 动画导演与实现 Skill
---

# 建委 AI 社群视频制作 Skill

这是一个通用的 Remotion 动画系统，不是某个案例的补丁集合。每次任务都先把输入归一化成“内容事实、视觉对象、空间关系、时间目标、可编辑字段和风险”，再选择适合的导演模式与实现模型。

## 适用范围

支持标题卡、海报动效、产品界面、数据图表、排行榜、流程、字幕、人物/物体、脚本分镜、图片转视频和图文混合输入。Remotion 是唯一实现基座；使用 React Composition、`useCurrentFrame()`、`useVideoConfig()`、`interpolate()`/`spring()`、Zod Props 和官方媒体组件。不要把 HyperFrames 或其他视频框架作为前置依赖。

## 自适应核心

1. **输入归一化**：区分用户明确事实、参考图观察、待验证内容和低风险默认值；读取图片尺寸、文字、主体、背景、层级、对齐、留白和可动对象。
2. **结构识别**：将任务归入一个主模式：`target-frame`（参考图还原）、`concept`（抽象观点）、`process`（流程/因果）、`data`（数字/比较）、`script`（多场景脚本）或 `raster-motion`（整图平面运动）。模式只决定策略，不改变通用质量门槛。
3. **导演决策**：确定唯一核心视觉、状态反差、记忆点、主动作因果、相机动机、收尾状态和稳定阅读区。默认只给一个最强方向；效果来自动作逻辑、层级和节奏，不来自装饰堆叠。
4. **自适应空间**：默认 2D；需要遮挡、视差或深度时用 2.5D；只有真实几何/灯光/绕行明显提升表达时用 3D。任何空间模型都必须回到目标构图。
5. **自适应布局**：所有文字、数字、Logo、图标和数据列先建立设计坐标、保护垫、最长值预算和唯一视觉所有者，再建立动画。使用稳定字体指标、tabular figures、固定锚点和整数像素；内容变化不能引起 sibling 挤压、基线跳动或亚像素漂移。
6. **自适应运动**：每个关键对象使用“驱动—预备—主动作—响应—回收—定格”链；共享归一化进度，明确 clamp 和缓动。禁止 CSS 动画、实时钟、未播种随机数、每帧测量布局和无目的镜头抖动。
7. **自适应保真**：参考图默认是最终目标帧。只重建需要独立运动/编辑的对象；未授权的文案、品牌、比例、背景色域、留白和对齐不改变。整图参考素材只用于分析/对比，不能作为片尾覆盖层。
8. **自适应验收**：按任务模式生成代表帧、可见性报告、布局稳定报告、最终帧对比和稳定区连续性报告；任何文字裁剪、数字漂移、背景漂色、重复视觉所有者或最后一秒换图都属于硬失败。

## 交付流程

- 只要方案：输出 Director Brief / Motion Blueprint，不写代码。
- 要制作：`规划确认 → 实现与检查 → 完整低清预览 → 用户确认 → 最终渲染`。用户明确要求直接执行时才跳过对应确认门。
- 默认交付参数化工程；MP4 是参数快照，编辑能力来自工程的 Zod Schema、Default Props 和绑定元素。
- 先加载 Remotion 官方 best practices，再按任务读取 `references/` 中相关契约；不要默认读取全部长文档。

## 参考资料路由

- 导演和创意：`director-strategy.md`、`motion-direction.md`、`remotion-only-director-contract.md`、`director-console-contract.md`
- 参考图与背景：`reference-fidelity-contract.md`、`background-fidelity-contract.md`、`input-and-image-analysis.md`
- 布局与可见性：`deterministic-layout-contract.md`、`visibility-and-clipping-contract.md`、`parameterization-contract.md`
- 实现、输出和验收：`remotion-contract.md`、`output-contract.md`、`quality-gates.md`、`render-performance-contract.md`；文字抗抖必须附 `check_layout_stability.py` 证据
- JSON 自动化：`motion-blueprint.schema.json`、`internal-production-brief.schema.json`及对应校验脚本

## 规划输出最低要求

画面理解、核心视觉、保留/修改/新增清单、空间模型、动作因果、相机路径、逐元素动作表、时间轴、图层与参数化字段、完整可见计划、负面约束、渲染流程和验收证据。参考图任务额外登记原图尺寸、关键边界框、背景采样和最终帧规则。

## 实现硬约束

动画全部由帧驱动；所有 `interpolate()` 有 clamp；稳定区相机回到恒等状态；受保护内容位于画布和裁剪祖先内；数字/列通过 `check_layout_stability.py`；参考图通过 `compare_reference_frame.py`、`audit_reference_render_path.py` 和 `check_settle_continuity.py`；运行项目已有类型检查、Lint 或测试，并查看开场、主动作峰值、稳定区和最终帧。

# Remotion 实施契约

本文件只保留跨版本相对稳定的实施原则。当前官方 Remotion Skill 与官方文档始终优先。

## 实施前路由

1. 创建视频或 Composition：加载 `remotion-create`。
2. 编写 React Markup、媒体、动效、文字、3D 或时间轴：加载 `remotion-markup`。
3. 需要 Studio 可选、可拖、可改关键帧：加载 `remotion-interactivity`。
4. 打开预览：加载 `remotion-studio`。
5. 用户明确要求导出或渲染：加载 `remotion-render`。
6. API、组件 Props、包名或版本不确定：加载 `remotion-docs` 查当前官方资料。

## 逐帧确定性

- 所有动画依赖 `useCurrentFrame()` 与 `useVideoConfig()`。
- 用秒构思，用 `秒 × fps` 写入时间点。
- `interpolate()` 明确输入范围、输出范围、左右 clamp 与 easing。
- 缩放按当前官方规则使用 perceptual scale 选项。
- 不使用 CSS 动画、CSS 过渡、Tailwind 动画类、`setTimeout`、实时钟或未播种随机数。

## 时间结构

- 用命名的 Sequence、Series 或 TransitionSeries 表达延迟、持续、重叠和转场。
- 多场景拆分为独立组件；复杂镜头也按职责拆出相机、背景、主体、文字和声音层。
- 注意转场重叠会改变总时长；按当前 timing API 计算，不凭场景时长简单相加。
- 需要预挂载的层按当前官方规则设置 premount。

## 素材

- 本地素材放在 `public/`，通过 `staticFile()` 引用。
- 图像、视频、音频、动画图片和 Canvas 图像使用当前 `remotion-markup` 推荐组件。
- 目标仓库旧规则曾要求所有静态图片一律使用 `<Img>`；当前官方 Skill 已提供 `<CanvasImage>`、`<AnimatedImage>` 等更细的选择。不要复制旧结论，实施时查当前规则。
- 对远程素材检查可访问性、CORS、稳定性和渲染时加载行为。

## Studio 可编辑性

- 可编辑 HTML/SVG 元素使用当前官方 `Interactive` 结构并命名。
- 文字只使用一次且固定时，按官方规则保持内联；动态或复用文字放入 Props。
- 可编辑样式和关键帧尽量内联；优先使用独立的 `scale`、`translate`、`rotate` 属性。
- Composition 的静态尺寸、fps、时长和默认 Props 按当前官方建议保持可识别结构；只有动态字段进入 `calculateMetadata()`。

## 3D

- 使用 `@remotion/three` 与明确 width/height 的 ThreeCanvas，并配置足够的灯光。
- 相机、物体、材质、粒子和着色器只由当前帧驱动；禁止 `useFrame()` 自主播放。
- ThreeCanvas 内的 Sequence 使用当前官方要求的 `layout="none"`。
- 3D 只解决真实空间问题；文字与界面通常保留在可编辑的 2D 层。

## 效果

- 普通 CSS/SVG 能完成时不引入 shader。
- 使用 Canvas/WebGL effect 前加载当前 effects 文档，确认包、导入路径、渲染 OpenGL 配置和可编辑参数。
- 每个效果都要服务焦点、速度或转场，不能仅用于填满画面。

## 参数化

- 用 Props 和 Zod 暴露用户可能修改的标题、颜色、素材、时长、动效强度和开关。
- 不固定沿用旧仓库写死的 Zod 或 Remotion 版本；通过项目锁文件和当前官方规则决定安装方式。

## 预览与渲染

- Codex 环境优先使用 `npx remotion studio --no-open`。
- 可用低分辨率 still 检查构图和关键帧，但它不能替代完整时间轴预览。
- 用户未明确要求渲染时不执行 `npx remotion render`。
- 渲染后核验输出文件存在、编码规格、时长、尺寸和警告，再报告完成。

## 来源与冲突策略

- Remotion 官方 Agent Skills：<https://github.com/remotion-dev/remotion/tree/main/packages/skills>
- Remotion 官方文档：<https://www.remotion.dev/docs>
- 用户指定的中文汇总仓库：<https://github.com/buainoai/remotion-skills>

中文仓库适合了解旧版规则分类和稳定概念，但当它与当前官方 Skill 冲突时，以当前官方 Skill 和当前项目版本为准。

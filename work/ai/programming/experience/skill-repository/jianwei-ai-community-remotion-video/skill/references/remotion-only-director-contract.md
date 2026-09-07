# Remotion-only director contract

本 Skill 的执行目标是 Remotion React composition。HyperFrames 不属于本项目依赖、规范或验收链路，不应作为实现前置条件。

保留旧版 `motion-director` 的有效原则：一句话也能启动导演分析；默认只给一个最强方向；参考图是目标最终帧；先规划后执行；用视觉隐喻、状态反差和单一记忆点提升效果；动效优先于装饰；2D/2.5D 优先，只有深度真正有表达价值时才使用 3D。

Remotion 实现必须以当前项目依赖和 Remotion 官方文档为准：帧驱动 `useCurrentFrame()`、`useVideoConfig()`、`interpolate()`/`spring()`，明确 Composition 尺寸和时长，参数化通过 Zod 与 Default Props，素材通过 Remotion 媒体组件加载。Remotion 官方定位是用 React 程序化创建视频和动效，代码是事实来源；因此“导演稿”必须最终落成可检查的 Composition、Props、代表帧和渲染产物。

旧版规则是创意与流程基线，不覆盖当前项目新增的保真、可见性、确定性和性能门槛。

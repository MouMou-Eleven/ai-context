# Remotion Skill 修订：数字与高密度布局确定性

日期：2026-09-05

## 问题

最新参考图视频中排名数字出现大小和位置抖动，整体还原度也不稳定。上一轮已覆盖参考图保真、裁剪和终帧连续性，但没有把数字字体指标、列宽、基线和亚像素定位作为独立硬门槛。

## 原因判断

常见触发链是：数字位数变化或字体回退改变墨迹宽度；自适应 flex/sibling 重新分配列位置；父级 scale/translate 产生亚像素栅格；计数或 spring 在 settle 段仍有 overshoot。单看最终帧无法发现这些跨帧问题。

## 本次调整

- 新增 `deterministic-layout-contract.md`：tabular figures、固定最长值宽度、整数像素锚点、单一视觉所有者、settle 段冻结。
- 新增 `check_layout_stability.py`：检查数字/列的跨帧 x/y/width/height 漂移和宽度变化。
- 在 SKILL.md 和 quality-gates.md 中把数字抖动列为硬失败，并要求代表帧跨帧验证。
- 同步本地安装版 skill；不改变旧版动画的创意方向，只收紧实现和验收约束。

## 通用性边界

这些规则适用于排行榜、数据卡片、仪表盘、字幕、价格、日期、计数器等所有数字或高信息密度布局；它们不会把某个排行榜案例写死为模板。对于确实需要数字滚动的场景，只允许内容值变化，几何锚点仍保持稳定。

## 方向校正

本项目明确以 Remotion 为唯一动画实现基座。旧版 motion-director 的创意与流程原则被吸收；HyperFrames 不再作为前置依赖。Remotion 官方说明其使用 React 程序化创建视频和动效，代码是事实来源（https://www.remotion.dev/）。

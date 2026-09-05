# Deterministic layout contract

动态数据、数字和高信息密度 UI 默认采用 `layout-locked` 几何。动画可以改变视觉状态，但不能让内容宽度、列锚点或基线随帧重新计算。

## 数字与列

- 数字使用等宽数字：优先 CSS `font-variant-numeric: tabular-nums lining-nums`，必要时使用明确支持 tabular figures 的字体；禁止在动画中切换字体、字重或字号。
- 为排名、分数、百分比、日期等字段预留固定宽度；按允许的最长值计算，不按当前值 shrink-to-fit。短值用左/右对齐规则固定在同一锚点。
- 文本、数字和条形图分别拥有稳定的 x/y 锚点；不要把数字放在会因 sibling 宽度变化而移动的 flex 自适应流中。
- 计算位置时先把设计坐标转换为整数像素（`Math.round`），同一元素的 `left/top/width/height` 在稳定区保持完全相同；禁止用未取整的小数 transform 造成亚像素抖动。
- 排名变化只改变字段内容或明确的数值插值，不改变列宽、基线、容器尺寸和其他行的位置。若数字位数变化，使用预留宽度、前导零或固定对齐策略。

## 动画与稳定区

- 任何数字滚动、计数或条形增长都必须由帧驱动、可复现，并在结束前进入明确的 settle 段；settle 段至少 8 帧，连续帧的布局框差值为 0。
- 数字不能跟随整体相机的 scale/rotate/translate 运动进入稳定区。相机回到恒等矩阵后，再检查数字墨迹框。
- 禁止对数字使用 spring 的未约束 overshoot、随机抖动、每帧重新测量文本宽度或基于 `toLocaleString` 的字体/分隔符变化。
- 同一字段只能有一个视觉所有者；禁止用第二个数字层交叉淡化来修正错位。

## 验证

导出代表帧或浏览器测量报告，至少包含动作峰值、settle 开始、settle 中间和最终帧。对每个数字/列记录 `x, y, width, height, baseline`，运行：

```bash
python scripts/check_layout_stability.py layout-samples.json --max-drift 0.25 --settle-from 3
```

若稳定区仍有漂移、宽度变化或字体指标变化，先修正布局和字体，再考虑任何装饰效果。

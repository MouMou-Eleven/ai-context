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

## 文字抗抖动

- 文字的 `left/top/width/height`, `font-size`, `line-height`, `letter-spacing`, `font-weight` 和 `transform-origin` 在一个动作阶段内保持固定；只让明确的运动属性按帧变化。
- 文字入场可以使用整体 `translate3d`、`rotateX/Y` 或揭示进度，但必须在进入阅读区前完成亚像素运动，稳定区对齐到整数像素；不要让每个字独立使用不同的 spring 或持续旋转。
- 同一文字层只允许一个主 transform 计算源。禁止父层和子层分别叠加未协调的 translate/scale/rotate，禁止同时用相机抖动和字层抖动表达同一个冲击。
- 使用 `translate3d` 时将设计坐标量化到整数像素；禁止 `translate(0.5px)`、逐字随机 offset、字体大小在相邻帧切换和每帧重新测量导致的版面跳变。
- 文字的 `opacity`、亮度或扫光可以变化，但不会改变实际边界框；强调效果在稳定区前归零，避免视觉重影被误判为文字抖动。
- 字体必须在渲染前加载并固定，禁止先用回退字体排版后再切换到目标字体；参数化改字使用预留容器和确定性的 auto-fit/换行策略。

## 验证

导出代表帧或浏览器测量报告，至少包含动作峰值、settle 开始、settle 中间和最终帧。对每个数字/列记录 `x, y, width, height, baseline`，运行：

```bash
python scripts/check_layout_stability.py layout-samples.json --max-drift 0.25 --settle-from 3
```

若稳定区仍有漂移、宽度变化或字体指标变化，先修正布局和字体，再考虑任何装饰效果。

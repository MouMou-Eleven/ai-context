# Remotion 参考图几何锁定与连续性审计

## 背景

2026-09-05 对 `C:\Users\Administrator\jianwei-part-cover` 的实测发现，上一版虽然能让最终静帧接近参考图，却在最后 135–143 帧通过 `FinalFrameLock` 将 `reference-frame.png` 整图 opacity 淡入。结果是前段布局与目标不一致，片尾出现双重文字、播放图标遮挡和突然换场；单一的最终帧像素比较无法识别这个问题。

## 新口径

- 图片任务默认模式从“终端参考图混合”改为 `layout-locked`。
- 参考图是整段动画的几何目标和事实来源，只能用于分析、校准和离线比较，不能在生产 Composition 中作为整图图层或片尾覆盖层。
- 每个可动/可编辑元素必须登记唯一视觉所有者、归一化目标边界框和最终状态；同一组件从动作阶段连续抵达该目标，不允许“前面重排、最后换图”。
- 用户若只想对整张图做推拉、旋转或视差，显式选择 `raster-motion`，从第一帧到最后一帧只保留同一个图片平面；不能再叠第二个参考层。
- 若无法可靠分离背景、保持排版和提供编辑能力，规划阶段必须诚实说明取舍并让用户选择，不得用整图渐显伪造像素级可编辑。

## 可执行变更

1. `motion-blueprint.schema.json` 与 `validate_blueprint.py` 新增并强制 `renderPolicy`、`terminalOverlay: false`、`targetLayoutLocked: true`、`visualOwners`、`finalHoldFrames`；模式改为 `layout-locked`、`raster-motion`、`approved-redesign`。
2. 新增 `scripts/audit_reference_render_path.py`，扫描生产 `src/` 中的参考图文件名、`FinalFrameLock`、`referenceOverlay`、`lockFinalFrame` 等信号；命中即失败。
3. 新增 `scripts/check_settle_continuity.py`，比较最终稳定区开始/中间/结束的至少三张静帧，拦截全画布跳变和片尾场景替换。
4. 质量门槛与渲染性能契约同步禁止整图终端覆盖，并要求先完成源码审计和连续性审计，再做最终帧像素对比。

## 影响

这是一项正向加固：不会删减已批准的主动作、镜头或参数化能力，而是移除会制造重影和错位的错误实现出口。默认仍是可在 Studio `Inspector → Default Props` 编辑文字、编号和颜色的参数化工程，仍先低清预览、后经用户确认全量渲染。

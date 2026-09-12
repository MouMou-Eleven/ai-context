# AI 执行进度、Remotion 本地接入与关键帧工作流

> 修订日期：2026-09-04

## 本轮结论

言剪 AI 的 AI 剪辑计划执行从“等待后一次性回执”升级为可观察的串行执行：计划面板和底部时间线同时显示当前步骤、完成数量、消息和失败状态。Remotion 在本地开发模式下被视为可执行能力，未配置远程服务时进入本地异步队列；HyperFrames 以可编辑动效配方接入 AI 时间线，而不是单独的孤立页面。

## 已落地能力

- `executeAiPlan` 为每个命令发出 `running`、结果状态和最终 `completed/failed` 事件；AI 面板显示步骤进度条，时间线右下角显示 AI 正在执行的动作。
- Remotion 能力预检在开发模式默认识别本地渲染，`YANCUT_REMOTION_LOCAL_ENABLED=false` 可显式关闭；生产环境仍要求远程渲染地址，避免把本地能力误当成云端服务。
- Remotion 包装命令继续映射为可编辑标题、标签和关键帧；HyperFrames 模板通过 `hyperframes-workflow.ts` 提供稳定的动效配方、阶段时序和可编辑参数，后续可替换为实际 HTML/CSS/GSAP 渲染器。
- 时间线工具栏新增“添加关键帧”：对已选视觉元素写入位置、缩放、旋转、透明度关键帧，对音频元素写入音量关键帧，使用现有命令历史可撤销。
- `getElementsAtTime` 对结束帧采用包含边界的判断，解决效果或元素到达结束位置后无法点击、预览或继续编辑的问题。
- 修复多选属性提示、预览上下文菜单、音频提示、素材替换提示等英文残留；中文面板不再显示 `elements selected.0` 或 `Click on an element...`。
- 参考 [OpenDesign](https://github.com/nexu-io/open-design) 的本地优先、可组合产物和“brief→artifact→preview→delivery”工作流，将 AI 计划作为可检查产物，并把执行状态反馈到编辑器主链路。

## 验证证据

- TypeScript：`tsc --noEmit -p apps/web/tsconfig.json` 通过。
- 本地规划器：8 个测试通过。
- Next.js：生产构建通过，37 条路由成功生成。
- 本地开发服务：`/studio` 返回 HTTP 200；未登录调用 `/api/yancut/ai/plan` 返回 HTTP 200，模型规划返回可执行命令；Remotion 包装计划的预检状态为 `ready`，理由为本机可直接渲染。
- 源码仓库已同步提交：本地提交 `c10df52`，远端提交 `300ef650a01a0838f64c0e311671239eb8e7a17e`。

## 边界与后续

- 本轮的 HyperFrames 是可编辑配方桥接，生产级云端渲染仍需配置队列地址、对象存储回写、并发限制和成本监控。
- Remotion 本地渲染依赖 Node/Chromium 环境；部署到秒嗒前需要按平台能力重新接线，并继续保留明确的远程队列失败与退款路径。
- AI 执行可视化已经真实接入，但复杂多轨工程、超长视频和大量素材仍需在目标部署环境做压力测试。

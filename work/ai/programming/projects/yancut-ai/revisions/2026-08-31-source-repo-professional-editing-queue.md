# 言剪 AI：自有源码仓库与专业剪辑能力落地

> 日期：2026-08-31
> 结论：源码主线已迁移到私有 `MouMou-Eleven/yancut-ai`；OpenCut 只保留为 `upstream` 跟踪源。专业剪辑能力通过网页端时间线命令实现，Remotion 通过统一队列合同接入。

## 一、自有源码仓库

- 本地路径：`F:\桌面文件\言剪AI`
- `origin`：`https://github.com/MouMou-Eleven/yancut-ai.git`
- `upstream`：`https://github.com/OpenCut-app/OpenCut.git`
- 本地主线：`main`，提交 `3db3ae4`
- GitHub 源码树：远端提交 `a001db3`
- 仓库可见性：私有

由于本机 Git 全局配置指向已停止的 `127.0.0.1:7890` 代理，HTTPS push 不可用；源码树已通过 GitHub Git Data API 写入并核验。GitHub 当前令牌不允许写入 Actions workflow，因此 `.github/workflows/bun-ci.yml` 未同步到远端，其他源码和资源已同步。

## 二、专业剪辑命令

### 真实转场

`apply_transition` 支持 `crossfade`、`dip-to-black` 和 `wipe-left`。实现方式是让相邻主视频片段产生可控重叠，再写入透明度/位移关键帧；黑场转场会在图形轨道插入黑色遮罩。所有修改通过 `TracksSnapshotCommand` 进入撤销历史。

### 音频 ducking

`duck_audio` 依据主视频和已标记人声元素的时间窗口，对背景音轨写入音量关键帧。起落时间和降低 dB 数可由 AI 计划指定，音量沿用现有 dB 语义，播放和导出都会读取自动化结果。

### 响度与波形

`analyze_audio` 复用时间线混音和 WAV 解码，按窗口输出 RMS、峰值、动态范围和波形数组，并给出 RMS-based LUFS 估计。它是浏览器内确定性编辑分析，不把未实现的广播级真峰值计量写成已完成能力。

### 代理预览

`generate_proxy` 使用浏览器 `MediaRecorder` 把视频绘制到低分辨率画布，生成 WebM 代理并挂到内存中的 `MediaAsset.proxyFile`。预览渲染器优先使用代理，音频和最终导出仍使用原始文件，刷新页面后代理需要重新生成。

### 速度曲线

`set_speed_curve` 把时间点/速率转换为分段曲线；视频渲染、音频重采样和播放调度都通过积分/反解得到源时间。保持音调时曲线走预渲染音频缓冲，避免把曲线误当成固定倍速。

### 长视频高光

`extract_highlights` 要求目标平台、单条时长和已导入素材证据。算法结合音频能量、字幕密度和主题词命中选择非重叠窗口，再用时间线快照压缩拼接。没有音频或字幕证据时返回跳过，不宣称已经完成语义理解。

## 三、Remotion 队列

- POST `/api/yancut/packaging/jobs` 返回带进度的 `queued` 任务。
- GET `/api/yancut/packaging/jobs/:job_id` 返回 `queued/running/completed/failed` 状态和输出地址。
- 未配置远端 URL 时，服务端异步调用本地 Remotion CLI，适合开发与演示。
- 配置 `YANCUT_REMOTION_RENDER_URL` 后，请求转发到云端 worker；worker 可在响应中返回 `id`、`status`、`progress`、`outputUrl` 和 `statusUrl`。
- 队列当前是 Node 进程内存存储；上线到秒哒或独立服务时必须替换为 Redis/Postgres 任务表，并补齐对象存储、重试、取消、并发和成本指标。

## 四、验证

- TypeScript 检查通过。
- Next.js 生产构建通过，生成 27/27 路由；包含 `/api/yancut/packaging/jobs/[job_id]`。
- 真实队列 smoke test：任务 `queued → running → completed`，返回 `/yancut/renders/a8122be0-53cf-4684-ba85-46025c4339f4.mp4`。
- 浏览器工作台与转场入口加载正常，控制台错误为 0。
- Bun 未安装，Bun 测试文件已加入源码但未在本机执行。

## 五、下一步

1. 把队列状态存储替换为 Redis/Postgres，并加入租约、取消和重试。
2. 让代理缓存可持久化，并补齐音画代理和预览切换按钮。
3. 加入广播交付需要的响度标准化、真峰值和 limiter。
4. 增加真实转场参数编辑、速度曲线 UI 和长视频语义模型评估。

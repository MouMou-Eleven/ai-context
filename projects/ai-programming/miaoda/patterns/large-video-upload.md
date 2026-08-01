# 大视频上传决策：新环境先实测，旧分片代理只兜底

> **当前状态：旧方案已被 2026-07-15 更新部分取代。** 秒哒已宣布取消“应用内 50MB 文件上传上限”，因此新项目不得默认套用永久分片架构；先做当前环境能力测试。本文后半部分保留 [pitfalls.md #14](../pitfalls.md) 在旧环境生产验证过的兼容实现。
>
> 旧环境兼容源码：[`../reference-materials/video-chunked-upload/`](../reference-materials/video-chunked-upload/README.md)；只有当前环境仍复现 CORS / 413 / supervisor kill 时才使用。

---

## 当前默认决策流程

1. 在当前应用、当前后端套餐和正式访问域名下，用一个无敏感内容的 200MB 测试视频上传。
2. 同时检查浏览器网络面板和后端日志：是否出现 CORS、413、函数超时/取消、对象大小不一致。
3. 上传成功后重新加载页面，确认对象仍存在，并测试 `<video>` 首播、拖动进度条和 Range 请求。
4. 如果平台原生上传全部通过，使用当前原生能力。为提高弱网可靠性，可以采用平台或云厂商原生 multipart / 断点续传，最终仍合成为一个正常对象；不使用本文件后半部分的“永久分片 + Range 代理”。
5. 只有测试仍出现旧环境三层墙，才启用兼容方案。

“取消 50MB 上限”与“无需分片”不是同一件事：前者是产品硬限制变化；后者是传输可靠性选择。200MB 文件即使能单次上传，移动网络下仍更适合可重试的 multipart，但应优先使用存储服务原生 multipart，而不是永久保存业务分片。

## 何时用 / 何时不用

| 场景 | 这个方案 |
|---|---|
| 2026-07-15 后已实测，当前环境上传大文件仍撞 CORS / 413 / supervisor kill | ✅ 用作兼容兜底 |
| 新应用尚未做 200MB 能力测试 | ❌ 先测试，不要直接套旧架构 |
| 平台原生上传或云厂商 multipart 已能稳定上传并得到完整对象 | ❌ 不用 |
| 单文件 < 30MB，Storage 直传不报错 | ❌ 不用，太重 |
| 自有 OSS / S3 + 服务端可调外网带宽与超时，不受 Supabase 限制 | ❌ 不用，直传 multipart 即可 |
| 文件需要**服务端再加工**（转码、抽帧、压缩） | ⚠️ 本方案返回的是分片伪装的 URL，不能给 ffmpeg 当输入。先合并到对象存储再加工。本方案只解决"播"。 |

---

## 架构总览

```
浏览器                                  Edge Function                Storage
  │                                          │                          │
  │── 1. 切 5MB ────┐                        │                          │
  │   (前端切片)                             │                          │
  │                                          │                          │
  │── POST /video-upload-chunk ──────────► [chunk] ── put ───────────► video-chunks/<id>/<idx>
  │   multipart: upload_id, chunk_index,     │   (5MB+128KB 容错)       │
  │              chunk                       │   uploaded_chunks++      │
  │                                          │                          │
  │   ... 重复 N 次 ...                      │                          │
  │                                          │                          │
  │── POST /video-upload-complete ─────────► [complete] ── list ─────► video-chunks/<id>/
  │   json: { upload_id }                    │   验证 0..N-1 全在       │
  │                                          │   status = 'completed'   │
  │  ◄── public_url: /video-serve?id=<id> ──│                          │
  │                                          │                          │
  │── <video src=public_url>                 │                          │
  │── GET /video-serve?id=<id>             [serve] ── signed urls ───► video-chunks/<id>/<i..j>
  │   Range: bytes=N-M                       │   流式拼接 + 切边        │
  │  ◄── 206 Partial Content ────────────────│                          │
  │      Content-Range: bytes N-M/total      │                          │
  │      Accept-Ranges: bytes                │                          │
```

**以下原则只适用于旧环境兼容方案**：
- 浏览器**永不**直打 Storage 端点（绕 CORS）
- Edge Function 单次操作**只读写一片**（绕资源上限）
- 永远**不写合并文件**（绕 storageFileSizeLimit）
- 视频 URL 永远是 `video-serve` 函数地址，**不是** Storage 公开 URL

---

## 数据库 / 桶配置

### 桶
- 名称：`video-chunks`
- 公开性：**私有**（chunk 通过 service role 读写，serve 通过签名 URL 读）
- 路径约定：`<upload_id>/<chunk_index>`，`upload_id` 是 UUID，`chunk_index` 从 0 起的整数
- 文件 contentType：`application/octet-stream`（不是 video/*，因为是分片不是完整视频）

### 表 `video_uploads`
本方案**消费**这个表，**不创建**。下面是从三个函数的 SQL 反推的最小字段集：

| 列名 | 类型 | 说明 |
|---|---|---|
| `id` | uuid PK | upload_id |
| `user_id` | uuid | 上传者，FK profiles.id |
| `chunk_count` | int | 总分片数 = ceil(total_size / 5MB) |
| `total_size` | bigint | 文件总字节数（**Range 算术依赖此字段精确**） |
| `mime_type` | text | 默认 `video/mp4` |
| `status` | text | `'uploading'` → `'completed'` |
| `uploaded_chunks` | int | 已上传分片数（chunk 函数递增） |
| `completed_at` | timestamptz | complete 函数填 |
| `storage_path` | text | 业务用，complete 函数原样回显 |

> **没有第四个 `init` 函数**：源码里只有 chunk / complete / serve 三个。`video_uploads` 行的创建在三个函数之外，由前端走 supabase-js insert 或调一个独立的初始化端点完成（前端切片前必须先拿到 `upload_id`、`chunk_count`、`total_size`）。

---

## 三个函数契约

### `video-upload-chunk` — 写一片到 Storage

| 项 | 值 |
|---|---|
| Method | `POST` |
| Auth | `Authorization: Bearer <user_jwt>`，且 `profiles.role==='admin'` 或 `is_super_admin===true` |
| Body | `multipart/form-data`，三个字段：`upload_id`, `chunk_index`（字符串整数）, `chunk`（File） |
| 单片上限 | `5 * 1024 * 1024 + 128 * 1024` 字节（5MB + 128KB 容错，超出 400） |
| 写入 | `video-chunks/<upload_id>/<chunk_index>`，`upsert: true`（**幂等关键**：重传同一片不报错） |
| 副作用 | `video_uploads.uploaded_chunks += 1`（非致命，失败也返回 200，因为 chunk 已落盘） |
| 200 返回 | `{ ok, chunk_index, uploaded_chunks, chunk_count }` |
| 409 | `status==='completed'` 时拒收新片 |
| 400 | `chunk_index >= chunk_count` 越界拒收 |

**为什么 5MB + 128KB**：5MB 是前后端约定的分片大小，128KB 容差吸收浏览器切 Blob 时的边界四舍五入（不留容差会偶发踩到一个字节超限）。

### `video-upload-complete` — 验证齐全 + 标记完成 + 给 URL

| 项 | 值 |
|---|---|
| Method | `POST` |
| Auth | 同 chunk |
| Body | `application/json`：`{ "upload_id": "..." }` |
| 流程 | 1) 读 session ⇒ 2) `storage.list("<upload_id>", {limit: chunk_count+10})` ⇒ 3) 检查 0..chunk_count-1 全在 ⇒ 4) `update status='completed', completed_at=now()` |
| 200 返回 | `{ public_url: "${SUPABASE_URL}/functions/v1/video-serve?id=<upload_id>", file_path: <session.storage_path> }` |
| 400 | 缺片时返回 `{ error, missing_chunks: [0,3,7] }` |
| 幂等 | 已 `completed` 直接返回相同 URL，不再校验 |

**关键**：返回的 `public_url` **指向 video-serve**，不指向 Storage。前端把这个值塞进 `<video src=>` 或写进数据库的视频字段。

### `video-serve` — Range 流式代理

| 项 | 值 |
|---|---|
| Method | `GET` |
| Auth | **无**（upload_id 是 UUID 不可猜，视频是公开课程内容） |
| Query | `?id=<upload_id>` |
| Range 解析 | `Range: bytes=N-M` 正则 `/bytes=(\d+)-(\d*)/`；缺 M 取 `total_size-1` |
| Range 算术 | `firstChunk = floor(rangeStart / 5MB)`；`lastChunk = min(floor(rangeEnd/5MB), chunk_count-1)`；`skipBytesInFirst = rangeStart - firstChunk * 5MB` |
| 签名 | 每片 `createSignedUrl("<upload_id>/<i>", 3600)`，覆盖 [firstChunk..lastChunk] |
| 流式 | `ReadableStream`：fetch 一片 → 首片切掉 `skipBytesInFirst` → `subarray(0, min(available, bytesRemaining))` → `enqueue` → 减 `bytesRemaining` |
| 200 / 206 | 有 Range 返 206，无 Range 返 200 全文 |
| 必返头 | `Content-Length`（精确）、`Accept-Ranges: bytes`、`Cache-Control: no-store`，206 还要 `Content-Range: bytes N-M/total` |
| 416 | `rangeStart > rangeEnd` 或 `rangeStart >= total_size`，返 `Content-Range: bytes */<total>` |
| 409 | `status !== 'completed'` |

**为什么不能合并 chunk 后再返**：合并就需要在内存里持有一段 ≥ 5MB 的拼接缓冲，多个并发拖动条会爆 Edge Function 内存。流式 + 一次只持有一片，是单函数能撑住高并发拖拽的唯一姿势。

---

## 前端契约（不在三个函数里，但必须遵守）

```js
const CHUNK_SIZE = 5 * 1024 * 1024;  // 必须等于 video-serve 的 CHUNK_SIZE，否则 Range 算术错位
const chunkCount = Math.ceil(file.size / CHUNK_SIZE);

// 1. 创建 video_uploads 行（自行实现，不在三个函数内）
const upload_id = await createVideoUploadRow({
  total_size: file.size,
  chunk_count: chunkCount,
  mime_type: file.type || 'video/mp4',
  status: 'uploading',
  uploaded_chunks: 0,
});

// 2. 顺序上传分片
for (let i = 0; i < chunkCount; i++) {
  const slice = file.slice(i * CHUNK_SIZE, (i + 1) * CHUNK_SIZE);
  const fd = new FormData();
  fd.append('upload_id', upload_id);
  fd.append('chunk_index', String(i));
  fd.append('chunk', slice);
  await fetch(`${SUPABASE_URL}/functions/v1/video-upload-chunk`, {
    method: 'POST',
    headers: { Authorization: `Bearer ${userJwt}` },
    body: fd,
  });
}

// 3. 完成
const { public_url } = await fetch(`${SUPABASE_URL}/functions/v1/video-upload-complete`, {
  method: 'POST',
  headers: { Authorization: `Bearer ${userJwt}`, 'Content-Type': 'application/json' },
  body: JSON.stringify({ upload_id }),
}).then(r => r.json());

// 4. 用 public_url 当视频源
videoEl.src = public_url;
```

**前端不可破坏的约定**：
- `CHUNK_SIZE` 必须 = 后端 `video-serve` 的 `CHUNK_SIZE`（当前 5MB）。改其中一个不改另一个 → 拖进度条画面错位。
- 分片必须**顺序**或带去重的并发上传，`chunk_index` 必须严格 0..N-1 全覆盖。
- `total_size` 必须 = 实际文件字节数，**不能预估**（Range 算术依赖）。

---

## 不可变常量速查表

| 常量 | 值 | 必须同步的位置 | 改动后果 |
|---|---|---|---|
| `CHUNK_SIZE` | `5 * 1024 * 1024` | 前端切片 + `video-serve` | 不一致 → Range 算术错位 → 拖动条乱跳 |
| `CHUNK_MAX_BYTES` | `5 * 1024 * 1024 + 128 * 1024` | 仅 `video-upload-chunk` | 改小 → 偶发 400；改大 → 接近 Edge Function 内存上限 |
| 桶名 | `video-chunks` | 三个函数全要改 | 改一个不改其他 → 写入成功但 serve 找不到 |
| 路径格式 | `<upload_id>/<chunk_index>` | 三个函数全要改 | 不一致 → list / signedUrl 全失效 |
| 签名 URL TTL | `3600` 秒 | 仅 `video-serve` | 改太短 → 大文件流式播放中途签名过期 |

---

## 已知边界

- **无断点续传 UI**：chunk 是 `upsert: true`（重复上传同一片 OK），但前端要自己实现"哪几片已传"的状态机，三个函数不管这个。
- **无并发上传保护**：同一 `upload_id` 多端并发上传不同片 → OK；同一 `upload_id` 多端并发上传同一片 → upsert 会让最后一个赢，无校验。
- **无视频长度校验**：complete 函数只检查"分片数对得上"，不验证拼起来是合法 mp4。前端在 init 时算错 `chunk_count` → complete 会通过 → serve 时浏览器解码失败。
- **无清理**：废弃的 upload_id 的分片会一直留在桶里。生产请加定时任务删除 `status='uploading' AND created_at < now()-interval '24h'` 的记录及其 chunks。

---

## 给秒哒喂提示词时的红线

写提示词的完整模板见 [`prompt-patterns.md` § 大文件上传：先测新环境，旧分片代理只兜底](../prompt-patterns.md#大文件上传先测新环境旧分片代理只兜底)。

先让秒哒只做能力测试并停止，不要一边测试一边改架构。确认仍复现旧限制后，再把 `reference-materials/video-chunked-upload/` 三个 ts 作为兼容源码喂给它，避免它重写后再次撞 #14 的旧环境三层墙。

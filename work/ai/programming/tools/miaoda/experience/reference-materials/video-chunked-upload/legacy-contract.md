# 旧环境分片上传合同与专用提示词

> 状态：历史兼容，非当前默认。2026-09-12从 `patterns/large-video-upload.md` 的旧架构章节与原 `prompt-patterns.md` 兼容模板迁入；没有修改三个TS参考文件，也没有在本轮复测生产环境。
> 进入条件：先按 [当前上传决策](../../patterns/large-video-upload.md) 核验会员/容量并测试，确认目标旧项目仍复现CORS、413或函数资源限制，再读本文件。
> 来源：[旧故障记录pitfalls #14](../../pitfalls.md)、[参考实现索引](./README.md)。旧“必须”只约束已选定的兼容实现，不约束新项目。
> 访问边界：旧 `video-serve` 无鉴权且返回可访问URL，只适合原案例已确定公开的视频；UUID不能代替授权。需私密、付费或按用户隔离的媒体必须另行设计鉴权，不直接套用。

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
| Auth | **无**（旧案例的视频原定公开；UUID不是访问授权，不能用于私密或付费内容保护） |
| Query | `?id=<upload_id>` |
| Range 解析 | `Range: bytes=N-M` 正则 `/bytes=(\d+)-(\d*)/`；缺 M 取 `total_size-1` |
| Range 算术 | `firstChunk = floor(rangeStart / 5MB)`；`lastChunk = min(floor(rangeEnd/5MB), chunk_count-1)`；`skipBytesInFirst = rangeStart - firstChunk * 5MB` |
| 签名 | 每片 `createSignedUrl("<upload_id>/<i>", 3600)`，覆盖 [firstChunk..lastChunk] |
| 流式 | `ReadableStream`：fetch 一片 → 首片切掉 `skipBytesInFirst` → `subarray(0, min(available, bytesRemaining))` → `enqueue` → 减 `bytesRemaining` |
| 200 / 206 | 有 Range 返 206，无 Range 返 200 全文 |
| 必返头 | `Content-Length`（精确）、`Accept-Ranges: bytes`、`Cache-Control: no-store`，206 还要 `Content-Range: bytes N-M/total` |
| 416 | `rangeStart > rangeEnd` 或 `rangeStart >= total_size`，返 `Content-Range: bytes */<total>` |
| 409 | `status !== 'completed'` |

**为什么不能合并 chunk 后再返**：合并就需要在内存里持有一段 ≥ 5MB 的拼接缓冲，多个并发拖动条会爆 Edge Function 内存。此旧实现采用流式且一次只持有一片；实际并发容量仍需在目标环境测试。

---

## 前端契约（不在三个函数里，但必须遵守）

下面是旧记录中的最小调用顺序示例，不是完整生产上传器；实际使用需补上传响应校验、失败停止/重试、断点状态和权限检查，不能把 `fetch` 返回视为上传成功。

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


## 旧环境专用提示词

**旧环境兼容提示词**：

```
@<秒哒后端技能> 我现在需要给后台加大视频上传。请打起十二分的精神专心执行！！

红线（必须严格遵守，违反必死）：
- ❌ 禁止前端通过 supabase-js 直接调 Storage 端点（含 createSignedUploadUrl / TUS / upload）——
  秒哒预览域名 *.miaoda.cn 不在 Storage 端点 CORS 白名单内，浏览器会直接拦
- ❌ 禁止把分片在 Edge Function 里合并成完整 mp4 写回 Storage——
  上传合并文件瞬间会被平台 storageFileSizeLimit 在 413 层堵死（已实测，TUS / ReadableStream 流式合并都没用）
- ❌ 禁止重写下述三个函数的逻辑或常量——参考实现已在生产验证
- ✅ 必须用三函数架构：video-upload-chunk（5MB 一片）+ video-upload-complete（验全 + 标完成）+ video-serve（Range 流式代理）
- ✅ 视频 URL 必须指向 video-serve 函数地址，不允许是 Storage 公开 URL
- 有Range请求时video-serve返回206 + Content-Range + Accept-Ranges: bytes；无Range请求按既有源码返回200，不能机械拒绝合法的整文件读取

参考实现（必须照抄、不允许另写）：
- reference-materials/video-chunked-upload/video-upload-chunk.ts
- reference-materials/video-chunked-upload/video-upload-complete.ts
- reference-materials/video-chunked-upload/video-serve.ts
直接原样部署到 supabase/functions/video-upload-chunk、video-upload-complete、video-serve。

不可变常量（前后端必须同步）：
- 分片大小 = 5 * 1024 * 1024（前端 + video-serve.ts L21）
- 桶名 = video-chunks（三个函数硬编码）
- 路径格式 = <upload_id>/<chunk_index>（三个函数硬编码）

表 schema 见 reference-materials/video-chunked-upload/README.md。
前端切片循环、断点续传 UI、video_uploads 行的创建端点需要你自己实现（这三个函数不管）。

测试场景：上传一个 200MB 的 mp4，complete 返回的 public_url 在 <video> 标签里能正常拖进度条。
```

**为什么兼容方案必须把“禁止合并”放红线**：在已确认仍受旧 Storage 上限影响的环境里，秒哒可能自动加上合并步骤，再次撞 413。这个红线只属于旧环境兼容方案，不是 2026-07-15 后所有新项目的默认规则。

**为什么必须把 references 路径塞进提示词**：参考 [参考实现复用](../../prompts/payment-integration.md)，秒哒会无视已提供实现自己另写一份。明确三个ts的固定路径与允许适配范围，可减少重写导致的偏差；实际使用前仍需核对当前合同。

**反面教材**：

```
❌ 帮我加大视频上传功能，最好支持断点续传
❌ 用 Supabase Storage 实现 mp4 上传
❌ 切片上传完后合并成完整视频写回 Storage
```

为什么失败：如果当前环境已经实测仍受旧限制，这些提示没有禁止合并、没有指明 video-serve 架构、没有引用已有实现，会再次撞旧环境三层墙；如果尚未测试，则问题在于过早选定架构。

# video-chunked-upload — 旧环境兼容源码

> **状态：参考实现 / 非当前默认。** 这三个 `.ts` 是 [`pitfalls.md` #14](../../pitfalls.md) 在旧后端环境中的处方实现，历史生产已验证。
>
> 2026-07-15 的仓库记录显示秒哒已取消“应用内 50MB 文件上传上限”。新项目必须先按 [`patterns/large-video-upload.md`](../../patterns/large-video-upload.md) 做当前环境能力测试；只有仍复现 CORS / 413 / supervisor kill 时才使用本目录。
>
> 完整的“为什么这样写、契约长什么样”在 [`patterns/large-video-upload.md`](../../patterns/large-video-upload.md)。
>
> 本目录的角色：**旧环境兼容时给 AI 喂“必须照抄、禁止重写”的参考实现**。

---

## 三个文件

| 文件 | Edge Function 名 | 职责 |
|---|---|---|
| [`video-upload-chunk.ts`](./video-upload-chunk.ts) | `video-upload-chunk` | 浏览器一片一片往这里 POST，写到 `video-chunks/<upload_id>/<idx>` |
| [`video-upload-complete.ts`](./video-upload-complete.ts) | `video-upload-complete` | 验所有分片在位 → 标记 `status='completed'` → 返回 `video-serve` URL |
| [`video-serve.ts`](./video-serve.ts) | `video-serve` | 伪装成完整视频文件：Range 请求来 → 计算覆盖的分片 → 流式拼接返回 206 |

---

## 不要改的地方

| 地方 | 改了会怎样 |
|---|---|
| `CHUNK_SIZE = 5 * 1024 * 1024`（serve.ts L21） | 必须 = 前端切片大小。改一个不改另一个 → 进度条乱跳、画面错位 |
| `CHUNK_MAX_BYTES = 5MB + 128KB`（chunk.ts L12） | 改小偶发 400；改大逼近 Edge Function 内存上限 |
| 桶名 `video-chunks` | 三个文件硬编码同一桶名，改要一起改 |
| 路径格式 `<upload_id>/<chunk_index>` | list / signedUrl 同样硬编码这个格式 |
| `createSignedUrl(..., 3600)` | 太短大文件流式播放中途签名会过期 |
| `video-serve` 不鉴权 | UUID 不可猜，加上鉴权反而会让 `<video>` 标签的 Range 请求失败（浏览器不会带 Authorization） |
| `Accept-Ranges: bytes` 头 | 没这个头 HTML5 `<video>` 不让拖进度条 |
| `Cache-Control: no-store` | 加缓存 → 切到下一个视频还放旧片段 |

---

## 需要自己实现的部分

这三个函数**不**包含：

1. **创建 `video_uploads` 表行的端点**：前端切片前必须先有 `upload_id` / `chunk_count` / `total_size`。可以走 supabase-js insert（前提是 RLS 允许 admin 写），也可以再写一个 `video-upload-init` Edge Function。
2. **前端切片上传循环**：见 [`patterns/large-video-upload.md` § 前端契约](../../patterns/large-video-upload.md#前端契约不在三个函数里但必须遵守)。
3. **断点续传 UI**：chunk 函数 `upsert: true` 让重传同一片不报错，但"哪几片已传"的状态机要前端自己维护。
4. **过期清理**：定时任务删除 `status='uploading' AND created_at < now()-interval '24h'` 的会话及其桶分片。

---

## 表 schema（从源码反推）

```sql
create table video_uploads (
  id              uuid primary key default gen_random_uuid(),
  user_id         uuid not null references profiles(id),
  total_size      bigint not null,
  chunk_count     int not null,
  uploaded_chunks int not null default 0,
  mime_type       text default 'video/mp4',
  status          text not null default 'uploading',  -- 'uploading' | 'completed'
  storage_path    text,
  created_at      timestamptz default now(),
  completed_at    timestamptz
);

-- 桶
insert into storage.buckets (id, name, public) values ('video-chunks', 'video-chunks', false);
```

---

## 部署速记

```bash
supabase functions deploy video-upload-chunk
supabase functions deploy video-upload-complete
supabase functions deploy video-serve

# 三个函数都需要这两个环境变量
# SUPABASE_URL（自动注入）
# SUPABASE_SERVICE_ROLE_KEY（自动注入，但要确认面板里 secret 已配）
```

`video-upload-chunk` 和 `video-upload-complete` 走 admin 校验（`profiles.role === 'admin' || is_super_admin === true`）。`video-serve` **不**走鉴权，因为 `<video>` Range 请求不会带 Authorization 头。

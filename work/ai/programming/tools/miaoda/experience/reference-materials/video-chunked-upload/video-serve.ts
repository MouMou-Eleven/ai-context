import { createClient } from "jsr:@supabase/supabase-js@2";

// ---------------------------------------------------------------------------
// STATUS: Legacy compatibility path for old Miaoda backends. Current paid plans
// document 500MB after front/back limits are synchronized. Test native upload
// first and use this only when an old project still hits CORS/413/timeouts.
//
// video-serve — 分片流式代理（彻底绕过 Supabase Storage 全局大文件限制）
//
// 架构背景：
//   平台全局 storageFileSizeLimit 使用 Math.min(global, bucket) 计算上限，
//   导致无论用直接 PUT 还是 TUS，写入合并文件都会触发 413。
//
// 解法：不合并，直接代理分片
//   1. GET /functions/v1/video-serve?id=<upload_id>
//   2. 从 DB 读取 total_size / chunk_count / mime_type
//   3. 解析 Range 请求头，计算覆盖的 chunk 范围
//   4. 逐 chunk fetch（签名 URL）→ 精确截取字节 → 流式推给客户端
//   5. 返回 206 Partial Content（有 Range）或 200（无 Range）
//
// 无需鉴权（upload_id 是 UUID，无法猜测；视频属于课程公开内容）
// Accept-Ranges: bytes  → HTML5 <video> 可拖拽进度条
// ---------------------------------------------------------------------------

const CHUNK_SIZE = 5 * 1024 * 1024; // 5 MB，必须与前端 uploadVideoToStorage 保持一致

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, OPTIONS",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type, range",
  "Access-Control-Max-Age": "86400",
};

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: corsHeaders });
  if (req.method !== "GET") {
    return new Response("Method Not Allowed", { status: 405, headers: corsHeaders });
  }

  const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
  const serviceKey  = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

  const adminClient = createClient(supabaseUrl, serviceKey, {
    auth: { persistSession: false },
  });

  // ── 解析 upload_id ────────────────────────────────────────────────
  const url      = new URL(req.url);
  const uploadId = url.searchParams.get("id");
  if (!uploadId) {
    return new Response(JSON.stringify({ error: "缺少参数 id" }), {
      status: 400,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }

  // ── 读取 session ──────────────────────────────────────────────────
  const { data: session, error: sessionErr } = await adminClient
    .from("video_uploads")
    .select("id, chunk_count, total_size, mime_type, status")
    .eq("id", uploadId)
    .maybeSingle();

  if (sessionErr || !session) {
    console.error("[video-serve] session not found:", uploadId, sessionErr);
    return new Response(JSON.stringify({ error: "视频不存在" }), {
      status: 404,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }

  if (session.status !== "completed") {
    return new Response(JSON.stringify({ error: "视频尚未上传完成" }), {
      status: 409,
      headers: { ...corsHeaders, "Content-Type": "application/json" },
    });
  }

  const totalSize  = session.total_size  as number;
  const chunkCount = session.chunk_count as number;
  const mimeType   = (session.mime_type as string) || "video/mp4";

  // ── 解析 Range 请求头 ─────────────────────────────────────────────
  const rangeHeader = req.headers.get("Range");
  let rangeStart = 0;
  let rangeEnd   = totalSize - 1;
  let isRangeRequest = false;

  if (rangeHeader) {
    const m = rangeHeader.match(/bytes=(\d+)-(\d*)/);
    if (m) {
      isRangeRequest = true;
      rangeStart = parseInt(m[1], 10);
      rangeEnd   = m[2] ? Math.min(parseInt(m[2], 10), totalSize - 1) : totalSize - 1;
    }
  }

  if (rangeStart > rangeEnd || rangeStart >= totalSize) {
    return new Response(null, {
      status: 416,
      headers: {
        ...corsHeaders,
        "Content-Range": `bytes */${totalSize}`,
      },
    });
  }

  const contentLength = rangeEnd - rangeStart + 1;

  // ── 计算覆盖的 chunk 范围 ─────────────────────────────────────────
  const firstChunkIdx       = Math.floor(rangeStart / CHUNK_SIZE);
  const lastChunkIdx        = Math.min(Math.floor(rangeEnd   / CHUNK_SIZE), chunkCount - 1);
  const skipBytesInFirst    = rangeStart - firstChunkIdx * CHUNK_SIZE;

  console.log(
    `[video-serve] id=${uploadId} range=${rangeStart}-${rangeEnd}/${totalSize}` +
    ` chunks=${firstChunkIdx}..${lastChunkIdx} skip=${skipBytesInFirst}`,
  );

  // ── 为需要的 chunk 批量签名 ───────────────────────────────────────
  const signedUrls: string[] = [];
  for (let i = firstChunkIdx; i <= lastChunkIdx; i++) {
    const { data: signed, error: signErr } = await adminClient.storage
      .from("video-chunks")
      .createSignedUrl(`${uploadId}/${i}`, 3600);
    if (signErr || !signed?.signedUrl) {
      console.error(`[video-serve] sign chunk ${i} error:`, signErr);
      return new Response(JSON.stringify({ error: `签名 chunk ${i} 失败` }), {
        status: 500,
        headers: { ...corsHeaders, "Content-Type": "application/json" },
      });
    }
    signedUrls.push(signed.signedUrl);
  }

  // ── 构建流式响应 ──────────────────────────────────────────────────
  let bytesRemaining = contentLength;

  const body = new ReadableStream({
    async start(controller) {
      for (let idx = 0; idx < signedUrls.length && bytesRemaining > 0; idx++) {
        const chunkGlobalIdx = firstChunkIdx + idx;
        let chunkRes: Response;
        try {
          chunkRes = await fetch(signedUrls[idx]);
        } catch (e) {
          console.error(`[video-serve] fetch chunk ${chunkGlobalIdx} error:`, e);
          controller.error(e);
          return;
        }
        if (!chunkRes.ok || !chunkRes.body) {
          const t = await chunkRes.text().catch(() => "(no body)");
          console.error(`[video-serve] chunk ${chunkGlobalIdx} HTTP ${chunkRes.status}`, t);
          controller.error(new Error(`chunk ${chunkGlobalIdx}: HTTP ${chunkRes.status}`));
          return;
        }

        const chunkBuf = new Uint8Array(await chunkRes.arrayBuffer());

        // 在首 chunk 跳过前 skipBytesInFirst 个字节
        const sliceStart = (idx === 0) ? skipBytesInFirst : 0;
        const available  = chunkBuf.byteLength - sliceStart;
        const toSend     = Math.min(available, bytesRemaining);

        controller.enqueue(chunkBuf.subarray(sliceStart, sliceStart + toSend));
        bytesRemaining -= toSend;
      }
      controller.close();
    },
  });

  const responseHeaders: Record<string, string> = {
    ...corsHeaders,
    "Content-Type":   mimeType,
    "Content-Length": String(contentLength),
    "Accept-Ranges":  "bytes",
    "Cache-Control":  "no-store",
  };
  if (isRangeRequest) {
    responseHeaders["Content-Range"] = `bytes ${rangeStart}-${rangeEnd}/${totalSize}`;
  }

  return new Response(body, {
    status:  isRangeRequest ? 206 : 200,
    headers: responseHeaders,
  });
});

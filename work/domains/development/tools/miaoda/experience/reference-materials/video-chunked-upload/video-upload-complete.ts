import { createClient } from "jsr:@supabase/supabase-js@2";

// ---------------------------------------------------------------------------
// STATUS: Legacy compatibility path for old Miaoda backends. Current paid plans
// document 500MB after front/back limits are synchronized. Test native upload
// first and use this only when an old project still hits CORS/413/timeouts.
//
// video-upload-complete — 验证分片完整性，标记完成，返回 video-serve 代理 URL
//
// 架构背景：
//   平台全局 storageFileSizeLimit = Math.min(global, bucket) 远小于大文件体积，
//   导致任何方式（PUT / TUS）写合并文件到 Storage 都会 413。
//
// 解法：
//   不合并文件——chunks 永久保留在 video-chunks 桶，
//   视频 URL 指向 video-serve edge function（流式分片代理，支持 Range 拖拽）。
// ---------------------------------------------------------------------------

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type, x-requested-with, accept, origin",
  "Access-Control-Max-Age": "86400",
  "Access-Control-Allow-Credentials": "false",
};

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders, "Content-Type": "application/json" },
  });
}

function logError(tag: string, err: unknown) {
  if (err instanceof Error) {
    console.error(tag, { message: err.message, stack: err.stack, raw: String(err) });
  } else {
    console.error(tag, { raw: String(err), type: typeof err });
  }
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: corsHeaders });

  try {
    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const serviceKey  = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

    if (!serviceKey) {
      console.error("[video-upload-complete] SUPABASE_SERVICE_ROLE_KEY is missing");
      return json({ error: "服务端配置错误：缺少 service role key" }, 500);
    }

    const adminClient = createClient(supabaseUrl, serviceKey, {
      auth: { persistSession: false },
    });

    // ── 鉴权 ─────────────────────────────────────────────────────────
    const authHeader = req.headers.get("Authorization");
    if (!authHeader) return json({ error: "未授权：缺少 Authorization 头" }, 401);

    const token = authHeader.replace("Bearer ", "");
    const { data: { user }, error: authErr } = await adminClient.auth.getUser(token);
    if (authErr || !user) {
      logError("[video-upload-complete] auth error", authErr);
      return json({ error: "Token 无效或已过期" }, 401);
    }

    const { data: profile } = await adminClient
      .from("profiles")
      .select("role, is_super_admin")
      .eq("id", user.id)
      .maybeSingle();

    const isAdmin = profile?.role === "admin" || profile?.is_super_admin === true;
    if (!isAdmin) return json({ error: "权限不足：仅管理员可上传视频" }, 403);

    // ── 解析请求体 ───────────────────────────────────────────────────
    const { upload_id } = await req.json() as { upload_id?: string };
    if (!upload_id) return json({ error: "缺少必填参数: upload_id" }, 400);

    // ── 读取会话 ──────────────────────────────────────────────────────
    const { data: session, error: sessionErr } = await adminClient
      .from("video_uploads")
      .select("*")
      .eq("id", upload_id)
      .maybeSingle();

    if (sessionErr || !session) {
      logError("[video-upload-complete] session not found", sessionErr);
      return json({ error: "upload_id 不存在" }, 404);
    }

    // ── 构造 serve URL（无论是否已完成都用同一地址）────────────────
    const serveUrl = `${supabaseUrl}/functions/v1/video-serve?id=${upload_id}`;

    // ── 幂等：已完成则直接返回 ────────────────────────────────────────
    if (session.status === "completed") {
      console.log("[video-upload-complete] idempotent return:", serveUrl);
      return json({ public_url: serveUrl, file_path: session.storage_path });
    }

    // ── 校验所有分片是否已到位 ────────────────────────────────────────
    const { data: storedChunks, error: listErr } = await adminClient.storage
      .from("video-chunks")
      .list(upload_id, { limit: session.chunk_count + 10 });

    if (listErr) {
      logError("[video-upload-complete] list chunks error", listErr);
      return json({ error: "列举分片失败", detail: listErr.message }, 500);
    }

    const storedIndices = new Set(
      (storedChunks ?? []).map((f) => parseInt(f.name, 10)).filter((n) => !isNaN(n)),
    );
    const missing: number[] = [];
    for (let i = 0; i < session.chunk_count; i++) {
      if (!storedIndices.has(i)) missing.push(i);
    }
    if (missing.length > 0) {
      console.warn("[video-upload-complete] missing chunks:", missing);
      return json({ error: `${missing.length} 个分片尚未上传`, missing_chunks: missing }, 400);
    }

    // ── 标记 completed ────────────────────────────────────────────────
    const { error: updateErr } = await adminClient
      .from("video_uploads")
      .update({
        status:       "completed",
        completed_at: new Date().toISOString(),
      })
      .eq("id", upload_id);

    if (updateErr) {
      logError("[video-upload-complete] update status error (non-fatal)", updateErr);
    }

    console.log("[video-upload-complete] marked completed, serve URL:", serveUrl);

    return json({
      public_url: serveUrl,
      file_path:  session.storage_path,
    });

  } catch (err) {
    logError("[video-upload-complete] unhandled top-level error", err);
    return json({
      error:  "服务器内部错误",
      detail: err instanceof Error ? err.message : String(err),
    }, 500);
  }
});

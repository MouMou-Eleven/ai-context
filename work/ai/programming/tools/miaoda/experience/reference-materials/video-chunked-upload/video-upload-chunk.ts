// Legacy compatibility path for old Miaoda backends. Current paid plans document
// a 500MB in-app upload cap after front/back limits are synchronized. Test the
// native path first; use this only when an old project still hits CORS/413/timeouts.
import { createClient } from "jsr:@supabase/supabase-js@2";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type, x-requested-with, accept, origin",
  "Access-Control-Max-Age": "86400",
  "Access-Control-Allow-Credentials": "false",
};

const CHUNK_MAX_BYTES = 5 * 1024 * 1024 + 128 * 1024; // 5MB + 128KB tolerance

function json(body: unknown, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { ...corsHeaders, "Content-Type": "application/json" },
  });
}

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response(null, { status: 204, headers: corsHeaders });

  try {
    const supabaseUrl = Deno.env.get("SUPABASE_URL")!;
    const serviceKey  = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!;

    if (!serviceKey) {
      console.error("[video-upload-chunk] SUPABASE_SERVICE_ROLE_KEY is missing");
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
    if (authErr || !user) return json({ error: "Token 无效或已过期" }, 401);

    const { data: profile } = await adminClient
      .from("profiles")
      .select("role, is_super_admin")
      .eq("id", user.id)
      .maybeSingle();

    const isAdmin = profile?.role === "admin" || profile?.is_super_admin === true;
    if (!isAdmin) return json({ error: "权限不足：仅管理员可上传视频" }, 403);

    // ── 解析 multipart/form-data ─────────────────────────────────────
    const contentType = req.headers.get("content-type") ?? "";
    if (!contentType.includes("multipart/form-data")) {
      return json({ error: "请求体必须是 multipart/form-data" }, 400);
    }

    let formData: FormData;
    try {
      formData = await req.formData();
    } catch (e) {
      console.error("[video-upload-chunk] formData parse error:", e);
      return json({ error: "无法解析 multipart/form-data", detail: String(e) }, 400);
    }

    const upload_id    = formData.get("upload_id") as string | null;
    const chunk_index  = formData.get("chunk_index") as string | null;
    const chunkFile    = formData.get("chunk") as File | null;

    if (!upload_id || chunk_index === null || !chunkFile) {
      return json({ error: "缺少必填字段: upload_id, chunk_index, chunk" }, 400);
    }

    const idx = parseInt(chunk_index, 10);
    if (isNaN(idx) || idx < 0) {
      return json({ error: "chunk_index 必须是非负整数" }, 400);
    }

    // ── 大小检查 ──────────────────────────────────────────────────────
    const chunkBytes = await chunkFile.arrayBuffer();
    if (chunkBytes.byteLength > CHUNK_MAX_BYTES) {
      return json({
        error: `分片 ${idx} 超过大小限制（${(chunkBytes.byteLength / 1024 / 1024).toFixed(2)}MB > 5MB）`,
      }, 400);
    }

    // ── 校验 upload_id 归属 ──────────────────────────────────────────
    const { data: session, error: sessionErr } = await adminClient
      .from("video_uploads")
      .select("id, user_id, chunk_count, status, uploaded_chunks")
      .eq("id", upload_id)
      .maybeSingle();

    if (sessionErr || !session) {
      console.error("[video-upload-chunk] session not found:", upload_id, sessionErr);
      return json({ error: "upload_id 不存在或已失效" }, 404);
    }
    if (session.status === "completed") {
      return json({ error: "上传会话已完成，不可继续上传分片" }, 409);
    }
    if (idx >= session.chunk_count) {
      return json({ error: `chunk_index ${idx} 超出范围（chunk_count=${session.chunk_count}）` }, 400);
    }

    // ── 写入 Storage 临时路径 ─────────────────────────────────────────
    const chunkPath = `${upload_id}/${idx}`;
    console.log(`[video-upload-chunk] writing chunk ${idx} (${chunkBytes.byteLength}B) → video-chunks/${chunkPath}`);

    const { error: storageErr } = await adminClient.storage
      .from("video-chunks")
      .upload(chunkPath, chunkBytes, {
        contentType: "application/octet-stream",
        upsert: true,
      });

    if (storageErr) {
      console.error(`[video-upload-chunk] storage upload error chunk ${idx}:`, storageErr);
      return json({ error: `存储分片失败: ${storageErr.message}` }, 500);
    }

    // ── 递增 uploaded_chunks ──────────────────────────────────────────
    const { error: updateErr } = await adminClient
      .from("video_uploads")
      .update({ uploaded_chunks: session.uploaded_chunks + 1 })
      .eq("id", upload_id);

    if (updateErr) {
      console.error("[video-upload-chunk] update uploaded_chunks error:", updateErr);
      // 非致命错误：chunk 已落盘，只是计数未更新
    }

    console.log(`[video-upload-chunk] chunk ${idx} OK, progress: ${session.uploaded_chunks + 1}/${session.chunk_count}`);

    return json({
      ok:              true,
      chunk_index:     idx,
      uploaded_chunks: session.uploaded_chunks + 1,
      chunk_count:     session.chunk_count,
    });
  } catch (err) {
    console.error("[video-upload-chunk] unhandled error:", err);
    return json({ error: "服务器内部错误", detail: String(err) }, 500);
  }
});

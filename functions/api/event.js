// Anonymous usage ping (no personal data). Logged only to Cloudflare's request logs.
export async function onRequestGet() {
  return new Response(null, { status: 204 });
}

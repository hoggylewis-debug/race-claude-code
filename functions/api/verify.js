export async function onRequestGet({ request, env }) {
  const sid = new URL(request.url).searchParams.get('session_id') || '';
  if (!/^cs_[A-Za-z0-9_]+$/.test(sid) || !env.STRIPE_SECRET_KEY) return Response.json({ paid: false });
  const r = await fetch('https://api.stripe.com/v1/checkout/sessions/' + sid, {
    headers: { Authorization: 'Bearer ' + env.STRIPE_SECRET_KEY },
  });
  if (!r.ok) return Response.json({ paid: false });
  const j = await r.json();
  return Response.json({ paid: j.payment_status === 'paid' });
}

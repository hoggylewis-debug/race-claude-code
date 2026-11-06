export async function onRequestPost({ request, env }) {
  if (!env.STRIPE_SECRET_KEY) return Response.json({ error: 'not configured' }, { status: 500 });
  const origin = new URL(request.url).origin;
  const body = new URLSearchParams({
    mode: 'payment',
    'line_items[0][quantity]': '1',
    'line_items[0][price_data][currency]': 'gbp',
    'line_items[0][price_data][unit_amount]': '249',
    'line_items[0][price_data][product_data][name]': 'SantaDraw Pro',
    'line_items[0][price_data][product_data][description]': 'Unlimited group size, exclusions, wishlists and printable cards. One-off payment.',
    success_url: origin + '/?paid={CHECKOUT_SESSION_ID}',
    cancel_url: origin + '/?cancelled=1',
    allow_promotion_codes: 'true',
  });
  const r = await fetch('https://api.stripe.com/v1/checkout/sessions', {
    method: 'POST',
    headers: { Authorization: 'Bearer ' + env.STRIPE_SECRET_KEY, 'Content-Type': 'application/x-www-form-urlencoded' },
    body,
  });
  const j = await r.json();
  if (!r.ok) return Response.json({ error: 'stripe error' }, { status: 502 });
  return Response.json({ url: j.url });
}

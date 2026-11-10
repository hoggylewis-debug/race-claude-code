export async function onRequestGet({ env }) {
  const key = env.STRIPE_SECRET_KEY || '';
  const sales = env.SALES_OPEN === '1' && !key.startsWith('sk_test_') && key.length > 0;
  return Response.json({ sales }, { headers: { 'Cache-Control': 'no-store' } });
}

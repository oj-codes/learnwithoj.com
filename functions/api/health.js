// Cloudflare Pages Function, served at /api/health.
//
// The first server-side route on the site. It answers with the commit and branch that
// Pages deployed, so a watcher can tell which build is live without reading the HTML.
// The Stripe webhook and the signed download handler for the marketplace land beside it.
export function onRequestGet({ env }) {
  const body = {
    ok: true,
    commit: env.CF_PAGES_COMMIT_SHA || null,
    branch: env.CF_PAGES_BRANCH || null,
  };
  return new Response(JSON.stringify(body), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

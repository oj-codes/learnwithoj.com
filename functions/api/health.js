// GET /api/health
//
// The first server-side route on the site. It answers with the commit and branch the
// deploy workflow passed in as vars, so a watcher can tell which build is live without
// reading the HTML. Locally, under wrangler dev, both are null.
export function health(request, env) {
  const body = {
    ok: true,
    commit: env.COMMIT_SHA || null,
    branch: env.BRANCH || null,
  };
  return new Response(JSON.stringify(body), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
    },
  });
}

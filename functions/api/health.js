// GET /api/health
//
// The first server-side route on the site. It answers with the Worker version that is
// serving, plus the commit and branch when the deploy command passed them in as vars, so
// a watcher can tell which build is live without reading the HTML. Locally, under
// wrangler dev, the commit and branch are null.
export function health(request, env) {
  const body = {
    ok: true,
    version: env.CF_VERSION_METADATA ? env.CF_VERSION_METADATA.id : null,
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

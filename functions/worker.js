// The Worker in front of the static site.
//
// Cloudflare serves every request from the uploaded assets first, except the paths listed
// under run_worker_first in wrangler.toml, which arrive here. Today that is /api/*, with one
// route. The Stripe webhook and the signed download handler for the marketplace go in
// functions/api/ beside health.js and get a line in the table below.
//
// Anything this Worker does not recognize falls through to the assets binding, so a miss
// gets the site's 404 page rather than a bare response. Deploys and previews run through
// Workers Builds, see wrangler.toml.

import { health } from "./api/health.js";

const routes = {
  "/api/health": health,
};

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const handler = routes[url.pathname];
    if (handler) {
      if (request.method !== "GET" && request.method !== "HEAD") {
        return new Response("Method not allowed", {
          status: 405,
          headers: { allow: "GET, HEAD", "cache-control": "no-store" },
        });
      }
      return handler(request, env);
    }
    return env.ASSETS.fetch(request);
  },
};

# Security

## Report a vulnerability

Report suspected vulnerabilities privately to `oj@learnwithoj.com`. Include the affected
URL or file, the triggering request or action, the expected and actual behavior, and the
possible impact. Redact credentials, personal information and customer data from examples.

Keep vulnerability details out of public issues, PR descriptions, review comments and
Actions logs. Use a private report for sensitive evidence.

## Scope and current implementation

This repository is the public marketing website. It contains plain HTML, one stylesheet,
vanilla JavaScript, generated agent-policy pages, and Cloudflare Pages Functions.

The GitHub Pages workflow currently publishes the repository root. Cloudflare Pages
configuration is checked in for the hosting move. The implemented Function is
`functions/api/health.js`, which returns a health flag and deployment commit and branch
metadata with `Cache-Control: no-store`.

Approved Stripe Checkout links and the Kit form are live B2C integrations. Their providers
handle the current checkout and email submission flows. This repo does not currently
implement a Stripe webhook, signed downloads, customer accounts or order storage. Treat
those as new security boundaries when introduced, rather than assuming they already exist.

## Assets and trust boundaries

- Public pages, assets, source, git history, PRs and CI logs are public surfaces. The deploy
  uploads the root, so a checked-in file must not rely on being unlinked to stay private.
- The internal repo holds private business and client material. Only approved output crosses
  into this repo. The public agent-page gate carries an allowlist, never the private
  blocklist or redaction exceptions. Review source changes internally and generated output
  here. Do not publish private evidence to explain a redaction.
- Browser input, request bodies, URL parameters, headers and third-party responses are
  untrusted. Validate the fields a handler uses, reject invalid requests and avoid placing
  untrusted strings into HTML or script execution contexts.
- Provider secrets belong in runtime environment bindings or CI secret storage. Public
  checkout links and the Kit form UID are intentionally public identifiers. They are not
  authentication credentials, and their presence alone is not a secret exposure.
- Booking and contact actions route through `https://book.learnwithoj.com`. Approved B2C
  purchases and email capture use the existing Stripe and Kit integrations. B2B pages keep
  those B2C integrations out.

## Review expectations

Read the general review rules in `AGENTS.md`. For a security finding, explain the attacker
input or capability, the reachable code path and the consequence. Separate an observed
vulnerability from an assumption that needs validation. Do not report a missing future
feature as a current vulnerability.

For Functions, validate inputs, use environment bindings for secrets, avoid logging request
bodies, and preserve `no-store` on dynamic responses. The health route's intended deployment
metadata is public, but adding other environment values to its response needs scrutiny.

When payment and download handlers are added, verify webhook signatures over the original
request body before trusting events. Derive purchase and download authorization from verified
server-side state, and handle duplicate payment events without duplicate fulfillment.
Do not trust a browser-supplied payment status or grant a download solely from its filename.

For GitHub Actions, keep permissions scoped to each job's purpose. Review changes that expose
secrets or grant write access to untrusted PR code. Treat PR content and dependency output
as data, and avoid interpolating them into executable shell commands. A deployment workflow
requires different permissions from a read-only checks workflow.

Changes to scripts, embeds, redirects, checkout destinations, data collection or deployment
configuration should explain the reason and any new access or data flow in the PR.

## Using this document with Codex

This file supplies repository security guidance. It does not enable automatic Security Review
or enforce checks. When configuring a separate Codex Security Review, select `SECURITY.md`
as the repository threat-model file to provide this context. Ordinary code review can still
identify security defects under the general review rules.

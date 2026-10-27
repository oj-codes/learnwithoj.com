# AGENTS.md

The README for agents, in the [agents.md](https://agents.md/) format that Codex, CodeRabbit,
Copilot, Cursor and most other coding agents read. `CLAUDE.md` is the full working agreement
and the source of truth for the business, the pages, the design tokens and the voice. This
file is the short version plus the review rules, and nothing here overrides `CLAUDE.md`.

## Project overview

Static marketing site for learnwithoj.com. Plain HTML, one stylesheet, vanilla JS, no build
step, no package manager, no framework. Two audiences on different pages (engineers on `/`,
companies on `/showcase`) plus explainer pages for general readers and the generated `/agents`
policy pages. The site is the proof of the founder's craft, so the bar is Stripe, Linear and
Vercel, not "good enough".

## Repo layout

- `index.html`, `showcase.html`, `resources.html`, `functional-emotions.html`, the hand-written pages
- `styles.css`, the only stylesheet, tokens at the top
- `agents/**`, generated from the internal repo and never edited here
- `functions/`, Cloudflare Pages Functions (`/api/health` today, Stripe webhook and signed downloads later)
- `tools/`, the checks (`tools/check`, `tools/last-reviewed`, `tools/policy-pii`)
- `.github/workflows/`, `ci.yaml` deploys, `checks.yaml` runs the checks on every PR

## How to run

```
python3 -m http.server 8000      # static preview
wrangler pages dev .             # preview with the Functions runtime
```

## Checks, and what done means

```
python3 tools/check                 # dates, names, HTML validity, internal links
python3 tools/check --links         # plus external links
python3 tools/check --lighthouse    # plus Lighthouse on the four main pages
python3 tools/check --voice         # plus the oj-voice linter from the internal repo
git config core.hooksPath .githooks # once per clone, runs the fast checks on commit
```

Done means `tools/check` is green, Lighthouse holds 95 or better in every category on every
page touched, `CHANGELOG.md` has an entry, a new page has a row in the pages table in
`CLAUDE.md`, and the `?v=` on `styles.css` is bumped on every page when the stylesheet changes.

## Conventions and PR expectations

- Commit as yourself, `git commit --author="Name <name@learnwithoj.com>"`. O.J. stays the
  committer. Trailers are `Claude-Session:` and `Model:` only.
- Branch per change, PR body signed with your name, `oj-codes` assigned. She merges by rebase.
- Commit titles are lowercase, present tense, and name the page or tool they touch.
- American spelling. Quoted material keeps its own spelling and punctuation.

## Constraints

- No build step, bundler, framework, `package.json` or `node_modules`, through launch.
- Every CTA goes through `https://book.learnwithoj.com`. The only email on the site is `oj@learnwithoj.com`.
- `agents/**` is generated. Change the source in the internal repo and regenerate.
- The 1% for the Planet footer block is a compliance surface. Its wording, logo, size and link are theirs.
- Stripe Checkout links and the Kit form are B2C surfaces and never appear on a B2B page.
- Stripe links and the Kit form UID are live production integrations, never placeholders.

## Code Review Rules

Codex and CodeRabbit apply these. Mechanical checks (validity, links, dates, names) run in CI
and are not review findings. Each rule states the problem, then the safe path.

### Blocking

- An email address other than `oj@learnwithoj.com`, a phone number, a street address, a
  client or contact name not already on the public site, or any secret, token or key.
  Safe path: the public site carries one address and nobody's private details.
- A build step, bundler, framework or package manifest. Safe path: plain files, and a
  Pages Function under `functions/` when something has to run server-side.
- A booking or contact CTA that bypasses `https://book.learnwithoj.com`. Safe path: the
  redirect rule owns the public link so vendors can change without touching pages.
- Stripe Checkout or the Kit email form on `showcase.html` or any page aimed at companies.
  Safe path: B2B pages route to the call, B2C pages sell.
- Any change to the 1% for the Planet footer block's wording, logo, size or link. Safe path:
  the block is copied from their guidelines and changes need O.J.'s sign-off.
- An edit under `agents/**`. Safe path: change the source in the internal repo, regenerate.
- A Pages Function that trusts input without validating it, logs request bodies, or stores a
  secret in code. Safe path: env bindings for secrets, verify Stripe signatures, `no-store`
  on dynamic responses.

### Craft

- A color, radius or spacing hardcoded instead of taken from the tokens at the top of
  `styles.css`. Safe path: add a token if one is missing.
- A stylesheet change without the `?v=` cache-bust bumped on every page that loads it.
- Missing or decorative-looking `alt` text, a skipped heading level, an interactive element
  unreachable by keyboard, a custom control with no visible focus state, an image without
  `width` and `height`. Safe path: accessibility ships inside the feature, not after it.
- Animation with no `prefers-reduced-motion: reduce` branch, or one that cannot hold 60fps.
  Safe path: reduce or remove the motion.
- A render-blocking script, a font loaded without `display=swap`, a third-party embed added
  without a reason in the PR. Safe path: defer, swap, or leave it out.

### Copy a visitor reads

- Em dashes, colons in prose, exclamation points, the bare word "engineers", the words
  "consultant" or "consulting", filler like "unlock" or "level up", British spellings. Safe
  path: `CLAUDE.md` "Brand voice". Quoted material from other people is exempt entirely.
- A "Last updated" date typed by hand on a living page. Safe path: the date comes from git
  through `tools/last-reviewed/check.py`.

### Not findings

The length of `CLAUDE.md`, the absence of a framework or a test suite, the single stylesheet,
inline JavaScript on a page, and the voice rules applied to quoted material. These are
decisions.

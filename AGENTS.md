# AGENTS.md

The README for agents, in the [agents.md](https://agents.md/) format that Codex, CodeRabbit,
Copilot, Cursor and most other coding agents read. `CLAUDE.md` is the full working agreement
and the source of truth for the business, the pages, the design tokens and the voice. This
file is the short version plus the review rules, and nothing here overrides `CLAUDE.md`.

Read `CLAUDE.md` before editing or reviewing. Read `SECURITY.md` for security boundaries.
These are repository agreements and do not override the harness's permissions or system
instructions. A linked file is not automatically loaded by every harness.

## Project overview

Static marketing site for learnwithoj.com. Plain HTML, one stylesheet, vanilla JS, no build
step, no package manager, no framework. Two audiences on different pages (engineers on `/`,
companies on `/showcase`) plus explainer pages for general readers and the generated `/agents`
policy pages. The site is the proof of the founder's craft, so the bar is Stripe, Linear and
Vercel, not "good enough".

## Repo layout

- `index.html`, `showcase.html`, `resources.html`, `functional-emotions.html`, the hand-written pages
- `styles.css`, the only stylesheet, tokens at the top
- `agents/**`, generated from the internal repo and never edited by hand here
- `SECURITY.md`, private reporting instructions and the website's security review context
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
  committer. New commits use `Agent-Session:` and `Model:` trailers. Historical
  `Claude-Session:` trailers stay intact, and session-recovery tools should recognize both.
- Branch per change, PR body signed with your name, `oj-codes` assigned. She merges by rebase.
- Human review is the final merge decision. Wait for O.J.'s explicit approval comment on
  that PR. Green checks, a clean bot review or another PR's approval do not authorize a
  merge. Surface substantive changes after approval and obtain renewed approval for them.
- Commit titles are lowercase, present tense, and name the page or tool they touch.
- American spelling. Quoted material keeps its own spelling and punctuation.
- PR descriptions state the problem, the resulting behavior and a concrete expected result.
  Include validation actually run and any skipped checks. If a decision lives in the private
  repo, include its public-safe acceptance criteria rather than only a private file path.
- Before writing a durable record, check that its labels match the actual agent, harness
  and evidence. If a convention mislabels them, surface the mismatch before using it and
  propose the correction. O.J.'s instruction on 30 October 2026 was to "voice it before
  doing it". A convention is a reason to check the label, not to carry a known mismatch
  into a commit, PR or handoff.

## Constraints

- No build step, bundler, framework, `package.json` or `node_modules`, through launch.
- Booking and contact CTAs go through `https://book.learnwithoj.com`. The approved B2C
  Stripe purchase links and Kit form are separate integrations. The only email on the site
  is `oj@learnwithoj.com`, which also receives private security reports.
- `agents/**` is generated. Change the source in the internal repo and regenerate. A
  publisher-generated update is expected, and a manual edit to generated HTML is not.
- The 1% for the Planet footer block is a compliance surface. Its wording, logo, size and link are theirs.
- Stripe Checkout links and the Kit form are B2C surfaces and never appear on a B2B page.
- Stripe links and the Kit form UID are live production integrations, never placeholders.

## Code Review Rules

Codex and CodeRabbit apply these. Review changed behavior for bugs as well as these project
rules. For each finding, identify the trigger, actual and expected behavior, and concrete
consequence, with the relevant file and lines. Report actionable defects introduced by the
change, and distinguish them from existing issues or optional preferences.

Mechanical checks belong in CI. Do not repeat a check's existing finding, but review gaps
in coverage and checks that silently skip or pass the wrong condition. A skipped check is
not a passing check. The voice linter lives in the private repo and may be absent from a
cloud checkout of this website. Report that limitation rather than claiming a voice pass.

The groups below describe repository expectations, not a mapping to the reviewer's severity
scale. Assign severity from the demonstrated impact. Each rule states the problem, then
the safe path. For sensitive findings, name the location and kind of exposure without
copying private details or secret values into a public review comment.

For attribution findings, verify the original PR commits against GitHub's commit metadata.
The cited commit must belong to the PR. Local review-workspace metadata alone is not
evidence that the submitted commit has the wrong author, committer or trailers. If the
original metadata is unavailable, report the verification limit rather than a violation.

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
- A manual edit under `agents/**`. Safe path: change the source in the internal repo and
  regenerate with the documented publisher. Publisher output is allowed in regeneration
  PRs. Review that output for publication errors without requesting manual HTML fixes.
- A Pages Function that trusts input without validating it, logs request bodies, or stores a
  secret in code. Safe path: env bindings for secrets, verify Stripe signatures, `no-store`
  on dynamic responses.

### Craft

- A color, radius or spacing hardcoded instead of taken from the tokens at the top of
  `styles.css`. Safe path: add a token if one is missing.
- A stylesheet change without the `?v=` cache-bust bumped on every page that loads it.
- Missing or unhelpful `alt` text on a meaningful image, a skipped heading level, an interactive element
  unreachable by keyboard, a custom control with no visible focus state, an image without
  `width` and `height`. Safe path: meaningful images have useful alt text and genuinely
  decorative images use `alt=""`. Accessibility ships inside the feature, not after it.
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

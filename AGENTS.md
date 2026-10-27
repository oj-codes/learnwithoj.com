# AGENTS.md

The working agreement for this repo is `CLAUDE.md`, which every agent reads first. It holds
the business context, the page structure, the design tokens, the brand voice rules and the
commit conventions. This file exists for the reviewers that look for it by this name, Codex
and CodeRabbit among them, and it adds nothing that `CLAUDE.md` does not already say.

## Code Review Rules

Review the diff against these, in this order of severity.

**Blockers.**
- A build step, a `package.json`, a bundler or a framework. The site is plain HTML, CSS and
  vanilla JS by decision, through launch.
- Any email address other than `oj@learnwithoj.com`, any secret, token or key, or a client's
  name that is not already on the public site.
- A booking or contact CTA that does not go through `https://book.learnwithoj.com`.
- Stripe Checkout links or the Kit email form on a B2B page (`showcase.html` or any page
  aimed at companies). Those are B2C surfaces only.
- Changes to the 1% for the Planet footer block that alter its wording, logo, size or link.
  That block is a compliance surface and its wording is theirs.
- Edits to `agents/**`. Those pages are generated from the internal repo and reviewed there.

**Craft and correctness.**
- Colors hardcoded instead of taken from the tokens at the top of `styles.css`.
- A change to `styles.css` without the `?v=` cache-bust parameter bumped on every page that
  loads it.
- Missing or meaningless `alt` text, a skipped heading level, an interactive element that
  cannot be reached or operated by keyboard, a custom control with no visible focus state.
- Animation without a `prefers-reduced-motion: reduce` branch.
- Layout that would shift on load, images without `width` and `height`.
- Scripts that block render, fonts without `display=swap`.

**Voice, in any copy a visitor reads.**
- Em dashes anywhere, colons in prose, exclamation points.
- The bare word "engineers" where "software and infrastructure engineers" is meant.
- "Consultant" or "consulting". Filler like "unlock", "level up", "take it to the next level".
- British spellings. The site is American English except inside quoted material.
- Quoted material from other people is exempt from all of the above.

**Housekeeping.**
- A notable change without a `CHANGELOG.md` entry, or a new page without a row in the
  pages table in `CLAUDE.md`.
- A "Last updated" date typed by hand on a living page. The date comes from git through
  `tools/last-reviewed/check.py`.

Do not comment on the length of `CLAUDE.md`, on the absence of a framework, or on the
choice to keep one stylesheet. Those are decisions, not oversights.

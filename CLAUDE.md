# CLAUDE.md - Learn with O.J.

## What this site is

Static landing site for [learnwithoj.com](https://learnwithoj.com). O.J. (Olivia Wilcox) offers career strategy, resume review, and 1:1 technical sessions for software and infrastructure engineers. The site sells three paid services and gives away a free AI-Assisted Development guide via email capture.

## Tech stack

- Plain HTML, CSS, vanilla JS. No framework, no build step, no bundler.
- Hosted on GitHub Pages. `CNAME` points to `learnwithoj.com`.
- Deploys via `.github/workflows/ci.yaml` on push to `main`.
- Stripe Checkout for paid services (links live in `index.html` `#pricing`).
- Kit (ConvertKit) for the email-gated AI guide. Form UID: `36c7f50077`.
- GoatCounter for analytics (script tag in both pages' `<head>`).

## File layout

```
index.html              Landing page
resources.html          Free resources page
styles.css              All styles (single shared stylesheet)
assets/                 Hero/about videos, headshot, og-image
testimonials/           Avatars + testimonials.md source
docs/                   Planning notes for future work
CHANGELOG.md            Versioned change log (semver-ish)
CLAUDE-landing-page-v1.md   Archived spec from the original landing-page rebuild
CLAUDE-resources-v1.md      Archived spec from the resources + AI guide build
```

The two `CLAUDE-*-v1.md` files are historical build specs. The work in them has shipped. Don't follow them as instructions, but read them if you need context on why something is the way it is.

## Page structure

### `index.html` (top to bottom)

Sticky header → sections in this order, each with an `id`:

1. `.hero` — circular video portrait, starburst "Free AI Guide" badge linking to `/resources.html#ai-guide`, "Let's Talk First" CTA to LinkedIn
2. `.credentials` — 20+ years / 2x Senior Engineer / SWE + SRE
3. `#who-for`
4. `#what-you-get`
5. `#topics`
6. `#how-it-works`
7. `#about`
8. `#testimonials` — JS-powered horizontal carousel, arrows shown only when overflowing (script inline at the bottom of `index.html`)
9. `#pricing` — Fresh Squeeze ($275), Career Accelerator ($900), Focused Hour ($325). Stripe Checkout links.
10. `#faq`
11. `#vision` — "The bigger picture"
12. `#cta-bottom` — "Ready to get started?"

Footer + a sticky `.mobile-cta` button at the bottom on small screens.

### `resources.html`

1. `Free Resources` heading + intro
2. `#ai-guide` — AI-Assisted Development guide, Kit form embed, "no spam" note
3. `#jd-match` — Resume-to-Job Match Score, "Coming Soon" badge

## Design system

Defined as CSS custom properties at the top of `styles.css`. Source of truth — don't hardcode colors elsewhere.

- Dark theme: `--color-bg` `#0a0f1a`, alt `--color-bg-alt` `#0f1524`, cards `--color-bg-card` `#141c2e`
- Teal accent: `--color-accent` `#38b6c1` (buttons, links, highlights)
- Coral accent: `#e8755a` — used only on the hero starburst badge to contrast with teal
- Font: Inter via Google Fonts, weights 400/500/600/700
- Container max widths: `--container-max` 720px, `--container-narrow` 600px, plus `.container-wide` and `.container-full` modifiers

## Brand voice

- No em dashes. Combine parallel short sentences with "and" not periods.
- "Software and infrastructure engineers," not just "engineers."
- Honest, direct, no-BS. If something is hard, say it's hard.
- No filler ("unlock your potential," "take it to the next level").
- "How" over "why" for systemic critique.
- Pronoun over repeated name.

## Conventions

- Edit `styles.css` directly. Don't introduce a `css/` subdirectory or split into multiple files.
- Don't add a build step, package manager, or framework.
- Stripe links and the Kit form UID are the live production integrations. Don't swap them for placeholders.
- New `index.html` sections get an `id` and follow the existing `.section` / `.section-alt` alternating background pattern.
- Update `CHANGELOG.md` with notable changes. The current latest entry is `2.3.0`.
- For local preview: `python3 -m http.server 8000`. The Kit form won't fully work locally (needs Kit's JS to load against the live form), but it should render.

## External links

- LinkedIn (primary CTA): `https://www.linkedin.com/in/learnwithoj/`
- Email: `oj@learnwithoj.com`

## Future plans

(Fill in here. `docs/` already contains early planning notes for a LinkedIn posts section and skill descriptions.)

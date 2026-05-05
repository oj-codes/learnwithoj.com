# CLAUDE.md - Learn with O.J.

## What this site is

Static landing site for [learnwithoj.com](https://learnwithoj.com). O.J. (Olivia Wilcox) offers career strategy, resume review, and 1:1 technical sessions for software and infrastructure engineers. The site sells three paid services and gives away a free AI-Assisted Development guide via email capture.

The site has two distinct audiences served by different pages. See "Pages and audiences" below.

## About the business

**Founder.** O.J. is a working senior software and infrastructure engineer with 20+ years of experience. She has leveled up to senior twice, first as a Senior Software Engineer, then as a Senior Site Reliability Engineer. Career range spans scrappy startups (smart TV apps competing with Netflix) through Fortune 100 (American Express).

**Brand positioning.** "A working engineer in your corner." The "working" part is load-bearing. She is not a coach from the sidelines, she is still actively doing the work. That is what gives every claim on the site credibility.

**Two lines of business.**
- B2C: 1:1 mentoring, resume review (Fresh Squeeze), career strategy, technical sessions for individual software and infrastructure engineers who haven't gotten the senior title yet. Sold via Stripe Checkout. Lives on `index.html`.
- B2B: Fractional engineering leadership, senior software engineering contracts, infrastructure and SRE consulting, AI-assisted development training for teams. Direct billing at $325/hr cash. Sold via direct contact, no Stripe. Lives on `showcase.html` and any future B2B-specific pages.

**Brand personality.** Collaborative. Real. Experienced. Irreverent. Determined. The tension between irreverent and determined is the sweet spot. The site can be playful and direct without ever feeling lightweight, because underneath the directness is someone with two decades of showing up.

**Long-term vision.** A learning platform for software and infrastructure engineers where they run real-world scenarios and get adaptive feedback in real time. Khan Academy for adult tech professionals, free at the point of use, funded by professional services. The B2B and B2C revenue streams pay for the platform build.

## Craft and polish standards

The site itself is the proof of capability. Every visitor is making a snap judgment about whether a senior software and infrastructure engineer built this. Hold every shipped element to a craft bar that matches that claim, not to "good enough."

**The bar.** The reference points are Stripe, Linear, Vercel, Ramp, and Anthropic. Pages built by teams that take frontend craft seriously. If a shipped element wouldn't look at home on those sites, it's not done yet.

**What "generic" looks like, and how to avoid it.** The default output of any AI-generated landing page has tells. Avoid them deliberately.

| Generic (avoid) | Crafted (target) |
|---|---|
| Drop shadows on every card | Shadows used selectively, with intent. Most surfaces use border or background contrast instead. |
| Default linear transitions | Custom cubic-bezier or specific ease-out curves around 200 to 300ms for state changes. |
| One thing changes on a button click (text "Copied!") | Multiple coordinated changes (text, icon, color, subtle scale) timed together |
| Stock "fade in on scroll" animations on every section | Restrained motion. One or two intentional moments, not a parade. |
| Generic monospace `<pre>` blocks with thin borders | Considered code-block chrome. Real typography. JetBrains Mono, Fira Code, or a system monospace stack with proper fallbacks. |
| Buttons that change color on hover and that's it | Hover states that feel alive. Subtle background shift, optional micro-shadow, optional 1px translate, all at once. |
| Section headers with the same H2 + paragraph pattern repeating | Visual rhythm. Alternating backgrounds, varying content widths, occasional pull quotes or callouts to break the cadence. |
| Default focus rings (browser blue) | Custom focus state in the brand teal, with 2px outline and a small offset. Visible without being ugly. |
| Generic copy ("Copied!", "Submit", "Click here") | Specific copy in O.J.'s voice. Owns the moment. |

**Performance is craft.** A jank-free 60fps interaction sends a stronger signal than any animation. If something animates, it should be smooth. If it can't be smooth, don't animate.

**Polish reveals itself.** A visitor scrolling slowly should notice the small things. A subtle gradient on a section divider. A pull quote with proper hanging punctuation. A button that responds to keyboard activation the same way it responds to a mouse click. These details aren't visible at a glance and that's the point. They reward attention.

**Don't ship the first draft.** When a section is "done," look at it next to the same section on the reference sites above. If it doesn't hold up, it isn't done. Iterate or simplify until it does.

**Accessibility is part of craft, not a separate workstream.** Custom focus states, aria-live for dynamic content, semantic HTML, keyboard navigation that mirrors mouse interaction. These ship as part of the feature, not a follow-up PR.

## Tech stack

- Plain HTML, CSS, vanilla JS. No framework, no build step, no bundler.
- Hosted on GitHub Pages. `CNAME` points to `learnwithoj.com`.
- Deploys via `.github/workflows/ci.yaml` on push to `main`.
- Stripe Checkout for paid B2C services (links live in `index.html` `#pricing`). Not used on B2B pages.
- Kit (ConvertKit) for the email-gated AI guide. Form UID: `36c7f50077`.
- GoatCounter for analytics (script tag in every page's `<head>`).

## File layout

```
index.html              B2C landing page
showcase.html           B2B referral page (post-event landing)
resources.html          Free resources page
styles.css              All styles (single shared stylesheet)
assets/                 Hero/about videos, headshot, og-image
testimonials/           Avatars + testimonials.md source
docs/                   Planning notes for future work
CHANGELOG.md            Versioned change log (semver-ish)
CLAUDE-landing-page-v1.md   Archived spec from the original landing-page rebuild
CLAUDE-resources-v1.md      Archived spec from the resources + AI guide build
CLAUDE-showcase-v1.md       Build spec for the B2B showcase page
```

The `CLAUDE-*-v1.md` files are historical or active build specs. Read them for context on why something is the way it is, or to follow the active spec.

## Pages and audiences

| Page | URL | Audience | Visitor intent |
|------|-----|----------|----------------|
| `index.html` | `/` | Software and infrastructure engineers who haven't gotten the senior title yet | Find a mentor, fix their resume, level up their career |
| `resources.html` | `/resources` | Same as index | Get the free AI-Assisted Development guide |
| `showcase.html` | `/showcase` | Founders, operators, investors, and peers met at networking events. People considering hiring O.J. for B2B work or referring her to someone who would | Decide if she's worth hiring or referring, then act |

Critically: visitors to `/showcase` did NOT come looking for resume reviews. They scanned a QR code from a pitch room or got the link from a referral. The page must speak to them, not pivot them to B2C services.

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
8. `#testimonials` — JS-powered horizontal carousel
9. `#pricing` — Fresh Squeeze ($275), Career Accelerator ($900), Focused Hour ($325). Stripe Checkout links.
10. `#faq`
11. `#vision` — "The bigger picture"
12. `#cta-bottom`

Footer + a sticky `.mobile-cta` button at the bottom on small screens.

### `resources.html`

1. `Free Resources` heading + intro
2. `#ai-guide` — AI-Assisted Development guide, Kit form embed, "no spam" note
3. `#jd-match` — Resume-to-Job Match Score, "Coming Soon" badge

### `showcase.html`

See `CLAUDE-showcase-v1.md` for full structure. High level:

1. Hero with the B2B ask in writing
2. What I do for companies (four service buckets with technical specificity)
3. How engagements work (rate, billing, contractor model, trust-but-verify approach)
4. Recent B2B work
5. How I show up when it matters (the DST story + Maher quote)
6. Send someone my way (copy/paste referral template + direct contact)
7. Small footer pointer toward `index.html` for 1:1 mentoring traffic

## Design system

Defined as CSS custom properties at the top of `styles.css`. Source of truth, don't hardcode colors elsewhere.

- Dark theme: `--color-bg` `#0a0f1a`, alt `--color-bg-alt` `#0f1524`, cards `--color-bg-card` `#141c2e`
- Teal accent: `--color-accent` `#38b6c1` (buttons, links, highlights)
- Coral accent: `#e8755a` — used only on the hero starburst badge to contrast with teal
- Font: Inter via Google Fonts, weights 400/500/600/700
- Container max widths: `--container-max` 720px, `--container-narrow` 600px, plus `.container-wide` and `.container-full` modifiers

If a build needs a monospace font (code blocks, terminal aesthetics), add it as a CSS variable and use a real stack. JetBrains Mono or Fira Code via Google Fonts, falling back to `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.

## Brand voice

Hard rules. These are not preferences, they are enforced.

- **No em dashes.** Anywhere. Use commas, periods, parentheses, or "and".
- **No colons in prose.** Colons are fine in tables, key-value pairs, and code.
- **Combine parallel short sentences with "and"** instead of periods. "I help engineers level up and I help companies ship faster." not "I help engineers level up. I help companies ship faster."
- **Software and infrastructure engineers, not just "engineers".** Always specify the field. "Software engineer" or "software and infrastructure engineer" depending on context. Never the bare word "engineer" or "engineers" alone. Exception: when quoting someone verbatim, or when the surrounding sentence has already established the field within the same paragraph.
- **"How" over "why"** for systemic critique. "How the promotion process actually works" not "Why the promotion process is broken."
- **Pronoun over repeated name.** Don't say "O.J." over and over.
- **Honest, direct, no-BS.** If something is hard, say it's hard. No "unlock your potential" or "take it to the next level" filler.
- **Calm and competent, not hyped.** No exclamation points unless someone is genuinely shouting. No motivational LinkedIn-template energy.

## Brand personality keywords (use as guardrails when writing)

| Keyword | What it means in copy |
|---------|----------------------|
| Collaborative | She works alongside teams, not over them. Words like "together," "alongside," "with your team." |
| Real | Admits what she doesn't know. Specific over abstract. Concrete examples over claims. |
| Experienced | 20+ years, two leveled-up roles, name-recognizable companies (Netflix-competing startups, American Express). Don't be shy about this. |
| Irreverent | The juice/O.J. brand angle. Dry humor when it fits. The opposite of corporate. Don't force it but don't water it down. |
| Determined | She doesn't quit. Maps to "showed up for years" stories like the K8s case. |

If a piece of copy could come from any other engineer's site, it's missing the irreverence. If it sounds like a stand-up routine, it's missing the determination.

## Proof points and stories available for use

These are real and have been validated. Use as needed.

**Quotes (already on the site).**
- Kirk Whitehead (Cloud Engineer, Blackbaud): paying mentoring client. Featured on homepage. The customer-interview gold quote not yet on site is "She's not some consultant, she's your team member."
- Alexander Maher (Senior Director, DataSnipper): hired her twice across two companies. "One of the most collaborative and positive team members I've worked with." Notable: Maher was one of the senior bosses in the room during the DST production-down incident (see story below). His later rehire was a direct downstream effect of seeing her operate in that crisis. Pair the story and the quote together when possible, the connection is real and worth surfacing.
- Sobia Soomro (Frontend Web Developer, creator of Lumina): testimonial about a technical writing collaboration.

**Stories (use selectively).**
- The DST production-down story: a viral LinkedIn post (119K+ impressions, 64K+ members reached, hundreds of inbound DMs). The CEO's highest-visibility system was down in production. She walked into the room, started asking questions specific-to-broad, and the room found the daylight saving time bug together. Alex Maher was one of the bosses in that room. The lesson: the engineer who gets called into the crisis isn't always the one with the deepest technical knowledge, it's the one people trust to ask the right questions and keep the room moving. Use for engineering judgment under pressure, and as the natural setup for the Maher quote.
- The Kubernetes story: hired onto a contentious K8s migration where the dev team wanted AWS and the infra team wanted Docker EE. Was treated as the enemy. Proposed demoing both instead of picking sides. AWS won on merit. The team that resisted became her strongest references. One of those engineers (Kirk) became a paying client years later. Use to demonstrate conflict navigation and compounding career outcomes.
- The Amex intern story: 6 of 6 interns on her team chose to stay permanently and cited her as the reason. Her boss gave her the highest score that year because of it. Use to demonstrate talent development, mentorship, leadership without title.
- The Lucie/Guiltless deal: a founder approached her at a networking event, objected to her hourly rate, then closed an AI-assisted development training for her team after a discovery call with her CTO. Use to demonstrate B2B sales motion and rate confidence.

**Numbers (current as of May 2026, verify before publishing).**
- 20+ years of engineering experience.
- 2 leveled-up senior roles (SWE then SRE).
- 25 discovery conversations completed.
- 119K+ impressions on a viral April LinkedIn post (64K+ members reached, hundreds of DMs). 60K+ of those impressions in the first 7 days.
- Multiple B2B contracts landed including a fractional CTO role.

## Conventions

- Edit `styles.css` directly. Don't introduce a `css/` subdirectory or split into multiple files.
- Don't add a build step, package manager, or framework.
- Stripe links and the Kit form UID are live production integrations. Don't swap them for placeholders.
- New `index.html` sections get an `id` and follow the existing `.section` / `.section-alt` alternating background pattern.
- B2B pages should NOT include Stripe Checkout buttons or the AI guide email capture. Those are B2C surfaces only.
- Update `CHANGELOG.md` with notable changes. The current latest entry is `2.3.0`.
- For local preview: `python3 -m http.server 8000`. The Kit form won't fully work locally (needs Kit's JS to load against the live form), but it should render.

## Performance and accessibility expectations

The site is the proof of capability. Hold it to a high bar.

- Lighthouse 95+ on Performance, Accessibility, Best Practices, and SEO for every page.
- Semantic HTML. Use `<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<footer>` correctly.
- Heading hierarchy must be sequential (no skipping from `h2` to `h4`).
- All interactive elements must be keyboard accessible. Visible focus states.
- Honor `prefers-reduced-motion: reduce` for any animation.
- Color contrast meets WCAG AA at minimum.
- Every image has meaningful `alt` text or empty `alt=""` if decorative.
- No layout shift on load (CLS < 0.1).
- Favicon, OG image, and Twitter card meta tags on every page.

## External links

- LinkedIn (primary CTA): `https://www.linkedin.com/in/learnwithoj/`
- Email: `oj@learnwithoj.com`
- Stripe Checkout (B2C only):
  - Fresh Squeeze: `https://buy.stripe.com/bJe5kDeDH5kM8lJ9CEabK06`
  - Career Accelerator: `https://buy.stripe.com/6oU9ATbrvbJaeK7dSUabK05`
  - Focused Hour: `https://buy.stripe.com/9B67sL7bfcNefOb6qsabK04`

## Future plans

(Fill in here. `docs/` already contains early planning notes for a LinkedIn posts section and skill descriptions.)

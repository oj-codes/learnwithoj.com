# CLAUDE-showcase-v1.md

Build spec for the B2B showcase landing page. Active spec, follow it.

## What this page is

A standalone B2B landing page at `/showcase` (file: `showcase.html`). The destination for QR codes printed on event materials and shared in post-event referrals. Currently in use for the ALW Showcase on May 7, 2026, but designed to be reusable for any future pitch event or B2B referral context.

## Who's visiting

Three intents, in roughly equal mix.

1. **Hire-myself.** Founder or operator who heard the pitch, has a need, and is sizing up whether to engage.
2. **Refer-someone.** Connector who likes O.J. and is thinking of someone in their network who fits. Needs language they can copy and forward.
3. **Due-diligence.** Investor, peer, or curious operator who's checking whether the brand holds up under scrutiny.

Critically, NONE of these visitors are software or infrastructure engineers looking for resume reviews or 1:1 mentoring. The B2C services do not appear on this page beyond a small footer pointer.

## Goals in priority order

1. **Confirm the visitor is in the right place.** Hero acknowledges the showcase context within the first three seconds of reading.
2. **Restate the ask in writing.** Visitor heard the pitch. They forgot the rate, the service mix, or the contract structure. Put it in plain text.
3. **Demonstrate technical capability through specificity and craft.** No "I do infrastructure." Real stacks, real problem types, real engagement model.
4. **Make it easy to refer.** A copy/paste intro template with one-click copy is the highest-leverage element on the page.
5. **Make it easy to act.** Email and LinkedIn at minimum. Calendar link if available.

## The capability proof is the page itself

This is non-negotiable. Read the "Craft and polish standards" section in `CLAUDE.md` before starting. The bar is Stripe, Linear, Vercel, Ramp, Anthropic. Not "good enough." The page is going to be opened by founders and operators making a snap judgment about whether O.J. can be trusted with serious technical work. Their judgment will be made before they read a single word of the copy. Make the page itself the answer.

Specifically:

- Performance budget: Lighthouse 95+ on every category.
- Semantic HTML throughout.
- Real keyboard navigation with visible focus states (custom, not browser default).
- `prefers-reduced-motion` honored.
- Open Graph card so when the URL is shared in a DM or Slack, the preview is polished.
- One UX craft moment that earns its keep: the copy-to-clipboard interaction on the referral template. Specs below in section 7.

## Page structure

In order, top to bottom.

### 1. Hero (`#hero`)

Eyebrow line above the H1: `ALW SHOWCASE  ·  MAY 7, 2026` in small caps, mint accent.

H1: `Glad we met.`

Subhead: `I'm O.J. and I'm a working senior software and infrastructure engineer taking on B2B contracts at $325/hr in cash. Senior engineering, architecture, and AI-assisted development. Below is everything you need to refer me, hire me, or send a question my way.`

Primary CTA button: `Email me` (mailto:oj@learnwithoj.com)
Secondary CTA button: `Connect on LinkedIn`
Tertiary anchor link: `Or send a referral ↓` (anchors to `#refer`)

No video or image in the hero. Just type and CTAs. The page should load instantly.

### 2. What I do for companies (`#services`)

Section heading: `What I do for companies`

Four buckets in a 2x2 grid (collapses to one column on mobile). Each bucket has a short heading, a one-line summary, and a tight list of specifics.

**Senior software engineering**
Production engineering work alongside your existing team. Go, Python, JavaScript. Refactoring legacy systems toward maintainability. Code review at staff and principal level. Turning vibecoded MVPs into production-ready software.

**Infrastructure and SRE**
Kubernetes and AWS, including managed K8s migrations. Observability built around SLOs and error budgets. CI/CD pipelines and deployment automation in GitHub Actions. On-call design, incident response, postmortem culture. Cost optimization.

**AI-assisted development**
Training engineering teams to use AI tools effectively in their actual codebase. Building agentic workflows that ship to production, not demos. Code review and evals for AI-generated code. Closing the gap between AI prototypes and reliable software.

**Fractional engineering leadership**
Technical strategy at the CTO and VP-Engineering level for small companies. Build versus buy decisions. Hiring and team scaffolding. Bridging dev, infra, and product without political theater.

### 3. How engagements work (`#how`)

Section heading: `How engagements work`

Five points presented as a clean list with short explanations.

1. **Direct billing at $325/hr in cash.** No agency markup, no equity-only deals. Invoiced through Learn with O.J. LLC.
2. **Independent contractor.** 1099 in the US. Your team retains full control of priorities and IP.
3. **Trust-but-verify start.** Most engagements begin with a small, well-defined project before scaling up. The first 10 to 20 hours prove the fit before either side commits to more.
4. **Alongside your existing team, not over them.** No throw-it-over-the-wall consulting. Pair programming, code review, async writeups, and showing up to your existing meetings on your existing tools.
5. **Specialists when needed.** A vetted network for cybersecurity, ML, and other domains outside the software and infrastructure scope. Brought in transparently, billed directly to you.

### 4. Recent B2B work (`#proof`)

Section heading: `Recent work`

Four short blocks. No client names. Just the shape and outcome.

- **Fractional CTO engagement, currently active.** Technical strategy, hiring, architecture review for a small B2B SaaS company.
- **AI-assisted development training.** Closed Q1 2026 after a single discovery call with the company's CTO. Multi-session training program for their distributed engineering team.
- **25 discovery conversations completed in the first quarter.** Across founders, operators, and engineering leaders. Pipeline of additional B2B engagements building from those.
- **LinkedIn content engine compounding.** A career story posted in mid-April reached 119,000+ impressions, 64,000+ members, and generated hundreds of inbound DMs. Inbound is converting.

### 5. Voices (`#voices`)

Curated testimonial carousel, narrower scope than the homepage's. Three cards in this order:

1. **Mohammad Abuhaija** — Director, SRE & Enterprise DevOps at American Express (managed O.J.). Strongest manager-perspective credibility for B2B audiences.
2. **Tom Schaeffer** — Founder, Executive Ghostwriter (hired O.J. early in her career at Float Left Interactive).
3. **Sylke Lopez** — Senior Designer at Microsoft (Dycom colleague). The "early to AI" beat — quotes the 2018 ML chatbot workshops.

Skip Maher in this carousel — he is already the trust-section pull quote, including him here would dilute him. Skip Kirk (paying mentee, not a manager), Susan / Peter (peers), Sobia (peer collab on a writing piece).

Each card includes the company logo below the attribution. Logos are sized via per-logo CSS overrides (square brand icons larger than wordmark logos for legibility); see "Company logos" notes in `styles.css`.

### 6. How I show up when it matters (`#trust`)

Section heading: `How I show up when it matters`

This section uses the DST production-down story. It's been market-validated (119K+ impressions on the original LinkedIn post). The story directly demonstrates the engineering judgment companies pay senior engineers for. Some visitors will recognize it from LinkedIn, which creates a credibility multiplier ("wait, that was you?").

The section ties the story to the Alexander Maher quote through a transition that names him as one of the bosses in the room during the incident. This is real, not a narrative invention. The connection is what makes the rehire data point hit harder.

**Story copy** (use this exact text, structured as paragraphs):

`A few years ago my boss walked past my desk and said "there's a problem" without stopping. I grabbed my laptop and followed.`

`The CEO's highest-visibility system was down in production. The room was full of senior infrastructure engineers and big bosses, with one developer eyes-down on his laptop trying to find it.`

`I started asking questions. Specific first, the code, the deployment, the config. When everything checked out I pulled back. What changed in the environment? What changed in the world? The room joined in. Daylight saving time came up. The dev checked. That was it.`

`I don't remember exactly who landed on it and it doesn't matter. We found it together and that's how it's supposed to work.`

**Punchline** (visually distinct, larger type, possibly with mint accent on key phrases):

`The engineer who gets called into the crisis isn't always the one with the deepest technical knowledge. It's the one people trust to ask the right questions and keep the room moving.`

**Transition to the quote** (smaller, sets up the testimonial):

`Alex Maher was one of the bosses in that room. A few years later he hired me. A few years after that he hired me again at a different company.`

**Pull quote** (Alexander Maher, styled distinctly with attribution below):

`I had the pleasure of working with Olivia across two companies. Having the opportunity to rehire someone says a lot about the trust and confidence you have in their character and contributions, and Olivia fully earned that confidence. She is one of the most collaborative and positive team members I've worked with.`

Attribution: `Alexander Maher  ·  Senior Director of Product, DataSnipper`

**Visual notes for this section.** This is the emotional center of the page. Treat the story like an editorial piece, not a marketing block. Slightly tighter type, more generous line height (1.7 to 1.8), narrower content width than the surrounding sections (around 600 to 640px), centered. The punchline should visually stop the scroll. Consider a thin mint accent line beside it, or a subtle change in background. The pull quote should feel like a quote, with proper hanging punctuation and visible attribution.

### 7. Send someone my way (`#refer`)

Section heading: `Send someone my way`

Lead line: `If you know a company that fits, here's intro language you can copy and forward. Edit it however you want.`

The template, displayed in a styled block. **This is the craft moment of the page.** The block and the button must feel handcrafted, not generic. See "Craft specs for the referral block" below.

Template text:

```
Subject: Quick intro: O.J. Wilcox (Learn with O.J.)

Hey [Name],

Wanted to introduce you to O.J. Wilcox, founder of Learn
with O.J. (learnwithoj.com).

She's a working senior software and infrastructure engineer
with 20+ years of experience across startup and Fortune 100
environments. She does fractional engineering leadership,
architecture and infrastructure consulting, and AI-assisted
development training for engineering teams. Currently taking
on B2B contracts at $325/hr in cash, direct billing.

I met her recently and was impressed by her depth and how she
operates. Worth a 15-minute conversation if you have an
engineering or AI need on your radar.

She's at oj@learnwithoj.com or learnwithoj.com.

[Your name]
```

#### Craft specs for the referral block (read carefully)

The default version of this UI is a `<pre>` with monospace and a "Copied!" button. That is the floor, not the target. Build the considered version.

**The block itself.**

- Use a real monospace font, not the browser default. Add JetBrains Mono or Fira Code to the site (Google Fonts) and use a proper fallback stack: `'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo, Consolas, monospace`.
- Background: slightly darker than the surrounding section, with a subtle border. Not just a flat box. Consider a 1px border in a teal-tinted neutral, or a `box-shadow: inset 0 1px 0 rgba(255,255,255,0.04)` style highlight on the top edge.
- Typography: line-height around 1.6 to 1.7. Font size around 14 to 15px. Comfortable for reading, not cramped.
- Padding: generous. At least 1.5rem on all sides. Code blocks that feel cramped read as cheap.
- Rounded corners at the same radius the rest of the site uses (check `styles.css`).
- Optional polish: a subtle terminal-style header bar with three small dots in muted colors. If used, keep it simple. No "code editor" line numbers, that's overkill.
- Visual hierarchy on the placeholders: `[Name]` and `[Your name]` should be subtly differentiated, perhaps in a muted teal, so the visitor's eye catches what they need to edit before sending.

**The copy button.**

- Position the button below the block, right-aligned or centered. Not floating inside the block.
- Default state: text reads `Copy intro template` with a small clipboard icon to the left. Use an inline SVG icon, not an emoji.
- Hover state: multiple coordinated changes. Subtle background shift toward teal, the icon grows by a hair (transform: scale(1.05)), and a 1px translate-y of -1px to lift the button. Transition all three with `transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1)`.
- Focus state: 2px teal outline with 4px offset. Keyboard activation (Enter or Space) triggers the same coordinated changes as a click.
- Click state (success): the button transforms simultaneously across multiple properties. Text changes from `Copy intro template` to `Off it goes ✓` (in O.J.'s voice, not generic). Icon swaps from clipboard to checkmark. Background shifts to a muted mint (use the brand mint token). Slight scale-up to 1.02 then back. All within 250ms. Hold the success state for 2 seconds, then revert with the same easing.
- Add `aria-live="polite"` on a visually-hidden status element that announces "Intro template copied to clipboard" so screen readers get parity with sighted users.
- Implementation: `navigator.clipboard.writeText` with a fallback to `document.execCommand('copy')` for older browsers. The fallback should be a working textarea-based copy, not a console error.
- Without JavaScript: the button still renders and is styled, but does nothing on click. The template text remains fully selectable for manual copy.

**Anti-patterns to avoid in this block.**

- Don't use a generic "Copied!" message. Use the specific copy in the spec.
- Don't use only a color change for the success state. Multiple changes happen together.
- Don't use a default linear transition. Use a cubic-bezier or proper ease-out.
- Don't rely on a tooltip to explain the copy action. The button label is the explanation.
- Don't use an emoji where an SVG icon belongs. Emojis render inconsistently across platforms.
- Don't ship without testing the keyboard path. Tab to the button, press Enter, watch the success state, verify the announcement reaches a screen reader.

#### Direct contact options

Below the copy button, three direct contact options as a horizontal list with appropriate spacing.

- `Email: oj@learnwithoj.com`
- `LinkedIn: linkedin.com/in/learnwithoj`
- (Optional, if calendar link exists) `Book 15 minutes: [calendar URL]`

### 8. Footer pointer (`#footer-pointer`)

A small section just above the footer.

`Looking for 1:1 career strategy or resume review for software and infrastructure engineers? Visit learnwithoj.com →`

Linked to `/`. Styled subtle, not a primary CTA.

### Footer

Standard site footer. Same as other pages.

## Visual design notes

- Inherit `styles.css` and the dark theme. No new CSS framework, no new color tokens beyond what's needed for the monospace stack.
- Match the existing site's typography (Inter, weights 400/500/600/700) and spacing rhythm.
- Section pattern: alternate `.section` and `.section-alt` for visual rhythm, same as `index.html`.
- The hero on this page is text-only, no video. Visually quieter than the homepage hero. That's intentional, the page is for serious visitors not first-time browsers.
- One mint accent (`#6ee7b7` or similar) on the eyebrow line and possibly the success state of the copy button. Use sparingly, the rest stays teal.
- The DST story section breaks the column rhythm slightly. Narrower content width, larger line height, treats the story like editorial. This is intentional contrast.

## Technical requirements

- File location: `showcase.html` at the repo root. GitHub Pages will serve this at `/showcase` automatically.
- Page weight under 100 KB excluding the Inter font (which is already cached from the homepage). The added monospace font is the largest new asset.
- No JS frameworks. Vanilla JS for the copy-to-clipboard interaction.
- All interactive elements must be keyboard-accessible with visible focus states.
- `prefers-reduced-motion: reduce` honored. The page should have minimal animation anyway.
- Meta tags: title, description, Open Graph (title, description, image, url, type), Twitter card (summary_large_image).
- OG image: reuse `assets/og-image.png` for now. A showcase-specific OG image can be added later.
- Page must work without JavaScript. The copy-to-clipboard button should still be visible and the email is selectable for manual copy.
- Add the GoatCounter analytics tag in `<head>` consistent with other pages.

## QA checklist before merge

- [ ] Lighthouse 95+ on Performance, Accessibility, Best Practices, SEO
- [ ] Heading hierarchy is sequential (h1, h2, h2, h2 ...)
- [ ] All interactive elements reachable by Tab, with visible focus
- [ ] Custom focus state, not browser default
- [ ] Copy-to-clipboard works in Chrome, Safari, Firefox
- [ ] Copy button success state has multiple coordinated changes (text, icon, color, scale), not just a text swap
- [ ] Copy button success copy is `Off it goes ✓`, not `Copied!`
- [ ] Aria-live announcement fires on successful copy
- [ ] Page renders correctly with JS disabled (template still readable, copy button gracefully degraded)
- [ ] Mobile (375px) and tablet (768px) layouts both look intentional
- [ ] DST story section has distinct typography (narrower width, larger line height)
- [ ] The Maher transition line ("Alex Maher was one of the bosses in that room...") is present and connects the story to the pull quote
- [ ] Pull quote has visible attribution and proper styling
- [ ] No bare word "engineer" or "engineers" anywhere in the page
- [ ] No em dashes anywhere
- [ ] No colons in prose
- [ ] All Stripe links omitted (this is B2B, no checkout)
- [ ] AI guide / Kit form omitted (B2C surface only)
- [ ] OG image and Twitter card meta tags present
- [ ] CHANGELOG.md updated to a new entry (likely 2.4.0)
- [ ] Section side-by-side comparison done against Stripe, Linear, Vercel, Ramp, or Anthropic. Each section holds up.

## Iterative build prompts

Feed these to Claude Code in order. Each prompt produces a verifiable result. Don't skip ahead, the order matters because each step builds on the previous one.

### Prompt 1: Skeleton and routing

```
Read CLAUDE.md and CLAUDE-showcase-v1.md fully before starting. Pay particular
attention to the "Craft and polish standards" section in CLAUDE.md. The bar
for this page is Stripe, Linear, Vercel, Ramp, Anthropic. Not "good enough."

Create showcase.html at the repo root. It should be a fully valid HTML document
that loads styles.css, includes the same <head> metadata pattern as resources.html
(GoatCounter analytics, favicon, viewport, charset), and uses the same site
header and footer markup pattern as the other pages.

Use the same sticky header used on index.html and resources.html, with the
"Learn with O.J." brand link going to / and the "Let's Talk" link going to
LinkedIn (https://www.linkedin.com/in/learnwithoj/).

Inside <main>, create empty <section> elements with these IDs in order:
hero, services, how, proof, trust, refer, footer-pointer. Each section should
have a TODO comment indicating what content goes there.

Set the <title> to "Learn with O.J. - For Companies and Referrers" and the
meta description to "B2B engineering, architecture, and AI-assisted development
work from a working senior software and infrastructure engineer with 20+ years
of experience."

Add Open Graph and Twitter card meta tags. Reuse assets/og-image.png for now.

Then start a local preview server and confirm the page loads at
http://localhost:8000/showcase and inherits the site styles correctly.
Don't touch any other files yet.
```

### Prompt 2: Hero section

```
Implement the #hero section in showcase.html using content from
CLAUDE-showcase-v1.md exactly. The eyebrow line is "ALW SHOWCASE  ·  MAY 7, 2026"
in small caps with the mint accent (#6ee7b7 or whichever closest token exists
in styles.css). The H1 is "Glad we met." The subhead is the full paragraph
specified in the spec.

Two CTA buttons. Primary "Email me" links to mailto:oj@learnwithoj.com. Secondary
"Connect on LinkedIn" links to https://www.linkedin.com/in/learnwithoj/. Use the
existing button styles from styles.css. Below the buttons, an anchor link
"Or send a referral ↓" pointing to #refer.

The hero should be visually quieter than the homepage hero. No video, no image,
generous vertical whitespace, the type does the work. Match the typographic
scale of the homepage hero so it feels like the same site.

Hover states on the buttons should feel alive (subtle background shift, optional
1px translate, transition over 200-300ms with a real ease curve, not linear).
Focus states must be custom (teal outline, 2px, with offset), not browser default.

Test on mobile (375px). The CTAs should stack vertically and touch targets
should meet the 44x44 minimum. Don't ship anything that fails that.
```

### Prompt 3: Services and engagement model

```
Implement #services and #how using the content in CLAUDE-showcase-v1.md.

#services has the heading "What I do for companies" and a 2x2 grid of four
service buckets. On mobile, the grid collapses to one column. Each bucket
has a bold heading, a short summary, and a tight bulleted or comma-separated
list of specifics. Match the visual pattern of the #what-you-get section on
index.html so it feels native to the site.

#how has the heading "How engagements work" and the five numbered points
specified in the spec. Use a clean numbered list with short explanations.
Match the visual pattern of #how-it-works on index.html.

Apply the alternating .section / .section-alt background pattern. After this
prompt, the page should read top-to-bottom as a coherent B2B story even
though the bottom half isn't built yet.
```

### Prompt 4: Proof and the DST story

```
Implement #proof and #trust using the content in CLAUDE-showcase-v1.md.

#proof has the heading "Recent work" and the four short blocks. No client names.
Style as a clean list, not as cards (we want it to feel matter-of-fact, not
like marketing). Each block has a short bold heading and a one or two sentence
description.

#trust has the heading "How I show up when it matters" and uses the DST
production-down story. The exact paragraph text is in the spec. Use it
verbatim.

This section is the emotional center of the page. Treat it differently from
the others. Narrower content width (around 600-640px), centered. Larger
line height (1.7-1.8). The story reads like editorial, not like a marketing
block.

The punchline ("The engineer who gets called into the crisis...") should
visually stop the scroll. Larger type, possibly with a thin mint accent line
beside it or a subtle background change. It must feel like a moment.

Then the transition line ("Alex Maher was one of the bosses in that room.
A few years later he hired me. A few years after that he hired me again at
a different company.") at smaller scale. This line is the bridge between
the story and the testimonial, and the connection is real, not narrative
glue. Maher was actually in the room. Treat it as a beat, not throwaway
copy. Allow it visual room.

Then the Alexander Maher pull quote, styled visually distinct (proper hanging
punctuation, larger type with appropriate line height, italics optional).
The attribution reads "Alexander Maher  ·  Senior Director of Product,
DataSnipper" below the quote.

Match the alternating section background pattern.
```

### Prompt 5: Referral kit with the craft moment

```
This is the craft moment of the page. Read the "Craft specs for the referral
block" section in CLAUDE-showcase-v1.md fully before writing any code. The
default version of this UI is generic. Build the considered version.

Implement #refer using the content in CLAUDE-showcase-v1.md.

The intro template lives in a styled block with these specifications:

1. Add JetBrains Mono via Google Fonts. Use the full fallback stack:
   'JetBrains Mono', 'Fira Code', ui-monospace, SFMono-Regular, Menlo,
   Consolas, monospace.
2. Background slightly darker than the surrounding section, with a subtle
   1px border in a teal-tinted neutral, plus an inset 1px highlight on the
   top edge.
3. Generous padding (1.5rem minimum). Line-height 1.6-1.7. Font size 14-15px.
4. Rounded corners matching the rest of the site.
5. The placeholders [Name] and [Your name] should be subtly differentiated
   (muted teal) so the visitor's eye finds them.

The template text from the spec must be preserved exactly, including line
breaks.

The copy button below the block:

1. Default state: "Copy intro template" with an inline SVG clipboard icon
   to the left. No emoji.
2. Hover: subtle background shift toward teal, icon scale to 1.05, 1px
   translate-y of -1px. All transitioned together with
   transition: all 200ms cubic-bezier(0.4, 0, 0.2, 1).
3. Focus: 2px teal outline with 4px offset. Keyboard (Enter/Space) activation
   triggers the same behavior as click.
4. Success state on copy: text changes to "Off it goes ✓" (NOT "Copied!"),
   clipboard icon swaps to checkmark, background shifts to muted mint,
   slight scale-up to 1.02 then back. All within 250ms. Hold for 2 seconds,
   revert with same easing.
5. Aria-live="polite" status element (visually hidden) announces "Intro
   template copied to clipboard" on success.
6. navigator.clipboard.writeText with document.execCommand('copy') fallback
   using a working textarea-based approach, not a console error.
7. Without JavaScript: button still renders and is styled, just inert on
   click. Template text remains selectable.

Test the keyboard path explicitly. Tab to the button, press Enter, verify
all four state changes happen, verify the screen reader announcement.

Below the button, three direct contact options as a horizontal list. Email
is mailto:, LinkedIn is the full URL.

After this section, implement #footer-pointer with the small "Looking for 1:1"
text linking to /. Style subtle, not a primary CTA.

Before declaring this done, open Stripe, Linear, or Anthropic in another tab.
Compare your copy block to a similar UI element on those sites. If yours
doesn't hold up, iterate.
```

### Prompt 6: Polish and ship

```
Final pass on showcase.html.

1. Run a Lighthouse audit. Target 95+ on Performance, Accessibility, Best
   Practices, and SEO. Fix anything below that bar. Common issues: missing
   alt text, contrast ratios, missing aria labels.

2. Test keyboard navigation through the entire page. Every interactive
   element should be reachable by Tab, in logical order, with a visible
   custom focus state (not the browser default).

3. Verify prefers-reduced-motion is honored. If there are any transitions
   or animations, they should be removed or shortened when the user has
   reduced motion enabled.

4. Test the page with JavaScript disabled. The copy-to-clipboard button
   should still be visible. The template text should still be selectable.
   Email and LinkedIn links should still work.

5. Run the page through a contrast checker. WCAG AA minimum on every
   text/background combination.

6. Test responsive layout at 320px, 375px, 768px, 1024px, and 1440px.
   Each width should look intentional, not like the page just happened
   to fit.

7. Side-by-side comparison: open showcase.html next to a comparable section
   on Stripe, Linear, Vercel, Ramp, or Anthropic. Each section should hold
   up. If any section feels like a step down in craft, iterate or simplify
   until it doesn't.

8. Update CHANGELOG.md with a new version entry (likely 2.4.0). Document
   the showcase page addition.

9. Run the QA checklist in CLAUDE-showcase-v1.md. Every item must pass.

When everything passes, commit on a feature branch (suggested name:
showcase-page-v1) and push. Don't merge to main until O.J. has reviewed
the live preview.
```

## After ship

Things to do once the page is live, in roughly this order.

- Verify the QR code resolves to the live page from a real phone, not just desktop.
- Set up a 301 or 302 redirect from `/alw` to `/showcase` if a future event uses a different slug. (Not needed for May 7, but worth thinking about.)
- Add a showcase-specific Open Graph image to `assets/` and reference it in showcase.html.
- Sweep `index.html` for bare "engineer" usage and fix per the language rule. (Out of scope for this build but worth scheduling.)

## Out of scope for v1

- A custom calendar booking embed. Email is sufficient for May 7.
- A separate `/refer` page. The `#refer` section on showcase.html is enough.
- Branded showcase OG image. The default OG image is fine for v1.
- Any kind of form or data capture. Direct contact only.

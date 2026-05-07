# Changelog
All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com), and this project adheres to semantic versioning where possible.


## [2.4.0] - 2026-05-06
### Added
- Showcase page (`showcase.html`) at `/showcase`, the B2B referral landing for ALW Showcase (May 7, 2026) and reusable for future pitch contexts. Hero with portrait video, four service buckets, engagement model, recent B2B work, the DST production-down story paired with the Maher pull quote, copy-to-clipboard referral template (success + error states with `aria-live` announcements), and a quiet pointer back to the B2C site
- `#voices` testimonial carousel on the showcase page, curated to former managers (Mohammad Abuhaija, Tom Schaeffer) and the AI-early peer (Sylke Lopez)
- Company logos rendered below each testimonial-author block on both `index.html` and `showcase.html` carousels — Microsoft, American Express, Blackbaud, DataSnipper, Meal Suite, Palm Beach State College, Tom Schaeffer & Co. Brand colors preserved; per-logo sizing for icons vs wordmarks; subtle outline on DataSnipper to delineate its navy square from the dark card
- JetBrains Mono (weights 400/500), loaded only on the showcase page, for the referral template's monospace block
- New design tokens: `--color-mint: #6ee7b7`, `--color-accent-deep: #157d86` (darker brand teal for solid CTAs that need WCAG AA white-on-teal contrast), and `--font-mono`
- Secondary button style (`.btn-secondary`) for ghost/outline CTAs
- Visually-hidden `.sr-only` utility for screen-reader-only content (used by the copy-button `aria-live` status node)
- Custom focus-visible rings on every link and button across the site (2px brand teal, 4px offset)
- `prefers-reduced-motion` handling for `.btn-primary` / `.btn-header` / `.feature-card` hover transforms, the testimonial carousel's scroll animation (jumps to target instead of 300ms RAF easing), and the hero `<video>` autoplay/loop (paused on load, poster image stands in)
- No-JavaScript fallback for the showcase referral template (button hidden via `.js`-class gate, italic instruction line shown via `<noscript>`)

### Changed
- Hero video re-encoded **10.97 MB → 327 KB** (480×588, x264 CRF 20, no audio, web-optimized) — sitewide load speedup
- Hero JPG poster shrunk **315 KB → 43 KB** at 395×480 — sitewide
- `.btn-header` "Let's Talk" CTA: background switched from `--color-accent` to `--color-accent-deep` (raises white-on-teal contrast from 2.43:1 to 4.87:1, clears WCAG AA), font-weight bumped 500 → 600
- Footer brand and email text shifted from `--color-text-dim` to `--color-text-muted` (clears WCAG AA at 15px)
- Hero eyebrow gradient now references `--color-mint` token instead of a hardcoded hex (no visual change)
- Carousel arrow visibility switched from `display: none/flex` toggle to `visibility/opacity` toggle so the flex row width stays stable — eliminates the layout-reflow stutter at scroll boundaries
- Testimonial track now uses `overscroll-behavior-x: contain` to prevent rubber-band on trackpad gestures at the boundary
- Google Fonts links on the showcase page load non-blocking via `preload` + `media="print" onload` swap pattern

## [2.3.0] - 2026-03-17
### Added
- Resources page (`resources.html`) with shared nav bar, footer, and consistent styling
- "Resources" link in navigation on all pages
- AI-Assisted Development guide section with Kit (ConvertKit) email capture form
- "Coming Soon" teaser for Resume-to-Job Match Score tool
- Starburst badge in hero section linking to the free guide (coral accent, SVG shape, positioned relative to profile image)

## [2.2.0] - 2026-03-16
### Added
- Sobia Soomro testimonial

### Changed
- Redesigned testimonials section as a horizontal carousel with arrow navigation
- Arrows appear only when cards overflow the viewport
- Testimonials section now spans full page width
- Updated service pricing: Fresh Squeeze $150 → $275, Focused Hour $200 → $325, Career Accelerator $550 → $900
- Updated Stripe payment links for all three services
- Updated Career Accelerator savings copy ($50 → $75)

## [2.0.0] - 2026-03-12
### Added
- Three service tiers: Fresh Squeeze (resume review), Career Accelerator (3-session bundle), Focused Hour (single session)
- "How It Works" section with three steps: Connect, Clarity, Go
- Pricing cards with Stripe Checkout buttons and "Start Here" badge on Fresh Squeeze
- FAQ questions for new service tiers (which service to start with, what happens after payment, upgrading)

### Changed
- Primary CTA changed from "Book a Session - $200" to "Let's Talk First" linking to LinkedIn
- Hero eyebrow and subtitle copy updated to reflect broader positioning
- "Who This Is For" and site copy updated to match brand voice guidelines
- Navigation button changed from "Book Session" to "Let's Talk"

### Removed
- Single $200/hr mentoring session offering

## [1.4.0] - 2025-12-19
### Added
- Peer support language in "Who This Is For" section for senior engineers
- Peer support context in FAQ answers

## [1.3.0] - 2025-12-17
### Changed
- Replaced static hero headshot with animated video (MP4 with poster fallback)
- Added video to About section

## [1.2.1] - 2025-12-12
### Fixed
- Added site.webmanifest for favicons
- Added favicon files

## [1.2.0] - 2025-12-11
### Added
- Open Graph meta tags for social sharing on LinkedIn, Facebook, and other platforms
- Twitter Card meta tags for rich previews when shared on Twitter/X
- Branded OG image for social sharing previews

## [1.1.0] - 2025-12-11
### Added
- GoatCounter analytics for privacy-friendly visitor tracking

### Improved
- Updated README to reflect current tech stack and project structure

## [1.0.0] - 2025-12-10
### Added
- Launched the new Learn with O.J. mentoring landing page.
- Implemented a dark, teal-accented design system with refined typography.
- Added hero section with CTA, supporting icon, and updated messaging.
- Added sections for offer details, pricing, how it works, vision, and FAQ.
- Added About section with headshot and revised first-person narrative.
- Added public commitment that mentoring revenue supports the learning platform mission.

### Improved
- Enhanced page structure, spacing, and alignment for clarity and readability.
- Added subtle animations and microinteractions for a polished experience.

### Removed
- Deprecated previous Hugo-based structure and placeholder content.


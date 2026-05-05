# CLAUDE.md - Learn with O.J. Site Enhancement: Resources + Guide Download

## Context

This is an incremental update to the Learn with O.J. landing page (learnwithoj.com). The site is static HTML/CSS/JS. The current page is a single-page landing with services, testimonials, FAQ, and CTAs. We are adding:

1. A "Resources" teaser section on the landing page
2. A new `/resources` page (resources.html) that hosts free resources
3. The first resource: an AI-Assisted Development guide (PDF) gated behind email capture via Kit (ConvertKit)

The existing CLAUDE.md from the previous landing page revamp is still the source of truth for brand voice, page structure, and design direction. This file covers only the NEW work being added.

## Brand Voice Reminders

- No em dashes. Combine parallel short sentences with "and" not periods.
- Use "software and infrastructure engineers" not just "engineers"
- No filler phrases like "unlock your potential" or "take your career to the next level"
- Honest, direct, no-BS tone. If something is hard, say it's hard. Don't oversell.
- Use "how" over "why" for systemic critique
- Pronoun over repeated name

## What We're Building

### 1. Resources Teaser Section (on index.html)

**Placement:** Between the "The bigger picture" section and the "Ready to get started?" CTA section.

**Purpose:** Surface the free guide and drive traffic to /resources. Keep it brief. This is a teaser, not the full resources page.

**Content direction:**
- Short heading like "Free Resources" or "Resources for Engineers"
- One card for the AI-Assisted Development guide with a brief description (2-3 sentences max), a thumbnail or icon, and a CTA that links to /resources or directly to the guide section on that page
- Design note: leave room for additional resource cards in the future (the resume/JD match tool, templates, etc.). Use a grid or flexible layout that works with 1 item now but scales to 3-4 items later

**Copy for the guide card:**
- Title: "AI-Assisted Development: A Practical Guide for Engineering Teams"
- Description should convey: it's a 10-page guide covering the AI development landscape, how to implement it on your team, and things people aren't talking about. Written by a working engineer, not a vendor pitch.
- CTA: "Get the Guide" linking to /resources#ai-guide or similar anchor

### 2. Resources Page (resources.html)

**Structure:**
- Same nav bar as index.html (Learn with O.J. logo left, "Let's Talk" button right linking to https://www.linkedin.com/in/learnwithoj/)
- Page heading: "Resources" or "Free Resources"
- Brief intro paragraph: something like "Tools, guides, and resources I'm building to help software and infrastructure engineers level up. Everything here is free."
- Resource cards/sections below, starting with just the AI guide

**AI-Assisted Development Guide Section:**
- Anchor: #ai-guide
- Title: "AI-Assisted Development: A Practical Guide for Engineering Teams"
- Description: 3-5 sentences expanding on what the guide covers. Emphasize that it's practical and written from hands-on experience, not theory. Mention it helped close a training deal (social proof without being salesy, e.g. "This guide has been used by engineering teams evaluating how to adopt AI-assisted development workflows.")
- Email capture form: Kit (ConvertKit) embedded form
- The form collects first name (optional) and email (required)
- On submit, Kit handles the delivery. The person gets an automated email with the PDF download link.
- Below the form, a small note: "No spam. Just the guide. You can unsubscribe anytime."

**Future-proofing:**
- The page should have a clean layout that accommodates additional resources over time
- Each resource gets its own section with an anchor ID
- Consider a "Coming Soon" placeholder for the resume/JD match tool with a brief teaser description. Something like: "Resume-to-Job Match Score: Paste your resume and a job description, get a keyword match score and tailoring suggestions. Coming soon." This sets expectations and builds interest without committing to a timeline.

### 3. Kit (ConvertKit) Integration

**How it works:**
- O.J. creates a Kit account (free tier) at kit.com
- Creates a "Form" in Kit for the AI guide download
- Uploads the PDF to Kit and sets it as the incentive email attachment (or links to a hosted version)
- Kit generates an HTML embed snippet
- We paste that snippet into resources.html in the guide section

**Implementation notes:**
- The Kit form embed is a chunk of HTML + JS that Kit provides. Drop it in as-is.
- Style the surrounding container to match the site's look and feel (dark background, teal accents, clean typography consistent with the rest of the site)
- The Kit form itself can be styled via Kit's form builder to roughly match, but don't fight it too hard. Getting it functional and reasonably styled is the priority.
- Test that the form submits correctly and the automated email delivers the PDF

## Design Guidelines

Match the existing site's visual language:
- Dark background (the current site uses a dark theme)
- Teal accent color for buttons and highlights (match the existing "Let's Talk" and service CTA buttons)
- Clean, readable typography consistent with the rest of the page
- Subtle animations are fine (the site already uses them for the portrait and images) but don't overdo it
- Mobile responsive, same as the rest of the site

## File Structure

```
learnwithoj.com/
  index.html          # existing, add resources teaser section
  resources.html      # new page
  assets/
    ai-guide-thumb.png  # thumbnail or icon for the guide card (create or use placeholder)
  css/
    (existing styles)   # add new styles inline or in existing stylesheet
```

## What NOT to Do

- Don't restructure or redesign the existing page sections. We're only ADDING the resources teaser between "The bigger picture" and "Ready to get started?"
- Don't change existing copy, CTAs, pricing, or service descriptions
- Don't add a full navigation menu or sidebar. Keep the single-page feel with the resources page as a clean secondary page.
- Don't over-engineer the email capture. Kit handles the heavy lifting. We just embed their form.
- Don't make the "Coming Soon" tool teaser look like it's available. Make it clearly labeled as upcoming.

## Kit Setup Steps (Manual, Do Before Running Prompts)

1. Go to kit.com and create a free account
2. Create a new Form (not a Landing Page)
3. In Form settings, set up the Incentive Email:
   - Upload the AI-Assisted Development guide PDF
   - Write a brief delivery email: "Here's your copy of the AI-Assisted Development guide. If you have questions or want to talk about implementing this on your team, reply to this email or book time at learnwithoj.com."
4. Design the form to collect: Email (required), First Name (optional)
5. Grab the HTML embed code from Kit
6. Save the embed code, you'll paste it in during Prompt 3

## Prompt Sequence for Claude Code

Run these in order. Test after each one before moving to the next.

### Prompt 1: Create the resources page shell

```
Read CLAUDE.md. Create resources.html with the same nav bar and footer as index.html. Add a page heading "Free Resources" and a brief intro paragraph. Add an empty section with id="ai-guide" and a placeholder that says "Guide section coming soon." Make sure the page is styled consistently with the existing site. Link it from the nav bar on both pages (add a "Resources" link).
```

### Prompt 2: Build the AI guide section on resources.html

```
Read CLAUDE.md. In resources.html, replace the placeholder in #ai-guide with the full guide section: title, description (3-5 sentences, see CLAUDE.md for direction), and a placeholder div where the Kit form embed will go. Also add the "Coming Soon" teaser for the resume/JD match tool below the guide section. Style everything to match the site.
```

### Prompt 3: Embed the Kit form

```
Read CLAUDE.md. Here's the Kit embed code:

<script async data-uid="36c7f50077" src="https://learn-with-o-j.kit.com/36c7f50077/index.js"></script>

Add it to the placeholder div in the #ai-guide section on resources.html. Style the surrounding container so it integrates cleanly with the page. Add the "No spam. Just the guide. You can unsubscribe anytime." note below the form.
```

### Prompt 4: Add the resources teaser to index.html

```
Read CLAUDE.md. Add a starburst badge to the hero section that links to /resources.html#ai-guide with the text "Free AI Guide." Place it inside the hero-video-wrapper div, positioned absolutely at the top-right of the circular profile image. Use an inline SVG for the starburst shape (8 points, mathematically generated for consistency, shallow valleys) with a coral/orange fill (#e8755a) to contrast with the teal buttons. Rotate the SVG shape ~15 degrees but keep the text horizontal. Position using left: calc(50% + offset) so it stays anchored relative to the centered image across screen sizes. The badge should scale up slightly and rotate on hover. Keep it small (75-80px) so it doesn't compete with the main CTA.
```

### Prompt 5: Polish and test

```
Read CLAUDE.md. Review both index.html and resources.html for:
- Consistent styling (colors, fonts, spacing, dark theme)
- Mobile responsiveness (test at 375px, 768px, 1024px widths)
- All links work (nav, CTAs, anchors, starburst badge links to /resources.html#ai-guide)
- The starburst badge stays anchored relative to the profile image at all screen sizes and doesn't overlap or obscure the image awkwardly on mobile
- The badge hover animation (scale + rotate) works smoothly
- The "Coming Soon" tool teaser looks clearly different from the available guide (maybe slightly muted/grayed)
- The Kit form embed loads correctly on resources.html (note: form submission won't work locally, just verify it renders)
Fix anything that's off.
```

## Notes

- The Kit form won't work in local development since it needs Kit's JS to load. Test the form integration on a deployed version or Kit's preview.
- The PDF guide should be hosted through Kit (as the incentive email attachment/link), not as a static file on the site. This ensures you capture the email before anyone gets the file.
- If you want to track downloads or conversions later, Kit has built-in analytics for form submissions.

# CLAUDE.md - Learn with O.J. Landing Page Update

## Context
This is the landing page for Learn with O.J. (learnwithoj.com), a coaching and career strategy business serving software and infrastructure engineers who are experienced but haven't gotten the senior title yet. The founder is O.J. (Olivia Wilcox), a senior engineer with 20+ years of experience across SWE and SRE.

The current site has a single offering (1:1 Mentoring Session, $200/hr) with a "Book a Session" button that hits people cold with the price. We're restructuring to add multiple service tiers and change the primary call-to-action from "pay me now" to "let's talk first."

## Key URLs
- LinkedIn profile: https://www.linkedin.com/in/learnwithoj/
- Email: oj@learnwithoj.com

## Tech Stack
- Plain HTML/CSS/JavaScript (static site, no framework)
- Hosted on GitHub Pages (repo: oj-codes/learnwithoj.com)
- Stripe Checkout embedded on page for payments
- No build step, no bundler, no dependencies

## Design Direction
- Keep the existing dark theme and color palette (dark navy background, teal/cyan accent color for buttons and highlights)
- Keep the circular profile photo in the hero
- Keep the credibility stats bar (20+ years / 2x Senior Engineer / SWE + SRE)
- The site should feel clean, confident, and personal. Not corporate, not salesy.

## Page Structure (top to bottom)

The current site already has good bones and a section flow that works. We're keeping the overall structure but updating content, replacing the single offering with three tiers, and shifting the primary CTA from "Book a Session - $200" to "Let's Talk First."

### 1. Navigation Bar
- Left: "Learn with O.J." (text logo, same as current)
- Right: "Let's Talk" button (teal accent, links to https://www.linkedin.com/in/learnwithoj/). Replaces the current "Book Session" button.
- Sticky nav on scroll

### 2. Hero Section
- Circular profile photo (keep current placement, styling, and animation)
- Eyebrow text: Replace "1:1 MENTORSHIP FOR ENGINEERS" with something like "A WORKING ENGINEER IN YOUR CORNER"
- Headline: Keep "Get unstuck. Level up. Reach senior." (this is strong, don't change it)
- Subtext: Update from the single-session pitch to something broader: "I help experienced engineers close the gap between where they are and where they should be. Real feedback, real strategy, no generic advice."
- Primary CTA button: "Let's Talk First" (links to https://www.linkedin.com/in/learnwithoj/). This is the dominant button. Replaces "Book a Session - $200."
- Small text under CTA: "Connect with me on LinkedIn and tell me what you're working on."

### 3. Credibility Stats Bar
- Keep as-is: 20+ / 2x / SWE + SRE
- These are effective, no changes needed

### 4. Who This Is For Section
- Already exists on current site. Update language to use "software and infrastructure engineers" and "experienced engineers who haven't gotten the title yet"
- This section should make the target audience feel seen and self-select

### 5. What You Get Section
- Update to reflect the three service tiers instead of the single session
- Brief overview of what working with O.J. looks like across the different offerings
- This is the "here's what's on the table" section, not the detailed pricing section

### 6. What We Cover Section
- Already exists on current site. Keep or update the list of topics/areas covered (career strategy, resume positioning, pair programming, code review, interview prep, architecture review, etc.)
- This helps people see that the sessions aren't just "career advice" but hands-on technical collaboration

### 7. How It Works Section
Explain the process so people understand the path before they see prices:
- Step 1: "Connect" - Reach out on LinkedIn. Tell me where you're stuck.
- Step 2: "Clarity" - We'll talk through your situation so I understand what you actually need.
- Step 3: "Go" - Book the right service and we hit the ground running. No wasted time.

### 8. Services / Pricing Section
Three tiers displayed as cards side by side (or stacked on mobile):

#### Fresh Squeeze - $275
- Resume review using an 8-stage diagnostic methodology
- What you get: A Feedback Letter with summary findings and actionable insights, plus a Premium Resume Review Report with detailed analysis, hiring manager perspective, action items, and example bullet rewrites
- Framing: This is the entry point. Position it as "start here if you're not sure where to begin"
- CTA: Stripe Checkout button "Get Fresh Squeeze - $275"
- Note: Consider a subtle visual indicator (like "Start Here" badge) to guide people toward this option

#### Career Accelerator - $900
- 3 sessions (60 min each), flexible format
- Sessions can be any mix: career strategy, pair programming, code review, interview prep, architecture review
- Framing: For engineers who want sustained support, not just a one-off
- Highlight the savings vs. 3 individual sessions ($975 value)
- CTA: Stripe Checkout button "Get Career Accelerator - $900"

#### Focused Hour - $325
- Single 60-minute session, any topic
- Pre-work intake + 60-min call + async follow-up (keep this from current site)
- Framing: For engineers who know exactly what they need and want to dive in
- CTA: Stripe Checkout button "Book Focused Hour - $325"

### 9. About Me Section
- Brief bio establishing credibility (20+ years, leveled up twice, SWE and SRE, real production experience)
- Already exists on current site. Keep the personal, conversational tone.

### 10. Testimonials Section
- Include any available testimonials from past clients or people O.J. has helped (paid or unpaid)
- Even 1-2 short quotes with names and titles adds significant trust
- If no testimonials are available yet, this section can be added later. Do not generate placeholder/fake testimonials.

### 11. Second CTA Section
- Another "Let's Talk First" button or similar CTA linking to https://www.linkedin.com/in/learnwithoj/ to catch people who scrolled all the way down
- Include a "Have questions? Email me at oj@learnwithoj.com" link as a secondary option (keep from current site)

### 12. Common Questions (FAQ) Section
- Already exists on current site. Review and update to reflect the new service tiers.
- Add questions like: "Which service should I start with?" (answer: reach out on LinkedIn and we'll figure it out together, or start with Fresh Squeeze if your resume needs work), "What happens after I pay?", "Can I upgrade from Fresh Squeeze to Career Accelerator?"

### 13. The Bigger Picture Section
- Already exists on current site. This talks about the long-term vision of building a free learning platform for engineers.
- Keep as-is or lightly update. This is a differentiator and shows O.J.'s values.

### 14. Footer
- Links: https://www.linkedin.com/in/learnwithoj/, oj@learnwithoj.com, GitHub (if desired)
- "Learn with O.J." branding
- Keep it minimal

## Voice and Copy Guidelines
- Use "software and infrastructure engineers" not just "engineers"
- Use "experienced engineers who haven't gotten the title yet" not "mid-career engineers"
- No em dashes anywhere. Use commas, periods, or restructure the sentence.
- Combine parallel short sentences with "and" not periods where it flows naturally
- No "mentor" or "mentorship" language. Use "career strategy," "1:1 sessions," "pair programming," etc.
- Conversational and direct. Write like you're talking to a fellow engineer, not pitching a corporate training program.
- No filler phrases like "unlock your potential" or "take your career to the next level"
- Honest and no-BS. If something is hard, say it's hard. Don't oversell.

### Brand Personality
The brand is: Collaborative. Real. Experienced. Irreverent. Determined.
- The tension between "irreverent" and "determined" is the sweet spot. Playful and approachable but never lightweight.
- The juice/beverage theme is intentional branding (O.J. = orange juice). Lean into it where it fits naturally (product names like "Fresh Squeeze") but don't force juice puns into every section.

### Key Positioning
- O.J. is a "working engineer helping other engineers level up." She's not coaching from the sidelines, she's still actively doing the work.
- What she teaches is closer to "operational career intelligence" and "professional operating skills" than generic career coaching. How to actually function inside an organization in a way that gets you promoted.
- The technical bar is table stakes. How you operate inside the org is what determines whether you clear it.
- Learn with O.J. serves engineers outside the Big Tech bubble: mid-size companies, healthcare orgs, fintechs, agencies, startups without formal engineering ladders.

### Copy to Use or Riff On
- Introduction: "I'm O.J., a working engineer helping other engineers level up. My goal is to show others the way to build careers that compound while I help companies move fast without breaking things."
- On credentials: "20+ years of software engineering experience from startups building smart TV apps competing with Netflix to Fortune 100 organizations like American Express. Leveled up twice, from senior SWE to senior SRE."
- On the rate objection: "You're not paying for an hour of my time. You're paying for an hour plus over 20 years of professional software experience plus all the extra unpaid time I spend working on projects to keep up with the latest technology."
- "I don't leave my clients wondering what to do next."

### Copy to Avoid
- "Unlock your potential" or any generic coaching language
- "Take your career to the next level"
- AI-sounding phrases like "You're not X. You're Y."
- LinkedIn-template energy (emojis, numbered lists, humble brags)
- The word "mentor" or "mentorship" anywhere on the page

## Stripe Integration
- Each service tier needs its own Stripe Checkout embed
- O.J. will create 3 Stripe products (Fresh Squeeze $275, Career Accelerator $900, Focused Hour $325) and provide the checkout embed code or payment link URLs
- Buttons should open Stripe Checkout directly (embedded or redirect, depending on what O.J. sets up)
- Fresh Squeeze: https://buy.stripe.com/bJe5kDeDH5kM8lJ9CEabK06
- Career Accelerator: https://buy.stripe.com/6oU9ATbrvbJaeK7dSUabK05
- Focused Hour: https://buy.stripe.com/9B67sL7bfcNefOb6qsabK04

## Important Notes
- The LinkedIn "Let's Talk First" CTA should be visually dominant over the Stripe buy buttons. The goal is to get people into a conversation first. The buy buttons are there for people who are ready, but the default path is: LinkedIn conversation first, then book.
- Prices are visible on the page (O.J. feels strongly about price transparency) but they're not the first thing you see. The first thing you see is the invitation to connect.
- Mobile responsive. Most traffic likely comes from LinkedIn on mobile.
- Keep page load fast. No heavy frameworks, no unnecessary assets.

## What NOT to Do
- Don't hide prices or make people fill out a form to see pricing
- Don't use "mentor" or "mentorship" anywhere
- Don't use em dashes
- Don't add a chatbot, popup, or email capture form
- Don't make it look like a SaaS landing page with feature comparison tables
- Don't use stock photos (the profile photo is O.J.'s actual photo with AI-animated movement, keep it as-is)

## Suggested Claude Code Prompt Sequence
Work in small increments. Test and commit after each prompt.

1. "Read CLAUDE.md. Update the nav bar: change 'Book Session' to 'Let's Talk' and link it to https://www.linkedin.com/in/learnwithoj/"

2. "Update the hero section: change the eyebrow text from '1:1 MENTORSHIP FOR ENGINEERS' to 'CAREER STRATEGY FOR SOFTWARE & INFRASTRUCTURE ENGINEERS'. Update the subtitle copy per CLAUDE.md. Replace the 'Book a Session - $200' button with a 'Let's Talk First' button linking to https://www.linkedin.com/in/learnwithoj/. Add small text underneath: 'Connect with me on LinkedIn and tell me what you're working on.' Keep the headline and photo as-is."

3. "Update the 'Who This Is For' section: replace any mention of 'mid-career' with 'experienced engineers who haven't gotten the title yet'. Use 'software and infrastructure engineers' instead of just 'engineers'. Remove any 'mentor/mentorship' language."

4. "Update the 'What You Get' section to reflect three service tiers (Fresh Squeeze resume review, Career Accelerator 3-session bundle, Focused Hour single session) instead of the single mentoring session. See CLAUDE.md for details on each tier."

5. "Add a Services/Pricing section with 3 cards per CLAUDE.md: Fresh Squeeze ($275), Career Accelerator ($900), Focused Hour ($325). Each card needs a description and a Stripe Checkout button using the URLs from CLAUDE.md. Add a 'Start Here' badge on Fresh Squeeze. Stack cards on mobile."

6. "Add a 'How It Works' section with 3 steps: Connect, Clarity, Go. Position it before the pricing section so people understand the process before seeing prices. See CLAUDE.md for step descriptions."

7. "Update the FAQ section to reflect the new service tiers. Add questions about which service to start with, what happens after payment, and whether you can upgrade from Fresh Squeeze to Career Accelerator."

8. "Add a testimonials section between About Me and the second CTA. Use placeholder structure for 1-2 testimonial cards (name, title, quote) that I can fill in later. If I provide actual testimonial text, use that instead."

9. "Update the second CTA section: replace any 'Book a Session' button with 'Let's Talk First' linking to LinkedIn. Keep the email link as a secondary option."

10. "Do a full review pass: check all copy for em dashes (replace with commas or periods), check for 'mentor/mentorship' language (replace per CLAUDE.md guidelines), check for 'mid-career' (replace with correct framing), and verify mobile responsiveness on all new sections."

For full brand context including positioning, case studies, and competitive landscape, reference the branding guide in the learnwithoj-internal repo (not included here, ask for it directly when needed).
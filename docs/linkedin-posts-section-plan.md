# LinkedIn Top Posts Section - Plan

## Overview
Add a section to the site showcasing top-performing LinkedIn posts. Start with 3 posts, scrollable carousel for adding more later (same pattern as testimonials).

## Card Design
- White/light background cards to mimic LinkedIn's look, or dark-themed to match the site (TBD)
- Each card includes:
  - O.J.'s avatar, name, and title at the top
  - Post text truncated to ~3-4 lines with "read more" linking to the actual LinkedIn post
  - Engagement stats at the bottom: thumbs up icon + count, comment icon + count
  - Small LinkedIn logo/icon on the card to signal the source

## Technical Approach
- Manually curated: pick top posts, paste the text, add engagement numbers and LinkedIn post URL
- No API needed (LinkedIn's API is locked down)
- Same horizontal scroll/carousel pattern already used for testimonials
- To update: edit the HTML directly when swapping or adding posts

## Placement on Page
- Near testimonials section (social proof adjacent). Could go between testimonials and services, or between "the bigger picture" and testimonials.

## Things to Decide
- Light cards (LinkedIn-style white bg, black text) vs dark cards (matching site theme)?
- Include engagement numbers (they go stale) or just show post content + "View on LinkedIn" link?
  - Compromise option: round the numbers ("50+ reactions") so they don't look outdated quickly
- Which 3 posts to feature first?

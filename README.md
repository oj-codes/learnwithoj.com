# Learn with O.J.

Career strategy and 1:1 technical sessions for software and infrastructure engineers.

## Overview

A static site for [learnwithoj.com](https://learnwithoj.com) offering career strategy, resume review, and hands-on technical sessions for experienced software and infrastructure engineers. Built with plain HTML, CSS, and JavaScript, deployed to Cloudflare Workers.

[![OpenSSF Scorecard](https://api.scorecard.dev/projects/github.com/oj-codes/learnwithoj.com/badge)](https://scorecard.dev/viewer/?uri=github.com/oj-codes/learnwithoj.com)

## Tech Stack

- HTML5
- CSS3 with animations and responsive design
- JavaScript (testimonials carousel)
- Inter font family via Google Fonts
- Stripe Checkout for payments
- Kit (ConvertKit) for email capture
- GoatCounter for privacy-friendly analytics
- Cloudflare Workers for hosting, with a Preview per pull request

## Project Structure

```
index.html        Landing page with hero, services, testimonials, FAQ, and about sections
resources.html    Free resources page with AI guide download and upcoming tools
styles.css        Shared styles with CSS variables, animations, and responsive breakpoints
assets/           Images and video content
testimonials/     Testimonial avatars and source content
CHANGELOG.md      Version history
CNAME             Custom domain configuration
.github/          GitHub Actions workflow for deployment
```

## Local Development

Run a local server to preview the site.

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Deployment

Every pull request gets its own Workers Preview from `.github/workflows/deploy.yaml`, posted as a comment on the PR. A merge to `main` deploys production the same way. `.github/workflows/ci.yaml` still deploys GitHub Pages, which serves the custom domain until DNS moves to the Worker.

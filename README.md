# Learn with O.J.

Landing page for 1:1 mentorship sessions for engineers.

## Overview

A static landing page for [learnwithoj.com](https://learnwithoj.com) that offers mentorship sessions for mid-level and aspiring senior software, DevOps, and SRE engineers. Built with plain HTML and CSS, deployed to GitHub Pages.

## Tech Stack

- HTML5
- CSS3 with animations and responsive design
- Inter font family via Google Fonts
- GoatCounter for privacy-friendly analytics
- GitHub Pages for hosting

## Project Structure

```
index.html      Landing page with hero, offerings, pricing, FAQ, and about sections
styles.css      Styles with CSS variables, animations, and responsive breakpoints
assets/         Images including headshot
CNAME           Custom domain configuration
.github/        GitHub Actions workflow for deployment
```

## Local Development

Run a local server to preview the site.

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Deployment

Pushes to `main` trigger the GitHub Actions workflow in `.github/workflows/ci.yaml`, which deploys the site to GitHub Pages. The custom domain is configured via the `CNAME` file.

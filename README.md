# Learn with O.J.

Landing page for Learn with O.J. - Guided paths to senior engineering.

## Overview

A clean, minimal landing page for 1:1 mentorship sessions, deployed via GitHub Pages at [learnwithoj.com](https://learnwithoj.com). The site presents mentorship offerings for mid-level and aspiring-senior software, DevOps, and SRE engineers.

## Tech Stack

- HTML5
- CSS3 (with animations and responsive design)
- Geist font family
- GitHub Pages

## Project Structure

- `index.html` - Main landing page with sections for hero, offerings, pricing, FAQ, and more
- `styles.css` - Stylesheet with animations, responsive breakpoints, and a teal/reliability color palette
- `assets/` - Image assets including headshot
- `CNAME` - Custom domain configuration

## Local Development

Serve the site locally using a simple HTTP server:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## Deployment

This repository is automatically deployed to GitHub Pages. The `CNAME` file configures the custom domain `learnwithoj.com`.


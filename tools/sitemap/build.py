#!/usr/bin/env python3
"""Write sitemap.xml from the pages that exist, dated from git, and fail when it drifts.

    python3 tools/sitemap/build.py          # rewrite sitemap.xml
    python3 tools/sitemap/build.py --check  # exit 1 if sitemap.xml is not what this would write

The page list is derived, not kept by hand: every root HTML page except the 404, plus every
agents/**/index.html the publisher wrote. URLs are the clean form the Worker serves, so
/showcase rather than /showcase.html, and lastmod is the date of the last commit that touched
the file, which is the same date the living-pages check trusts. tools/check runs --check, so a
new page that forgets the sitemap fails before it ships.
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SITE = "https://learnwithoj.com"
SKIP = {"404.html"}


def pages():
    out = []
    for p in sorted(ROOT.glob("*.html")):
        if p.name in SKIP:
            continue
        out.append(("/" if p.name == "index.html" else "/" + p.stem, p))
    for p in sorted((ROOT / "agents").rglob("index.html")):
        out.append(("/" + p.parent.relative_to(ROOT).as_posix() + "/", p))
    return out


def lastmod(path):
    r = subprocess.run(["git", "log", "-1", "--format=%as", "--", str(path.relative_to(ROOT))],
                       cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip() or None


def render():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, path in pages():
        date = lastmod(path)
        lines.append("  <url>")
        lines.append(f"    <loc>{SITE}{url}</loc>")
        if date:
            lines.append(f"    <lastmod>{date}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def main():
    target = ROOT / "sitemap.xml"
    want = render()
    if "--check" in sys.argv:
        have = target.read_text() if target.exists() else ""
        if have != want:
            print("sitemap.xml is stale. Run python3 tools/sitemap/build.py and commit it.")
            return 1
        print(f"sitemap.xml lists {want.count('<url>')} pages and matches the tree.")
        return 0
    target.write_text(want)
    print(f"wrote sitemap.xml with {want.count('<url>')} pages")
    return 0


if __name__ == "__main__":
    sys.exit(main())

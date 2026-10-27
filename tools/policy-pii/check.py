#!/usr/bin/env python3
"""Flag PII and uncleared names in the generated agent pages before they ship.

Site-side twin of the internal repo's tools/policy-pii/check.py. That one scans the
Markdown sources and holds the blocklist. This one scans the rendered HTML under
agents/**/index.html and holds no blocklist at all, because this repo is public and a
list of people who have not consented to being named is the last thing to commit to it.

So the gate here is the allowlist. Anything name-shaped that is not on allowlist.txt
fails, and so does any hard pattern (email, phone, money, government id, street
address). The allowlist and names.py are copied verbatim from the internal repo on each
regeneration of the agent pages. names.py holds the list parser and the patterns for both
gates, so what counts as a hit is defined once; only the HTML stripping lives here.

Stdlib only, no venv, so it runs in the Checks workflow and in the pre-commit hook.

A failure prints the page, the line and the kind of hit, never the matched text, because
the Checks workflow runs in a public repo and an Actions log is a published page nobody
files as one. Pass --verbose for the matched text when running locally, which is what
tools/check does outside CI.
"""

import argparse
import html
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
from names import HARD, NAME, OWN_DOMAIN, load_list  # noqa: E402

# OWN_DOMAIN, HARD and NAME come from names.py, the one place both gates define what
# counts as a hit. Only the stripping below is HTML-specific.

# HTML furniture that would otherwise generate noise. Blocks are blanked with their
# newlines kept, so a reported line number is the line in the file.
STRIP = [
    re.compile(r"<head\b.*?</head>", re.S | re.I),      # title, meta, JSON-LD
    re.compile(r"<nav\b.*?</nav>", re.S | re.I),        # site chrome
    re.compile(r"<footer\b.*?</footer>", re.S | re.I),  # legal name, 1% block
    re.compile(r"<script\b.*?</script>", re.S | re.I),
    re.compile(r"<style\b.*?</style>", re.S | re.I),
    re.compile(r"<pre\b.*?</pre>", re.S | re.I),        # fenced code
    re.compile(r"<code\b.*?</code>", re.S | re.I),      # inline code
    re.compile(r"""\b(?:href|src)\s*=\s*(?:"[^"]*"|'[^']*')""", re.I),  # link targets
    re.compile(r"<[^>]+>"),                             # every remaining tag
    re.compile(r"https?://\S+"),                        # bare urls in text
]


def pages():
    return sorted(p.relative_to(REPO).as_posix() for p in (REPO / "agents").rglob("index.html"))


def scan(text, allow):
    """Return fails as a list of (kind, matched text, line number)."""
    clean = text
    for pat in STRIP:
        clean = pat.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), clean)
    clean = html.unescape(clean)

    def lineno(i):
        return clean.count("\n", 0, i) + 1

    fails = []
    for kind, pat in HARD:
        for m in pat.finditer(clean):
            hit = m.group(0)
            if kind == "email" and hit.lower().endswith(OWN_DOMAIN):
                continue
            fails.append((kind, hit, lineno(m.start())))

    for m in NAME.finditer(clean):
        hit = m.group(0)
        if hit not in allow:
            fails.append(("name not on allowlist", hit, lineno(m.start())))
    return fails


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--file", nargs="+", metavar="PATH",
                    help="scan these HTML files instead of agents/**/index.html")
    ap.add_argument("--verbose", action="store_true",
                    help="print the matched text. Local runs only, never in a public CI log")
    a = ap.parse_args()

    allow = set(load_list("allowlist.txt"))
    if not allow:
        sys.exit("allowlist.txt is missing or empty beside this script, so nothing can pass")

    targets = a.file if a.file else pages()
    total = 0
    for rel in targets:
        p = pathlib.Path(rel) if a.file else REPO / rel
        if not p.exists():
            print("MISSING  %s is not on disk" % rel)
            total += 1
            continue
        for kind, hit, ln in scan(p.read_text(encoding="utf-8"), allow):
            if a.verbose:
                print("FAIL     %s:%d  %s: %s" % (rel, ln, kind, hit))
            else:
                print("FAIL     %s:%d  %s" % (rel, ln, kind))
            total += 1

    n = len(targets)
    print("%d FAIL across %d %s" % (total, n, "file" if n == 1 else "files"))
    if total:
        print("A name cleared for publication goes on allowlist.txt in the internal repo, "
              "then the pages are regenerated. Anything else comes off the page.")
        if not a.verbose:
            print("Run with --verbose locally to see the matched text.")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())

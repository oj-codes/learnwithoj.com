#!/usr/bin/env python3
"""Keep the "Last updated" date on each living page true to git.

Ported 23 October 2026 from the internal repo's tools/policy-dates/check.py,
which can only see pages published from there. A page whose source lives in
this repo needs the same rule here: the date comes from the last commit that
changed something other than the date itself, and CI fails on drift.

    python3 tools/last-reviewed/check.py          # report drift, exit 1 if any
    python3 tools/last-reviewed/check.py --fix    # rewrite the dates to match git

The page carries <time class="explainer-reviewed" datetime="YYYY-MM-DD">Month D YYYY</time>
and, when present, a JSON-LD "dateModified" that is kept in step. "datePublished"
is left alone.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

# Which pages are living documents is a decision, so it is a list here and
# not a glob. Add a page when it gets the "Last updated" line.
PAGES = [
    "functional-emotions.html",
]

TIME = re.compile(
    r'<time class="explainer-reviewed" datetime="(\d{4}-\d{2}-\d{2})">([^<]+)</time>')
LD = re.compile(r'"dateModified": "(\d{4}-\d{2}-\d{2})"')
MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]


def _without_dates(line):
    """The line with its date stamps replaced by a sentinel, for comparison."""
    line = TIME.sub('<time class="explainer-reviewed" datetime="DATE">DATE</time>', line)
    return LD.sub('"dateModified": "DATE"', line)


def _only_touches_the_date(sha, path):
    """True if this commit changed nothing in the file but its date stamps.

    Compares the removed and added lines with the dates blanked, so an edit
    elsewhere on the same line as a date still counts as a content change.
    """
    diff = subprocess.run(
        ["git", "show", "--format=", "--unified=0", sha, "--", path],
        cwd=ROOT, capture_output=True, text=True).stdout
    removed = [_without_dates(l[1:]) for l in diff.splitlines()
               if l.startswith("-") and not l.startswith("---")]
    added = [_without_dates(l[1:]) for l in diff.splitlines()
             if l.startswith("+") and not l.startswith("+++")]
    return bool(removed) and removed == added


def git_date(path):
    """ISO and long-form date of the last commit that changed the page in a way that counts.

    Author date, not committer date. This repo merges by rebase, which rewrites
    the committer date on every merge and would make every page stale the day
    it landed.
    """
    log = subprocess.run(
        ["git", "log", "--format=%H %as", "--", path],
        cwd=ROOT, capture_output=True, text=True).stdout.strip().splitlines()
    for entry in log:
        sha, iso = entry.split()
        if _only_touches_the_date(sha, path):
            continue
        y, m, d = iso.split("-")
        return iso, f"{MONTHS[int(m) - 1]} {int(d)} {y}"
    return None


def dirty(paths):
    out = subprocess.run(["git", "status", "--porcelain", "--", *paths],
                         cwd=ROOT, capture_output=True, text=True).stdout
    return [l[3:].strip() for l in out.splitlines() if l.strip()]


def main():
    fix = "--fix" in sys.argv
    problems = 0
    for page in PAGES:
        path = ROOT / page
        if not path.exists():
            print(f"Missing: {page}")
            problems += 1
            continue
        text = path.read_text(encoding="utf-8")
        found = TIME.search(text)
        if not found:
            print(f"No <time class=\"explainer-reviewed\"> in {page}")
            problems += 1
            continue
        want = git_date(page)
        if want is None:
            print(f"Not yet committed: {page}, nothing to compare")
            continue
        iso, long = want
        ld = LD.search(text)
        ok = found.group(1) == iso and found.group(2) == long and (not ld or ld.group(1) == iso)
        if ok:
            continue
        problems += 1
        print(f"{'Fixed' if fix else 'Stale'}: {page}")
        print(f"  was:  {found.group(2)} ({found.group(1)})")
        print(f"  want: {long} ({iso})")
        if fix:
            text = TIME.sub(f'<time class="explainer-reviewed" datetime="{iso}">{long}</time>', text)
            text = LD.sub(f'"dateModified": "{iso}"', text)
            path.write_text(text, encoding="utf-8")
    if dirty(PAGES) and not fix:
        print("\nUncommitted changes on a listed page. The date comes from the last commit,"
              " so commit first and run again.")
    if problems:
        if fix:
            print("\nRun again to confirm, then commit. The date trails by one commit until"
                  " the fix itself is committed.")
        else:
            print(f"\n{problems} page(s) out of date. Run with --fix.")
        sys.exit(1)
    print(f"All {len(PAGES)} living page(s) carry the right date.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The one place that knows how the name lists are parsed.

Imported by check.py and by publish.py's redaction transform, and copied verbatim
into the site repo's CI alongside the lists. Tern's point, 26 October 2026, and it is
the difference between two gates and one silent pass: if the site copy parsed a line
differently it would match nothing and pass everything. So the parsing lives here and
nobody reimplements the split.

The contract, decided by O.J. on 26 October 2026:

  * blocklist.txt holds full names, one per line, no special syntax.
  * A blocklist name is redacted whole, and each of its words is redacted on its own,
    plus each word's possessive. Case-sensitive, whole word.
  * redaction-exceptions.txt spares a bare word that would otherwise be caught.
    The full name is still redacted either way.

Her reasoning for the split over a hand-written variant list: both approaches match
"Mark" the same way and only differ in who types it, and a false positive shows up in
the redaction review list before the merge.
"""
from __future__ import annotations   # names.py runs under whatever python the site CI has.
                                      # Without this, `re.Pattern | None` on line 61 is evaluated
                                      # at import time and raises TypeError on 3.9, which is what
                                      # /usr/bin/python3 is on this machine. Found 27 October 2026
                                      # while checking the port, before it reached a CI step.
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
PLACEHOLDER = "[client name]"


def load_list(name: str) -> list[str]:
    """One entry per line. Blank lines and # comments out."""
    p = HERE / name
    if not p.exists():
        return []
    return [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()
            if ln.strip() and not ln.lstrip().startswith("#")]


def redaction_terms() -> list[str]:
    """Every string to redact, longest first.

    Longest first matters: "Mark Lathem" has to match before "Mark", or the full name
    comes out as "[client name] Lathem" and the surname survives.

    No possessive variants in here on purpose. A word boundary already closes before
    the apostrophe, so matching "Mark" inside "Mark's reply" yields "[client name]'s
    reply" and the sentence still reads. Adding "Mark's" as its own term produced
    "[client name] reply" instead, which is the sort of thing that reaches a public
    page looking like a typo rather than a redaction.
    """
    spared = set(load_list("redaction-exceptions.txt"))
    terms: set[str] = set()
    for full in load_list("blocklist.txt"):
        terms.add(full)
        for word in full.split():
            if word in spared or len(word) < 2:
                continue
            terms.add(word)
    return sorted(terms, key=len, reverse=True)


def redaction_pattern() -> re.Pattern | None:
    """One alternation, case-sensitive, whole word. None when the blocklist is empty."""
    terms = redaction_terms()
    if not terms:
        return None
    return re.compile(r"\b(" + "|".join(re.escape(t) for t in terms) + r")\b")

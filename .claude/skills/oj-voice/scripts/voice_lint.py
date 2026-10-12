#!/usr/bin/env python3
"""Mechanical voice check for O.J.'s writing. Run on any draft before delivering it.
Usage: python3 voice_lint.py draft.md   (or .html / .txt; HTML tags and <pre>/<code> blocks are stripped)
Exit code 1 if anything is flagged. Every flag is a place to look, not an automatic fix."""
import re, sys, html

BANNED = [
    (r"\bland(s|ed|ing)?\b", "lands/landed"), (r"\bshapes?\b", "shape/shapes"), (r"\bgenuine(ly)?\b", "genuine"),
    (r"\bhonest(ly)?\b", "honest/honestly"), (r"load-bearing", "load-bearing"), (r"\bquiet(ly)?\b", "quiet/quietly"),
    (r"\bconsult(ant|ing)\b", "consultant/consulting"), (r"\bAI[- ]tools?\b", "AI tool(s)"), (r"\busing AI\b", "using AI"),
    (r"\bcosts? you\b", "costs you (any form)"), (r"\bperform(s|ed|ing)?\b", "performs (use acts/does/works)"),
    (r"\bpush back\b", "push back (use disagree)"), (r"\bnudge\b", "nudge (use reminder)"), (r"\bin the room\b", "in the room"),
    (r"\breceipts\b", "receipts"), (r"went sideways", "went sideways"), (r"\bclocked\b", "clocked"), (r"sat with", "sat with"),
    (r"turn(ed|ing) it over", "turned it over"), (r"it'?s not nothing", "it's not nothing"), (r"\bis what matters\b", "X is what matters"),
    (r"\bit'?s not [^.]{1,40}?,? it'?s\b", "it's not X it's Y"), (r"\bpercent\b", "percent (use %)"), (r"\bodd\b", "odd (use weird)"),
    (r"\bmid-career\b", "mid-career"), (r"\bwhat I teach\b", "what I teach"), (r"\bthe user\b", "user (use human)"),
    (r"\b(does|do|is|are|will|can) not\b|\bcannot\b", "uncontracted form"),
    (r"\bhad (been|done|gone|seen|made|said|put|taken|found|given|sent|told|known|thought|come|become|built|kept|left|felt|got|gotten|run|read|written|\w+ed)\b", "past perfect (she uses simple past: 'I tested', not 'I had tested')"),
    (r"\b(I|we|you|they|he|she|it)'d (been|done|gone|seen|made|said|put|taken|found|given|sent|told|known|thought|come|become|built|kept|left|felt|got|gotten|run|read|written|\w+ed)\b", "'d + participle = past perfect (simple past instead; \"I'd rather\" is fine)"),
]

def clean(text):
    text = re.sub(r"(?is)<(pre|code|style|script)[^>]*>.*?</\1>", " ", text)
    text = re.sub(r"(?s)```.*?```", " ", text)
    text = re.sub(r"(?s)<[^>]+>", "\n", text)
    return html.unescape(text)

def main(path):
    raw = open(path, encoding="utf-8").read()
    text = clean(raw)
    paras = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n|\n", text)]
    paras = [p for p in paras if p]
    flags = []
    def add(kind, snippet): flags.append((kind, snippet[:140]))
    for p in paras:
        if "\u2014" in p or " -- " in p: add("EM DASH", p)
        for m in re.finditer(r",\s+(and|but)\s", p):
            s = p[max(0, m.start()-60):m.end()+40]
            add("COMMA BEFORE and/but (clear unless list or two long clauses)", s)
        for m in re.finditer(r"[a-z)\]\"'”]:\s+\S", p):
            add("COLON IN PROSE (join the sentence instead, unless it's hers)", p[max(0, m.start()-50):m.end()+40])
        if re.match(r"And\b", p) or re.search(r"[.!?]\s+And\b", p): add("SENTENCE STARTS WITH And", p)
        for pat, name in BANNED:
            for m in re.finditer(pat, p, re.I):
                add("BANNED: " + name, p[max(0, m.start()-40):m.end()+40])
        for m in re.finditer(r"\b(\w+(?: \w+){0,3}), (\w+(?: \w+){0,3}),? (and|or) (\w+(?: \w+){0,3})\b", p):
            before = p[max(0, m.start()-3):m.start()]
            if not before.endswith(", "):
                add("POSSIBLE LIST OF THREE (make it two or four)", m.group(0))
        sents = [s for s in re.split(r"(?<=[.!?])\s+", p) if len(s.split()) > 2]
        if len(sents) > 3: add("PARAGRAPH OVER 3 SENTENCES (public docs)", p)
        shorts = [s for s in sents if len(s.split()) <= 4]
        if len(shorts) >= 2: add("POSSIBLE STACCATO (join short sentences)", p)
    words = re.findall(r"\b\w+(?:'\w+)?\b", text.lower())
    grams = {}
    for i in range(len(words)-3):
        g = " ".join(words[i:i+4]); grams[g] = grams.get(g, 0) + 1
    for g, n in grams.items():
        if n > 1 and not re.match(r"^(the|a|of|to|in|and|it|is|that|for|on) ", g):
            add("REPEATED PHRASE x%d" % n, g)
    for kind, s in flags: print(f"[{kind}] {s}")
    print(f"\n{len(flags)} flags in {path}")
    return 1 if flags else 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))

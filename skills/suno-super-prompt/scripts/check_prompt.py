#!/usr/bin/env python3
"""Validate a Suno SUPER PROMPT.

Usage:
    python3 check_prompt.py prompt.txt [--ban word ...]
    cat prompt.txt | python3 check_prompt.py -

The prompt must contain the labels TITLE:, LYRICS:, STYLE: and EXCLUDE:.
Character counts include spaces and line breaks, exactly as Suno counts the
pasted field (the label itself, e.g. "STYLE:", is not counted).
Exits with status 1 when a hard rule fails.

Limits (override with flags if Suno changes them):
    TITLE           80     --title-limit
    LYRICS        5000     --lyrics-limit
    STYLE         1000     --style-limit
    EXCLUDE       1000     --exclude-limit
    STYLE+EXCLUDE 1000     --combined-limit (house rule; 0 disables)
"""

import argparse
import re
import sys

TITLE_LIMIT = 80
LYRICS_LIMIT = 5000
STYLE_LIMIT = 1000
EXCLUDE_LIMIT = 1000
STYLE_EXCLUDE_LIMIT = 1000
NEAR_LIMIT = 0.95

REQUIRED_EXCLUDES = ["crowd noise", "audience", "applause", "crowd chants"]

BANNED = [
    "neon", "static", "velvet", "echo", "echoes", "shadow", "shadows", "ember", "embers",
    "ashes", "ignite", "ignites", "inferno", "shattered", "fractured", "tapestry", "symphony",
    "canvas", "mosaic", "labyrinth", "abyss", "void", "cosmos", "celestial", "ethereal",
    "eternal", "infinite", "horizon", "twilight", "moonlight", "starlight", "stardust",
    "whisper", "whispers", "whispered", "haunting", "phantom", "halo", "throne", "kingdom",
    "fairytale", "destiny", "wildfire", "beneath", "amidst", "embrace", "linger", "lingering",
    "unspoken", "unbroken", "unravel", "intertwined", "resonate", "cascade", "kaleidoscope",
]

LABELS = ("TITLE", "LYRICS", "STYLE", "EXCLUDE")


def parse(text):
    # The "Characters — ..." count line printed under a prompt is not part of any field.
    text = re.sub(r"^\s*Characters\s*[—–-].*$", "", text, flags=re.MULTILINE)
    pattern = re.compile(r"^\s*(%s)\s*:" % "|".join(LABELS), re.MULTILINE)
    matches = list(pattern.finditer(text))
    fields = {}
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        fields[m.group(1)] = text[m.end():end].strip()
    return fields


def sung_text(lyrics):
    """Lyrics without [[directions]] and [section] tags."""
    no_dirs = re.sub(r"\[\[.*?\]\]", " ", lyrics, flags=re.DOTALL)
    return re.sub(r"\[[^\[\]]*\]", " ", no_dirs)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="prompt file, or - for stdin")
    ap.add_argument("--ban", nargs="*", default=[], help="extra banned words for this project")
    ap.add_argument("--title-limit", type=int, default=TITLE_LIMIT)
    ap.add_argument("--lyrics-limit", type=int, default=LYRICS_LIMIT)
    ap.add_argument("--style-limit", type=int, default=STYLE_LIMIT)
    ap.add_argument("--exclude-limit", type=int, default=EXCLUDE_LIMIT)
    ap.add_argument("--combined-limit", type=int, default=STYLE_EXCLUDE_LIMIT,
                    help="STYLE+EXCLUDE house rule; 0 disables")
    args = ap.parse_args()

    text = sys.stdin.read() if args.file == "-" else open(args.file, encoding="utf-8").read()
    fields = parse(text)
    errors, warnings = [], []

    for label in LABELS:
        if not fields.get(label):
            errors.append(f"missing {label}:")

    title = fields.get("TITLE", "")
    lyrics = fields.get("LYRICS", "")
    style = fields.get("STYLE", "")
    exclude = fields.get("EXCLUDE", "")
    combined = len(style) + len(exclude)

    counts = [
        ("TITLE", len(title), args.title_limit),
        ("LYRICS", len(lyrics), args.lyrics_limit),
        ("STYLE", len(style), args.style_limit),
        ("EXCLUDE", len(exclude), args.exclude_limit),
    ]
    if args.combined_limit:
        counts.append(("STYLE+EXCLUDE", combined, args.combined_limit))

    for name, size, limit in counts:
        if size > limit:
            errors.append(f"{name} is {size} chars, {size - limit} over the {limit} limit")
        elif size > limit * NEAR_LIMIT:
            warnings.append(f"{name} is {size}/{limit} chars, within 5% of the limit")

    excl_lower = exclude.lower()
    for item in REQUIRED_EXCLUDES:
        if item not in excl_lower:
            errors.append(f"EXCLUDE is missing '{item}'")

    banned = set(w.lower() for w in BANNED + args.ban)
    sung = (fields.get("TITLE", "") + " " + sung_text(lyrics)).lower()
    hits = sorted({w for w in banned if re.search(r"\b%s\b" % re.escape(w), sung)})
    if hits:
        errors.append("banned words in lyrics/title: " + ", ".join(hits))

    if style and not re.search(r"\b\d{2,3}\s*BPM\b", style, re.IGNORECASE):
        warnings.append("STYLE has no BPM")

    sections = re.findall(r"\[([^\[\]]+)\](?!\])(\s*\[\[)?", lyrics)
    bare = [name for name, has_dir in sections if not has_dir]
    if bare:
        warnings.append("sections without a [[direction]]: " + ", ".join(bare))

    if "fade-out" not in excl_lower and "fade out" not in excl_lower:
        warnings.append("'fade-out' not excluded (fine only if a fade is intended)")

    print("  ·  ".join(f"{name}: {size}/{limit}" for name, size, limit in counts))
    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("WARN   ", w)
    if not errors and not warnings:
        print("OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

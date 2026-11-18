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
NEAR_LIMIT = 0.97  # warn above 970/1,000: the writing target for STYLE+EXCLUDE

CROWD_BLOCK = ["crowd noise", "audience", "applause", "crowd chants", "no crowd"]

# Keep in sync with references/lyric-craft.md.
# BANNED fails the prompt: never acceptable in sung text.
BANNED = [
    "neon", "static", "velvet", "echo", "echoes", "shadow", "shadows", "ember", "embers",
    "ashes", "spark", "sparks", "ignite", "ignites", "inferno", "shattered", "fractured",
    "tapestry", "symphony", "canvas", "mosaic", "labyrinth", "abyss", "void", "cosmos",
    "celestial", "ethereal", "eternal", "infinite", "horizon", "twilight", "moonlight",
    "starlight", "stardust", "whisper", "whispers", "whispered", "haunting", "phantom", "halo",
    "throne", "kingdom", "fairytale", "fate", "destiny", "wildfire", "beneath", "amidst",
    "embrace", "linger", "lingering", "unspoken", "unbroken", "undone", "unravel", "intertwined",
    "resonate", "cascade", "kaleidoscope",
    "soul on fire", "storm inside", "rise from the ashes", "in the dark", "through the night",
    "fading light", "city lights", "burning bright",
    # Portuguese AI-core (for lyrics written in Portuguese)
    "sussurro", "sussurros", "eternidade", "infinito", "horizonte", "abismo", "labirinto",
    "sinfonia", "tapeçaria", "etéreo", "celestial", "alma em chamas", "luzes da cidade",
]
# AVOID warns: fine when literal, AI-core when used as metaphor or stock setting.
AVOID = [
    "ghost", "ghosts", "crown", "chains", "cage", "wings", "flames", "electric", "heartbeat",
    "pulse", "midnight", "3 a.m.", "3am", "kitchen", "television", "empty streets",
]

LABELS = ("TITLE", "LYRICS", "STYLE", "EXCLUDE")

LONG_LINE = 70        # sung line longer than this is probably two lines
LONG_DIRECTION = 300  # [[direction]] longer than this should be cut down


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


def lyric_layout(lyrics):
    """Warnings for lyrics that are not one sung phrase per line."""
    out = []
    inline, long_lines, long_dirs = [], [], []
    for line in lyrics.splitlines():
        s = line.strip()
        if not s:
            continue
        m = re.match(r"^\[([^\[\]]+)\](?!\])\s*(\S.*)?$", s)
        if m and m.group(2):
            inline.append(m.group(1))
        for d in re.findall(r"\[\[(.*?)\]\]", s):
            if len(d) > LONG_DIRECTION:
                long_dirs.append(d[:30] + "…")
        sung = re.sub(r"\[\[.*?\]\]|\[[^\[\]]*\]", "", s).strip()
        if len(sung) > LONG_LINE:
            long_lines.append(sung[:40] + "…")
    if inline:
        out.append("put each [Section], its [[direction]] and the lyrics on separate lines: "
                   + ", ".join(inline))
    if long_lines:
        out.append(f"{len(long_lines)} sung line(s) over {LONG_LINE} chars; break them where "
                   "the singer breathes: " + " | ".join(long_lines[:3]))
    if long_dirs:
        out.append(f"[[direction]] over {LONG_DIRECTION} chars; keep it to 1-3 short sentences: "
                   + " | ".join(long_dirs[:3]))
    sung_lines = [l.strip().lower() for l in sung_text(lyrics).splitlines() if l.strip()]
    if sung_lines and max(sung_lines.count(l) for l in sung_lines) < 2:
        out.append("no sung line repeats; give the chorus a hook line that comes back")
    return out


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
            warnings.append(f"{name} is {size}/{limit} chars, within 3% of the limit")

    excl_lower = exclude.lower()
    excl_items = [i.strip(" .") for i in excl_lower.split(",")]
    for item in CROWD_BLOCK:
        if item not in excl_items:
            errors.append(f"EXCLUDE is missing '{item}'")
    if exclude and all(i in excl_items for i in CROWD_BLOCK) and excl_items[:5] != CROWD_BLOCK:
        warnings.append("EXCLUDE should start with: " + ", ".join(CROWD_BLOCK))

    sung = " " + (title + " " + sung_text(lyrics)).lower() + " "

    def found(words):
        return sorted({w.lower() for w in words
                       if re.search(r"(?<![\w])%s(?![\w])" % re.escape(w.lower()), sung)})

    hits = found(BANNED + args.ban)
    if hits:
        errors.append("banned words in lyrics/title: " + ", ".join(hits))
    soft = [w for w in found(AVOID) if w not in hits]
    if soft:
        warnings.append("check these are literal, not AI-core metaphors: " + ", ".join(soft))

    if style and not re.search(r"\b\d{2,3}\s*BPM\b", style, re.IGNORECASE):
        warnings.append("STYLE has no BPM")
    elif style and not re.match(r"\s*\d{2,3}\s*BPM\b", style, re.IGNORECASE):
        warnings.append("STYLE should open with BPM, key and tuning")

    sections = re.findall(r"\[([^\[\]]+)\](?!\])(\s*\[\[)?", lyrics)
    bare = [name for name, has_dir in sections if not has_dir]
    if bare:
        warnings.append("sections without a [[direction]]: " + ", ".join(bare))

    layout = lyric_layout(lyrics)
    warnings.extend(layout)

    if "fade-out" not in excl_lower and "fade out" not in excl_lower:
        warnings.append("'fade-out' not excluded (fine only if a fade is intended)")

    # Same format the skill asks to print under every prompt; paste it as is.
    print("Characters — " + " · ".join(
        f"{name} {size:,}/{limit:,}" for name, size, limit in counts if name != "TITLE"))
    for e in errors:
        print("ERROR  ", e)
    for w in warnings:
        print("WARN   ", w)
    if not errors and not warnings:
        print("OK")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Check a SKILL.md has valid frontmatter: name (kebab-case, <= 64 chars) and description (<= 1024 chars)."""

import pathlib
import re
import sys


def main(path):
    text = open(path, encoding="utf-8").read()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        sys.exit(f"{path}: missing YAML frontmatter")
    meta = dict(
        line.split(":", 1) for line in match.group(1).splitlines() if ":" in line and not line.startswith(" ")
    )
    meta = {k.strip(): v.strip() for k, v in meta.items()}
    errors = []
    name = meta.get("name", "")
    description = meta.get("description", "")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
        errors.append(f"invalid name: {name!r}")
    if not description:
        errors.append("missing description")
    elif len(description) > 1024:
        errors.append(f"description is {len(description)} chars (max 1024)")
    for ref in re.findall(r"`((?:references|scripts|examples)/[^`\s]+)`", text):
        if not pathlib.Path(path).parent.joinpath(ref.split(" ")[0]).exists():
            errors.append(f"referenced file not found: {ref}")
    if errors:
        sys.exit("\n".join(f"{path}: {e}" for e in errors))
    print(f"{path}: OK (name={name}, description={len(description)} chars)")


if __name__ == "__main__":
    main(sys.argv[1])

# Contributing

Thanks for helping make Suno prompts sound less like AI. Contributions in English or Portuguese are welcome.

## What we're looking for

- **Techniques that Suno respects**: a STYLE phrasing, an EXCLUDE combination or a `[[direction]]` pattern that fixed a real problem.
- **Troubleshooting rows**: "Suno did X" → the fix that worked.
- **Banned vocabulary**: words that make lyrics read as machine-written.
- **Examples**: complete SUPER PROMPTS that produced a good song.
- Bug fixes and tests for `check_prompt.py`.

## Ground rules

- **Evidence over opinion.** Say which Suno model version you tested and how many generations you compared. Suno changes between versions.
- **No copyrighted lyrics.** Not even short excerpts of famous songs.
- **No artist names inside STYLE examples.** Translate references into sonic descriptors (see `references/style-engineering.md`).
- **Respect the limits.** Every example must pass `check_prompt.py` (TITLE 80, LYRICS 5,000, STYLE 1,000, EXCLUDE 1,000, STYLE+EXCLUDE 1,000).

## Where things go

| Change | File |
|---|---|
| Workflow, rules, checklist | `skills/suno-super-prompt/SKILL.md` (keep it short) |
| Syntax and section names | `references/super-prompt-format.md` |
| STYLE techniques | `references/style-engineering.md` |
| EXCLUDE blocks | `references/exclude-library.md` |
| Lyric rules and banned words | `references/lyric-craft.md` (+ `BANNED` in `scripts/check_prompt.py`) |
| Acoustic, feat, cover, remaster | `references/special-versions.md` |
| Symptom → fix | `references/troubleshooting.md` |
| Full prompts | `examples/NN-technique-title.txt` + a row in `examples/README.md` |

## Development

```bash
git clone https://github.com/jasonmello/awesome-suno-prompt-skill
cd awesome-suno-prompt-skill
python3 -m unittest discover -s tests -v
python3 scripts/validate_skill.py skills/suno-super-prompt/SKILL.md
```

No dependencies beyond the Python 3.9+ standard library.

## Pull requests

1. Fork and create a branch (`technique/acoustic-lock-v5`, `fix/count-line-parsing`).
2. Make the change, add or update tests/examples.
3. Add a line under **Unreleased** in `CHANGELOG.md`.
4. Open the PR and fill in the template.

By contributing you agree that your contribution is licensed under the MIT License and that you follow the [Code of Conduct](CODE_OF_CONDUCT.md).

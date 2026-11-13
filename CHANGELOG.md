# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.2.0] - 2026-11-13

### Changed

- Renamed the project from `awesome-suno-prompt-skill` to `suno-super-prompt` (the `awesome-` prefix is reserved by convention for curated lists). Old GitHub URLs redirect; the website moved to https://jasonmello.github.io/suno-super-prompt/ and the Claude Code install is now `/plugin install suno-super-prompt@suno-super-prompt`.

### Added

- GitHub Pages website with SEO metadata, structured data, sitemap and social preview image.
- `references/release-ready.md`: release-quality STYLE/EXCLUDE add-ons, a table of common generation artifacts and fixes, a human-production plan (stems, re-recording, mix and master), honest crediting and AI disclosure, and a copy-paste release-plan prompt.
- Starter prompt rule 12 (release quality) and a README FAQ entry.
- The skill declines requests to remove watermarks, alter metadata or hide AI use, and offers the release-ready workflow instead.

## [1.1.0] - 2026-11-02

Improvements from a blind test: a fresh Claude instance used only the skill folder to write a single.

### Added

- Validator prints the `Characters — …` count line in the exact format the skill requires, ready to paste.
- Validator requires `no crowd`, warns when the crowd block isn't first, and warns when STYLE doesn't open with BPM.
- Two-tier vocabulary check: **banned** words and phrases fail the prompt; **avoid** words (midnight, kitchen, heartbeat, crown…) warn so you confirm they're literal. The lists match `lyric-craft.md`.
- Single concept format (title, theme, story, sonic direction, hook) in `SKILL.md` and `album-workflow.md`.
- Rules for naming repeated sections, and for using backing vocals with a single lead singer.
- README: "Works with any AI" section with ChatGPT Project/GPT setup (the creator's preferred tool), and an "About the creator" section.

### Changed

- Character budget states upfront that STYLE + EXCLUDE ≤ 1,000 is the binding limit: plan STYLE ≈ 700 + EXCLUDE ≈ 250.
- UPPERCASE guidance for first generations: one or two elements, the one the user stressed or the genre-defining one.
- Concept-before-prompt allows both in one reply when the user explicitly asks.
- Examples now open STYLE with BPM/key and include the full crowd block.

## [1.0.0] - 2026-11-02

### Added

- `suno-super-prompt` skill: SUPER PROMPT format (TITLE, LYRICS with `[sections]` and `[[directions]]`, STYLE, EXCLUDE), album/EP workflow and pre-send checklist.
- References: format, STYLE engineering, EXCLUDE library, lyric craft (banned AI vocabulary), special versions (acoustic lock, vocal cast, remaster, cover, false start), album workflow, troubleshooting.
- `check_prompt.py` validator: per-field character limits (TITLE 80, LYRICS 5,000, STYLE 1,000, EXCLUDE 1,000, STYLE+EXCLUDE 1,000), banned words, required crowd excludes, missing directions.
- Four worked examples, Portuguese starter prompt for other chat assistants, Claude Code plugin and marketplace manifests.
- Test suite, CI, issue and pull request templates.

[Unreleased]: https://github.com/jasonmello/suno-super-prompt/compare/v1.2.0...HEAD
[1.2.0]: https://github.com/jasonmello/suno-super-prompt/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/jasonmello/suno-super-prompt/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/jasonmello/suno-super-prompt/releases/tag/v1.0.0

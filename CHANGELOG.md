# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Changed

- README: "Works with any AI" section (ChatGPT, Claude, Gemini, Grok, DeepSeek, Copilot…) with step-by-step ChatGPT Project/GPT setup; notes that the creator prefers ChatGPT for generating songs.

## [1.0.0] - 2026-11-02

### Added

- `suno-super-prompt` skill: SUPER PROMPT format (TITLE, LYRICS with `[sections]` and `[[directions]]`, STYLE, EXCLUDE), album/EP workflow and pre-send checklist.
- References: format, STYLE engineering, EXCLUDE library, lyric craft (banned AI vocabulary), special versions (acoustic lock, vocal cast, remaster, cover, false start), album workflow, troubleshooting.
- `check_prompt.py` validator: per-field character limits (TITLE 80, LYRICS 5,000, STYLE 1,000, EXCLUDE 1,000, STYLE+EXCLUDE 1,000), banned words, required crowd excludes, missing directions.
- Four worked examples, Portuguese starter prompt for other chat assistants, Claude Code plugin and marketplace manifests.
- Test suite, CI, issue and pull request templates.

[Unreleased]: https://github.com/jasonmello/awesome-suno-prompt-skill/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/jasonmello/awesome-suno-prompt-skill/releases/tag/v1.0.0

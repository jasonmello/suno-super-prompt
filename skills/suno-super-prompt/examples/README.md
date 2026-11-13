# Examples

Prompts in the current layout: `[Section]`, its `[[direction]]` and the lyrics on separate lines, one sung phrase per line. 01–05 come from the projects this skill was built on (band "Bleed Saints"); 06 shows a non-rock genre. All pass `scripts/check_prompt.py`.

| File | Technique it shows |
|---|---|
| `01-bass-led-alt-rock-leave-late.txt` | Forcing bass as the lead instrument; concrete storytelling; outro callback |
| `02-acoustic-lock-good-on-paper.txt` | 100% voice + acoustic guitar lock, repeated in every section |
| `03-vocal-cast-feat-after-midnight.txt` | Male lead + female feature in long blocks, singer labels, VOCAL CAST sentence |
| `04-no-bass-instrumental-intro-what-you-came-for.txt` | Removing the bass, short instrumental intro instead of a cold open, late heavy release |
| `05-false-start-genre-switch-keep-the-good-part.txt` | **Reference model for the layout.** Pop → metal false start, motif that returns, chorus repeated word for word |
| `06-dance-pop-female-lead-same-time-next-week.txt` | Non-rock genre: nu-disco dance-pop, hook on beat one, post-chorus, key change |

Paste each field into Suno's Custom mode: TITLE → Song Title, LYRICS → Lyrics, STYLE → Style of Music, EXCLUDE → Exclude Styles.

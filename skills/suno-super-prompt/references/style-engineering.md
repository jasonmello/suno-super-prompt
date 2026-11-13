# STYLE engineering

STYLE is a lean production brief, not a tag soup and not an essay. Short, terse fragments of technical information beat comma lists of adjectives ("anthemic, emotional, cinematic, radio-ready…" gives generic results) and also beat long prose: when STYLE is crowded, Suno averages the instructions and the song comes out generic. Aim for 500–750 characters, 2–3 genres at most, and cut every adjective that doesn't change the sound. Pick the starting point from `genre-playbook.md`.

## Order of information

Write it in this order so the most important facts come first:

1. **Tempo, key, tuning** — `150 BPM, F# minor, drop F# guitars.`
2. **Genre blend** — 2–3 genres max, most important first. `Modern electronic alternative metal, melodic post-hardcore, dark R&B verse groove.`
3. **Intro behaviour** — `Vocal and full band on beat one; no intro.` / `Four-bar instrumental intro: …`
4. **Signature riff or motif** — describe it musically (see below).
5. **Instrument roles** — the one Suno keeps burying goes in UPPERCASE.
6. **VOCAL CAST + delivery** — who sings, how, and how many.
7. **Hook instruction** — name the hook in caps and say how it should be sung.
8. **Arrangement map** — first chorus vs later choruses, solo length, bridge, breakdown, final chorus.
9. **Ending** — `abrupt stop`, `hard cut`, `natural acoustic-string decay`.
10. **Production feel** (optional, a few words) — `Organic performance, natural room.` / `Polished, warm, groove-first.` Don't default to "dry": a fully dry vocal exposes generation artifacts.

Optional: target duration (`approximately 3:30`) — tends to keep the arrangement compact.

## Never put artist names in STYLE

Suno blocks or ignores them. Translate references into descriptors:

| Reference (conversation only) | What goes into STYLE |
|---|---|
| Raspy pop-punk lead (Sum 41-type) | `raspy male rock tenor, bright punk bite, chest-led verses, cracked high melodic belts` |
| Bad Omens-type dark electronic metal | `dark electronic alternative metal, sensual tension, deliberate vocal space, late crushing payoff` |
| Falling In Reverse-type arena hits | `arena-ready alternative metal, explosive melodic chorus, electronic post-hardcore accents` |
| Grunge influence | `abrasive grunge guitar phrasing, wiry tension, loose attack` |
| Metallica-type riffing | `riff-first heavy/thrash metal, tight downpicking, open-string gallop, twin-guitar harmonies` |
| Visual-kei guitar interplay | `angular dual-guitar interplay, chromatic stabs, bent harmonics` |
| 80s nostalgia | `nostalgic 1980s analog synth textures, gated snare` |
| Pop-princess intro | `bright bubblegum synth-pop, glossy plucked synth, programmed handclaps` |

You may name the reference in your explanation to the user — just not in the Suno fields.

## Forcing an instrument to be heard (the "say it three times" rule)

Example — the user wanted bass as the lead element:

- STYLE: `DEEP ELECTRIC BASS IS THE LEAD INSTRUMENT: thick low fundamentals, gritty midrange definition, syncopated melodic riff, loud and clearly audible throughout, including choruses. Bass and kick occupy distinct spaces.`
- [[directions]] in most sections: `Bass leads`, `Keep the low bass full and exposed`, `Deep bass remains prominent beneath the guitars`.
- EXCLUDE: `buried bass`.

The same pattern works for guitars (`MASSIVE DISTORTED GUITARS ON BEAT ONE … never lose weight` + exclude `buried guitars, soft opening, clean intro`).

## Removing an instrument

Say it's absent, say what replaces its job, and exclude every synonym.

- STYLE: `No bass instruments; low-end weight comes from kick and rhythm guitars.`
- [[directions]]: `No electric bass, no synth bass.`
- EXCLUDE: `electric bass, synth bass, bass solos, slap bass`.

## Separating groove from vocal style

When the user wants an R&B (or funk, trap…) *groove* but a rock *voice*, split the two explicitly — otherwise Suno turns the singer into a crooner.

- STYLE: `R&B INSTRUMENTAL GROOVE ONLY: swung sixteenths, syncopated deep electric bass, tight pocket drums. VOCALS STRICTLY ROCK: raspy male tenor, chest-led tone, clear consonants, huge gritty chorus belts. Restrained verses remain firm, never crooned.`
- EXCLUDE: `R&B vocals, soul vocals, melisma, vocal runs, crooning, breathy falsetto, gospel ad-libs`.

## Intro control

| User wants | STYLE | EXCLUDE |
|---|---|---|
| Hit hard immediately | `Hook and heavy guitars on beat one; no intro.` | `slow intro, soft intro, ambient opening, fade-in, clean intro, synth intro, bass-only intro, long intro` |
| Short instrumental intro, not a cold open | `Four-bar instrumental intro: distinctive mid-register synth motif …` | `cold open, long ambient intro` |
| Chorus first | `[Opening Hook]` section + `sung hook on beat one` | `instrumental intro` |

## Describing a riff so Suno can play it

Vague: "memorable riff". Better — give rhythm, contour and recurrence:

- `Signature two-bar riff: low-A attacks grouped 3+3+2, rest, high C-B-Bb phrase resolving to A. Repeat faithfully; develop its answer in chorus and solo.`
- `Recurring four-bar hook: three low attacks, rising octave slide, dissonant high answer. Exact riff returns between sections.`
- `Heavy four-note guitar motif C#–E–D#–G# opens immediately.`
- Cross-track unity: `Bridge briefly recalls the preceding track's rising riff before returning to this song's descending hook.`

## Tunings

Write the tuning in the first sentence and match the key: `drop B / B minor`, `drop C# / C# minor`, `drop F# / F# minor`. For very low tunings spell it out:
`DROP A seven-string guitars (A-E-A-D-G-B-E, low to high)` and add `muddy low end` to EXCLUDE.

## Drums

- Double kick: `Punchy acoustic drums with prominent DOUBLE-KICK PEDAL: precise bursts in transitions, sixteenth-note double bass in the heavy release and final chorus.` EXCLUDE `blast beats` (and `nonstop double kick` if it should stay accented).
- Electronic + real: `punchy acoustic drums reinforced by electronic hits`.
- Pop 80s: `punchy gated snare`.

## Breakdowns that serve the song

`Four-bar half-time breakdown transforms the main riff with full rests and double-kick flurries.` — tie the breakdown to the song's own riff and give it a bar count. EXCLUDE `generic chug breakdown, endless breakdowns, endless chugs`.

## Screams in measured doses

`one brief pitched scream` / `two intelligible raw screams` / `one short intelligible scream`, written in UPPERCASE in the lyrics where they happen. EXCLUDE `nonstop screaming` (or `constant screaming`).

## Hooks

- Name the hook: `Memorable TALK ME HOME hook`.
- Shape it: `repeat the same simple melodic contour for both opening questions, long open vowels on EASY and ME, clear space between phrases`.
- Rhythm: `Four-line chorus with identical rhythm on GO GO GO and HOME HOME HOME`.
- Space: `Hold FOR, then leave a short instrumental gap.`

## Dynamic maps

Suno follows "first / second / final" instructions well:

`First chorus stays sparse and hypnotic; second adds weight; final chorus opens into huge guitars.`

## Odd meters and fractures

`Four-bar 7/8 bridge; sharp 4/4 return into stop-start half-time breakdown.` / `Evolving instrumental middle: 6/8 at unchanged eighth-note pulse, melodic first solo, sharp return to 4/4 for answering solo.`

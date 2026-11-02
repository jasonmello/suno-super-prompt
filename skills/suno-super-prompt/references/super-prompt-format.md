# SUPER PROMPT format

## Where each field goes in Suno (Custom mode)

| SUPER PROMPT field | Suno field |
|---|---|
| TITLE | Song Title |
| LYRICS (everything, including `[ ]` and `[[ ]]`) | Lyrics |
| STYLE | Style of Music |
| EXCLUDE | Exclude Styles (under "More options") |

## Bracket grammar

| Mark | Meaning | Example |
|---|---|---|
| `[Section]` | Structure tag. Suno reads it as a section boundary. | `[Pre-Chorus]` |
| `[[direction]]` | Production direction for the section that follows. Instruments, dynamics, vocal behaviour, what must not happen. | `[[Drums drop; bent guitar, deep bass. No crowd.]]` |
| `(words)` | Backing vocal / echo. Keep short and rare. | `(Leave late.)` |
| `UPPERCASE LINE` | Inside lyrics: a shouted or screamed line. | `I DON'T HAVE TO EARN THIS!` |
| `[[Hard stop.]]` | Standalone direction between lines to control the ending or a silence. | `[[One beat of silence.]]` |

Put the `[[ ]]` immediately after the `[Section]` tag, on the same line, then the lyric lines. A standalone `[[ ]]` between stanzas works for mid-section events (stops, silences, riff returns).

## Lyric layout

Two layouts both work; pick one per song and stay consistent.

- **Prose lines** (more compact, good for long songs near the 5,000-char limit): sentences separated by periods inside a section, stanzas separated by a blank line.
- **Broken lines** (classic lyric sheet): one sung phrase per line. Easier to read rhythm and line length.

## Naming repeated sections

- **Number sections whose lyrics change:** `[Verse 1]`, `[Verse 2]`, `[Pre-Chorus 2]`.
- **Repeat the exact tag for identical repeats:** a chorus sung the same way twice is `[Chorus]` both times — it helps Suno reuse the melody.
- **Rename variants:** a chorus that's cut down, delayed or rewritten gets its own name — `[Short Chorus]`, `[Half-Chorus]`, `[Final Chorus]`.

## Backing vocals with a single lead singer

"One singer only" means one *person*. Doubles and harmonies of that same voice are fine — say so: `restrained male doubles only`, `light male harmony on the last line`. Keep `( )` echoes short and rare. Exclude what would add other people: `female vocals, duet, gang vocals, choir`.

## Section vocabulary (go beyond Intro/Verse/Chorus)

Openings: `[Opening Riff]`, `[Opening Hook]` (chorus sung first), `[Opening Verse]` (vocal on beat one), `[Instrumental Lead-In]`, `[Instrumental Intro]`, `[False Start — Instrumental]`, `[Electronic Opening]`.

Middle: `[Turn]`, `[Build]`, `[Refrain]`, `[Post-Chorus]`, `[Riff Response]`, `[Riff Return]`, `[Instrumental Hook]`, `[Instrumental Detour]`, `[Instrumental Fracture]`, `[Instrumental Collision]`, `[Half-Chorus]`, `[Short Chorus]`, `[Guitar Solo]`, `[Acoustic Turnaround]`, `[Dislocated Bridge]`, `[Heavy Release]`, `[Breakdown]`, `[Break]`, `[Emotional Lift]`.

Endings: `[Final Chorus]`, `[Final Tag]`, `[Hard Ending]`, `[Ending]`, `[Outro]`, `[Instrumental Ending]`.

Singer labels (multi-vocal songs): `[Verse 1 — Male Lead]`, `[Female Solo]`, `[Guest Rap Verse]`, `[Bridge — Both]`. See `special-versions.md`.

## What a good [[direction]] contains

1. **Instruments present** and their role ("Bass leads; sparse muted guitar").
2. **Energy / density** ("Guitars choke off", "Full-width impact", "Pull back to bass and one clean guitar").
3. **Vocal delivery** ("Close, dry, raspy vocal", "cracked melodic belt", "almost spoken but pitched").
4. **One negative** where Suno tends to drift ("No vocal chant", "No metal breakdown", "No female voice in this section").
5. Optional **bar counts** ("Four bars", "Eight-bar solo") and **events** ("One-beat stop, then full band").

Length: 1–3 short sentences. Acoustic songs need the full instrument lock in *every* direction (see `special-versions.md`).

## Annotated example (abridged)

```
TITLE: DON'T CLEAN UP

LYRICS:

[Opening Riff] [[Immediate full-band entrance. Tight low-tuned guitar hook, deep electric bass, punchy drums and short distorted synth accents. Four bars; no fade-in.]]

[Verse 1] [[Urgent raspy vocal over a driving bass groove. Clipped guitars leave space for the words.]] Someone put the chairs back wrong. Your jacket's hanging off the door. We got halfway through that song before you spilled yours on the floor.

[Refrain] [[Keep the chorus intimate at first: full deep bass, tight kick, restrained guitar. Open into heavy guitars on the fifth line.]] Don't clean up just yet. I like the proof that you were here. ...

[Instrumental Hook] [[Two bars of the main guitar hook. Bass doubles the low accents. No vocal chant.]]

...

[Final Chorus] [[One-beat stop, then full-band release. Altered lyrics, highest emotional intensity.]] Won't clean up just yet. ...

[Outro] [[Opening riff returns, shorter and heavier. No atmospheric fade.]] Found your jacket on the chair. I'll keep it till you come again. [[Hard stop.]]

STYLE: 138 BPM, B minor, drop B guitars. Modern electronic alternative metal, melodic post-hardcore, dark R&B verse groove. Immediate four-bar full-band riff; no slow opening. Deep electric bass with thick fundamentals and gritty definition stays prominent beneath guitars. Raspy male tenor: urgent conversational verses, cracked high melodic belts, restrained harmonies. First chorus starts over bass and kick, then opens halfway; later choruses hit wide immediately. Eight-bar melodic guitar solo. Altered final chorus; heavy riff outro and hard stop.

EXCLUDE: crowd noise, audience, applause, crowd chants, no crowd, live ambience, slow intro, grunge, ambient fade-in, generic chug breakdown, nonstop screaming, buried bass, robotic vocals, orchestral swells.
```

Why it works:
- The first chorus is deliberately held back and the direction says *when* it opens — Suno follows dynamic maps better than adjectives.
- The outro calls back an object from verse 1 (the jacket) — story closure.
- STYLE repeats the arrangement map in one line, so even if Suno skims the lyrics directions it still gets the shape.

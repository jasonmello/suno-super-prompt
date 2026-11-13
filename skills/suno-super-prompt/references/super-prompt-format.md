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
| `[[direction]]` | Production direction, on its own line under the section tag. Instruments, dynamics, vocal behaviour, what must not happen. 1–3 short sentences. | `[[Drums drop; bent guitar, deep bass.]]` |
| `(words)` | Backing vocal / echo. Keep short and rare. | `(Leave late.)` |
| `UPPERCASE LINE` | Inside lyrics: a shouted or screamed line. | `I DON'T HAVE TO EARN THIS!` |
| `[[Hard stop.]]` | Standalone direction between lines to control the ending or a silence. | `[[One beat of silence.]]` |

## Layout (one phrase per line)

```
[Chorus]
[[Huge melodic hook over heavy open chords. Strong repeated rhythm on KEEP THE GOOD PART.]]
You can keep the good part.
I was there for all the rest.
You can tell them that you loved me.
You can leave out what came next.
```

- `[Section]` alone on its line; its `[[direction]]` alone on the next line; then the lyrics. Never put lyrics on the tag line.
- **One sung phrase per line**, cut where the singer breathes. A line rarely needs more than ~10 syllables (~55 characters); the validator warns above 70.
- **Stanzas of 2–4 lines** (sometimes 5), separated by a blank line.
- A standalone `[[...]]` between stanzas marks an event: `[[One beat of silence.]]`, `[[Four instrumental bars.]]`, and `[[Hard stop.]]` at the very end.
- Never write a verse as a paragraph of sentences. Suno phrases melody by line breaks; run-on lines come out rushed, recited and robotic.

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
3. **Vocal delivery** ("Close raspy vocal", "cracked melodic belt", "almost spoken but pitched").
4. **One negative** where Suno tends to drift ("No vocal chant", "No metal breakdown", "No female voice in this section").
5. Optional **bar counts** ("Four bars", "Eight-bar solo") and **events** ("One-beat stop, then full band").

Length: 1–3 short sentences, under ~300 characters (the validator warns above that). Acoustic songs need the full instrument lock in *every* direction (see `special-versions.md`).

## Annotated example

`examples/05-false-start-genre-switch-keep-the-good-part.txt` is the reference model for layout and density. Abridged:

```
TITLE: KEEP THE GOOD PART

LYRICS:

[False Start — Instrumental]
[[156 BPM. Four bars of bright bubblegum synth-pop in A major: glossy plucked SYNTH, playful ascending melody, programmed handclaps. No vocals, no guitar, no bass instruments.]]

[Violent Switch]
[[Cut the pop arrangement dead. Transform its melody into an A-minor drop-A guitar riff. Eight instrumental bars.]]

[Verse 1]
[[One raspy male rock tenor, sharp chest-led singing over a relentless syncopated riff.]]
You picked the picture where I'm laughing.
Cut the argument out of frame.
Everybody says we looked so happy.
I know exactly what you'd say.

[Chorus]
[[Huge melodic hook over heavy open chords. Strong repeated rhythm on KEEP THE GOOD PART.]]
You can keep the good part.
I was there for all the rest.
You can tell them that you loved me.
You can leave out what came next.

...

[Breakdown]
[[One beat of silence. Crushing drop-A riff in half-time. First line sung low; final lines screamed clearly.]]
I was there.

I WAS THERE WHEN NO ONE WATCHED.

...

[Ending]
[[Two bars of the sugary intro synth alone. Abruptly interrupt it with one full-band guitar attack.]]
You looked so happy.
I helped you look like that.

[[Hard stop.]]

STYLE:
156 BPM. Four-bar bubblegum synth-pop fakeout in A major: glossy plucked SYNTH, sweet ascending hook, programmed handclaps, light kick. Abrupt cut into A minor, seven-string drop-A metal. Transform the SAME pop motif into a memorable heavy guitar riff. ...

EXCLUDE:
crowd noise, audience, applause, crowd chants, no crowd, acoustic guitar, fingerpicking, strummed intro, electric bass, synth bass, female vocals, rap, choir, country, melisma, robotic tuning, constant screaming, EDM drops, fade-out.
```

Why it works:
- Every section is easy to scan: tag, short direction, short lines. Suno phrases the melody where the lines break.
- The chorus comes back word for word three times (plus a half-chorus); the hook line opens and closes it.
- The pop motif from the intro returns in the Riff Return, the Instrumental Collision and the Ending, so the genre switch feels designed, not random.
- STYLE is terse fragments in the order Suno needs them; nothing in it repeats what the directions already carry except the critical elements.

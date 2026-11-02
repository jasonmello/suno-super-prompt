# Special versions

## Acoustic lock (100% voice + acoustic guitar)

The hardest thing to get out of Suno. Left any room, it "arranges" the song: electric lifts in the chorus, a bass, brushes, a crowd. Learned by iterating until it worked:

### Rules

1. **Count the sources.** `EXACTLY TWO SOURCES: one solo male lead voice and one steel-string acoustic guitar, performed together in one intimate take. NO OTHER INSTRUMENTS OR LAYERS.`
2. **Use demo vocabulary**, not production vocabulary: `acoustic demo, unplugged demo, singer-songwriter, bedroom demo, dry close-mic vocal, dry close-mic acoustic guitar`.
3. **Remove every word that implies growth or a band**: no *build, lift, fuller, swell, rise, band, solo, live, arena, cinematic, post-hardcore, emo rock*. Even "build through performance" can trigger drums — prefer `intensity comes only from the voice and the strumming`.
4. **Don't name a band reference** in STYLE for the acoustic take — "strong <band ballad> influence" pulls in that ballad's full-band arrangement.
5. **Repeat the lock in every [[direction]]**, every section: `one voice, one acoustic guitar, nothing else`.
6. **Replace the solo** with `[Acoustic Turnaround] [[Two bars on the same acoustic guitar alone. No overdub, second guitar, percussion or other sound.]]`.
7. **No percussive guitar**: `no body tapping, slaps or percussive technique` (Suno reads tapping as percussion).
8. **No room**: `dry close recording, no artificial ambience, no room sound`.
9. **End on the guitar**: `End with natural acoustic-string decay.` or `Guitar stops before the final unaccompanied words.`
10. **Shorter lyric** reduces the chance Suno "grows" the arrangement — consider cutting a verse or the second pre-chorus.
11. **Title**: append `(Acoustic Demo)` — the word *demo* helps.

### STYLE template

```
Pure acoustic studio reinterpretation, <BPM> BPM, <key>. EXACTLY TWO SOURCES: one solo male lead voice and one steel-string acoustic guitar, one intimate take. NO OTHER INSTRUMENTS OR LAYERS. Acoustic demo, singer-songwriter. Naturally raspy tenor, conversational verses, vulnerable choruses, unforced vocal cracks. Single guitar fingerpicks verses and strums open chords in choruses; no body tapping or percussive technique. Intensity comes only from voice and strumming. Two-bar passage on the same guitar instead of a solo. Dry close recording, no room sound, no crowd. End with natural acoustic-string decay.
```

### EXCLUDE template

```
crowd noise, audience, applause, crowd chants, live ambience, electric guitar, clean electric guitar, distorted guitar, lead guitar, second guitar, overdubs, bass, drums, percussion, shaker, tambourine, kick, snare, cymbals, claps, stomps, guitar tapping, piano, strings, synths, pads, loops, backing vocals, harmonies, vocal doubles, choir, reverb wash, delay, swell, riser, full-band build, screaming
```

### Section direction template

`[[Only one solo male voice and one fingerpicked acoustic guitar. No other instruments, layers, percussion or audience. Dry, intimate.]]`

Vary only the guitar technique (fingerpicked / open strumming / one quiet chord) and the vocal intensity between sections. Never vary the instrumentation.

### If it still fails

Shorten STYLE to this single line and regenerate:
`acoustic demo, one male vocal and one single acoustic guitar only, no band, no accompaniment, no additional instruments under any circumstance`

## Vocal cast (feat., duet, guest rapper, second singer)

Suno often ignores who-sings-what when voices alternate quickly. Make the cast easy to follow:

1. **Long blocks, few switches.** Lead sings everything up to the second chorus; guest takes one whole section; lead returns and finishes alone. Avoid line-by-line trading.
2. **Label every section with the singer** in UPPERCASE inside the direction: `[Male Vocal] [[SOLO MALE LEAD. No female voice in this section.]]`, `[Female Solo] [[FEMALE GUEST ALONE for this entire section. No male backing vocals.]]`.
3. **Instrumental gaps between singers**: `[Instrumental Transition] [[Two bars without vocals. Clear separation before the female feature.]]`.
4. **VOCAL CAST sentence in STYLE**: `VOCAL CAST: one raspy MALE rock lead sings every section except the single labeled FEMALE SOLO. Female guest sings that entire middle section alone. Instrumental breaks separate singers. Male returns after guitar solo and finishes alone. No duet or overlapping singers.`
5. **Describe each voice so they contrast**: lead `bright raspy male rock tenor, punk bite`; guest `deep resonant gothic male baritone, fully sung low melody, controlled vibrato` or `deep dry baritone rapper, spoken delivery, precise rhythm, no singing`.
6. **EXCLUDE the mix-ups**: `duet, overlapping singers, alternating voices within sections, mixed backing vocals` — or for rap: `overlapping lead and rapper, melodic guest rap`.
7. Put `FEATURE: <guest description>` after the title line if useful.
8. Tell the user honestly that markers improve but don't guarantee the distribution; regenerate or use Suno's editing tools for stubborn takes.

One singer narrating two characters: say it — `One raspy male tenor narrates both spouses` — and exclude `female vocals, duet, theatrical voices`.

## Remaster

The user pastes an old lyric and asks to fit it into the current record.

- Keep the song's core idea and its strongest hook line; rewrite the rest to the album's lyric standard (concrete, no banned words).
- Match the album's sonic identity (e.g. "more emo/post-hardcore mainstream, less generic metalcore").
- Keep the original's distinctive moments if they serve the song (e.g. "slower first half of the final chorus, then explosion"; "instrumental breakdown with double pedal and harmonized guitars").
- Label it in the tracklist as a deluxe/bonus track if it's heavier than the core album, and say so in STYLE: `heavier than the core album but still cohesive with <ALBUM>`.

## Cover / reinterpretation

- Do **not** write out copyrighted lyrics. Say so briefly.
- Deliver: concept, the sequence of `[Section] [[direction]]` blocks the user will interleave with their licensed lyric sheet, STYLE and EXCLUDE.
- STYLE: `Preserve the original vocal melody against a darker, heavier arrangement. Recast the recognizable instrumental motif as guitar/synth call-and-response.`

## Alternate versions (bonus tracks)

Pick the song whose meaning changes most in the new arrangement — e.g. a defiant chorus that becomes a confession when it's just voice and guitar. Position it as an epilogue/bonus after the closer.

| Version | Key moves |
|---|---|
| Acoustic / Unplugged | Acoustic lock above; keep lyrics unchanged when asked; drop to ~76 BPM. |
| Electropop | `Immediate pulsing synth bass, tight electronic kick, plucked synth hook`; EXCLUDE `distorted guitars, metal riffs, screaming, vocal chops`. Keep the original hook melody: `Preserve <HOOK> melody as the central hook.` |
| 80s dark metal pop | `Nostalgic 1980s analog synth textures with modern heavy guitars, punchy gated snare, memorable four-note synth hook`; EXCLUDE `cheesy retro pastiche, saxophone, disco`. |

## False start (genre fake-out)

E.g. it starts like a sugary teen-pop song and then a heavy metal riff takes over.

```
[False Start — Instrumental] [[156 BPM. Four bars of bright bubblegum synth-pop in A major: glossy plucked SYNTH, playful ascending melody, programmed handclaps, light electronic kick. Cheerful, almost sugary. No vocals, no guitar.]]

[Violent Switch] [[Cut the pop arrangement dead. Immediately transform its melody into an A-minor drop-A guitar riff, full-band stop, hard snare, driving double kick. Eight instrumental bars.]]
```

STYLE: say both halves and that the **same motif** is transformed. EXCLUDE what would soften the switch (`acoustic guitar, fingerpicking, strummed intro`). Bring the fake-out back at the end for an ironic close (`Two bars of the sugary intro synth alone. Abruptly interrupt it with one full-band guitar attack.`).

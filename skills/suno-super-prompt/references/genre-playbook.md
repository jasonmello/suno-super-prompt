# Genre playbook

Starting points for STYLE and EXCLUDE in any genre. Use the card for the user's genre, blend at most two or three cards, and always adapt to their references. Every EXCLUDE still opens with the crowd block (`crowd noise, audience, applause, crowd chants, no crowd`) and usually ends with `fade-out`; the guards below come after it.

How to read a card:
- **BPM**: typical range; pick one number.
- **STYLE core**: the essentials, in the order STYLE wants them. Add the intro, hook, arrangement map and ending for the specific song.
- **Voice**: delivery words Suno responds to.
- **Sections**: structures that feel native to the genre.
- **Guards**: what Suno drifts toward in this genre; exclude only what it actually drifts to.
- **Watch out**: the usual reason the result sounds generic or "AI".

## Pop

- **BPM** 95–125
- **STYLE core**: `<BPM>, <key>. Modern pop. Hook on beat one or short 2-bar intro. Punchy kick and claps, warm synth bass, bright plucked synths, clean guitar or piano motif. Polished, wide, radio-ready chorus.`
- **Voice**: `clear pop lead, intimate verses, big catchy chorus, stacked harmonies of the same voice`.
- **Sections**: Opening Hook, Verse, Pre-Chorus, Chorus, Post-Chorus (one repeated word or short phrase), Bridge, Final Chorus with a key change or a changed line.
- **Guards**: `rock guitars, metal, rap, choir, orchestral intro, slow intro`.
- **Watch out**: lists of feelings ("I feel alive, I feel free"). Pop lives on one specific hook line repeated a lot.

## Dance-pop / nu-disco / house

- **BPM** 115–128
- **STYLE core**: `<BPM>, <key>. Nu-disco dance-pop. Four-on-the-floor kick, claps on two and four, bouncing OCTAVE BASS, muted funk guitar stabs, string stabs, synth brass.`
- **Voice**: `confident pop vocal, light conversational verses, big hook`.
- **Sections**: Opening Hook, Verse, Pre-Chorus (thins out), Chorus, Post-Chorus (riff or vocal chop), Breakdown (bass and claps only), Final Chorus.
- **Guards**: `EDM drop, dubstep, trap hi-hats, heavy guitars, ballad intro`.
- **Watch out**: Suno adds a long build and an EDM drop unless you exclude it. See `examples/06-dance-pop-female-lead-same-time-next-week.txt`.

## Rock / alternative

- **BPM** 90–150
- **STYLE core**: `<BPM>, <key>. Alternative rock. Wide distorted guitars, driving acoustic drums, melodic electric bass.`
- **Voice**: `raspy male rock tenor` / `gritty female rock alto`, `chest-led verses, cracked high belts`.
- **Sections**: Opening Riff, Verse, Turn, Chorus, Instrumental Break, Bridge, Final Chorus, Hard Ending.
- **Guards**: `EDM drops, trap hi-hats, glossy pop vocals, robotic tuning`.
- **Watch out**: "epic, anthemic, cinematic" turns it into stadium wallpaper. Give a riff and a dynamic map instead. See `examples/01-bass-led-alt-rock-leave-late.txt`.

## Pop-punk / emo

- **BPM** 150–190
- **STYLE core**: `<BPM>, <key>. Pop-punk. Fast palm-muted power chords, bright punk bite, snappy snare, melodic bass runs.`
- **Voice**: `bright nasal male punk tenor, catchy chorus, no gang vocals`.
- **Sections**: Opening Hook, Verse, Chorus, Half-Time Bridge, Final Chorus.
- **Guards**: `metalcore breakdowns, nonstop screaming, synths, choir`.

## Metal / metalcore / nu metal

- **BPM** 90–180
- **STYLE core**: `<BPM>, <key>, drop <tuning> guitars. <Subgenre>. Riff described by rhythm and contour. Tight double kick in bursts. Half-time breakdown built from the main riff.`
- **Voice**: `melodic chest belts with measured screams` (say how many).
- **Sections**: Opening Riff, Verse, Chorus, Riff Return, Breakdown, Final Chorus.
- **Guards**: `nonstop screaming, generic chug breakdown, endless breakdowns, blast beats, choir`.
- **Watch out**: see `style-engineering.md` for tunings, drums and riffs. See `examples/04-no-bass-instrumental-intro-what-you-came-for.txt` and `05-…`.

## Hip-hop / rap

- **BPM** 80–100 (boom bap), 130–160 (trap, written as half-time)
- **STYLE core**: `<BPM>, <key>. <Boom bap / trap / drill>. Hard kick, crisp snare or clap, <808 bass / sampled bass>, <loop: piano, soul sample, guitar>. Sparse, beat-first mix.`
- **Voice**: `male/female rapper, precise rhythm, clear diction, <laid-back / aggressive> flow`; sung hook if wanted: `melodic sung hook`.
- **Sections**: Intro (short), Verse (16 bars), Hook, Verse, Hook, Bridge or Outro.
- **Lyrics**: internal rhymes and multisyllabic rhymes; one bar per line; hooks very short and repeated.
- **Guards**: `rock guitars, choir, orchestral, singing in verses` (if verses must be rapped), `autotune` (if wanted clean).
- **Watch out**: generic "grind, hustle, money" verses. Specific places, names, details.

## R&B / soul

- **BPM** 65–100
- **STYLE core**: `<BPM>, <key>. Contemporary R&B. Swung sixteenths, deep round bass, soft electric piano chords, crisp snaps, airy pads.`
- **Voice**: `smooth <male/female> R&B lead, controlled runs only on phrase endings, stacked harmonies`.
- **Sections**: Verse, Pre-Chorus, Chorus, Bridge with a vocal lift, Outro ad-libs.
- **Guards**: `distorted guitars, rock drums, EDM drop, excessive melisma`.

## Electronic (EDM, techno, synthwave)

- **BPM** 120–130 (house/techno), 85–118 (synthwave), 140–175 (dubstep/DnB)
- **STYLE core**: `<BPM>, <key>. <Subgenre>. <Lead synth described: saw, pluck, arpeggio>. <Drum pattern>. Clear build and drop map.`
- **Voice**: `featured vocal on the hook only` or `instrumental, no vocals`.
- **Sections**: Intro, Build, Drop, Breakdown, Build, Drop, Outro.
- **Guards**: `acoustic guitar, rock drums, live band, rap` and, for instrumentals, `vocals, vocal chops`.

## Country

- **BPM** 70–120
- **STYLE core**: `<BPM>, <key>. Modern country. Acoustic guitar strum, twangy electric guitar, pedal steel, fiddle accents, steady live drums.`
- **Voice**: `warm southern male/female lead, slight twang, clear storytelling`.
- **Sections**: Verse, Chorus, Verse, Chorus, Bridge, Final Chorus with the twist.
- **Guards**: `synths, trap hi-hats, EDM, metal guitars`.
- **Watch out**: country loves a story, but the hook still repeats. One twist in the final chorus is enough.

## Folk / singer-songwriter / acoustic

- **BPM** 60–110
- **STYLE core**: `<BPM>, <key>. Singer-songwriter. Fingerpicked acoustic guitar, light piano or none, close-mic intimate vocal, natural room.`
- **Sections**: Verse, Refrain, Verse, Refrain, Bridge, Refrain.
- **Guards**: `drums, electric guitar, synths, choir, reverb wash`.
- For voice + guitar only, use the Acoustic lock in `special-versions.md`.

## Ballad (pop / piano / power ballad)

- **BPM** 60–80
- **STYLE core**: `<BPM>, <key>. Piano ballad. Solo piano verses, strings enter in the second chorus, full drums only in the final chorus.`
- **Voice**: `emotional <male/female> lead, soft verses, powerful final chorus`.
- **Guards**: `EDM drop, rap, distorted guitars, choir` (unless wanted).
- **Watch out**: "tears, rain, heart, forever" clichés. One concrete moment carries the song.

## Reggaeton / Latin pop

- **BPM** 88–100
- **STYLE core**: `<BPM>, <key>. Reggaeton / Latin pop. Dembow rhythm, deep 808 bass, plucked synth or Spanish guitar motif, crisp percussion.`
- **Voice**: `<male/female> Latin pop vocal, rhythmic verses, melodic chorus`; Spanish lyrics if chosen in the intake.
- **Sections**: Intro (short hook), Verse, Pre-Chorus, Chorus, Verse 2, Chorus, Outro.
- **Guards**: `rock guitars, EDM drop, choir, slow intro`.

## Sertanejo (Brazil)

- **BPM** 70–100 (romântico), 120–160 (universitário / arrocha in half-time)
- **STYLE core**: `<BPM>, <key>. Sertanejo universitário. Acoustic guitar strum, viola caipira accents, accordion (sanfona) riff, punchy pop drums, warm bass.`
- **Voice**: `Brazilian male duo singing in thirds` / `female sertanejo lead`, `heartfelt, slightly nasal, clear diction`.
- **Sections**: Verse, Pre-Chorus, Chorus, Verse, Chorus, Bridge, Final Chorus.
- **Lyrics**: usually Portuguese; plain everyday phrases, drinking/heartbreak/bar situations, very repeated chorus.
- **Guards**: `rock guitars, EDM, rap, choir, English vocals` (if lyrics are Portuguese).

## Funk brasileiro / baile funk

- **BPM** 130 (funk mandelão / 150 BPM variants), 95–100 (funk melody)
- **STYLE core**: `<BPM>, <key>. Brazilian funk. Tamborzão beat, heavy 808 kicks, vocal chants of the hook, minimal synth stabs.`
- **Voice**: `Brazilian MC, rhythmic chanted delivery, short catchy hook`.
- **Lyrics**: Portuguese; very short lines, the hook repeated many times.
- **Guards**: `rock guitars, orchestral, choir, slow intro, ballad`.

## Pagode / samba

- **BPM** 85–105
- **STYLE core**: `<BPM>, <key>. Pagode / samba. Cavaquinho, pandeiro, tantã, surdo, banjo, acoustic guitar 7 strings.`
- **Voice**: `warm Brazilian male lead, relaxed swing, group backing on the chorus` (backing vocals, not crowd).
- **Guards**: `electric guitars, EDM, rap, rock drums`.

## MPB / bossa nova

- **BPM** 60–130
- **STYLE core**: `<BPM>, <key>. Bossa nova. Nylon-string guitar with bossa comping, soft brushed drums, upright bass, light flute or piano.`
- **Voice**: `soft, intimate Brazilian vocal, almost spoken, gentle phrasing`.
- **Guards**: `distorted guitars, EDM, heavy drums, belting`.

## Gospel / worship

- **BPM** 65–130
- **STYLE core**: `<BPM>, <key>. Contemporary worship. Piano and pads intro, electric guitar swells, steady drums, building to a big final chorus.`
- **Voice**: `<male/female> worship lead, sincere, building to a strong belt; choir on the final chorus only` (if wanted).
- **Guards**: `rap, EDM drop, metal` and `choir` until the final chorus.

## K-pop / J-pop

- **BPM** 100–140
- **STYLE core**: `<BPM>, <key>. K-pop. Genre-switching sections, punchy trap-pop beat, bright synths, a dance-break section.`
- **Voice**: `group vocals: rap verse, sung pre-chorus, high belted chorus`, labelled per section.
- **Guards**: `rock ballad, orchestral, slow intro`.

## Lo-fi / chill / instrumental

- **BPM** 70–90
- **STYLE core**: `<BPM>, <key>. Lo-fi hip-hop instrumental. Warm Rhodes chords, dusty drum loop, soft bass, vinyl texture.`
- Instrumental tracks: write section tags and `[[directions]]` only (no lyrics), and EXCLUDE `vocals, vocal chops, singing, rap`.

## Mixing genres

- Name the base genre first and the blend second: `Dark alternative rock with an R&B rhythmic pocket.`
- Split groove and voice when they come from different genres (see `style-engineering.md` → "Separating groove from vocal style").
- For a hard switch between genres, use a False Start (see `special-versions.md` and `examples/05-false-start-genre-switch-keep-the-good-part.txt`).

# Troubleshooting: "Suno did X"

Each fix touches three places: STYLE, the section [[directions]], and EXCLUDE.

| Symptom / user feedback | STYLE | [[directions]] | EXCLUDE |
|---|---|---|---|
| Electric guitar / drums / bass appear in the acoustic version | Rewrite with the acoustic lock (`EXACTLY TWO SOURCES…`); remove *build, lift, band, live, solo*; remove band references | Lock sentence in every section; replace solo with `[Acoustic Turnaround]` | Full acoustic EXCLUDE template (`special-versions.md`) |
| Starts slow / soft / with ambience | `Hook and heavy guitars on beat one; no intro.` | First section is `[Opening Hook]` or `[Opening Riff] [[Immediate full-band impact… No intro or fade-in.]]` | `slow intro, soft intro, ambient opening, fade-in, clean intro, synth intro, bass-only intro` |
| User doesn't want a cold open | `Four-bar instrumental intro: <motif>.` | `[Instrumental Intro] [[Four bars… No vocals.]]` | `cold open` |
| Sounds grunge / retro / garage when it should be modern | `Modern arena-ready alternative metal…, polished low end` | `tight`, `precise stops` | `grunge, loose garage drums, retro production, shoegaze` |
| Too grungy *and* too slow → wants Bring Me The Horizon / Bad Omens / Falling In Reverse energy | Raise to ~140–156 BPM, drop tuning, electronic accents, beat-one vocal | Beat-one hook, synth accents, eight-bar solo | as above + `whispered opening` |
| Bass buried | `DEEP ELECTRIC BASS … loud and clearly audible throughout` | `Bass leads`, `bass remains prominent` in most sections | `buried bass` |
| Wants **no** bass | `No bass instruments; low-end weight comes from kick and rhythm guitars.` | `No electric bass, no synth bass.` | `electric bass, synth bass, bass solos, slap bass` |
| Singer croons / does R&B runs | `VOCALS STRICTLY ROCK … never crooned` + `R&B INSTRUMENTAL GROOVE ONLY` | `firm chest voice, no soul runs` | `R&B vocals, soul vocals, melisma, crooning, breathy falsetto, gospel ad-libs` |
| Singers in the wrong order / overlapping | `VOCAL CAST:` sentence | UPPERCASE singer label in each section, instrumental gap between singers, long blocks | `duet, overlapping singers, alternating voices within sections` |
| Not heavy enough at the start | `MASSIVE DISTORTED GUITARS ON BEAT ONE … never lose weight` | heavy riff in first section | `soft opening, clean intro, buried guitars` |
| Endless chugging breakdown | Breakdown with bar count, built from the song's own riff | `[Breakdown] [[four bars… full rests…]]` | `generic chug breakdown, endless chugs` |
| Too much screaming | `one brief pitched scream` | UPPERCASE only on that one line | `nonstop screaming` |
| Theme turned into sound effects (guns, heart monitor, moans) | — | — | theme SFX block (`exclude-library.md`) |
| Fades out | `abrupt stop / hard ending` | `[[Hard stop.]]` at the end | `fade-out` |
| Crowd / applause in a studio track | `Dry close recording` / `studio` | `no audience` in intimate sections | base crowd block + `live ambience` |
| Lyrics "sound like AI" | — | Rewrite with concrete objects, dialogue, banned-word sweep | `generic AI wording` (cosmetic) |
| Rhymes not harmonious | — | Rewrite with slant rhymes, natural word order; read aloud | `forced rhymes` |
| Lines too long | — | One breath per line; split sentences | `long lyric lines` |
| Lines too short | — | Medium lines, one full clause each | `very short lyric lines` |
| Not sentimental enough | Slower, intimate clean intro, simple direct heartbreak lyrics | Fewer images, plainer words, a quiet admission in the bridge | `flashy guitar solos, big arena production` |
| Chorus not catchy | Name the hook in caps; same melodic contour for parallel lines; open vowels | Leave space after the hook word | `excessive vocal runs` |

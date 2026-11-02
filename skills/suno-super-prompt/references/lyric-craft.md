# Lyric craft — writing like a real band

## Banned vocabulary (AI-core)

These rules apply to the **sung text** (lyrics and title). `[[directions]]` are production notes for Suno, so a phrase like `No static noise` there is fine. `scripts/check_prompt.py` uses the same two lists — keep them in sync when editing.

### Banned — never use, unless the user explicitly asks

neon, static, velvet, echo, echoes, shadow, shadows, ember, embers, ashes, spark, sparks, ignite, inferno, shattered, fractured, tapestry, symphony, canvas, mosaic, labyrinth, abyss, void, cosmos, celestial, ethereal, eternal, infinite, horizon, twilight, moonlight, starlight, stardust, whisper, whispers, whispered, haunting, phantom, halo, throne, kingdom, fairytale, fate, destiny, wildfire, beneath, amidst, embrace, linger, lingering, unspoken, unbroken, undone, unravel, intertwined, resonate, cascade, kaleidoscope.

Phrases: "soul on fire", "storm inside", "rise from the ashes", "in the dark", "through the night", "fading light", "city lights", "burning bright".

### Avoid — allowed only when literal, never as metaphor or stock setting

ghost(s), crown, chains, cage, wings, flames, electric, heartbeat, pulse, midnight, 3 a.m., kitchen, television, empty streets.

"The crown of his cap was torn" is literal and fine. "You wear your pain like a crown" is AI-core. The validator warns on these so you double-check them.

### Project-specific bans

The user can extend the list mid-conversation ("no kitchen, television, beneath"; "no days or hours in the lyric"). Treat those as banned for the rest of the project, and pass them to the validator with `--ban`.

## What to write instead: concrete, filmable moments

| AI-core | Real band |
|---|---|
| "I'm drowning in the echoes of our past" | "Dad kept the engine running while I packed." |
| "Your love was a shattered symphony" | "You picked the picture where I'm laughing. Cut the argument out of frame." |
| "We burned like neon in the night" | "We used to play until the power tripped, run upstairs and throw the breaker switch." |

Techniques:

- **Objects carry emotion.** A jacket left on a chair, the oil the dad always checks, a cheap guitar cable that has to be bent to work, a photo where he's in the frame.
- **Dialogue in quotes.** Short, plain, overheard: `He asked me if I'd checked the oil. I said, "I'm not a kid."`
- **The same gesture changes meaning.** Verse 1: he refuses the oil check. Bridge: he hands over the keys — `"Have a look. I've got time."`
- **Small admissions beat big declarations.** `I said, "Yeah, just busy." You said, "You said that last time."`
- **Outro callback.** End on an object or line from verse 1.
- **Ambiguity is allowed.** Freedom or self-sabotage? Leave the listener a question.
- **Let horror/tragedy stay unexplained.** Hint at the entity, don't describe it.

## Choruses

- Natural phrase length — not telegram-short, not run-on. The sweet spot is the classic 2000s emo chorus: 6–10 syllables per line, 4–8 lines.
- One **title line** repeated at least twice, ideally opening and closing the chorus.
- **Repeated melodic anchors**: same rhythm for parallel lines (`I used to leave early. Now I leave late.`).
- **Open vowels** on held words (late, away, home, me, go).
- **Twist the final chorus**: change one or two lines so the story resolves (`I look good on paper. But Friday, come at eight.`).
- Post-chorus: a fragment of the hook, not a chant (`For a change! For a change!`).
- Avoid gang/crowd chants unless the user wants them.

## Line length

The user corrected both extremes in practice:
- "Lines are too long" → cut each line to one breath, split long sentences into two lines.
- "Lines are too short" → back to medium phrases with a full thought each.

Default to **medium**: one full clause per line, 6–12 syllables in verses.

## Rhyme

- Prefer slant and near rhymes over forced perfect rhymes (`packed / back`, `fine / time`, `door / floor`; twisting syntax to land a rhyme is not).
- Never invert word order to rhyme ("the night we did divide").
- Consistent rhyme scheme inside a stanza, free between stanzas.
- Read it aloud: if it sounds like a greeting card, rewrite.

## Theme guardrails

- No gothic or fantasy clichés; no abstract metaphor chains.
- Dark subjects (killer, war, depravation, death) are told through specific human detail, not gore or explicit language.
- Covers: never reproduce copyrighted lyrics. Write directions only and ask the user to paste their licensed copy.
- Don't quote or closely paraphrase famous songs, even as "inspiration". Use them only to calibrate line length or mood.

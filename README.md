<div align="center">

# Awesome Suno Prompt Skill

**Write Suno prompts that sound like a real band, not AI.**
**Prompts para o Suno que soam como banda de verdade, não como IA.**

[![CI](https://github.com/jasonmello/awesome-suno-prompt-skill/actions/workflows/ci.yml/badge.svg)](https://github.com/jasonmello/awesome-suno-prompt-skill/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Agent Skill](https://img.shields.io/badge/Agent%20Skill-SKILL.md-8A2BE2)](skills/suno-super-prompt/SKILL.md)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Works with any AI](https://img.shields.io/badge/works%20with-ChatGPT%20%7C%20Claude%20%7C%20Gemini%20%7C%20any%20AI-orange)](#works-with-any-ai)

[English](#english) · [Português](#português)

</div>

---

## English

An open-source AI skill that turns any AI assistant (ChatGPT, Claude, Gemini, Grok, DeepSeek, Copilot…) into the **creative director and producer** of your band. It writes complete Suno **SUPER PROMPTS** (title, lyrics with production directions, style and exclude), always within Suno's character limits.

It packages techniques learned across several albums, EPs and singles by a creator with **2+ years of intensive AI-music production** and **monetized releases on Spotify, Apple Music, YouTube Music** and other platforms ([about the creator](#about-the-creator)):

- A **STYLE** structure Suno follows (BPM, key, tuning, riff, instrument roles, vocal cast, arrangement map).
- **EXCLUDE** blocks that stop crowd noise, slow intros, buried bass and theme sound effects.
- An **acoustic lock** for takes that are 100% voice and acoustic guitar.
- A **vocal cast** method so Suno respects singer order in feats and duets.
- **Lyric rules** against AI-core: banned vocabulary, concrete storytelling, singable choruses.
- A **validator** that fails any prompt over the limits.

### Quick look

```text
TITLE: LEAVE LATE

LYRICS:
[Verse 1] [[Close, dry, raspy vocal. Bass leads; sparse muted guitar, loose half-time pocket.]]
Dad kept the engine running while I packed. One bag, two shirts, a speaker in the back. ...

[Chorus] [[Wide distorted guitars, open drums, huge melodic hook. Deep bass remains prominent.]]
I used to count the days till I could leave. Now I take the long way down our street. ... (Leave late.)

STYLE: 92 BPM, F# minor, half-time verses. Modern dark alternative rock with an R&B rhythmic pocket ...
DEEP ELECTRIC BASS IS THE LEAD INSTRUMENT ... Raspy male tenor ... bass-led abrupt outro.

EXCLUDE: crowd noise, audience, applause, crowd chants, no crowd, glossy pop vocals, buried bass, fade-out ...

Characters — LYRICS 3,289/5,000 · STYLE 786/1,000 · EXCLUDE 209/1,000 · STYLE+EXCLUDE 995/1,000
```

`[ ]` section · `[[ ]]` production direction · `( )` backing vocal · UPPERCASE line = shouted/screamed

### Works with any AI

The skill is plain text: rules, references and examples. Any assistant that accepts custom instructions or file attachments can use it: ChatGPT, Claude, Gemini, Grok, DeepSeek, Copilot, Le Chat, local models…

> **Creator's pick:** I use it every day, and my favourite for generating the songs is **ChatGPT**. That's where every album, EP and single behind these techniques was written. The other assistants work too, so use whichever you like best.

**ChatGPT (creator's choice)**

1. Create a **Project** (or a custom **GPT**).
2. Paste [`SKILL.md`](skills/suno-super-prompt/SKILL.md) into the instructions. If you write in Portuguese, the [starter prompt](prompts/starter-prompt-pt.md) works as well.
3. Upload the files from [`references/`](skills/suno-super-prompt/references) and [`examples/`](skills/suno-super-prompt/examples) as project files / knowledge.
4. Start with: *"Create the concept for my band's new EP…"* and go track by track.

ChatGPT can run `check_prompt.py` in its code tool when you upload it, which gives you exact character counts.

**Gemini, Grok, DeepSeek and others:** paste `SKILL.md` (or the starter prompt) at the start of the chat, or into a Gem / custom-instructions slot, and attach the references.

### Install (Claude)

**Claude Code: as a plugin**

```bash
/plugin marketplace add jasonmello/awesome-suno-prompt-skill
/plugin install suno-super-prompt@awesome-suno-prompt-skill
```

**Claude Code: manually**

```bash
git clone https://github.com/jasonmello/awesome-suno-prompt-skill
cp -r awesome-suno-prompt-skill/skills/suno-super-prompt ~/.claude/skills/
```

**Claude.ai / Claude desktop app**: download [`skills/suno-super-prompt`](skills/suno-super-prompt) as a `.zip` and upload it under *Settings → Capabilities → Skills*.

### Usage

Just ask:

> "Create a 5-track EP concept for my post-hardcore band. Raspy male vocalist. References: My Chemical Romance, Sum 41, Bad Omens."

> "Next track."

> "Make the acoustic version of track 2: voice and guitar only."

> "Suno put an electric guitar in the acoustic take. Fix it."

### Character limits

| Field | Limit |
|---|---|
| TITLE | 80 |
| LYRICS (including `[ ]`, `[[ ]]`, `( )`) | 5,000 |
| STYLE | 1,000 |
| EXCLUDE | 1,000 |
| STYLE + EXCLUDE together | 1,000 |

Counts include spaces and line breaks. Every prompt ends with a count line, and the validator rejects anything over the limit:

```bash
python3 skills/suno-super-prompt/scripts/check_prompt.py my-prompt.txt --ban kitchen television
```

Limits can be changed with flags (`--style-limit`, `--exclude-limit`, `--combined-limit 0` …) if Suno changes them.

### Repository layout

```text
skills/suno-super-prompt/
├── SKILL.md                     # role, workflow, rules, limits, checklist
├── references/
│   ├── super-prompt-format.md   # bracket grammar, section vocabulary
│   ├── style-engineering.md     # how to write STYLE Suno obeys
│   ├── exclude-library.md       # EXCLUDE blocks by genre, voice, theme
│   ├── lyric-craft.md           # banned AI words, hooks, rhyme, storytelling
│   ├── special-versions.md      # acoustic lock, feat/duet, remaster, cover
│   ├── album-workflow.md        # concept, tracklist, singles, bonus, cover art
│   └── troubleshooting.md       # "Suno did X" → fix
├── scripts/check_prompt.py      # validator (stdlib only)
└── examples/                    # complete prompts that worked
prompts/starter-prompt-pt.md     # copy-paste prompt for other assistants
tests/                           # validator test suite
```

### FAQ

**Does it guarantee Suno will follow everything?** No. Suno is probabilistic. These techniques raise the hit rate a lot, especially the "say it three times" rule (section direction + UPPERCASE in STYLE + opposite in EXCLUDE). Regenerate when a take drifts.

**Why no artist names in STYLE?** Suno blocks or ignores them. The skill translates references into sonic descriptors.

**Can it write covers?** It writes the arrangement directions only. Paste your own licensed lyrics.

---

## Português

Uma skill de IA open source que transforma qualquer assistente (ChatGPT, Claude, Gemini, Grok, DeepSeek, Copilot…) no **diretor criativo e produtor musical** da sua banda. Ela gera **SUPER PROMPTS** completos para o Suno (título, letra com direções de produção, style e exclude), sempre dentro dos limites de caracteres.

Reúne as técnicas usadas na criação de vários álbuns, EPs e singles por um criador com **mais de 2 anos de experiência intensa em produção musical com IA** e **músicas monetizadas no Spotify, Apple Music, YouTube Music** e outras plataformas ([sobre o criador](#sobre-o-criador)):

- **STYLE** estruturado do jeito que o Suno obedece: BPM, tom, afinação, riff, papel de cada instrumento, elenco vocal e mapa do arranjo.
- Blocos de **EXCLUDE** contra público, intro lenta, baixo enterrado e efeitos sonoros do tema.
- **Trava acústica** para versões 100% voz e violão.
- Método de **elenco vocal** para o Suno respeitar a ordem dos cantores em feats e duetos.
- **Regras de letra** contra "AI-core": palavras proibidas, storytelling concreto, refrões cantáveis.
- **Validador** que reprova qualquer prompt acima dos limites.

### Funciona com qualquer IA

A skill é só texto: regras, referências e exemplos. Qualquer assistente que aceite instruções personalizadas ou anexos consegue usá-la, como ChatGPT, Claude, Gemini, Grok, DeepSeek, Copilot, Le Chat e modelos locais.

> **A preferência do criador:** eu uso no dia a dia, e o meu favorito para gerar as músicas é o **ChatGPT**. Foi nele que nasceram todos os álbuns, EPs e singles que deram origem a essas técnicas. As outras IAs também funcionam, então use a que você preferir.

**No ChatGPT (a escolha do criador):**

1. Crie um **Projeto** (ou um **GPT** personalizado).
2. Cole o [prompt inicial em português](prompts/starter-prompt-pt.md) ou o [`SKILL.md`](skills/suno-super-prompt/SKILL.md) nas instruções.
3. Envie os arquivos de [`references/`](skills/suno-super-prompt/references) e [`examples/`](skills/suno-super-prompt/examples) como arquivos do projeto.
4. Comece com: *"Crie o conceito do novo EP da minha banda…"* e siga faixa a faixa.

Se você também enviar o `check_prompt.py`, o ChatGPT pode rodá-lo na ferramenta de código e conferir a contagem exata de caracteres.

**Gemini, Grok, DeepSeek e outras:** cole o prompt inicial (ou o `SKILL.md`) no começo da conversa, num Gem ou nas instruções personalizadas, e anexe as referências.

### Instalação no Claude

**Claude Code (plugin):**

```bash
/plugin marketplace add jasonmello/awesome-suno-prompt-skill
/plugin install suno-super-prompt@awesome-suno-prompt-skill
```

**Claude Code (manual):** copie `skills/suno-super-prompt` para `~/.claude/skills/`.

**Claude.ai / app do Claude:** compacte a pasta `skills/suno-super-prompt` em `.zip` e envie em *Settings → Capabilities → Skills*.

### Como usar

> "Crie o conceito de um EP de 5 faixas para minha banda de post-hardcore. Vocal masculino rouco. Referências: My Chemical Romance, Sum 41, Bad Omens."

> "Próxima faixa."

> "Faça a versão acústica da faixa 2, só voz e violão."

> "O Suno colocou guitarra elétrica na versão acústica. Corrija."

### Limites de caracteres

TITLE **80** · LYRICS **5.000** · STYLE **1.000** · EXCLUDE **1.000** · STYLE + EXCLUDE juntos **1.000**. Os limites contam espaços e quebras de linha. Todo prompt termina com a linha de contagem, e o `check_prompt.py` reprova qualquer campo acima do limite.

### As 8 regras de ouro

1. **Nada de "AI-core"**: sem neon, static, velvet, echoes, shadows, beneath. Use cenas concretas, objetos e diálogos.
2. **O EXCLUDE sempre começa com** `crowd noise, audience, applause, crowd chants, no crowd`.
3. **Varie a arquitetura**: nem toda música precisa ser Intro/Verse/Chorus.
4. **Refrões cantáveis**, com o último refrão mudando uma linha.
5. **Toda seção tem uma `[[direção]]`.**
6. **Fale três vezes**: nas `[[ ]]`, no STYLE em MAIÚSCULAS e o oposto no EXCLUDE.
7. **Sem nomes de artistas no STYLE.**
8. **Exclua o som literal do tema**, como tiros numa música de guerra.

---

## About the creator

**Jason Mello** ([@jasonmello](https://github.com/jasonmello)) has over **two years of intensive, hands-on work** producing music with AI. His releases are **monetized and distributed on Spotify, Apple Music, YouTube Music** and other streaming platforms.

Every rule in this skill comes from that practice: the fixes that made Suno obey, and the lyric standards that kept songs from sounding machine-made. ChatGPT is his day-to-day tool for writing the songs, and the skill is built to work with any AI.

## Sobre o criador

**Jason Mello** ([@jasonmello](https://github.com/jasonmello)) tem **mais de dois anos de experiência intensa** produzindo música com IA. Suas músicas são **monetizadas e distribuídas no Spotify, Apple Music, YouTube Music** e outras plataformas de streaming.

Cada regra desta skill vem dessa prática: as correções que fizeram o Suno obedecer e o padrão de letra que evita músicas com cara de máquina. O ChatGPT é a ferramenta do dia a dia dele para escrever as músicas, e a skill foi feita para funcionar com qualquer IA.

---

## Contributing / Contribuindo

Found a STYLE phrase or EXCLUDE trick that Suno respects? See [CONTRIBUTING.md](CONTRIBUTING.md) and open an issue or PR. Mention the Suno model version you tested.

## License

[MIT](LICENSE) © Jason Mello. This is an independent community project, not affiliated with or endorsed by Suno, Inc. Example lyrics are original works from the author's projects.

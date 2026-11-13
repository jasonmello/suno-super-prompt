"""Tests for skills/suno-super-prompt/scripts/check_prompt.py.

Run: python3 -m unittest discover -s tests -v
"""

import pathlib
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILL = ROOT / "skills" / "suno-super-prompt"
SCRIPT = SKILL / "scripts" / "check_prompt.py"
EXAMPLES = sorted((SKILL / "examples").glob("*.txt"))

CROWD = "crowd noise, audience, applause, crowd chants, no crowd, fade-out"


def build(title="T", lyrics_len=None, style_len=None, exclude_len=None, lyrics=None):
    """Build a prompt whose fields have exact character counts."""
    if lyrics is None:
        head = "[Verse]\n[[Bass leads.]]\nla la\nla la\n"
        lyrics = head + "a" * ((lyrics_len or 40) - len(head))
    style = "120 BPM, A minor. "
    style += "x" * ((style_len or 40) - len(style))
    exclude = CROWD + "y" * ((exclude_len or len(CROWD)) - len(CROWD))
    return f"TITLE: {title}\nLYRICS:\n{lyrics}\nSTYLE: {style}\nEXCLUDE: {exclude}\n"


def run(prompt, *flags):
    proc = subprocess.run(
        [sys.executable, "-I", str(SCRIPT), "-", *flags],
        input=prompt, capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout


class Limits(unittest.TestCase):
    def test_lyrics_boundary(self):
        self.assertEqual(run(build(lyrics_len=5000))[0], 0)
        code, out = run(build(lyrics_len=5001))
        self.assertEqual(code, 1)
        self.assertIn("LYRICS is 5001 chars, 1 over", out)

    def test_style_boundary(self):
        self.assertEqual(run(build(style_len=1000), "--combined-limit", "0")[0], 0)
        code, out = run(build(style_len=1001), "--combined-limit", "0")
        self.assertEqual(code, 1)
        self.assertIn("STYLE is 1001 chars", out)

    def test_exclude_boundary(self):
        self.assertEqual(run(build(exclude_len=1000), "--combined-limit", "0")[0], 0)
        code, out = run(build(exclude_len=1001), "--combined-limit", "0")
        self.assertEqual(code, 1)
        self.assertIn("EXCLUDE is 1001 chars", out)

    def test_combined_boundary(self):
        self.assertEqual(run(build(style_len=500, exclude_len=500))[0], 0)
        code, out = run(build(style_len=500, exclude_len=501))
        self.assertEqual(code, 1)
        self.assertIn("STYLE+EXCLUDE is 1001 chars", out)

    def test_title_boundary(self):
        self.assertEqual(run(build(title="T" * 80))[0], 0)
        self.assertEqual(run(build(title="T" * 81))[0], 1)

    def test_custom_limit_flag(self):
        self.assertEqual(run(build(style_len=900), "--style-limit", "800", "--combined-limit", "0")[0], 1)

    def test_count_line_is_not_counted(self):
        prompt = build(exclude_len=200) + "\nCharacters — LYRICS 40/5,000 · STYLE 40/1,000\n"
        code, out = run(prompt)
        self.assertEqual(code, 0)
        self.assertIn("EXCLUDE 200/1,000", out)

    def test_prints_count_line_in_skill_format(self):
        _, out = run(build(lyrics_len=3289, style_len=786, exclude_len=209))
        self.assertEqual(
            out.splitlines()[0],
            "Characters — LYRICS 3,289/5,000 · STYLE 786/1,000 · EXCLUDE 209/1,000 · STYLE+EXCLUDE 995/1,000",
        )


class Rules(unittest.TestCase):
    def test_missing_crowd_excludes(self):
        prompt = "TITLE: T\nLYRICS:\n[Verse] [[x]] la\nSTYLE: 90 BPM\nEXCLUDE: fade-out\n"
        code, out = run(prompt)
        self.assertEqual(code, 1)
        self.assertIn("missing 'crowd noise'", out)

    def test_no_crowd_is_required(self):
        prompt = build().replace(", no crowd", "")
        code, out = run(prompt)
        self.assertEqual(code, 1)
        self.assertIn("missing 'no crowd'", out)

    def test_crowd_block_order_warns(self):
        prompt = build().replace("EXCLUDE: crowd noise,", "EXCLUDE: fade-in, crowd noise,")
        code, out = run(prompt)
        self.assertEqual(code, 0)
        self.assertIn("EXCLUDE should start with", out)

    def test_style_must_open_with_bpm(self):
        prompt = build().replace("STYLE: 120 BPM, A minor. ", "STYLE: Dark rock, 120 BPM. ")
        code, out = run(prompt)
        self.assertEqual(code, 0)
        self.assertIn("STYLE should open with BPM", out)

    def test_banned_phrase(self):
        code, out = run(build(lyrics="[Verse] [[x]] We ran through the night"))
        self.assertEqual(code, 1)
        self.assertIn("through the night", out)

    def test_avoid_words_only_warn(self):
        code, out = run(build(lyrics="[Verse] [[x]] Back by midnight with the kitchen light on"))
        self.assertEqual(code, 0)
        self.assertIn("kitchen, midnight", out)

    def test_banned_words_in_sung_text(self):
        code, out = run(build(lyrics="[Verse] [[Bass leads.]] Neon echoes beneath the sky"))
        self.assertEqual(code, 1)
        self.assertIn("beneath, echoes, neon", out)

    def test_banned_words_ignored_inside_directions(self):
        code, _ = run(build(lyrics="[Verse] [[No static noise.]] Dad kept the engine running"))
        self.assertEqual(code, 0)

    def test_project_ban_flag(self):
        code, out = run(build(lyrics="[Verse] [[x]] Back in the kitchen"), "--ban", "kitchen")
        self.assertEqual(code, 1)
        self.assertIn("kitchen", out)

    def test_inline_section_warns(self):
        code, out = run(build(lyrics="[Verse] [[Bass leads.]] Hold on\nHold on"))
        self.assertEqual(code, 0)
        self.assertIn("separate lines: Verse", out)

    def test_new_layout_has_no_layout_warning(self):
        _, out = run(build(lyrics="[Verse]\n[[Bass leads.]]\nHold on\nHold on"))
        self.assertNotIn("separate lines", out)

    def test_long_line_warns(self):
        long = "word " * 16
        code, out = run(build(lyrics=f"[Verse]\n[[x]]\n{long}\nHold on\nHold on"))
        self.assertEqual(code, 0)
        self.assertIn("over 70 chars", out)

    def test_long_direction_warns(self):
        code, out = run(build(lyrics="[Verse]\n[[" + "a" * 301 + "]]\nHold on\nHold on"))
        self.assertEqual(code, 0)
        self.assertIn("[[direction]] over 300", out)

    def test_no_repeated_line_warns(self):
        _, out = run(build(lyrics="[Verse]\n[[x]]\nOne line\nAnother line"))
        self.assertIn("no sung line repeats", out)

    def test_portuguese_banned_word(self):
        code, out = run(build(lyrics="[Verso]\n[[x]]\nUm sussurro na porta\nNa porta"))
        self.assertEqual(code, 1)
        self.assertIn("sussurro", out)

    def test_labels_on_their_own_line(self):
        prompt = ("TITLE: T\n\nLYRICS:\n\n[Verse]\n[[x]]\nHold on\nHold on\n\n"
                  "STYLE:\n90 BPM, A minor. Pop.\n\nEXCLUDE:\n" + CROWD + "\n")
        code, out = run(prompt)
        self.assertEqual(code, 0, out)
        self.assertIn("STYLE 21/1,000", out)

    def test_missing_field(self):
        code, out = run("TITLE: T\nLYRICS:\n[Verse] [[x]] la\n")
        self.assertEqual(code, 1)
        self.assertIn("missing STYLE:", out)


class Examples(unittest.TestCase):
    def test_examples_exist(self):
        self.assertGreaterEqual(len(EXAMPLES), 1)

    def test_every_example_passes(self):
        for path in EXAMPLES:
            with self.subTest(example=path.name):
                code, out = run(path.read_text(encoding="utf-8"))
                self.assertEqual(code, 0, out)


if __name__ == "__main__":
    unittest.main()

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
        head = "[Verse] [[Bass leads.]] "
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
        self.assertIn("EXCLUDE: 200/1000", out)


class Rules(unittest.TestCase):
    def test_missing_crowd_excludes(self):
        prompt = "TITLE: T\nLYRICS:\n[Verse] [[x]] la\nSTYLE: 90 BPM\nEXCLUDE: fade-out\n"
        code, out = run(prompt)
        self.assertEqual(code, 1)
        self.assertIn("missing 'crowd noise'", out)

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

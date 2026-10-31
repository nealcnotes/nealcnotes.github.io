"""Lesson 1's Python programs, run as she'd type them."""
import subprocess
import sys
from pathlib import Path

from extract_blocks import extract

LESSON = Path(__file__).parent.parent / "posts" / "lesson1-setup-gauss.qmd"


def python_block(marker):
    blocks = [c for lang, c in extract(LESSON.read_text())
              if lang == "python" and marker in c]
    assert len(blocks) == 1, f"{marker!r} in {len(blocks)} python blocks"
    return blocks[0]


def run(code):
    return subprocess.run([sys.executable, "-c", code],
                          capture_output=True, text=True)


def test_check_py_reports_all_1000_agree():
    out = run(python_block("def sum_to"))
    assert out.returncode == 0, out.stderr
    assert out.stdout.strip().splitlines()[-1] == "all 1000 agree"


def test_why_check_py_uses_only_what_she_has_met():
    # Neal, 2026-10-31: every construct is introduced before it's used.
    # By check.py she has met =, ==, if, for, range, print and assert;
    # all(... for ...) needs generators, which come later.
    code = python_block("def sum_to")
    for later in ("all(", " for n in range(1000))", "[", "lambda"):
        assert later not in code, later


def test_a_wrong_formula_trips_check_py():
    code = python_block("def sum_to").replace("total + k", "total + k + 1")
    out = run(code)
    assert "AssertionError" in out.stderr

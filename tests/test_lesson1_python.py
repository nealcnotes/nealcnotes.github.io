"""Lesson 1's Python programs, run as she'd type them."""
import subprocess
import sys
from pathlib import Path

from extract_blocks import extract

LESSON = Path(__file__).parent.parent / "posts" / "lesson1-setup-gauss.qmd"
CHECK = 'print("all 1000 agree")'  # marks check.py: sum_to is in several programs now


def python_block(marker):
    blocks = [c for lang, c in extract(LESSON.read_text())
              if lang == "python" and marker in c]
    assert len(blocks) == 1, f"{marker!r} in {len(blocks)} python blocks"
    return blocks[0]


def run(code):
    return subprocess.run([sys.executable, "-c", code],
                          capture_output=True, text=True)


def test_check_py_reports_all_1000_agree():
    out = run(python_block(CHECK))
    assert out.returncode == 0, out.stderr
    assert out.stdout.strip().splitlines()[-1] == "all 1000 agree"


def test_why_check_py_uses_only_what_she_has_met():
    # Neal, 2026-10-31: every construct is introduced before it's used.
    # By check.py she has met =, ==, if, def, for, range, print and assert;
    # all(... for ...) needs generators, which come later, and // is only
    # met in passing (2 * sum == n * (n + 1) says it without dividing).
    code = python_block(CHECK)
    for later in ("//", "all(", " for n in range(1000))", "[", "lambda"):
        assert later not in code, later


def test_a_wrong_formula_trips_check_py():
    code = python_block(CHECK).replace("total + k", "total + k + 1")
    out = run(code)
    assert "AssertionError" in out.stderr


def blocks(lang):
    return [c for l, c in extract(LESSON.read_text()) if l == lang]


def test_why_def_comes_right_after_if():
    """Neal, 2026-11-01: def is met right after if, so every later
    program (loop.py, gauss.py, invariant.py, check.py) is built on a
    named recipe, and check.py is no longer the place functions appear."""
    py = blocks("python")
    first = lambda word: next(i for i, c in enumerate(py) if word in c)
    assert first("if ") < first("def ") < first("for "), \
        "def should come after if and before for"


def test_every_python_block_runs_on_its_own():
    """Small, complete, real: each block is a whole program she can
    run (or type into python3), never a fragment that needs a missing
    def. Exit 0, or the deliberate AssertionError of the assert demo."""
    for code in blocks("python"):
        out = run(code)
        assert out.returncode == 0 or code.startswith("assert 4"), \
            f"{code[:60]!r}: {out.stderr[-300:]}"


def test_each_cp_copies_a_file_she_already_has():
    """Neal, 2026-11-01: each improvement starts from a copy (`cp old
    new`), so the last working program stays. A cp is only right if
    its source exists by then: made earlier with nvim or cp."""
    have, copies = set(), 0
    for lang, code in extract(LESSON.read_text()):
        if lang not in ("fish", "bash"):
            continue
        for line in code.splitlines():
            words = line.split()
            if words[:1] == ["nvim"] and len(words) == 2:
                have.add(words[1])
            elif words[:1] == ["cp"]:
                src, dst = words[-2:]
                assert src in have, f"cp {src}: she has no {src} yet"
                have.add(dst)
                copies += 1
    assert copies >= 3, f"only {copies} cp; each program grows from the last"

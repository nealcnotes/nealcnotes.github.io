"""Lesson 1's Lean part has her paste each Lean block below the last,
in one editor, so the blocks together must make one program."""
import re
import subprocess
from collections import Counter
from pathlib import Path

import pytest

from extract_blocks import extract

LESSON = Path(__file__).parent.parent / "posts" / "lesson1-setup-gauss.qmd"


def lean_blocks():
    return [code for lang, code in extract(LESSON.read_text()) if lang == "lean"]


def test_each_name_is_defined_once_across_the_lean_blocks():
    # A second `def sum` in the same editor is an error she can't fix
    # without knowing the lesson meant "replace", not "add below".
    names = Counter(
        m.group(1)
        for b in lean_blocks()
        for m in re.finditer(r"^(?:def|theorem)\s+(\w+)", b, re.M)
    )
    assert names, "no Lean definitions found"
    assert [n for n, c in names.items() if c > 1] == []


LEAN = Path.home() / ".elan/bin/lean"


@pytest.mark.skipif(not LEAN.exists(), reason="Lean not installed")
def test_the_lean_blocks_run_and_owe_one_proof(tmp_path):
    # What she sees in the web page's right-hand panel, in page order.
    src = tmp_path / "Lesson.lean"
    src.write_text("".join(lean_blocks()))
    out = subprocess.run([LEAN, src], capture_output=True, text=True)
    lines = out.stdout.splitlines()
    assert [l for l in lines if "warning" not in l] == ["5050", "5050", "true"]
    assert "error" not in out.stdout
    assert "declaration uses `sorry`" in out.stdout


def test_the_claim_is_about_two_programs_agreeing():
    src = "".join(lean_blocks())
    assert re.search(r"^def sumFormula \(n : Nat\) : Nat :=", src, re.M)
    assert re.search(r"^theorem agree \(n : Nat\) : sumLoop n = sumFormula n",
                     src, re.M)


# A proof of `agree` she never sees, kept here to show the claim is true.
STEP = """
theorem step (n : Nat) : sumLoop (n+1) = sumLoop n + (n+1) := by
  simp [sumLoop, List.range'_concat, List.foldl_append]
  omega

"""
PROOF = """  induction n with
  | zero => simp [sumLoop, sumFormula]
  | succ m ih => rw [step, ih]; simp [sumFormula]; grind
"""


@pytest.mark.skipif(not LEAN.exists(), reason="Lean not installed")
def test_why_the_claim_on_the_page_is_provable(tmp_path):
    # She asks Claude to translate her proof and expects Lean to accept
    # it. If the printed claim were false (a typo), no honest translation
    # could pass, and the lesson would blame her proof.
    src = "".join(lean_blocks())
    src = src.replace("theorem agree", STEP + "theorem agree")
    src = src.replace("  sorry\n", PROOF)
    f = tmp_path / "Proved.lean"
    f.write_text(src)
    out = subprocess.run([LEAN, f], capture_output=True, text=True)
    assert out.returncode == 0, out.stdout
    assert "sorry" not in out.stdout

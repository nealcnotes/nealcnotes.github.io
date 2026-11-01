"""Lesson 1's nvim steps, typed into a clean nvim (`--clean`: no config,
as on her fresh Ubuntu), must turn each copied program into exactly the
next program the page shows. If the lesson's code and its steps drift
apart, these fail.

The keys mirror the numbered steps in the lesson; `\\<BS>` marks the
Backspace the lesson asks for after a `return` or `assert`, where nvim
guesses the next line still belongs inside the block (it can't know
when a block ends: the Indentation section's point).
"""
import shutil
import subprocess

import pytest

from test_lesson1_python import blocks

pytestmark = pytest.mark.skipif(not shutil.which("nvim"), reason="no nvim")


def program(*markers):
    found = [c for c in blocks("python") if all(m in c for m in markers)]
    assert len(found) == 1, f"{markers}: {len(found)} blocks"
    return found[0]


def type_into(tmp_path, start, keys):
    """Open `start` as a .py file in clean nvim, press `keys`, save."""
    f = tmp_path / "prog.py"
    f.write_text(start)
    script = tmp_path / "keys.vim"
    script.write_text("".join(f'exe "normal {k}"\n' for k in keys) + "wq\n")
    subprocess.run(["nvim", "--clean", "--headless", "-S", str(script), str(f)],
                   capture_output=True, timeout=20, check=True)
    return f.read_text()


def test_decide_becomes_parity(tmp_path):
    keys = ["dd", "Odef parity(n):\\<Esc>",           # steps 1-2
            "j>>j>>j>>j>>",                           # step 3
            'kkccreturn \\"even\\"\\<Esc>',             # step 4
            'jjccreturn \\"odd\\"\\<Esc>',
            "Go\\<CR>\\<BS>print(7, parity(7))\\<CR>print(10, parity(10))\\<Esc>"]
    got = type_into(tmp_path, program("n = 7", "is odd"), keys)
    assert got == program("def parity", "print(7, parity(7))")


def test_parity_becomes_loop(tmp_path):
    keys = ["Gdddd", "ofor k in range(1, 6):\\<CR>print(k, k * k, parity(k))\\<Esc>"]
    got = type_into(tmp_path, program("def parity", "print(7, parity(7))"), keys)
    assert got == program("range(1, 6)")


def test_gauss_becomes_invariant(tmp_path):
    keys = [":5\\<CR>", "ccassert 2 * total == k * (k + 1)\\<Esc>"]
    got = type_into(tmp_path, program("print(k, total)"), keys)
    assert got == program("assert 2 * total", "print(sum_to(100))")


def test_invariant_becomes_check(tmp_path):
    keys = ["Gccfor n in range(1000):\\<CR>assert 2 * sum_to(n) == n * (n + 1)"
            '\\<CR>\\<BS>print(\\"all 1000 agree\\")\\<Esc>']
    got = type_into(tmp_path, program("assert 2 * total", "print(sum_to(100))"), keys)
    assert got == program('print("all 1000 agree")')

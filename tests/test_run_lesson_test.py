"""run-lesson-test.sh finds its own folder however it is started.

The real run takes minutes in podman; here podman and uv are fakes on
PATH that succeed at once, so only the script's own shell logic runs.
"""
import os
import subprocess
from pathlib import Path

TESTS = Path(__file__).parent
SITE = TESTS.parent


def fake_tools(tmp_path):
    """podman and uv stand-ins that do nothing and succeed."""
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    for name in ("podman", "uv"):
        tool = bin_dir / name
        tool.write_text("#!/bin/sh\nexit 0\n")
        tool.chmod(0o755)
    return bin_dir


def test_why_here_ignores_cdpath(tmp_path):
    """Neal's shell sets CDPATH, and with it a relative `cd` prints the
    directory it found, so `here=$(cd tests && pwd)` once captured the
    path twice (newline in the middle) and every `cp "$here"/...` failed
    (2026-10-31, started as `bash tests/run-lesson-test.sh` from tmux).
    `CDPATH= cd` keeps the capture to pwd's one line."""
    env = dict(os.environ,
               PATH=f"{fake_tools(tmp_path)}:{os.environ['PATH']}",
               CDPATH=f".:..:{SITE.parent}")
    run = subprocess.run(["bash", "tests/run-lesson-test.sh"], cwd=SITE,
                         env=env, capture_output=True, text=True, timeout=60)
    assert "cannot stat" not in run.stderr, run.stderr
    assert run.returncode == 0, run.stderr

"""Pull a lesson's fenced code blocks into numbered files, in page order.

The container test runs these files, so it always tests the lesson as
written, not a copy that drifts. Block N in language L becomes
NN.L (e.g. 07.bash, 12.fish, 15.python, 20.lean).

Usage: python3 -I extract_blocks.py LESSON.qmd OUTDIR   (DEBUG=1 for detail)
"""
import os
import re
import sys

from loguru import logger

FENCE = re.compile(r"^```(\w+)\s*$")


def extract(text):
    """Return [(lang, code)] for every ```lang fenced block, in order."""
    blocks, lang, buf = [], None, []
    for line in text.splitlines():
        if lang is None:
            m = FENCE.match(line)
            if m:
                lang, buf = m.group(1), []
        elif line.startswith("```"):
            blocks.append((lang, "\n".join(buf) + "\n"))
            lang = None
        else:
            buf.append(line)
    assert lang is None, f"unclosed ```{lang} block"
    return blocks


def main(src, out):
    logger.remove()
    logger.add(sys.stderr, level="DEBUG" if os.environ.get("DEBUG") else "INFO")
    blocks = extract(open(src).read())
    os.makedirs(out, exist_ok=True)
    for i, (lang, code) in enumerate(blocks, 1):
        name = f"{i:02d}.{lang}"
        with open(os.path.join(out, name), "w") as f:
            f.write(code)
        logger.debug("{}: {} lines, starts {!r}", name, code.count("\n"), code[:40])
    logger.info("{} blocks from {} -> {}", len(blocks), src, out)


if __name__ == "__main__":
    main(*sys.argv[1:3])

"""The site: a Quarto blog whose home page lists posts, newest first.

Old Jekyll posts (2023-24) and the new lessons sit side by side in
posts/, as .md and .qmd: Quarto reads both the same way, but unlike
Jekyll it takes a post's date only from its header, never its filename.
"""
import datetime
import re
from pathlib import Path

import yaml

SITE = Path(__file__).parent.parent
POSTS = sorted((SITE / "posts").glob("*.*md"))      # on the home page
ARCHIVE = sorted((SITE / "archive").glob("2*.*md"))  # old, linked from the footer
ALL = POSTS + ARCHIVE


def header(path):
    """The YAML block between the first two --- lines."""
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(), re.S)
    assert m, f"{path.name}: no YAML header"
    return yaml.safe_load(m.group(1))


def test_there_are_posts():
    assert len(ALL) >= 8, [p.name for p in ALL]


def test_why_old_comics_live_in_the_archive():
    """The home page is for the new work (lessons); the 2023-24 comics
    moved to archive/ (Neal, 2026-10-31), still public, one footer link
    away, so their URLs keep working for anyone who has them."""
    assert ARCHIVE
    assert not any("old-comics" in header(p)["categories"] for p in POSTS)
    cfg = yaml.safe_load((SITE / "_quarto.yml").read_text())
    footer = str(cfg["website"]["page-footer"])
    assert "archive/" in footer


def test_why_every_post_has_a_date_in_its_header():
    """Jekyll read the date from `2023-11-05-mergetool.md`; Quarto
    doesn't, so a post without `date:` would sort as undated in the
    listing (and show no date)."""
    for p in ALL:
        h = header(p)
        assert h.get("title"), p.name
        assert isinstance(h.get("date"), datetime.date), f"{p.name}: date {h.get('date')!r}"


def test_a_dated_filename_agrees_with_its_header():
    for p in ALL:
        m = re.match(r"(\d{4}-\d{2}-\d{2})-", p.name)
        if m:
            assert str(header(p)["date"]) == m.group(1), p.name


def test_lesson_1_is_the_newest_post():
    newest = max(POSTS, key=lambda p: header(p)["date"])
    assert newest.name == "lesson1-setup-gauss.qmd"


def test_categories_are_a_list_and_tags_are_folded_in():
    """Quarto's listings browse by `categories:` only, so the old
    `tags:` move there rather than vanish."""
    for p in ALL:
        h = header(p)
        assert "tags" not in h, p.name
        assert isinstance(h.get("categories"), list), p.name


def test_why_the_build_carries_cname():
    """`quarto publish gh-pages` replaces the whole branch each time;
    without CNAME in the output, GitHub drops the custom domain."""
    assert (SITE / "CNAME").read_text().strip() == "nealcnotes.com"
    cfg = yaml.safe_load((SITE / "_quarto.yml").read_text())
    assert "CNAME" in cfg["project"]["resources"]


def test_no_jekyll_left():
    for name in ("_config.yml", "Gemfile", "_posts", "_includes", "_sass", "index.md"):
        assert not (SITE / name).exists(), name


def test_why_posts_carry_no_html_comments():
    """Promotion strips the draft's `<!-- ... -->` notes (state, Q&A,
    Claude's comments): they are invisible on the page but readable in
    its source, and the working copy with them stays in _drafts/ (the
    essentialine pattern)."""
    for p in ALL:
        assert "<!--" not in p.read_text(), f"{p.name} still has a comment"


NOTE_MARKS = ("[claude:", ">> Claude")


def test_why_posts_carry_no_bracket_notes():
    """Notes to Claude written as plain text, `[claude: ...]`, aren't
    HTML comments, so stripping comments leaves them in and Markdown
    shows them on the page (lesson 1 went live with one, 2026-10-31).
    Promotion fails until each is answered and folded into a comment."""
    for p in ALL:
        text = p.read_text().lower()
        for mark in NOTE_MARKS:
            assert mark.lower() not in text, f"{p.name}: {mark} note left in"


def test_why_notebooks_ship_as_downloads_not_pages():
    """The pandas posts link /assets/notebooks/*.ipynb for readers to
    download. Left to its defaults Quarto renders every .ipynb into a
    page (and did, during the first publish, 2026-10-31); the render
    list keeps Quarto to the home page and posts/. Asks Quarto itself
    (`quarto inspect`, ~1 s) which files it would render."""
    import json
    import subprocess
    out = subprocess.run(["quarto", "inspect"], cwd=SITE, capture_output=True,
                         text=True, check=True, timeout=60).stdout
    inputs = {str(Path(f).relative_to(SITE)) for f in json.loads(out)["files"]["input"]}
    assert not any(f.endswith(".ipynb") for f in inputs), inputs
    assert {"index.qmd", "posts/lesson1-setup-gauss.qmd", "archive/index.qmd"} <= inputs
    assert len(inputs) == 2 + len(ALL)


VIDEO = re.compile(r"\{\{<\s*video\s+(\S+)")


def test_every_local_video_a_post_embeds_exists():
    """Posts embed video with Quarto's `{{< video path >}}` shortcode;
    a local path (not a URL) must be a file beside the post, or the page
    ships an empty player. Short clips live in the repo and GitHub Pages
    serves them; long ones would go to a video host (essentialine uses
    Cloudflare Stream: its ~200 MB files exceed GitHub's 100 MB limit)."""
    seen = 0
    for p in ALL:
        for src in VIDEO.findall(p.read_text()):
            src = src.strip("\"'")
            if src.startswith("http"):
                continue
            seen += 1
            f = p.parent / src
            assert f.is_file(), f"{p.name}: {src} missing"
            assert f.stat().st_size < 50_000_000, f"{src}: too big for the repo"
    assert seen, "no post embeds a local video yet"


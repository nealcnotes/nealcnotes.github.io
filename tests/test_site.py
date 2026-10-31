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
POSTS = sorted((SITE / "posts").glob("*.*md"))


def header(path):
    """The YAML block between the first two --- lines."""
    m = re.match(r"---\n(.*?)\n---\n", path.read_text(), re.S)
    assert m, f"{path.name}: no YAML header"
    return yaml.safe_load(m.group(1))


def test_there_are_posts():
    assert len(POSTS) >= 8, [p.name for p in POSTS]


def test_why_every_post_has_a_date_in_its_header():
    """Jekyll read the date from `2023-11-05-mergetool.md`; Quarto
    doesn't, so a post without `date:` would sort as undated in the
    listing (and show no date)."""
    for p in POSTS:
        h = header(p)
        assert h.get("title"), p.name
        assert isinstance(h.get("date"), datetime.date), f"{p.name}: date {h.get('date')!r}"


def test_a_dated_filename_agrees_with_its_header():
    for p in POSTS:
        m = re.match(r"(\d{4}-\d{2}-\d{2})-", p.name)
        if m:
            assert str(header(p)["date"]) == m.group(1), p.name


def test_lesson_1_is_the_newest_post():
    newest = max(POSTS, key=lambda p: header(p)["date"])
    assert newest.name == "lesson1-setup-gauss.qmd"


def test_categories_are_a_list_and_tags_are_folded_in():
    """Quarto's listings browse by `categories:` only, so the old
    `tags:` move there rather than vanish."""
    for p in POSTS:
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

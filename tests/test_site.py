"""The site: course notes, not a blog (Neal, 2026-11-20).

Each course is a section of the sidebar in _quarto.yml, its parts in
course order; Previous / Next follow that order, and the home page
links each course's first part. Dates are shown, but order nothing.
Posts sit flat in posts/, as .md or .qmd; Quarto takes a post's date
only from its header, never its filename.
"""
import datetime
import re
from pathlib import Path

import yaml

SITE = Path(__file__).parent.parent
POSTS = sorted((SITE / "posts").glob("*.*md"))      # the courses' parts
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


def config():
    return yaml.safe_load((SITE / "_quarto.yml").read_text())


def courses():
    """[(course title, [post file names in course order]), ...]"""
    return [(sec["section"], [Path(c).name for c in sec["contents"]])
            for sec in config()["website"]["sidebar"]["contents"]]


def test_why_courses_are_ordered_by_the_sidebar():
    """Course notes, not a blog: the order is written once, in the
    sidebar, and Previous / Next walk it (page-navigation). Every post
    belongs to exactly one course, so none drops out of the menu and
    none is reached by two paths."""
    listed = [name for _, parts in courses() for name in parts]
    assert len(listed) == len(set(listed)), listed
    assert sorted(listed) == sorted(p.name for p in POSTS)
    assert config()["website"]["page-navigation"] is True


def test_why_the_home_page_only_links_each_course():
    """The home page names each course and links its first part; it
    repeats no order, so the sidebar stays the only list."""
    index = (SITE / "index.qmd").read_text()
    for title, parts in courses():
        assert title in index, title
        assert f"posts/{parts[0]}" in index, (title, parts[0])
        for later in parts[1:]:
            assert f"posts/{later})" not in index, later


SHORT_LINK = re.compile(r"^/([a-z]+)/index\.html$")


def test_why_each_course_has_a_short_link():
    """So a course can be shared as nealcnotes.com/trig/ (Neal,
    2026-11-20): its first part carries one Quarto `aliases:` entry,
    `/<name>/index.html`, and the build writes a redirect page there.
    Later parts carry none, so each short link means one course."""
    names = []
    for title, parts in courses():
        aliases = header(SITE / "posts" / parts[0]).get("aliases", [])
        assert len(aliases) == 1, (title, aliases)
        assert SHORT_LINK.match(aliases[0]), (title, aliases[0])
        names.append(aliases[0])
        for later in parts[1:]:
            assert "aliases" not in header(SITE / "posts" / later), later
    assert len(names) == len(set(names)), names


def test_why_recently_added_keeps_the_feed():
    """A short "Recently added" listing, newest first, keeps the RSS
    feed (index.xml) alive for anyone subscribed from the blog days."""
    listing = header(SITE / "index.qmd")["listing"]
    assert listing["feed"] is True
    assert listing["sort"] == "date desc"
    assert listing["max-items"] == 5


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



def test_why_posts_that_run_python_are_frozen():
    """A ```{python} cell runs at render time, which needs Jupyter;
    the publishing machine (x280) has none, and the first publish of
    moneymath-how-long failed on it (2026-11-07). With `freeze: auto`
    Quarto reuses the committed `_freeze/` output instead of rerunning
    the cell, so the post must be rendered once (anywhere, e.g.
    `uv run --with jupyter ... quarto render <post>`) and `_freeze/`
    committed."""
    config = yaml.safe_load((SITE / "_quarto.yml").read_text())
    runs_code = [p for p in POSTS if re.search(r"^```\{python", p.read_text(), re.M)]
    assert runs_code, "no post runs Python: drop this test and the freeze"
    assert config.get("execute", {}).get("freeze") == "auto"
    for p in runs_code:
        frozen = SITE / "_freeze" / "posts" / p.stem / "execute-results" / "html.json"
        assert frozen.exists(), f"{p.name}: not frozen ({frozen} missing)"

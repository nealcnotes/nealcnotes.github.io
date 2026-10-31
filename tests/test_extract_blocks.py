"""The container test trusts extract_blocks to hand it every block, in order."""
from extract_blocks import extract

PAGE = """Intro.

```bash
pwd
ls
```

Text with `inline` code.

```python
2 + 2
```

```{python}
not a plain fence: a Quarto executable cell, skipped
```
"""


def test_blocks_come_out_in_page_order_with_their_language():
    assert extract(PAGE) == [("bash", "pwd\nls\n"), ("python", "2 + 2\n")]


def test_unclosed_block_fails_loudly():
    try:
        extract("```bash\npwd\n")
    except AssertionError as e:
        assert "unclosed" in str(e)
    else:
        raise AssertionError("expected a failure")

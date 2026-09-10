import pytest

from text_workbench.core import normalize, split_text, summarize


@pytest.mark.parametrize(
    "raw,clean,tokens",
    [
        ("  Hello\tWORLD\nhello  ", "hello world hello", ["hello", "world", "hello"]),
        ("", "", []),
        (" \n\t", "", []),
        (" Café\t世界 ", "café 世界", ["café", "世界"]),
        ("Hi, there!", "hi, there!", ["hi,", "there!"]),
    ],
)
def test_rules(raw, clean, tokens):
    assert normalize(raw) == clean
    assert normalize(normalize(raw)) == clean
    assert split_text(raw) == tokens
    assert summarize(raw) == {"characters": len(clean), "words": len(tokens)}

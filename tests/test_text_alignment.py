import pytest
from src.text_alignment.util import text_alignment


def test_returns_list():
    result = text_alignment(5)
    assert isinstance(result, list)


def test_first_line():
    result = text_alignment(5)
    assert result[0].strip() == "H"


def test_last_line():
    result = text_alignment(5)
    assert result[-1].strip() == "H"


def test_top_cone_middle():
    result = text_alignment(5)
    assert result[2].strip() == "HHHHH"


def test_contains_middle_bar():
    result = text_alignment(5)
    assert "H" * 25 in result[11]


def test_total_lines():
    result = text_alignment(5)
    assert len(result) == 21


def test_invalid_input():
    with pytest.raises(ValueError):
        text_alignment(0)


def test_negative_input():
    with pytest.raises(ValueError):
        text_alignment(-3)
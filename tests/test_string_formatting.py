import pytest
from src.string_formatting.util import print_formatted


def test_number_1():
    assert print_formatted(1) == [
        "1 1 1 1"
    ]


def test_number_2():
    assert print_formatted(2) == [
        " 1  1  1  1",
        " 2  2  2 10"
    ]


def test_number_5():
    assert print_formatted(5) == [
        "  1   1   1   1",
        "  2   2   2  10",
        "  3   3   3  11",
        "  4   4   4 100",
        "  5   5   5 101"
    ]


def test_number_8():
    result = print_formatted(8)

    assert result[-1] == "1000 10  8 1000"


def test_invalid_number():
    with pytest.raises(ValueError):
        print_formatted(0)


def test_negative_number():
    with pytest.raises(ValueError):
        print_formatted(-5)
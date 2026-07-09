import pytest
from src.merge_the_tools.util import merge_the_tools


def test_hackerrank_example():
    assert merge_the_tools("AABCAAADA", 3) == [
        "AB",
        "CA",
        "AD"
    ]


def test_no_duplicates():
    assert merge_the_tools("ABCDEFGH", 2) == [
        "AB",
        "CD",
        "EF",
        "GH"
    ]


def test_all_duplicates():
    assert merge_the_tools("AAAAAA", 2) == [
        "A",
        "A",
        "A"
    ]


def test_single_character_chunks():
    assert merge_the_tools("ABCDE", 1) == [
        "A",
        "B",
        "C",
        "D",
        "E"
    ]


def test_entire_string_one_chunk():
    assert merge_the_tools("BANANA", 6) == [
        "BAN"
    ]


def test_numeric_characters():
    assert merge_the_tools("11223344", 2) == [
        "1",
        "2",
        "3",
        "4"
    ]


def test_invalid_k():
    with pytest.raises(ValueError):
        merge_the_tools("ABCDE", 0)
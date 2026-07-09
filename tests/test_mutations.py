import pytest
from src.mutations.util import mutate_string


def test_mutate_middle_character():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"


def test_mutate_first_character():
    assert mutate_string("hello", 0, "H") == "Hello"


def test_mutate_last_character():
    assert mutate_string("python", 5, "N") == "pythoN"


def test_single_character_string():
    assert mutate_string("a", 0, "b") == "b"


def test_numeric_string():
    assert mutate_string("12345", 2, "9") == "12945"


def test_position_out_of_range():
    with pytest.raises(IndexError):
        mutate_string("hello", 10, "a")


def test_negative_position():
    with pytest.raises(IndexError):
        mutate_string("hello", -1, "a")


def test_multiple_characters():
    with pytest.raises(ValueError):
        mutate_string("hello", 2, "ab")
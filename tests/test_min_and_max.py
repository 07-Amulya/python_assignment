import pytest
from src.min_and_max.util import find_max_of_row_mins


def test_sample_case():
    matrix = [
        [2, 5],
        [3, 7],
        [1, 3]
    ]
    assert find_max_of_row_mins(matrix) == 3


def test_square_matrix():
    matrix = [
        [5, 4, 3],
        [8, 7, 6],
        [2, 9, 1]
    ]
    assert find_max_of_row_mins(matrix) == 6


def test_single_row():
    matrix = [
        [10, 20, 30]
    ]
    assert find_max_of_row_mins(matrix) == 10


def test_single_column():
    matrix = [
        [5],
        [8],
        [2]
    ]
    assert find_max_of_row_mins(matrix) == 8


def test_negative_numbers():
    matrix = [
        [-1, -2],
        [-3, -4]
    ]
    assert find_max_of_row_mins(matrix) == -2


def test_same_values():
    matrix = [
        [5, 5],
        [5, 5]
    ]
    assert find_max_of_row_mins(matrix) == 5


def test_empty_matrix():
    with pytest.raises(ValueError):
        find_max_of_row_mins([])
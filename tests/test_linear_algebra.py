import pytest
from src.linear_algebra.util import calculate_determinant


def test_2x2_matrix():
    matrix = [
        [1.0, 2.0],
        [3.0, 4.0]
    ]
    assert calculate_determinant(matrix) == -2.0


def test_identity_matrix():
    matrix = [
        [1.0, 0.0],
        [0.0, 1.0]
    ]
    assert calculate_determinant(matrix) == 1.0


def test_3x3_matrix():
    matrix = [
        [6.0, 1.0, 1.0],
        [4.0, -2.0, 5.0],
        [2.0, 8.0, 7.0]
    ]
    assert calculate_determinant(matrix) == -306.0


def test_singular_matrix():
    matrix = [
        [1.0, 2.0],
        [2.0, 4.0]
    ]
    assert calculate_determinant(matrix) == 0.0


def test_single_element_matrix():
    matrix = [
        [5.0]
    ]
    assert calculate_determinant(matrix) == 5.0


def test_empty_matrix():
    with pytest.raises(ValueError):
        calculate_determinant([])


def test_non_square_matrix():
    matrix = [
        [1.0, 2.0, 3.0],
        [4.0, 5.0, 6.0]
    ]

    with pytest.raises(ValueError):
        calculate_determinant(matrix)
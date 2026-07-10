import pytest
from src.iterables_and_iterators.util import calculate_probability


def test_sample_case():
    letters = ['a', 'a', 'c', 'd']
    assert round(calculate_probability(letters, 2), 4) == 0.8333


def test_all_a():
    letters = ['a', 'a', 'a']
    assert calculate_probability(letters, 2) == 1.0


def test_no_a():
    letters = ['b', 'c', 'd']
    assert calculate_probability(letters, 2) == 0.0


def test_k_equals_1():
    letters = ['a', 'b', 'c']
    assert round(calculate_probability(letters, 1), 4) == 0.3333


def test_k_equals_n():
    letters = ['a', 'b', 'c']
    assert calculate_probability(letters, 3) == 1.0


def test_invalid_k():
    with pytest.raises(ValueError):
        calculate_probability(['a', 'b'], 3)


def test_empty_list():
    assert calculate_probability([], 0) == 0.0
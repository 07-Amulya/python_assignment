import pytest
from src.no_idea.util import calculate_happiness


def test_sample_case():
    arr = [1, 5, 3]
    set_a = {3, 1}
    set_b = {5, 7}

    assert calculate_happiness(arr, set_a, set_b) == 1


def test_all_in_set_a():
    arr = [1, 2, 3]
    set_a = {1, 2, 3}
    set_b = {4, 5}

    assert calculate_happiness(arr, set_a, set_b) == 3


def test_all_in_set_b():
    arr = [1, 2, 3]
    set_a = {4, 5}
    set_b = {1, 2, 3}

    assert calculate_happiness(arr, set_a, set_b) == -3


def test_no_matches():
    arr = [1, 2, 3]
    set_a = {4, 5}
    set_b = {6, 7}

    assert calculate_happiness(arr, set_a, set_b) == 0


def test_same_element_in_both_sets():
    arr = [1]
    set_a = {1}
    set_b = {1}

    assert calculate_happiness(arr, set_a, set_b) == 0


def test_empty_array():
    arr = []
    set_a = {1, 2}
    set_b = {3, 4}

    assert calculate_happiness(arr, set_a, set_b) == 0


def test_duplicate_elements():
    arr = [1, 1, 2, 2]
    set_a = {1}
    set_b = {2}

    assert calculate_happiness(arr, set_a, set_b) == 0
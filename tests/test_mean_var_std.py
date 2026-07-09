import pytest
import numpy as np
from src.mean_var_std.util import calculate_statistics


def test_sample_case():
    matrix = [
        [1, 2],
        [3, 4]
    ]

    mean, var, std = calculate_statistics(matrix)

    assert np.array_equal(mean, np.array([1.5, 3.5]))
    assert np.array_equal(var, np.array([1., 1.]))
    assert std == round(float(np.std(np.array(matrix))), 11)


def test_single_row():
    matrix = [
        [2, 4, 6]
    ]

    mean, var, std = calculate_statistics(matrix)

    assert np.array_equal(mean, np.array([4.0]))
    assert np.array_equal(var, np.array([0., 0., 0.]))
    assert std == round(float(np.std(np.array(matrix))), 11)


def test_single_column():
    matrix = [
        [1],
        [2],
        [3]
    ]

    mean, var, std = calculate_statistics(matrix)

    assert np.array_equal(mean, np.array([1., 2., 3.]))
    assert np.array_equal(var, np.array([0.66666667]))
    assert std == round(float(np.std(np.array(matrix))), 11)


def test_all_same_values():
    matrix = [
        [5, 5],
        [5, 5]
    ]

    mean, var, std = calculate_statistics(matrix)

    assert np.array_equal(mean, np.array([5., 5.]))
    assert np.array_equal(var, np.array([0., 0.]))
    assert std == 0.0


def test_negative_numbers():
    matrix = [
        [-1, -2],
        [-3, -4]
    ]

    mean, var, std = calculate_statistics(matrix)

    assert np.array_equal(mean, np.array([-1.5, -3.5]))
    assert np.array_equal(var, np.array([1., 1.]))
    assert std == round(float(np.std(np.array(matrix))), 11)


def test_empty_matrix():
    with pytest.raises(ValueError):
        calculate_statistics([])
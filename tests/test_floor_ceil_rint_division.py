import pytest
import numpy as np
from src.floor_ceil_rint_division.util import floor_ceil_rint_division


def test_sample_case():
    floor_arr, ceil_arr, rint_arr = floor_ceil_rint_division(
        [1.1, 2.2, 3.3, 4.4, 5.5]
    )

    assert np.array_equal(floor_arr, np.array([1., 2., 3., 4., 5.]))
    assert np.array_equal(ceil_arr, np.array([2., 3., 4., 5., 6.]))
    assert np.array_equal(rint_arr, np.array([1., 2., 3., 4., 6.]))


def test_negative_numbers():
    floor_arr, ceil_arr, rint_arr = floor_ceil_rint_division(
        [-1.1, -2.9]
    )

    assert np.array_equal(floor_arr, np.array([-2., -3.]))
    assert np.array_equal(ceil_arr, np.array([-1., -2.]))
    assert np.array_equal(rint_arr, np.array([-1., -3.]))


def test_integer_values():
    floor_arr, ceil_arr, rint_arr = floor_ceil_rint_division(
        [1.0, 2.0, 3.0]
    )

    assert np.array_equal(floor_arr, np.array([1., 2., 3.]))
    assert np.array_equal(ceil_arr, np.array([1., 2., 3.]))
    assert np.array_equal(rint_arr, np.array([1., 2., 3.]))


def test_single_value():
    floor_arr, ceil_arr, rint_arr = floor_ceil_rint_division([4.7])

    assert np.array_equal(floor_arr, np.array([4.]))
    assert np.array_equal(ceil_arr, np.array([5.]))
    assert np.array_equal(rint_arr, np.array([5.]))


def test_empty_input():
    with pytest.raises(ValueError):
        floor_ceil_rint_division([])


def test_zero_values():
    floor_arr, ceil_arr, rint_arr = floor_ceil_rint_division([0.0])

    assert np.array_equal(floor_arr, np.array([0.]))
    assert np.array_equal(ceil_arr, np.array([0.]))
    assert np.array_equal(rint_arr, np.array([0.]))
import numpy as np

np.set_printoptions(legacy='1.13')


def floor_ceil_rint_division(numbers):
    """
    Returns floor, ceil, and rint of the given numbers.

    Args:
        numbers (list): List of float values.

    Returns:
        tuple: (floor_array, ceil_array, rint_array)

    Raises:
        ValueError: If the input list is empty.
    """

    if not numbers:
        raise ValueError("Input list cannot be empty.")

    arr = np.array(numbers)

    return (
        np.floor(arr),
        np.ceil(arr),
        np.rint(arr)
    )
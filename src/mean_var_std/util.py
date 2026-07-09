import numpy as np


def calculate_statistics(matrix):
    """
    Calculates mean (axis=1), variance (axis=0),
    and standard deviation of the entire matrix.

    Args:
        matrix (list): 2D list of integers.

    Returns:
        tuple: (mean_array, var_array, std_value)

    Raises:
        ValueError: If the matrix is empty.
    """

    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    arr = np.array(matrix)

    mean = np.mean(arr, axis=1)
    var = np.var(arr, axis=0)
    std = round(float(np.std(arr, axis=None)), 11)

    return mean, var, std
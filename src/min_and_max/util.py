import numpy as np


def find_max_of_row_mins(matrix):
    """
    Returns the maximum value among the minimum values of each row.

    Args:
        matrix (list): 2D list of integers.

    Returns:
        int: Maximum of the row minimums.

    Raises:
        ValueError: If the matrix is empty.
    """

    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    arr = np.array(matrix)

    row_mins = np.min(arr, axis=1)
    return int(np.max(row_mins))
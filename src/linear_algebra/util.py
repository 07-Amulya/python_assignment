import numpy as np


def calculate_determinant(matrix):
    """
    Calculates the determinant of a square matrix.

    Args:
        matrix (list): Square matrix represented as a 2D list.

    Returns:
        float: Determinant rounded to 2 decimal places.

    Raises:
        ValueError: If the matrix is empty or not square.
    """

    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    rows = len(matrix)

    for row in matrix:
        if len(row) != rows:
            raise ValueError("Matrix must be square.")

    arr = np.array(matrix)

    return round(float(np.linalg.det(arr)), 2)
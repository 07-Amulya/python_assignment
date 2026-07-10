import math


def calculate_probability(letters, k):
    """
    Calculates the probability of selecting at least one 'a'
    when choosing k elements.

    Args:
        letters (list): List of lowercase letters.
        k (int): Number of selections.

    Returns:
        float: Probability.

    Raises:
        ValueError: If k is invalid.
    """

    n = len(letters)

    if k < 0 or k > n:
        raise ValueError("Invalid value of k.")

    count_a = letters.count('a')

    # If no 'a' exists
    if count_a == 0:
        return 0.0

    # If every letter is 'a'
    if count_a == n:
        return 1.0

    non_a = n - count_a

    if non_a < k:
        return 1.0

    probability = 1 - (
        math.prod(range(non_a - k + 1, non_a + 1)) /
        math.prod(range(n - k + 1, n + 1))
    )

    return probability
def calculate_happiness(arr, set_a, set_b):
    """
    Calculates the happiness score.

    Args:
        arr (list): List of integers.
        set_a (set): Set of liked integers.
        set_b (set): Set of disliked integers.

    Returns:
        int: Happiness score.
    """

    happiness = 0

    for num in arr:
        if num in set_a:
            happiness += 1
        if num in set_b:
            happiness -= 1

    return happiness
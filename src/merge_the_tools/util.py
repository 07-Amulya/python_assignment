def merge_the_tools(string, k):
    """
    Splits the string into substrings of length k and removes duplicate
    characters while preserving their order.

    Args:
        string (str): Input string.
        k (int): Length of each substring.

    Returns:
        list: List of processed substrings.

    Raises:
        ValueError: If k is less than or equal to 0.
    """

    if k <= 0:
        raise ValueError("k must be greater than 0.")

    result = []

    for i in range(0, len(string), k):
        substring = string[i:i + k]
        unique = ""

        for ch in substring:
            if ch not in unique:
                unique += ch

        result.append(unique)

    return result
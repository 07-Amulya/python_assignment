def text_alignment(t):
    """
    Generates the HackerRank Text Alignment pattern.

    Args:
        t (int): Thickness (should be an odd positive number).

    Returns:
        list: List of strings representing the pattern.

    Raises:
        ValueError: If thickness is not positive.
    """

    if t <= 0:
        raise ValueError("Thickness must be greater than 0.")

    s = "H"
    output = []

    # Top Cone
    for i in range(t):
        output.append(
            (s * (2 * i + 1)).center(2 * t - 1)
        )

    # Top Pillars
    for _ in range(t + 1):
        output.append(
            (s * t).center(2 * t) +
            (s * t).center(6 * t)
        )

    # Middle Belt
    for _ in range((t + 1) // 2):
        output.append(
            (s * (5 * t)).center(6 * t)
        )

    # Bottom Pillars
    for _ in range(t + 1):
        output.append(
            (s * t).center(2 * t) +
            (s * t).center(6 * t)
        )

    # Bottom Cone
    for i in range(t):
        output.append(
            ((s * (2 * (t - i) - 1)).center(2 * t - 1)).rjust(6 * t)
        )

    return output
def can_pile_up(blocks):
    """
    Determines whether the blocks can be piled up.

    Args:
        blocks (list): List of cube side lengths.

    Returns:
        str: "Yes" if the cubes can be piled, otherwise "No".
    """

    blocks = blocks.copy()

    while blocks:
        length = len(blocks)
        take = max(blocks[0], blocks[-1])

        if take == blocks[-1]:
            blocks.pop()
        else:
            blocks.pop(0)

        if not blocks:
            return "Yes"

        if max(blocks[0], blocks[-1]) > take:
            return "No"

    return "Yes"
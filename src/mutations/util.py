def mutate_string(string, position, character):
    """
    Replaces the character at the given position in the string.

    Args:
        string (str): Original string.
        position (int): Index to replace.
        character (str): New character.

    Returns:
        str: Modified string.

    Raises:
        IndexError: If position is out of range.
        ValueError: If character is not a single character.
    """

    if position < 0 or position >= len(string):
        raise IndexError("Position out of range.")

    if len(character) != 1:
        raise ValueError("Character must be a single character.")

    string_list = list(string)
    string_list[position] = character

    return ''.join(string_list)
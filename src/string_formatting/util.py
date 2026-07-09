def print_formatted(number):
    """
    Returns decimal, octal, hexadecimal, and binary representations
    of numbers from 1 to number.

    Args:
        number (int): Maximum number.

    Returns:
        list: List of formatted strings.

    Raises:
        ValueError: If number is less than 1.
    """

    if number < 1:
        raise ValueError("Number must be greater than 0.")

    width = len(bin(number)) - 2
    result = []

    for i in range(1, number + 1):
        d = str(i).rjust(width)
        o = oct(i)[2:].rjust(width)
        x = hex(i)[2:].upper().rjust(width)
        b = bin(i)[2:].rjust(width)

        result.append(f"{d} {o} {x} {b}")

    return result
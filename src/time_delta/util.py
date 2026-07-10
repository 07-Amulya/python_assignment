from datetime import datetime


def time_delta(t1, t2):
    """
    Calculates the absolute difference between two timestamps.

    Args:
        t1 (str): First timestamp.
        t2 (str): Second timestamp.

    Returns:
        str: Difference in seconds as a string.
    """

    fmt = "%a %d %b %Y %H:%M:%S %z"

    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    delta = abs(int((dt1 - dt2).total_seconds()))

    return str(delta)
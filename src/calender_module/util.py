import calendar


def get_day_name(month, day, year):
    """
    Returns the day of the week in uppercase.

    Args:
        month (int): Month (1-12)
        day (int): Day of the month
        year (int): Year

    Returns:
        str: Day name in uppercase.

    Raises:
        ValueError: If the given date is invalid.
    """

    try:
        weekday = calendar.weekday(year, month, day)
        return calendar.day_name[weekday].upper()
    except ValueError:
        raise ValueError("Invalid date.")
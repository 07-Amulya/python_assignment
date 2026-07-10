import re


def is_valid_email(email):
    """
    Checks whether an email address is valid.

    Args:
        email (str): Email address.

    Returns:
        bool: True if valid, otherwise False.
    """

    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return bool(re.fullmatch(pattern, email))


def filter_mail(emails):
    """
    Filters valid email addresses.

    Args:
        emails (list): List of email addresses.

    Returns:
        list: Sorted list of valid email addresses.
    """

    return sorted(list(filter(is_valid_email, emails)))
from src.validating_email_address.util import (
    is_valid_email,
    filter_mail,
)


def test_valid_email():
    assert is_valid_email("lara@hackerrank.com") is True


def test_valid_email_with_numbers():
    assert is_valid_email("user123@test1.org") is True


def test_valid_email_with_underscore():
    assert is_valid_email("john_doe@test.net") is True


def test_invalid_missing_at():
    assert is_valid_email("abcgmail.com") is False


def test_invalid_missing_domain():
    assert is_valid_email("abc@") is False


def test_invalid_long_extension():
    assert is_valid_email("abc@test.comm") is False


def test_invalid_special_character():
    assert is_valid_email("abc+1@test.com") is False


def test_filter_mail():
    emails = [
        "abc@gmail.com",
        "xyz@test.org",
        "abc+1@test.com",
        "wrong.com",
        "hello@test.co"
    ]

    assert filter_mail(emails) == [
        "abc@gmail.com",
        "hello@test.co",
        "xyz@test.org"
    ]


def test_empty_list():
    assert filter_mail([]) == []
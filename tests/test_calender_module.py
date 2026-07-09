import pytest
from src.calender_module.util import get_day_name


def test_sample_case():
    assert get_day_name(8, 5, 2015) == "WEDNESDAY"


def test_new_year():
    assert get_day_name(1, 1, 2024) == "MONDAY"


def test_christmas():
    assert get_day_name(12, 25, 2023) == "MONDAY"


def test_leap_day():
    assert get_day_name(2, 29, 2024) == "THURSDAY"


def test_end_of_year():
    assert get_day_name(12, 31, 2025) == "WEDNESDAY"


def test_invalid_month():
    with pytest.raises(ValueError):
        get_day_name(13, 10, 2024)


def test_invalid_day():
    with pytest.raises(ValueError):
        get_day_name(2, 30, 2024)


def test_invalid_date():
    with pytest.raises(ValueError):
        get_day_name(4, 31, 2023)
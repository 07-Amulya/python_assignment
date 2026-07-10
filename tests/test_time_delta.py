import pytest
from src.time_delta.util import time_delta


def test_sample_case():
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"

    assert time_delta(t1, t2) == "25200"


def test_same_time():
    t1 = "Sat 02 May 2015 19:54:36 +0530"
    t2 = "Sat 02 May 2015 19:54:36 +0530"

    assert time_delta(t1, t2) == "0"


def test_one_hour_difference():
    t1 = "Mon 01 Jan 2024 12:00:00 +0000"
    t2 = "Mon 01 Jan 2024 13:00:00 +0000"

    assert time_delta(t1, t2) == "3600"


def test_timezone_difference():
    t1 = "Mon 01 Jan 2024 12:00:00 +0530"
    t2 = "Mon 01 Jan 2024 12:00:00 +0000"

    assert time_delta(t1, t2) == "19800"


def test_reverse_order():
    t1 = "Mon 01 Jan 2024 10:00:00 +0000"
    t2 = "Mon 01 Jan 2024 08:00:00 +0000"

    assert time_delta(t1, t2) == "7200"


def test_invalid_date():
    with pytest.raises(ValueError):
        time_delta(
            "Invalid Date",
            "Mon 01 Jan 2024 08:00:00 +0000"
        )


def test_invalid_format():
    with pytest.raises(ValueError):
        time_delta(
            "2024-01-01",
            "2024-01-02"
        )
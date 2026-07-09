import pytest
from src.named_tuple.util import calculate_average_marks


def test_sample_case():
    columns = ["ID", "MARKS", "NAME", "CLASS"]
    student_data = [
        ["1", "97", "Raymond", "7"],
        ["2", "50", "Steven", "4"],
        ["3", "91", "Adrian", "9"],
        ["4", "72", "Stewart", "5"],
        ["5", "80", "Peter", "6"]
    ]

    assert calculate_average_marks(columns, student_data) == 78.0


def test_single_student():
    columns = ["ID", "MARKS", "NAME", "CLASS"]
    student_data = [
        ["1", "100", "Alice", "10"]
    ]

    assert calculate_average_marks(columns, student_data) == 100.0


def test_two_students():
    columns = ["ID", "MARKS", "NAME", "CLASS"]
    student_data = [
        ["1", "60", "Bob", "8"],
        ["2", "80", "John", "8"]
    ]

    assert calculate_average_marks(columns, student_data) == 70.0


def test_zero_marks():
    columns = ["ID", "MARKS", "NAME", "CLASS"]
    student_data = [
        ["1", "0", "Tom", "5"],
        ["2", "100", "Jerry", "5"]
    ]

    assert calculate_average_marks(columns, student_data) == 50.0


def test_empty_student_data():
    columns = ["ID", "MARKS", "NAME", "CLASS"]

    with pytest.raises(ValueError):
        calculate_average_marks(columns, [])


def test_different_column_order():
    columns = ["MARKS", "ID", "CLASS", "NAME"]
    student_data = [
        ["95", "1", "10", "Alice"],
        ["85", "2", "10", "Bob"]
    ]

    assert calculate_average_marks(columns, student_data) == 90.0
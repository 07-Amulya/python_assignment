import pytest
from src.finding_percentage.util import calculate_average


def test_calculate_average_student1():
    student_marks = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63]
    }

    assert calculate_average(student_marks, "Krishna") == 68.0


def test_calculate_average_student2():
    student_marks = {
        "Krishna": [67, 68, 69],
        "Arjun": [70, 98, 63]
    }

    assert calculate_average(student_marks, "Arjun") == 77.0


def test_average_with_float_marks():
    student_marks = {
        "Amulya": [80.5, 90.0, 89.5]
    }

    assert calculate_average(student_marks, "Amulya") == 86.66666666666667


def test_single_subject():
    student_marks = {
        "John": [100]
    }

    assert calculate_average(student_marks, "John") == 100.0


def test_student_not_found():
    student_marks = {
        "Alice": [80, 90, 100]
    }

    with pytest.raises(KeyError):
        calculate_average(student_marks, "Bob")
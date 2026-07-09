from collections import namedtuple


def calculate_average_marks(columns, student_data):
    """
    Calculates the average MARKS using namedtuple.

    Args:
        columns (list): List of column names.
        student_data (list): List of student records.

    Returns:
        float: Average marks rounded to 2 decimal places.

    Raises:
        ValueError: If no student records are provided.
    """

    if not student_data:
        raise ValueError("Student data cannot be empty.")

    Student = namedtuple("Student", columns)

    total_marks = 0

    for record in student_data:
        student = Student(*record)
        total_marks += int(student.MARKS)

    return round(total_marks / len(student_data), 2)
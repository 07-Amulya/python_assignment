def calculate_average(student_marks, query_name):

    if query_name not in student_marks:
        raise KeyError(f"{query_name} not found")

    scores = student_marks[query_name]
    return sum(scores) / len(scores)
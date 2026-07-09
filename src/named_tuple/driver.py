from util import calculate_average_marks

if __name__ == "__main__":
    n = int(input())
    columns = input().split()

    student_data = []

    for _ in range(n):
        student_data.append(input().split())

    result = calculate_average_marks(columns, student_data)
    print(result)
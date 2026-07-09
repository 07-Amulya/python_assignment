if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores    
    query_name = input()
    
    for i, j in student_marks.items():
        if i == query_name:
            result = sum(j)/3.00
            print(f"{result:.2f}")
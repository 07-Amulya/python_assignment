from util import calculate_determinant

if __name__ == "__main__":
    n = int(input())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(float, input().split())))

    result = calculate_determinant(matrix)
    print(result)
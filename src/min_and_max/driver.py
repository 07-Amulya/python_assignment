from util import find_max_of_row_mins

if __name__ == "__main__":
    n, m = map(int, input().split())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    result = find_max_of_row_mins(matrix)
    print(result)
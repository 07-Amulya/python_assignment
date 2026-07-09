from util import calculate_statistics

if __name__ == "__main__":
    n, m = map(int, input().split())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    mean, var, std = calculate_statistics(matrix)

    print(mean)
    print(var)
    print(std)
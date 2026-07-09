from util import calculate_happiness

if __name__ == "__main__":
    n, m = map(int, input().split())

    arr = list(map(int, input().split()))
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    result = calculate_happiness(arr, set_a, set_b)
    print(result)
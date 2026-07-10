from util import calculate_probability

if __name__ == "__main__":
    n = int(input())
    letters = input().split()
    k = int(input())

    result = calculate_probability(letters, k)
    print(result)
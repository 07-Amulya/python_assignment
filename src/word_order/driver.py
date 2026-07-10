from util import get_word_order

if __name__ == "__main__":
    n = int(input())

    words = []

    for _ in range(n):
        words.append(input())

    distinct_count, frequencies = get_word_order(words)

    print(distinct_count)
    print(*frequencies)
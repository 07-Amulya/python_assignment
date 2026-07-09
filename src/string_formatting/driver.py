from util import print_formatted

if __name__ == "__main__":
    n = int(input())

    result = print_formatted(n)

    for line in result:
        print(line)
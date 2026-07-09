from util import mutate_string

if __name__ == "__main__":
    s = input()
    i, c = input().split()

    result = mutate_string(s, int(i), c)
    print(result)
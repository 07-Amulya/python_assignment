from util import can_pile_up

if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        blocks = list(map(int, input().split()))

        print(can_pile_up(blocks))
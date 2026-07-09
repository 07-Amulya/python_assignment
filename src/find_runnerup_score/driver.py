from util import find_runner_up_score

if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().split()))

    result = find_runner_up_score(scores)
    print(result)
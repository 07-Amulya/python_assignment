from util import get_day_name

if __name__ == "__main__":
    month, day, year = map(int, input().split())

    result = get_day_name(month, day, year)
    print(result)
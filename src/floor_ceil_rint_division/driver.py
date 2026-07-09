from util import floor_ceil_rint_division

if __name__ == "__main__":
    numbers = list(map(float, input().split()))

    floor_arr, ceil_arr, rint_arr = floor_ceil_rint_division(numbers)

    print(floor_arr)
    print(ceil_arr)
    print(rint_arr)
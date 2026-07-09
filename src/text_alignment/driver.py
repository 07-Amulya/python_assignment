from util import text_alignment

if __name__ == "__main__":
    thickness = int(input())

    result = text_alignment(thickness)

    for line in result:
        print(line)
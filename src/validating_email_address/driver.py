from util import filter_mail

if __name__ == "__main__":
    n = int(input())

    emails = []

    for _ in range(n):
        emails.append(input())

    result = filter_mail(emails)
    print(result)
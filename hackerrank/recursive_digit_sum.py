"""

link: From Hackerrank grid Challenge
level: basic
score: 0

"""

def sum_digits(num: str):
    total = 0
    for i in num:
        total+= int(i)
    return total

def superDigit(n: str, k: int):
    n = str(sum_digits(n)*k)
    while len(n) > 1:
        total = 0
        for i in n:
            total+= int(i)
        n = str(total)
    return int(n)


if __name__ == "__main__":
    print(superDigit("9955", 5))
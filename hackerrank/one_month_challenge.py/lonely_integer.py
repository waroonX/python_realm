"""

link: https://www.hackerrank.com/challenges/lonely-integer/problem
level: Easy
score: 20

"""

def lonelyinteger(a):
    start = a[0]
    for num in a[1:]:
        start ^= num
    return start


if __name__ == "__main__":
    print(lonelyinteger([0, 9, 1, 2, 1, 2, 0]))
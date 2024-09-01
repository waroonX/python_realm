"""

link: https://www.hackerrank.com/challenges/halloween-sale/problem
level: easy
score: 20


70 >= 20 + 17 + 14 + 11 + 8

70 >= 20 + (20-3) + (20-6) + (20-9) + (20-12)

70 >= (20*5) - (3*1 + 3*2 + 3*3 + 3*4)

70 >= (20*5) - (3*10)

70 >= 5(20 - 6)


80
"""

def howManyGames(p, d, m, s):
    n = 0
    while s >= p:
        s -= p
        p = max(p-d, m)
        n += 1
    return n

if __name__ == "__main__":
    print(howManyGames(20, 3, 6, 70))
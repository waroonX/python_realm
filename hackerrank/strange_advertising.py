"""

link: https://www.hackerrank.com/challenges/strange-advertising/problem
level: easy
score: 15

2 = (5//2)
5 = (5//2) + ((5//2)*3)//2 = 
9 = (5//2) + ((5//2)*3)//2 + ((((5//2)*3)//2) * 3)//2
15
24


2 = 0
5 = 3
9 = 4
15 = 6
24 = 9
37 = 13
"""

def viralAdvertising(n):
    seed = 5
    total = 0
    for _ in range(n):
        seed = (seed//2)
        total += seed
        seed =  seed * 3
    return total

if __name__ == "__main__":
    print(viralAdvertising(6))
"""
link: https://www.hackerrank.com/challenges/minimum-distances/problem
level: easy
score: 20
"""

def minimumDistances(a):
    mem = {}
    min_score = 9999
    for i, num in enumerate(a):
        if num not in mem:
            mem[num] = i
            continue
        diff = i - mem[num]
        mem[num] = i
        if diff < min_score:
            min_score = diff
    return min_score if min_score != 9999 else -1

if __name__ == "__main__":
    arr = [7, 1, 3, 4, 1, 7, 2, 7]
    print(minimumDistances(arr))
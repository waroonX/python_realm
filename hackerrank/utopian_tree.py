"""
link: https://www.hackerrank.com/challenges/utopian-tree/problem
level: easy
score: 20
"""

def utopianTree(n):
    start = 1
    for _ in range(n):
        if start%2==0:
            start +=1
        else:
            start *=2
    return start

if __name__ == "__main__":
    print(utopianTree(5))
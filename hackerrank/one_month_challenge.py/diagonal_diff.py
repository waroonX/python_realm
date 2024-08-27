"""

link: https://www.hackerrank.com/challenges/diagonal-difference/problem
level: Easy
score: 10

"""

from typing import List

def diagonalDifference(arr: List[List[int]]) -> int:
    n = len(arr)
    sum1, sum2 = 0, 0
    for i in range(n):
        for j in range(n):
            if i==j:
                sum1+=arr[i][j]
            if j==n-i-1:
                sum2+=arr[i][j]
    return abs(sum1-sum2)

if __name__ == "__main__":
    arr = [
        [11, 2, 4],
        [4, 5, 6],
        [10, 8, -12]
    ]
    print(diagonalDifference(arr))
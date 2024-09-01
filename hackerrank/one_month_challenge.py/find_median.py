"""

link: https://www.hackerrank.com/challenges/find-the-median/problem
level: Easy
score: 35

"""

def findMedian(arr):
    n = len(arr)
    arr.sort()
    return arr[n//2]

if __name__ == "__main__":
    arr = [0, 1, 2, 4, 6, 5, 3]
    print(findMedian(arr))
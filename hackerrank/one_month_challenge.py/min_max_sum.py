"""

link: https://www.hackerrank.com/challenges/mini-max-sum/problem
level: Easy
score: 10

"""

def miniMaxSum(arr):
    arr.sort()
    print(sum(arr[:4]), sum(arr[1:]))

if __name__ == "__main__":
    miniMaxSum([1, 2, 3, 4, 5])
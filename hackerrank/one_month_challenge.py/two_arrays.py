"""

link: https://www.hackerrank.com/challenges/two-arrays/problem
level: Easy
score: 40

"""

def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    n = len(A)
    
    for i in range(n):
        if A[i] + B[i] < k:
            return "NO"
    return "YES"

if __name__ == "__main__":
    set1 = (5, [1, 2, 2, 1], [3, 3, 3, 4])
    set2 = (10, [2, 1, 3], [7, 8, 9])
    print(twoArrays(*set1))
    print(twoArrays(*set2))
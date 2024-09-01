"""

link: https://www.hackerrank.com/challenges/flipping-the-matrix/problem
level: Medium
score: 30

"""

def flippingMatrix(matrix):
    n = len(matrix)//2
    total = 0
    for i in range(n):
        for j in range(n):
            total+=max(matrix[i][j], matrix[i][2*n-j-1], matrix[2*n-i-1][j], matrix[2*n-i-1][2*n-j-1])
    return total

if __name__ == "__main__":
    arr = [
        [112, 42, 83, 119], 
        [56, 125, 56, 49], 
        [15, 78, 101, 43], 
        [62, 98, 114, 108]
    ]
    print(flippingMatrix(arr))
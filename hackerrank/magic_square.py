"""
Link: https://www.hackerrank.com/challenges/magic-square-forming/problem
"""

SUM = 15
N = 3

def is_magic_square(s):
    n = len(s)
    h_sum = [0]*n
    v_sum = [0]*n
    d_sum = 0
    d_sum2 = 0
    for i in range(n):
        for j in range(n):
            h_sum[i] += s[i][j]
            v_sum[j] += s[i][j]
            if i==j:
                d_sum += s[i][j]
            if j==n-i-1:
                d_sum2 += s[i][j]
    sums = h_sum + v_sum + [d_sum, d_sum2]
    magic_sums = list(filter(lambda sum1: sum1==SUM, sums))
    return len(magic_sums) == 8

def rotate(A, reverse=False):
    AT = [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(N):
        for j in range(N):
            if reverse:
                AT[N-j-1][i] = A[i][j]
            else:
                AT[j][N-i-1] = A[i][j]
    return AT

def reverse(A):
    return [row[::-1] for row in A]
    
def generate_3x3_magic_squares():
    seed = [
        [4,3,8],
        [9,5,1],
        [2,7,6]
    ]
    
    magic_squares = []
    magic_squares.append(seed)
    magic_squares.append(reverse(seed))
    
    for _ in range(N):
        seed = rotate(seed)
        magic_squares.append(seed)
        magic_squares.append(reverse(seed))
    return magic_squares

def calculate_min_cost(s, magic_squares):
    min_total = 99
    for magic in magic_squares:
        total = 0
        for row_a, row_b in zip(magic, s):
            for elem_a, elem_b in zip(row_a, row_b):
                total += abs(elem_a-elem_b)
        if total < min_total:
            min_total = total
    return min_total
        

def formingMagicSquare(s):
    magic_squares = generate_3x3_magic_squares()
    return calculate_min_cost(s, magic_squares)

if __name__ == "__main__":
    A = [
        [4, 8, 2],
        [4, 5, 7],
        [6, 1, 6]
    ]
    formingMagicSquare(A)
"""

link: From Hackerrank grid Challenge
level: basic
score: 0

"""

def gridChallenge(grid):
    n = len(grid)
    for i in range(n):
        grid[i] = "".join(sorted(grid[i]))
    
    alpha = "".join(grid)
    for i in range(n):
        word = alpha[i::n]
        sorted_word = "".join(sorted(word))
        if word != sorted_word:
            return "NO"
    return "YES"

if __name__ == "__main__":
    grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
    print(gridChallenge(grid))
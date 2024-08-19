"""
from : Hack sussex Coders Cup 2022
"""

def is_valid_sudoku(arr):
    count_dict = {}
    for row in arr:
        for elem in row:
            if elem in count_dict:
                return False
            else:
                count_dict[elem] = 1
    return True

if __name__ == "__main__":
    sudoku = [
        [1, 0, 3],
        [4, 1, 6],
        [7, 8, 9]
    ]
    print(is_valid_sudoku(sudoku))
#!/bin/python3

import math
import os
import random
import re
import sys


def decode_matrix(matrix, n, m):
    decoded_str = "".join([matrix[i][j] for j in range(m) for i in range(n)])
    # for j in range(m):
    #     for i in range(n):
    #         print(matrix[i][j])
    other = re.sub(r"([A-Za-z0-9]+)[^A-Za-z0-9]+([A-Za-z0-9]+)", r'\g<1> \g<2>', decoded_str)
    print(other)

# first_multiple_input = input().rstrip().split()

first_multiple_input = "7 3".rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

test = ["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"]

for _ in range(n):
    # matrix_item = input()
    matrix.append(test[_])
    
decode_matrix(matrix, n, m)
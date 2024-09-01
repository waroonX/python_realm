#!/bin/python3

"""
link: https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem
level: medium
score: 30

Comments:
Explanation of the problem solving aspect of this problem:

The only we way can move a ball is by swapping it with another ball. This means:

If a container starts with n balls, it will have to end with n balls. It is easier to think of each container having a certain number of "slots". At the start, each slot is full, and in the end each slot will have to be full.
Each type of ball needs to end up in its own container. This means that if there are k balls of a certain type, there must be container with k slots where these balls can end up.
This means that we can count - how many slots does each container have - how many balls are there of each type

For each type of ball, there needs to be a matching container with the same number of slots.

Implementation: 

1. Find the sum of each row (number of slots per container) 
2. Find the sum of each column (number of balls of each type) 
3. convert the array of row sums to a counter 
4. convert the array of column sums to a counter 
5. Return "Possible" if the counters are equal, else return "Impossible
"""
from collections import Counter

def organizingContainers(container):
    n = len(container)
    cont_sum = [0]*n
    ball_sum = [0]*n
    for i in range(n):
        for j in range(n):
            cont_sum[i] += container[i][j]
            ball_sum[j] += container[i][j]
                
    # cont_sum.sort()
    # ball_sum.sort()
    cont_sum = Counter(cont_sum)
    ball_sum = Counter(ball_sum)
    return "Possible" if cont_sum == ball_sum else "Impossible"

if __name__ == '__main__':
    arr = [
        [997612619, 934920795, 998879231, 999926463],
        [960369681, 997828120, 999792735, 979622676],
        [999013654, 998634077, 997988323, 958769423],
        [997409523, 999301350, 940952923, 993020546]
    ]
    print(organizingContainers(arr))
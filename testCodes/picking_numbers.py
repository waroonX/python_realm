"""
link: https://www.hackerrank.com/challenges/picking-numbers/problem
level: easy
score: 20
"""

from collections import defaultdict

def pickingNumbers(a):
    a.sort()
    n = len(a)
    mem= {}
    max_len = 0
    for i in range(n):
        num = a[i]
        if num in mem:
            continue
        mem[a[i]] = 1
        len1 = 1
        for j in range(i+1,n):
            if 0 <= abs(num-a[j]) <= 1:
                len1+=1
            else:
                break
        if len1 > max_len:
            max_len = len1
    return max_len

def pickingNumbers_opt(a):
    mem = defaultdict(int)
    for num in a:
        mem[num] += 1
    length = 0
    for num, count in mem.items():
        length = max(length, count+mem.get(num+1, 0))
        
    return length
            

if __name__ == '__main__':
    arr = [1,2,3,4,3,2,1,2,3,4,5,6,7,2,3,4,5,6]
    print(pickingNumbers_opt(arr))
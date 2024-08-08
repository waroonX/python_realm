"""

link: https://www.hackerrank.com/challenges/bigger-is-greater/problem
level: medium
score: 35

Solution: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm

e k h d c

5 10 7 4 3
==================
dkhc
4 10 7 3

hcdk
7 3 4 10

=================
v a r u t
20 1 7 18 17

v a u r t
20 1 18 7 17


abdc

acbd
"""


def biggerIsGreater(w):
    n = len(w)
    
    for i in range(n-1, 0, -1):
        if w[i-1] < w[i]:
            for j in range(n-1, i-1, -1):
                if w[j] > w[i-1]:
                    return w[:i-1]+ w[j]+ (w[i:j]+ w[i-1]+ w[j+1:])[::-1]
            break
    return "no answer"

if __name__ == "__main__":
    print(biggerIsGreater("dkhc"))
    # "va" + "u" + 
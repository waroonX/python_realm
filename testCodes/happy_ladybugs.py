"""
link: https://www.hackerrank.com/challenges/happy-ladybugs/problem
level: easy
score: 30

Comments:
Dont bother swapping characters until you find a valid string. Here is the trick:

Happy Conditions:

= There are at least one empty cell and there is no Letter with count 1

OR

= There is no empty cell but the given string is happy
"""

from collections import defaultdict

def happyLadybugs(b):
    is_under_found = False
    unnatural_found = False
    letter_with_count1 = False
    letter_dict = defaultdict(int)
    count = 0
    for i, l in enumerate(b):
        if l == "_":
            is_under_found = True
        else:
            letter_dict[l] += 1
            count += 1
            if i == len(b)-1 or b[i] != b[i+1]:
                if count == 1:
                    unnatural_found = True
                count = 0
    for val in letter_dict.values():
        if val == 1:
            letter_with_count1 = True
            
    return ("NO" if letter_with_count1 else "YES") if is_under_found else ("NO" if unnatural_found else "YES")

if __name__ == "__main__":
    string = "AABCBC"
    print(happyLadybugs(string))
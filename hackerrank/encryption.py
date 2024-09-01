"""

link: https://www.hackerrank.com/challenges/encryption/problem
level: medium
score: 30

"""

from math import sqrt, floor, ceil

def encryption(s):
    s = s.replace(' ', '')
    n = len(s)
    
    root = sqrt(n)
    y = ceil(root)
    
    encrypt = ""
    
    for i in range(y):
        encrypt += s[i::y] + " "
        
    return encrypt

if __name__ == "__main__":
    print(encryption("ifmanwas meanttos tayonthe groundgo dwouldhavegivenu sroots"))
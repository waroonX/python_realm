"""
This is a mock test

Looks easy
"""

def is_palindrome(s):
    n =len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True

def palindromeIndex(s):
    if is_palindrome(s):
        return -1
    n =len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            if is_palindrome(s[:i]+s[i+1:]):
                return i
            
            if is_palindrome(s[:n-i-1]+s[n-i:]):
                return n-i-1
    return -1
            
    

if __name__ == "__main__":
    print(palindromeIndex("aaaaaaaaaaaaaaaaaabaaaaaaa"))
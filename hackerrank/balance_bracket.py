"""

link: From Hackerrank grid Challenge
level: intermediate
score: 0


"""

def isBalanced(s):
    matcher = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }
    
    stack = []
    
    for char in s:
        if char in matcher:
            if not stack:
                return "NO"
            if stack.pop() != matcher[char]:
                return "NO"
        else:
            stack.append(char)
    return "YES" if not stack else "NO"

if __name__ == "__main__":
    s = "({([()](})"
    print(isBalanced(s))
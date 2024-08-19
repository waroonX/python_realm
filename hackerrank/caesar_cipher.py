"""
This is a mock test

Looks easy
"""

def caesarCipher(s, k):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_dict = {a:i for i,a in enumerate(alpha)}
    cipher = ""
    for l in s:
        temp = ""
        l = str(l)
        if l.isalpha():
            if l.isupper():
                l = alpha[(alpha_dict[l.lower()]+k)%26].upper()
            else:
                l = alpha[(alpha_dict[l]+k)%26]
        cipher += l
    return cipher

if __name__ == "__main__":
    print(caesarCipher("I am Varun baby!!!", k=3))
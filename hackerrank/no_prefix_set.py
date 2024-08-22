"""

link: https://www.hackerrank.com/challenges/no-prefix-set/problem
level: Hard
score: 50

"""

def noPrefix(words):
    memory = {}
    result = ""
    found = False
    for word in words:
        temp = memory
        for letter in word:
            if letter in temp:
                if not temp[letter]:
                    found = True
                    result = word
                    break
                temp = temp[letter]
            else:
                temp[letter] = {}
                temp = temp[letter]
        if temp:
            found = True
            result = word
            break
    print("BAD SET" if found else "GOOD SET")
    print(result)

if __name__ == "__main__":
    noPrefix(['defgab', 'abcde', 'aabcde', 'bbbbbbbbbb','aab', 'jabjjjad'])
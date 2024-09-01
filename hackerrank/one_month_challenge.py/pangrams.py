"""

link: https://www.hackerrank.com/challenges/pangrams/problem
level: Easy
score: 20

"""

def pangrams(s: str) -> str:
    mem = {}
    for letter in s:
        if letter.isalpha():
            mem[letter.lower()] = mem.get(letter.lower(), 0) + 1
    return "pangram" if len(mem) == 26 else "not pangram"
            


if __name__ == "__main__":
    print(pangrams("We promptly judged antique ivory buckles for the prize"))
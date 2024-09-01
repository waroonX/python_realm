"""

link: https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem
level: Easy
score: 100

"""

def birthday(s, d, m):
    total = 0
    count = 0
    start = 0
    for i in range(len(s)):
        total += s[i]
        if (total == d) and (i-start+1 == m):
            count += 1
            total -= s[start]
            start += 1
        elif total > d or i-start+1 >= m:
            total -= s[start]
            start += 1
    return count

if __name__ == "__main__":
    print(birthday([2,2,1,3,2], 4, 2))
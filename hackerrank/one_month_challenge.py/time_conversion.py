"""

link: https://www.hackerrank.com/challenges/time-conversion/problem
level: Easy
score: 15

"""

def timeConversion(s: str) -> str:
    hour = s[:2]
    apm = s[-2:]
    if apm == 'PM':
        if int(hour) != 12:
            hour = str(int(hour) + 12)
    else:
        if int(hour) == 12:
            hour = "00"
    return f"{hour}{s[2:-2]}"

if __name__ == "__main__":
    print(timeConversion("11:59:59PM"))
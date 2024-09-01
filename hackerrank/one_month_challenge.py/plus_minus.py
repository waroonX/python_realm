"""

link: https://www.hackerrank.com/challenges/plus-minus/problem
level: Easy
score: 10

"""

def plusMinus(arr):
    tot, pos, neg, zer = 0,0,0,0
    
    for num in arr:
        tot+=1
        if num > 0:
            pos += 1
        elif num == 0:
            zer += 1
        else:
            neg += 1
            
    print(round(pos/tot, 6))
    print(round(neg/tot, 6))
    print(round(zer/tot, 6))

if __name__ == "__main__":
    plusMinus([-4, 3, -9, 0, 4, 1])
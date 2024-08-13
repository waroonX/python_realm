"""

link: https://www.hackerrank.com/challenges/pairs/problem
level: Medium
score: 50


"""

def pairs(k, arr):
    numeo = {}
    count = 0
    for a in arr:
        numeo[a] = 1
    for a in arr:
        add = a+k
        if add in numeo:
            count+=1
    return count
            
        

if __name__ == "__main__":
    print(pairs(2, [1, 5, 3, 4, 2]))
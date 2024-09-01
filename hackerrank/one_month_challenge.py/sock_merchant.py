"""

link: https://www.hackerrank.com/challenges/sock-merchant/problem
level: Easy
score: 10

"""

def sockMerchant(n, ar):
    mem = {}
    count = 0
    for num in ar:
        if num in mem:
            del mem[num]
            count += 1
        else:
            mem[num] = 1
    return count
       
   
if __name__ == "__main__":
    print(sockMerchant(10, [10, 20, 20, 10, 10, 30, 50, 10, 20, 50]))
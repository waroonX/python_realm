"""

link: https://www.hackerrank.com/challenges/jesse-and-cookies/problem
level: Easy
score: 25

"""

from heapq import heapify, heappop, heappush

def cookies(k, A):
    heapify(A)
    
    n = len(A)
    
    turns = 0
    sub1 = heappop(A)
    while n > 1 and k > sub1:
        heappush(A, sub1 + 2* heappop(A))
        n-=1
        turns += 1
        sub1 = heappop(A)
    
    return turns if sub1 >= k else -1

if __name__ == "__main__":
    ans = cookies(7,[1, 2, 3, 9, 10, 12])
    print(ans)
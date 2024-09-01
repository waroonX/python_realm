"""

link: https://www.hackerrank.com/challenges/tower-breakers-1/problem
level: Easy
score: 15

"""

def towerBreakers(n, m):
    return 2 if (m==1) or n%2==0 else 1
    
if __name__=="__main__":
    print(towerBreakers(1, 4))
    print(towerBreakers(2, 2))
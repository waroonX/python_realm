"""

link: https://www.hackerrank.com/challenges/one-week-preparation-kit-lego-blocks/problem
level: Medium
score: 100

"""

def legoBlocks(h, w):
    modulo = pow(10,9) + 7
    
    T = [0] * (w+1)
    S = [0] * (w+1)
    S[1] = 1
    
    T[1:5] = [1, 2, 4, 8]
    
    for i in range(5, w+1):
        T[i] = (T[i-1] + T[i-2] + T[i-3] + T[i-4]) % modulo
            
    for i in range(w+1):
        T[i] = pow(T[i], h, modulo)
    
    for i in range(2, w+1):
        total = 0
        for ii in range(1, i):
            total += (S[ii] * T[i-ii]) % modulo
        S[i] = (T[i] - total) % modulo
    return S[w] % modulo

if __name__ == "__main__":
    ans = legoBlocks(2,3)
    print(ans)
    # assert ans == 3375, "Did not work"
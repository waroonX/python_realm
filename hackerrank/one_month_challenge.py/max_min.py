"""

link: https://www.hackerrank.com/challenges/angry-children/problem
level: Medium
score: 35

"""

def maxMin(k, arr):
    n = len(arr)
    arr.sort()
    diff = arr[k-1]-arr[0]
    for i in range(1, n-k+1):
        diff = min(arr[k+i-1] - arr[i], diff)
        if not diff:
            break
    return diff
        
       
if __name__ == "__main__":
    print(maxMin(4, [1,2,3,4,10,20,30,40,100,200]))
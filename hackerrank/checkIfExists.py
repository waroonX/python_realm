def checkIfExist(arr: list) -> bool:
    l = len(arr)
    check = {}
    for i in range(0, l):
        if arr[i] % 2 == 0:
            if arr[i] * 2 in check or arr[i] / 2 in check:
                return True
            else:
                check[arr[i]] = None
        elif arr[i] * 2 in check or arr[i] / 2 in check:
            return True
        else:
            check[arr[i]] = None
    return False


if __name__ == "__main__":
    print(checkIfExist([10, 2, 5, 3]))


"""
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

More formally check if there exists two indices i and j such that :

    i != j
    0 <= i, j < arr.length
    arr[i] == 2 * arr[j]

 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: N = 10 is the double of M = 5,that is, 10 = 2 * 5.

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1
"""

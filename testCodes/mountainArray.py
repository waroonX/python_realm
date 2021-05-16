def validMountainArray(arr: list) -> bool:
    l = len(arr)
    if l < 3:
        return False
    i = 0
    j = l - 1
    while i < l - 1 and arr[i + 1] > arr[i]:
        i += 1
    while arr[j - 1] > arr[j] and j > 0:
        j -= 1
    if i == j and i != 0 and j != l - 1:
        return True
    else:
        return False


if __name__ == "__main__":
    print(validMountainArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false

Example 2:

Input: arr = [3,5,5]
Output: false

Example 3:

Input: arr = [0,3,2,1]
Output: true

def validMountainArray(self, A):
        i, j, n = 0, len(A) - 1, len(A)
        while i + 1 < n and A[i] < A[i + 1]: i += 1
        while j > 0 and A[j - 1] > A[j]: j -= 1
        return 0 < i == j < n - 1
"""

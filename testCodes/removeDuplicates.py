def removeDuplicates(nums: list) -> int:
    l = len(nums)
    i = l - 1
    j = l - 1
    while i > 0:
        if nums[i] == nums[i - 1]:
            temp = nums[i - 1]
            nums[i - 1 : j] = nums[i : j + 1]
            nums[j] = temp
            j -= 1
        i -= 1
    print(nums)
    return j + 1


if __name__ == "__main__":
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

"""
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

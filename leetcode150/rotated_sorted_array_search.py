"""
Link:  https://leetcode.com/problems/search-in-rotated-sorted-array/
Level: Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    left = 0
    right = n-1
    while(left <= right):
        mid = (right+left)//2
        if nums[mid] == target:
            return mid
        
        if nums[left] <= nums[mid] and (nums[left] <= target <= nums[mid]):
            right = mid
        elif nums[left] <= nums[mid] and (target < nums[left] or target > nums[mid]):
            left = mid + 1
        elif nums[mid] <= nums[right] and (nums[mid] <= target <= nums[right]):
            left = mid
        elif nums[mid] <= nums[right] and (target < nums[mid] or target > nums[right]):
            right = mid - 1
        else:
            return -1
    return -1


print(search([5,1,2,3,4], 1))
print(search([4,5,6,7,0,1,2], 0))
print(search([5, 1, 3], 5))
print(search([4,5,6,7,0,1,2], 3))
print(search([4,5,6,7,0,1,2], 5))
print(search([1], 0))
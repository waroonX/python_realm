def sortArrayByParity(nums: list) -> list:
    even_index = 0
    for index in range(len(nums)):
        if nums[index] % 2 == 0:
            nums[index], nums[even_index] = nums[even_index], nums[index]
            even_index += 1
    return nums


if __name__ == "__main__":
    print(sortArrayByParity([3, 1, 2, 4, 5, 6, 7, 8]))

"""
Given an array nums of non-negative integers, return an array consisting of all the even elements of nums, followed by all the odd elements of nums.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 

Note:

1 <= nums.length <= 5000
0 <= nums[i] <= 5000
"""

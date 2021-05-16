def moveZeroes(nums: list) -> None:
    l = len(nums)
    i = l - 1
    j = l - 1
    while i > -1:
        if nums[i] == 0:
            nums[i:j] = nums[i + 1 : j + 1]
            nums[j] = 0
            j -= 1
        i -= 1
    print(nums)


if __name__ == "__main__":
    print(moveZeroes([0, 1, 2, 3]))

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?

zero_index=0
        for index in range(len(nums)):
            if(nums[index]!=0):
                nums[index],nums[zero_index]=nums[zero_index],nums[index]
                zero_index+=1
"""

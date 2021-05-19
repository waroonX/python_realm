def thirdMax(nums: list) -> int:
    l = len(nums)
    f, s, t = None, None, None
    for e in nums:
        if f == None or e > f:
            f = e
    if l < 3:
        return f
    for e in nums:
        if e < f and (s == None or e > s):
            s = e
    s = s if s != None else f
    for e in nums:
        if e < s and (t == None or e > t):
            t = e
    return t if t != None else f


if __name__ == "__main__":
    print(thirdMax([3, 3, 4, 3, 4, 3, 0, 3, 3]))


"""
Given integer array nums, return the third maximum number in this array. If the third maximum does not exist, return the maximum number.

 

Example 1:

Input: nums = [3,2,1]
Output: 1
Explanation: The third maximum is 1.
Example 2:

Input: nums = [1,2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:

Input: nums = [2,2,3,1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Can you find an O(n) solution?
"""

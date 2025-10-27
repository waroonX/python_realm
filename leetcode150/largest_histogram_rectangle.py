"""
Link:  https://leetcode.com/problems/largest-rectangle-in-histogram/description/
Level: Hard

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104
"""
from typing import List

def largestRectangleArea(heights: List[int]) -> int:
    stack = []
    max_area = 0
    for i, n in enumerate(heights):
        if stack:
            top = stack[-1]
            top_val = heights[top]
            if n >= top_val:
                stack.append(i)
            else:
                # print(f"We are in val:{n};index:{i} - Stack {stack} - Max {max_area}")
                for index in stack[::-1]:
                    if heights[index] >= n:
                        max_area = max(max_area, (i-index)*heights[index])
                        stack.pop()
                    else:
                        break
        else:
            stack.append(i)
            max_area = max(max_area, n)
    return max_area

print(largestRectangleArea([2,1,5,6,2,3]))
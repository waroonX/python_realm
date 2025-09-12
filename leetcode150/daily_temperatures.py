"""
Link:  https://leetcode.com/problems/daily-temperatures/
Level: Medium

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

 

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
 

Constraints:

1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

from typing import List

class Stack:
    def __init__(self):
        self.container = []
        self.length = 0

    def push(self, value):
        self.length += 1
        self.container.append(value)

    def pop(self):
        if not self.is_empty():
            self.length -= 1
            return self.container.pop()

    def peek(self):
        return self.container[-1] if self.container else None

    def is_empty(self):
        return self.length == 0

    def size(self):
        return self.length

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    peak_stack = Stack()
    n = len(temperatures)
    ans_list = [0]*n
    for i, num in enumerate(temperatures):
        if not peak_stack.is_empty():
            val = peak_stack.peek()
            while ((not peak_stack.is_empty()) and (num > temperatures[val])):
                val = peak_stack.pop()
                ans_list[val] = i - val
                val = peak_stack.peek()
        peak_stack.push(i)
    return ans_list

print(dailyTemperatures([73,74,75,71,69,72,76,73]))
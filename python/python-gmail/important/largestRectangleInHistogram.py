#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    http://oj.leetcode.com/problems/largest-rectangle-in-histogram/
Solution:
    * use stack: stack = [(index, value)]
Time Complexity:
Space Complexity:
Result: AC
Note: very important
'''

class Solution:
    def solve(self, li):
        li.append(-1)
        stack = []
        result = 0
        for i in range(len(li)):
            while len(stack) != 0 and stack[-1][1] > li[i]:
                item = stack.pop()
                if len(stack) == 0:
                    result = max(result, item[1]*(i))
                else:
                    result = max(result, item[1]*(i-stack[-1][0]-1))
            stack.append((i, li[i]))
        return result

    # @param height, a list of integer
    # @return an integer
    def largestRectangleArea(self, height):
        return self.solve(height)

s = Solution()
print s.largestRectangleArea([2,1,5,6,2,3])
print s.largestRectangleArea([2,1,5,6,2,3])
print s.largestRectangleArea([])
print s.largestRectangleArea([2])
print s.largestRectangleArea([2,2,2,2,1])
print s.largestRectangleArea([2,0,2])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

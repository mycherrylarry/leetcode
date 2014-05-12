#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

Solution:
Time Complexity: O(N*N)
Space Complexity: O(N*N)
Result: AC
'''

class Solution:
    def findMaximalRectangleOfList(self, li):
        li.append(-1)
        stack = []
        result = 0
        i = 0
        while i< len(li):
            if len(stack) == 0 or li[stack[-1]] <= li[i]:
                stack.append(i)
                i += 1
            else:
                index = stack.pop()
                if len(stack) == 0:
                    result = max(result, li[index]*(i))
                else:
                    result = max(result, li[index]*(i-stack[-1]-1))
        return result

    # @param matrix, a list of lists of 1 length string
    # @return an integer
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0: return 0
        h, w = len(matrix), len(matrix[0])
        route = [[0]*w for i in range(h+1)]
        for i in range(1, h+1):
            for j in range(w):
                if matrix[i-1][j] == "1":
                    route[i][j] = route[i-1][j]+1
        result = 0
        for i in range(1, h+1):
            result = max(self.findMaximalRectangleOfList(route[i]), result)
        return result

s = Solution()
print s.findMaximalRectangleOfList([0,0,2,3,1,2,2])
matrix = [[1,0,1], [1,1,1]]
matrix = [["1"]]
print s.maximalRectangle(matrix)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

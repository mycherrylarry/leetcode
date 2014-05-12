#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
Resolution:
    * DFS
Time Complexity:
Space Complexity:
Result: 
    DP: AC
    DFS: Limit Exceeded
Note:
    * pruning
    * minus
    * maybe could improved by DP
'''

class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0 or len(triangle[0]) ==0: return 0
        route = [0]*len(triangle)
        tmp = [0]*len(triangle)
        route[0] = triangle[0][0]
        for j in range(1, len(triangle)):
            for i in range(len(triangle)):
                tmp[i] = route[i]
            for i in range(len(triangle[j])):
                a, b = i-1, i
                if a <0: a = 0
                if b > j-1: b = j-1
                route[i] = min(tmp[a], tmp[b]) + triangle[j][i]
        return min(route)

class Solution1:
    def __init__(self):
        self.result = 1000000000

    def solve(self, route, triangle, i, j):
        if j == len(triangle):
            self.result = min(self.result, route)
            return
        if i > j: return
        self.solve(route + triangle[j][i], triangle, i, j+1)
        self.solve(route + triangle[j][i], triangle, i+1, j+1)

    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0 or len(triangle[0]) ==0: return 0
        self.solve(0, triangle, 0, 0)
        return self.result

s = Solution()
print s.minimumTotal([[2], [1,2]])
print s.minimumTotal([[2]])
print s.minimumTotal([[-1],[2,3],[1,-1,-3]])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

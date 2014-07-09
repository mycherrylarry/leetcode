#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a MxN grid filled with non-negative numbers, find a path from top left to
    bottom right which minimizes the sum of all numbers along its path.

Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
    check if you can only move either down or right at any point in time.
'''

class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        h = len(grid)
        if h == 0: return 0
        w = len(grid[0])
        if w == 0: return 0
        route = [[0] * w for i in range(h)]
        route[0][0] = grid[0][0]
        for i in range(1, h):
            route[i][0] = route[i-1][0] + grid[i][0]
        for j in range(1, w):
            route[0][j] = route[0][j-1] + grid[0][j]
        for i in range(1, h):
            for j in range(1, w):
                route[i][j] = min(route[i-1][j], route[i][j-1]) + grid[i][j]
        return route[h-1][w-1]

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

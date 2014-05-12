#!/usr/bin/env python
from unittest import *

'''
Description:
    1. Simple DP
Time Complexity: O(M*N)
Result: AC
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        h = len(obstacleGrid)
        if h == 0: return 0
        w = len(obstacleGrid[0])
        if w == 0: return 0
        route = [[0]* w for item in range(h)]
        i = 0
        while i < w:
            if obstacleGrid[0][i] == 1:
                break
            route[0][i] = 1
            i += 1
        i = 0
        while i < h:
            if obstacleGrid[i][0] == 1:
                break
            route[i][0] = 1
            i += 1
        for i in range(1, h):
            for j in range(1, w):
                if obstacleGrid[i][j] == 0:
                    route[i][j] = route[i-1][j] + route[i][j-1]
                else:
                    route[i][j] = 0
        return route[h-1][w-1]

s = Solution()
print s.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])

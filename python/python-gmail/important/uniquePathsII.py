#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution: Dynamic Programming
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:

    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        h = len(obstacleGrid)
        if h == 0: return 0
        w = len(obstacleGrid[0])
        if w == 0: return 0
        route = [[0]* w for i in range(h)]
        if obstacleGrid[0][0] == 0:
            route[0][0] = 1
        # init
        for i in range(1, h):
            if obstacleGrid[i][0] == 0 and route[i-1][0] != 0:
                route[i][0] = 1
        for j in range(1, w):
            if obstacleGrid[0][j] == 0 and route[0][j-1] != 0:
                route[0][j] = 1
        for i in range(1, h):
            for j in range(1, w):
                if obstacleGrid[i][j] == 0:
                    route[i][j] = route[i-1][j] + route[i][j-1]
        return route[h-1][w-1]


s = Solution()
g = [
          [0,0,0],
            [0,1,0],
              [0,0,0]
              ]
print s.uniquePathsWithObstacles(g)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from unittest import *

'''
Description: Simple DP
TimeComplexity: O(N*N)
Result: AC
'''
class Solution:
    def uniquePaths(self, m, n):
        if m == 0 or n == 0: return 0
        route = [[0]*n for item in range(m)]
        for i in range(m):
            route[i][0] = 1
        for j in range(n):
            route[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                route[i][j] = route[i-1][j] + route[i][j-1]
        return route[m-1][n-1]

s = Solution()
print s.uniquePaths(3, 2)
print s.uniquePaths(1, 2)
    

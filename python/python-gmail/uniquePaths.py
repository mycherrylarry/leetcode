#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method: DP
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        if m == 0 or n == 0: return 0
        route = [[1]*m for item in range(n)]
        for i in range(1, n):
            for j in range(1, m):
                route[i][j] = route[i-1][j] + route[i][j-1]
        return route[n-1][m-1]

s = Solution()
print s.uniquePaths(3,4)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

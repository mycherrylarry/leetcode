#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    def createRoute(self, s):
        n = len(s)
        route = [['*']*n for i in range(n)]
        def create(x, y, n):
            while x >= 0 and y < n:
                if route[x+1][y-1] == 1 and s[x] == s[y]:
                    route[x][y] = 1
                else:
                    route[x][y] = 0
                x -= 1
                y += 1
        for i in range(n):
            route[i][i] = 1
            x, y = i-1, i+1
            create(x, y, n)
        for i in range(n-1):
            if s[i] == s[i+1]:
                route[i][i+1] = 1
            else:
                route[i][i+1] = 0
            x, y = i-1, i+2
            create(x, y, n)
        return route

    def solve(self, s, route):
        n = len(s)
        # DP, stores the minimum split parts
        li = [n+1]*(n+1)
        li[0] = 0
        li[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                if route[j][i-1] == 1:
                    li[i] = min(li[i], li[j]+1)
        return li[-1]-1

    # @param s, a string
    # @return an integer
    def minCut(self, s):
        if len(s) in (0, 1): return 0
        route = self.createRoute(s)
        return self.solve(s, route)

s = Solution()
print s.minCut("aabcbac")
#List.prettyPrint(head)
#Tree.prettyPrint(root)

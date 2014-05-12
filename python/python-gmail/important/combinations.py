#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

    For example,
    If n = 4 and k = 2, a solution is:

    [
        [2,4],
        [3,4],
        [2,3],
        [1,2],
        [1,3],
        [1,4],
    ]
Description:
    * DFS
Time Complexity:
Space Complexity:
Result: AC
'''

class Solution:
    def solve(self, result, route, index, n, k):
        if len(route) == k:
            result.append([item for item in route])
            return
        if index == n:
            return
        for i in range(index, n):
            route.append(i+1)
            self.solve(result, route, i+1, n, k)
            route.pop()

    # @return a list of lists of integers
    def combine(self, n, k):
        result = []
        route = []
        self.solve(result, route, 0, n, k)
        return result

s = Solution()
print s.combine(4,2)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from unittest import *

'''
Description: DFS + HashMap(Set)
Time Complexity:
Result: AC
'''

class Solution:

    def quickSort(self, li):
        if len(li) in (0, 1): return li
        lesser = self.quickSort(filter(lambda x: x<= li[-1], li[:-1]))
        bigger = self.quickSort(filter(lambda x: x>  li[-1], li[:-1]))
        return lesser + [li[-1]] + bigger
    
    def solve(self, S, i, route, result):
        n = len(S)
        if n == i:
            result[tuple([item for item in route])] = 1
            return
        j = i+1
        while j < len(S) and S[j] == S[i]:
            j += 1
        self.solve(S, j, route, result)
        route.append(S[i])
        self.solve(S, i+1, route, result)
        route.pop()
    
    
    def subsetsWithDup(self, S):
        S = self.quickSort(S)
        route = []
        result = {}
        self.solve(S, 0, route, result)
        return [list(item) for item in result.keys()]


s = Solution()
#print subsetsWithDup(range(3))
print s.subsetsWithDup([1, 2, 2])

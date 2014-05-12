#!/usr/bin/env python
from unittest import *

'''
Description: DFS
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
            result.append([item for item in route])
            return
        self.solve(S, i+1, route, result)
        route.append(S[i])
        self.solve(S, i+1, route, result)
        route.pop()
    
    def subsets(self, S):
        S = self.quickSort(S)
        result = []
        route = []
        self.solve(S, 0, route, result)
        return result

s = Solution()
print s.subsets(range(3))

'''
class Solution:
    def subsets(self, S):
        subset = [[]]
        for item in sorted(S):
            subset += [i+[item] for i in subset]
    return subset
    '''

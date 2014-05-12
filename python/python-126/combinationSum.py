#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
    [7] 
    [2, 2, 3] 

Description:
    1. DFS
Time Complexity:
Result:
'''

class Solution:
    def solve(self, candidates, target, result, route, index):
        total = sum(route)
        if total == target:
            result.append([item for item in route])
            return
        if index >= len(candidates) or total > target:
            return
        i = 0
        t = total
        while t <= target:
            route += [candidates[index]]*i
            self.solve(candidates, target, result, route, index+1)
            for j in range(i):
                route.pop()
            t += candidates[index]*i
            i += 1
    
    def combinationSum(self, candidates, target):
        candidates.sort()
        result = []
        route = []
        self.solve(candidates, target, result, route, 0)
        return result

s = Solution()
print s.combinationSum([7,6,3,2], 7)

#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a collection of integers that might contain duplicates, S, return all possible subsets.
Method: DFS
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
    * needs practise
    * classic DFS
'''

class Solution:
    def solve(self, S, index, route, result):
        if index == len(S):
            result.append([item for item in route])
            return
        i = index + 1
        while i <len(S) and S[i] == S[index]:
            i += 1
        self.solve(S, i, route, result)
        route.append(S[index])
        self.solve(S, index+1, route, result)
        route.pop()

    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S.sort()
        result = []
        route = []
        self.solve(S, 0, route, result)
        return result

s = Solution()
print s.subsetsWithDup([1,2,2])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a set of distinct integers, S, return all possible subsets.
Method: DFS
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
    Elements in a subset must be in non-descending order.
    The solution set must not contain duplicate subsets.
'''
class Solution:
    def solve(self, S, route, result, index):
        if index == len(S):
            result.append([item for item in route])
            return
        self.solve(S, route, result, index+1)
        route.append(S[index])
        self.solve(S, route, result, index+1)
        route.pop()

    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        S.sort()
        result =[]
        self.solve(S, [], result, 0)
        return result
                            
s = Solution()
print s.subsets([1,2,3])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Resolution:
    * reverse every sequence before add the element
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    def solve(self, n):
        if n == 0: return [[0]]
        if n == 1: return [[0], [1]]
        lesser = self.solve(n-1)
        result = []
        for item in lesser:
            result.append([0] + item)
        for item in lesser[::-1]:
            result.append([1] + item)
        return result

    # @return a list of integers
    def grayCode(self, n):
        route = self.solve(n)
        return [(reduce(lambda x,y: x*2+y, item)) for item in route]


s = Solution()
print s.grayCode(3)
print s.grayCode(0)
print s.grayCode(1)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem: Implement pow(x, n)
Description: Divide and Conquer
Time Complexity:
Space Complexity:
Result: AC
'''

class Solution:
    def solve(self, x, n):
        if n == 0: return 1.0
        if n == 1: return x
        half = self.solve(x, n/2)
        remainder = self.solve(x, n%2)
        return half * half * remainder

    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n>=0:
            return self.solve(x, n)
        else:
            return 1.0/self.solve(x, -n)

s = Solution()
print s.pow(2,-3)
print s.pow(0.00001, 2147483647)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

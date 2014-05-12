#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:

    "((()))", "(()())", "(())()", "()(())", "()()()"
Solution:
    * DFS
Time Complexity:
Space Complexity:
Result: AC
Note:
    * spaning
'''

class Solution:
    def solve(self, result, route, num_left, num_right, n):
        if (num_left + num_right) >= 2*n or num_left < num_right:
            if num_left == n and num_right == n:
                result.append("".join([item for item in route]))
            return
        route.append(")")
        self.solve(result, route, num_left, num_right+1, n)
        route.pop()
        route.append("(")
        self.solve(result, route, num_left+1, num_right, n)
        route.pop()

    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        result = []
        route = []
        self.solve(result, route, 0, 0, n)
        return result

s = Solution()
print s.generateParenthesis(8)

#List.prettyPrint(head)
#Tree.prettyPrint(root)

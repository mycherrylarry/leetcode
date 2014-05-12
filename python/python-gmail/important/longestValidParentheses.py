#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

    For "(()", the longest valid parentheses substring is "()", which has length = 2.

    Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
Description:
    * Use stack
Time Complexity: O(N)
Space Complexity: O(N)
Result: AC
'''

class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack =[]
        result = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(("(", i))
            else:
                if len(stack) == 0 or stack[-1][0] == ")":
                    stack.append((")", i))
                else:
                    stack.pop()
                    if len(stack) == 0:
                        result = max(result, i+1)
                    else:
                        result = max(result, i-stack[-1][1])
        return result

s = Solution()
print s.longestValidParentheses(")()())")
#List.prettyPrint(head)
#Tree.prettyPrint(root)

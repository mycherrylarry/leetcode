#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @return a boolean
    def isValid(self, s):
        pairs = {')':'(', ']': '[', '}' : '{'}
        stack = []
        for c in s:
            if c in pairs.values():
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != pairs[c]:
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True

s = Solution()
print s.isValid("()()")
print s.isValid("(()()")
print s.isValid("(()())")
print s.isValid("(()()))")
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note: understand what the problem whats
'''

class Solution:
    def solve(self, a, b):
        if a == None and b == None: return True
        if a == None: return False
        if b == None: return False
        if a.val != b.val: return False
        return self.solve(a.left, b.right) and self.solve(a.right, b.left)

    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None: return True
        return self.solve(root.left, root.right)

s = Solution()
print s.isSymmetric(root)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Description:
Time Complexity:
Space Complexity:
Result: AC
'''

class Solution:
    def solve(self, root):
        if root == None: return 0
        left = self.solve(root.left)
        right = self.solve(root.right)
        if left == -1 or right == -1:
            return -1
        if abs(left-right) > 1:
            return -1
        return max(left, right) + 1

    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if self.solve(root) == -1:
            return False
        return True


s = Solution()
print s.isBalanced(root)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

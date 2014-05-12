#!/usr/bin/env python
from unittest import *
#print root

'''
Description: Given a binary tree, find its minimum depth.
    1. recursion
    2. pay attention to the situations.
Time Complexity:
Result: AC
'''
class Solution:
    def minDepth(self, root):
        if root == None: return 0
        if root.left == None and root.right == None: return 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        elif root.right == None:
            return self.minDepth(root.left) + 1
        else:
            return min(self.minDepth(root.right), self.minDepth(root.left)) + 1


s = Solution()
print s.minDepth(root)

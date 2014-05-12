#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a binary tree, find the maximum path sum.

    The path may start and end at any node in the tree.
Description:
Time Complexity:
Space Complexity:
Result: AC
'''

class Solution:
    def __init__(self):
        self.maxLen = -100000000

    def height(self, root):
        if root == None: return -100000000
        left = self.height(root.left)
        right = self.height(root.right)
        h = max(0, left, right) + root.val
        self.maxLen = max(self.maxLen, h, root.val+left+right)
        return h

    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        self.height(root)
        return self.maxLen

root = TreeNode(-1)
root.left = TreeNode(-2)
s = Solution()
print s.maxPathSum(root)
Tree.prettyPrint(root)

#List.prettyPrint(head)

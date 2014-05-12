#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Description: VERY SIMPLE
Time Complexity:
Space Complexity:
Result: AC
'''


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None: return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

root.right.left.right = TreeNode(1)
s = Solution()
print s.maxDepth(root)
#List.prettyPrint(head)
Tree.prettyPrint(root)

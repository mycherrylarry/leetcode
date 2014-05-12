#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Assume a BST is defined as follows:

    The left subtree of a node contains only nodes with keys less than the node's key.
    The right subtree of a node contains only nodes with keys greater than the node's key.
    Both the left and right subtrees must also be binary search trees.

Solution:
    * set up minimum and maximum boundaries for each binary search tree
Time Complexity:
Space Complexity:
Result: AC
Note: 
    * pay attention to the requirement, if not sure, ask the interviewers.
'''

class Solution:
    # @param mi = minimum boundary
    # @param mx = maximum boundary
    def check(self, root, mi, mx):
        if root == None: return True
        if root.val >= mx or root.val <= mi:
            return False
        left = self.check(root.left, mi, root.val)
        right = self.check(root.right, root.val, mx)
        return left and right
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        return self.check(root, -10000000, 10000000)

s = Solution()
#List.prettyPrint(head)
Tree.prettyPrint(root)
print s.isValidBST(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given inorder and postorder traversal of a tree, construct the binary tree.

Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0: return None
        pivot = postorder[-1]
        index = inorder.index(pivot)
        root = TreeNode(pivot)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index:-1])
        return root

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

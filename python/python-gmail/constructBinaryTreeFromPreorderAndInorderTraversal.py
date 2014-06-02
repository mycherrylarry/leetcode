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
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(preorder) == 0: return None
        pivot = preorder[0]
        index = inorder.index(pivot)
        root = TreeNode(pivot)
        root.left = self.buildTree(preorder[1:index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

s = Solution()
root = s.buildTree([1,2,3,4,5,6], [3,2,4,1,6,5])

#List.prettyPrint(head)
Tree.prettyPrint(root)

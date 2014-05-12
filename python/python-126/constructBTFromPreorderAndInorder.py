#!/usr/bin/env python
from unittest import *
#print root
from util.Tree import *

'''
Description:
    Simple
Time Complexity:
Result: AC
'''

class Solution:

    def buildTree(self, preorder, inorder):
        if len(preorder) == 0: return None
        pix = preorder[0]
        index = inorder.index(pix)
        root = TreeNode(pix)
        root.left = self.buildTree(preorder[1: index+1], inorder[:index])
        root.right = self.buildTree(preorder[index+1:], inorder[index+1:])
        return root

s = Solution()
root = s.buildTree([3,4,2,1,5,6], [2,4,1,3,6,5])
Tree.prettyPrint(root)



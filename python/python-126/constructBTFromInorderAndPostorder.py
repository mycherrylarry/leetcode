#!/usr/bin/env python
from unittest import *
#print root
from util.Tree import *

'''
Description:
    1. No duplicates
    2. Easy
Time Complexity:
Result: AC
Additon: what about duplicates?
'''

class Solution:
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0: return None
        pix = postorder[-1]
        index = inorder.index(pix)
        root = TreeNode(pix)
        root.left = self.buildTree(inorder[:index], postorder[:index])
        root.right = self.buildTree(inorder[index+1:], postorder[index: -1])
        return root

s = Solution()
root = s.buildTree([2,4,1,3,6,5], [2,1,4,6,5,3])
Tree.prettyPrint(root)


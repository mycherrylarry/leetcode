#!/usr/bin/env python

'''
result: AC
'''
from unittest import *
from util.Tree import *

class Solution:
    def flatten(self, root):
        if root == None:
            return
        l = self.flatten(root.left)
        r = self.flatten(root.right)
        head = TreeNode(0)
        head.right = l
        pre = head
        p = head.right
        while p != None:
            pre = p
            p = p.right
        pre.right = r
        root.right = head.right
        root.left = None
        return root


s = Solution()
r = s.flatten(root)
print r

#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    Simple
Time Complexity:
Result: AC
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, num):
        if len(num) == 0: return None
        mid = len(num)/2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root



s = Solution()
print s.sortedArrayToBST(range(0)).val

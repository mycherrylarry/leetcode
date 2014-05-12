#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num) == 0: return None
        mid = len(num)/2
        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])
        return root

s = Solution()
h = s.sortedArrayToBST(range(10))
Tree.prettyPrint(h)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

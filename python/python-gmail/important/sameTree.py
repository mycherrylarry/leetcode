#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Description:
Time Complexity:
Space Complexity:
Result: AC
'''


class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        if p == None and q == None: return True
        if p == None: return False
        if q == None: return False
        if p.val != q.val: return False
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)
        return left and right


#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

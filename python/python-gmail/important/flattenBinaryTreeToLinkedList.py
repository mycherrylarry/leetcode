#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
Time Complexity: O(N)
Space Complexity: O(1)
Result: AC
Note:
    * 2 ways to deal with this problem
    * this way is better
    * store the tail of a tree
'''

class Solution:
    def solve(self, root):
        if root == None: return (None, None)
        h = root
        left_h, left_t = self.solve(root.left)
        right_h, right_t = self.solve(root.right)
        h.left = None
        if left_h == None and right_h == None:
            return (h, h)
        if left_h == None:
            h.right = right_h
            return (h, right_t)
        if right_h == None:
            h.right = left_h
            return (h, left_t)
        h.right = left_h
        left_t.right = right_h
        return (h, right_t)

    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        self.solve(root)

Tree.prettyPrint(root)
print "+++++++++++++"
s = Solution()
s.flatten(root)
Tree.prettyPrint(root)

#List.prettyPrint(head)

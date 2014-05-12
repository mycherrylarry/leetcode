#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Resolution:
    * DFS
Time Complexity:
Space Complexity:
Result: AC
Note:
    * cannot use DP
    * minus
'''


class Solution:
    def solve(self, route, root, sum):
        if root == None: return False
        route += root.val
        if root.left == None and root.right == None:
            if route == sum: return True
            return False
        left = self.solve(route, root.left, sum)
        right = self.solve(route, root.right, sum)
        if left or right:
            return True
        return False

    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        return self.solve(0, root, sum)

Tree.prettyPrint(root)
s = Solution()
print "XXX"
print s.hasPathSum(root, 9)
#List.prettyPrint(head)

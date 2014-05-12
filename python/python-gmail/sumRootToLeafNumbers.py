#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Description: Simple
Time Complexity:
Space Complexity:
Result: AC
'''

class Solution:
    def __init__(self):
        self.total = 0

    def solve(self, route, root):
        if root == None: return
        route.append(root.val)
        if root.left == None and root.right == None:
            self.total += reduce(lambda x,y: x*10+y, route)
            route.pop()
            return
        self.solve(route, root.left)
        self.solve(route, root.right)
        route.pop()

    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        self.solve([], root)
        return self.total

root = TreeNode(1)
l = TreeNode(2)
r = TreeNode(3)
t = TreeNode(4)
root.left = l
root.right = r
r.right = t

s = Solution()
print s.sumNumbers(root)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

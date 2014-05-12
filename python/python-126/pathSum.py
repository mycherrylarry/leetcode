#!/usr/bin/env python
from unittest import *

'''
Dwscription: Simple DFS
result: AC
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, sum, current_sum):
        if root == None: return False
        if root.left == None and root.right == None:
            if root.val + current_sum == sum:
                return True
            else:
                return False
        left  = self.dfs(root.left, sum, current_sum + root.val)
        right = self.dfs(root.right, sum, current_sum + root.val)
        return left or right
    
    
    def hasPathSum(self, root, sum):
        if root == None: return False
        return self.dfs(root, sum, 0)

root = TreeNode(-2)
root.right = TreeNode(-3)

s = Solution()
print s.hasPathSum(root, -5)





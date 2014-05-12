#!/usr/bin/env python
from unittest import *

'''
Description: Simple DFS with route
Result: AC
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, target_sum, route, result):
        if root.left == None and root.right == None:
            if (sum(route)+root.val) == target_sum:
                result.append([item for item in route]+[root.val])
            return
        route.append(root.val)
        if root.left != None:
            left  = self.dfs(root.left, target_sum, route, result)
        if root.right != None:
            right = self.dfs(root.right, target_sum, route, result)
        route.pop()
    
    def hasPathSum(self, root, sum):
        if root == None: return []
        result = []
        route = []
        self.dfs(root, sum, route, result)
        return result

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
root.right.right.left = TreeNode(5)

s = Solution()
print s.hasPathSum(root, 22)
#print s.hasPathSum(root, 23)
#print s.hasPathSum(root, 18)
#print s.hasPathSum(root, 26)
#print s.hasPathSum(root, 27)
#print s.hasPathSum(root, 2)





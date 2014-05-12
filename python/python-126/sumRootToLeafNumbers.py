#!/usr/bin/env python

'''
Description:
Time Complexity:
Result: AC
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self, root, route, nums):
        if root == None:
            return
        newRoute = [item for item in route]
        newRoute.append(root.val)
        self.dfs(root.left, newRoute, nums)
        self.dfs(root.right, newRoute, nums)
        if root.left == None and root.right == None:
            nums.append(newRoute)
    
    def sumNumbers(self, root):
        nums = []
        self.dfs(root, [], nums)
        return sum([reduce(lambda x, y: x*10 +y, item) for item in nums])
    


root = TreeNode(1)
l = TreeNode(2)
r = TreeNode(3)
#t = TreeNode(4)
root.left = l
root.right = r
#r.left = t

s = Solution()
print s.sumNumbers(root)

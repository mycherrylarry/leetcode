#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Note: Recursive solution is trivial, could you do it iteratively?

Description:
Time Complexity:
Space Complexity:
Result:
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        result = []
        if root == None: return result
        stack = [root]
        while len(stack)!=0:
            item = stack.pop()
            result.append(item.val)
            if item.right != None:
                stack.append(item.right)
            if item.left != None:
                stack.append(item.left)
        return result




s = Solution()
print s.preorderTraversal(root)

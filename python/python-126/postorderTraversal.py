#!/usr/bin/env python
from unittest import *

'''
Description: Simple
Time Complexity:
Result: AC
'''

from util.Tree import Tree

t = Tree()
root = t.createTree(range(10))

class Solution:
    def postOrder(self, root, result):
        if root == None:
            return
        self.postOrder(root.left, result)
        self.postOrder(root.right, result)
        result.append(root.val)
    
    def postorderTraversal(self, root):
        result = []
        self.postOrder(root, result)
        return result


s = Solution()
print s.postorderTraversal(root)

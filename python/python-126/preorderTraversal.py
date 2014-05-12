#!/usr/bin/env python
from unittest import *

'''
Description: Simple
Time Complexity:
Result: AC
'''

class Solution:
    def preOrder(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.preOrder(root.left, result)
        self.preOrder(root.right, result)
    
    def preorderTraversal(self, root):
        result = []
        self.preOrder(root, result)
        return result


s = Solution()
print s.preorderTraversal(root)

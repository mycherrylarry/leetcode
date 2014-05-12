#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
Time Complexity:
Result: AC
'''

class Solution:
    def inorder(self, root, result):
        if root == None: return
        self.inorder(root.left, result)
        result.append(root.val)
        self.inorder(root.right, result)
    
    
    def inorderTraversal(self, root):
        result = []
        self.inorder(root, result)
        return result

s = Solution()
print s.inorderTraversal(root)


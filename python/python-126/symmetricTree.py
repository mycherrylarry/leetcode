#!/usr/bin/env python
from unittest import *
#print root

'''
Description:

Time Complexity:
Result: AC
'''

class Solution:
    def subTreeSymmetric(self, p, q):
        if p != None and q == None: return False
        if p == None and q != None: return False
        if p == None: return True
        if p.val != q.val: return False
        return self.subTreeSymmetric(p.left, q.right) and self.subTreeSymmetric(p.right, q.left)
    
    def isSymmetric(self, root):
        if root == None: return True
        return self.subTreeSymmetric(root.left, root.right)
    
s = Solution()
print s.isSymmetric(root)


#!/usr/bin/env python
from unittest import *
from util.Tree import *
#print root

'''
Description:
    Simple
Time Complexity:
Result: AC
'''

class Solution:
    def maxDepth(self, root):
        if root == None: return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right))+1

s = Solution()
print s.maxDepth(root)
Tree.prettyPrint(root)


#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
    1. Recursion
Time Complexity:
Result: AC
'''

class Solution:
    def generate(self, li):
        if len(li) == 0: return [None]
        if len(li) == 1: return [TreeNode(li[0])]
        result = []
        for i in range(len(li)):
            left = self.generate(li[:i])
            right = self.generate(li[i+1:])
            for item_l in left:
                for item_r in right:
                    root = TreeNode(li[i])
                    root.left = item_l
                    root.right = item_r
                    result.append(root)
        return result
    
    def generateTrees(self, n):
        return self.generate(range(1,n+1))

s = Solution()
for item in s.generateTrees(10):
    Tree.prettyPrint(item)
    print "========="

#List.prettyPrint(head)

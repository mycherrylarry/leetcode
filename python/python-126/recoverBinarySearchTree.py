#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
    1. Inorder tranverse
Time Complexity:
Result: AC
'''

class Solution:
    def inorder(self, root, route):
        if root == None: return
        self.inorder(root.left, route)
        route.append(root)
        self.inorder(root.right, route)
    
    def recoverTree(self, root):
        route = []
        self.inorder(root, route)
        a, b = route[0], route[0]
        i = 0
        while i < len(route)-1:
            if route[i].val > route[i+1].val:
                break
            i += 1
        j = len(route)-1
        while j > 0:
            if route[j].val < route[j-1].val:
                break
            j -= 1
        route[i].val, route[j].val = route[j].val, route[i].val
        return root


s = Solution()
#List.prettyPrint(head)
Tree.prettyPrint(root)

s.recoverTree(root)
Tree.prettyPrint(root)

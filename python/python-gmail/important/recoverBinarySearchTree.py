#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Two elements of a binary search tree (BST) are swapped by mistake.

    Recover the tree without changing its structure.
Description:
    * Search the tree in order, and recover the result
    * Given two pointers, marked i and j, i scan from the start, and j scan from the end.
    * Swap i and j' values
Time Complexity: O(N)
Space Complexity: O(1)
Result: AC
'''

class Solution:
    def inorder(self, root, route):
        if root == None: return
        self.inorder(root.left, route)
        route.append(root)
        self.inorder(root.right, route)

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        route = []
        self.inorder(root, route)
        i = 0
        while i < len(route)-1 and route[i].val<=route[i+1].val:
            i += 1
        j = len(route)-1
        while j > 0 and route[j].val>=route[j-1].val:
            j -= 1
        route[i].val, route[j].val = route[j].val, route[i].val
        return root

s = Solution()
s.recoverTree(root)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

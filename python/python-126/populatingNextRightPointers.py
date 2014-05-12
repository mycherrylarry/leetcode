#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    1. Level order traverse
Time Complexity:
Result: AC for both populationNextRightPointers
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    def connect(self, root):
        if root == None: return root
        queue = [root]
        while len(queue) != 0:
            new_queue = []
            p = None
            for item in queue:
                if item.left != None:
                    new_queue.append(item.left)
                if item.right != None:
                    new_queue.append(item.right)
            for item in queue[::-1]:
                item.next = p
                p = item
            queue = new_queue
        return root
    
root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(4)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

s = Solution()
s.connect(root)
print root.left.next.val



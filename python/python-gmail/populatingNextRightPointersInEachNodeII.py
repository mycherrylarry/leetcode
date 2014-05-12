#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None: return
        queue = [root, "#"]
        while len(queue) != 0:
            node = queue[0]
            del(queue[0])
            if node != "#":
                if queue[0] != "#":
                    node.next = queue[0]
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                if queue[0] == "#":
                    queue.append("#")

s = Solution()
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
s.connect(root)
print root.left.next.val
#List.prettyPrint(head)
#Tree.prettyPrint(root)
s.connect(root)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

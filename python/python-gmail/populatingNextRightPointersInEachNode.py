#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Method: Level Search
Resolution:
    *. One queue
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
    # tag '#' means the end of each level
    def connect(self, root):
        if root == None: return
        queue = [root, '#']
        while len(queue) != 0:
            node = queue[0]
            del(queue[0])
            if node != '#':
                if queue[0] != '#':
                    node.next = queue[0]
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
                # the end of row
                if queue[0] == '#':
                    queue.append('#')

s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
s.connect(root)
print root.left.next.val
#List.prettyPrint(head)
#Tree.prettyPrint(root)

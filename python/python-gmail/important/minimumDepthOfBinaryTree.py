#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a binary tree, find its minimum depth.
Method: Recursion
Resolution:
    * if root is None: return 0
    * if root is leaf: return 1
    * check left nodes and right nodes, return the minimum of them
    * pay attention to the condition when there's None children
Time Complexity:
Space Complexity:
Result:
    * pay attention to the question
    * never thought it to be simple
    * use use cases to check the output
Note:
'''

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root == None: return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return self.minDepth(root.right) + 1
        if root.right == None:
            return self.minDepth(root.left) + 1
        return min(self.minDepth(root.right), self.minDepth(root.left)) + 1
                            


#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).
Method: Queue
Resolution:
    * Use queue to record every level of the tree, and stores the result
Time Complexity: O(N)
Space Complexity: O(N)
Result: AC
Note:
'''

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        result = []
        if root == None: return result
        queue = [root]
        while len(queue) != 0:
            result.append([item.val for item in queue])
            new_queue = []
            for item in queue:
                if item.left != None:
                    new_queue.append(item.left)
                if item.right != None:
                    new_queue.append(item.right)
            queue = new_queue
        return result

s = Solution()
print s.levelOrder(root)
#List.prettyPrint(head)
Tree.prettyPrint(root)

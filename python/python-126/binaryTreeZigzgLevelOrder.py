#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    1. set pos = 0, if pos == 0: print from left to right, if pos == 1: print from right to left
Time Complexity:
Result: AC
'''
class Solution:

    def zigzagLevelOrder(self, root):
        if root == None: return []
        queue = [root]
        result = []
        pos = 0
        while len(queue) != 0:
            new_queue = []
            if pos == 0:
                result.append([item.val for item in queue])
            else:
                result.append([item.val for item in queue[::-1]])
            pos = (pos+1) % 2
            for item in queue:
                if item.left != None:
                    new_queue.append(item.left)
                if item.right != None:
                    new_queue.append(item.right)
            queue = new_queue
        return result

s = Solution()
print s.zigzagLevelOrder(root)


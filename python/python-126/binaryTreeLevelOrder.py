#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    Simple
Time Complexity:
Result: AC
'''

class Solution:
    def levelOrder(self, root):
        if root == None: return []
        queue = [root]
        result = []
        while len(queue) != 0:
            result.append([item.val for item in queue])
            new_queue = []
            for item in queue:
                if item.left != None: new_queue.append(item.left)
                if item.right != None: new_queue.append(item.right)
            queue = new_queue
        return result

s = Solution()
print s.levelOrder(root)


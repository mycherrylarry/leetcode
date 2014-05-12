#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        result = []
        if root == None: return result
        stack = [(root, 0)]
        while len(stack) != 0:
            p, p_tag = stack.pop()
            if p_tag == 0:
                stack.append((p, 1))
                if p.left != None:
                    stack.append((p.left, 0))
            else:
                result.append(p.val)
                if p.right != None:
                    stack.append((p.right, 0))
        return result
                

s = Solution()
print s.inorderTraversal(root)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

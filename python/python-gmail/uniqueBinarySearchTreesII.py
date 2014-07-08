#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    def generate(self, li):
        if len(li) == 0: return [None]
        result = []
        for i in range(len(li)):
            left = self.generate(li[:i])
            right = self.generate(li[i+1:])
            for l_item in left:
                for r_item in right:
                    root = TreeNode(li[i])
                    root.left = l_item
                    root.right = r_item
                    result.append(root)
        return result

    # @return a list of tree node
    def generateTrees(self, n):
        return self.generate(range(1, n+1))

s = Solution()
result = s.generateTrees(3)
print result
#List.prettyPrint(head)
#Tree.prettyPrint(root)

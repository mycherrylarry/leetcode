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
    def jump(self, A):
        step = 0
        cur = 0
        last = 0
        for i in range(len(A)):
            if i > last:
                last = cur
                step += 1
            cur = max(cur, i + A[i])
        return step

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

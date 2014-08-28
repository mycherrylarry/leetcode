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
    not solved by myself, needs discussion
'''

class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        maxCover, start = 0, 0
        while (start <= maxCover) and (start < len(A)):
            if (A[start] + start) > maxCover:
                maxCover = A[start] + start
            if maxCover >= (len(A)-1):
                return True
            start += 1
        return False

class Solution:
    def canJump(self, A):
        cur = 0
        for i in range(len(A)):
            if i > cur:
                return False
            cur = max(cur, i + A[i])
        return True

s = Solution()
print s.canJump([2,3,1,1,4])
print s.canJump([3,2,1,0,4])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

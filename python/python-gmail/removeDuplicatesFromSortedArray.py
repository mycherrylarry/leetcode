#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
Time Complexity: O(N)
Space Complexity: O(1)
Result: AC
Note: offset is the key
'''

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        n = len(A)
        if n in (0, 1): return n
        offset = 0
        tag = A[0]
        for i in range(1, n):
            if A[i] == tag:
                offset += 1
            else:
                tag = A[i]
                A[i-offset] = A[i]
        return n-offset

A=[1,1,2,2,3]
s = Solution()
print s.removeDuplicates(A)
print A

#List.prettyPrint(head)
#Tree.prettyPrint(root)

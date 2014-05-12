#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
    * binary search
Time Complexity:
Space Complexity:
Result: AC
Note:
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        l, r = 0, len(A)
        while l < r:
            mid = (l+r)/2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

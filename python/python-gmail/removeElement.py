#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given an array and a value, remove all instances of that value in place and return the new length.

    The order of elements can be changed. It doesn't matter what you leave beyond the new length.
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        offset = 0
        for i in range(len(A)):
            if A[i] == elem:
                offset += 1
            else:
                A[i-offset] = A[i]
        return len(A)-offset

s = Solution()
print s.removeElement([1,1,1,2,1,1,1],1)
print s.removeElement([1,1,1,2,1,1,1],2)
print s.removeElement([],2)
print s.removeElement([2,2],2)
print s.removeElement([2],2)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

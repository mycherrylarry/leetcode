#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Methods: Three pointers
Solution:
Time Complexity: O(N)
Space Complexity: O(1)
Result: AC
'''
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        if len(A) in(0, 1): return 
        i, j, k, p = 0, 0, 0, 0
        while p < len(A):
            if A[p] == 2:
                A[k] = 2
                k += 1
            elif A[p] == 1:
                A[k] = 2
                A[j] = 1
                k += 1
                j += 1
            else:
                A[k] = 2
                A[j] = 1
                A[i] = 0
                k += 1
                j += 1
                i += 1
            p += 1

s = Solution()
li = [2,1,0,2,1,0,0,1,2]
s.sortColors(li)
print li
#List.prettyPrint(head)
#Tree.prettyPrint(root)

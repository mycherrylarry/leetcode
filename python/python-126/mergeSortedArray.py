#!/usr/bin/env python
from unittest import *
#print root

'''
Description: Merge from end to front
Time Complexity: O(N)
Result: AC
'''

class Solution:
    # merge B to A
    def merge(self, A, m, B, n):
        i, j, p = m-1, n-1, m+n-1
        while i >= 0 and j >= 0:
            if A[i] < B[j]:
                A[p] = B[j]
                p -= 1
                j -= 1
            else:
                A[p] = A[i]
                p -= 1
                i -= 1
        if j >= 0:
            for i in range(j+1):
                A[i] = B[i]
        return A

A = [2,4,6,9,0,0,0]
B = [1,3,10]
s = Solution()
print s.merge(A, 4, B, 3)





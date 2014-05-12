#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
Time Complexity:
Result: AC
'''


class Solution:
    def trap(self, A):
        if len(A) in (0, 1, 2): return 0
        mx = max(A)
        result = 0
        for item in A: result += (mx - item)
        s = A[0]
        i = 0
        # from left to right
        while s < mx:
            if A[i] > s:
                s = A[i]
            result -= (mx - s)
            i += 1
        j = len(A) - 1
        s = A[-1]
        while s < mx:
            if A[j] > s:
                s = A[j]
            result -= (mx - s)
            j -= 1
        return result

s = Solution()
print s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print s.trap([2,2,1])
print s.trap([0,2,0])





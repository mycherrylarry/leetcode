#!/usr/bin/env python
from unittest import *

'''
Description:
    1. Binary Search
Time Complexity:
Result: AC
'''
class Solution:
    def binarySearch(self, n):
        if n in (0, 1): return n
        i, j = 0, n
        while i<j:
            mid = (i+j)/2
            if n/mid == mid:
                return mid
            elif n/mid > mid:
                i = mid + 1
            else:
                j = mid
        return (i-1)
    
    def sqrt(self, x):
        return self.binarySearch(x)

s = Solution()
print s.binarySearch(9)
print s.binarySearch(100)
print s.binarySearch(25)
print s.binarySearch(1)
print s.binarySearch(0)
print s.binarySearch(2)
print s.binarySearch(-100)

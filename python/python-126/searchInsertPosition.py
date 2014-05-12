#!/usr/bin/env python

class Solution:

    def searchInsert(self, A, target):
        if len(A) == 0: return 0
        i, j = 0, len(A)
        while i < j:
            mid = (i+j)/2
            if A[mid] == target:
                return mid
            elif A[mid] < target:
                i = mid+1
            else:
                j = mid
        return i

s = Solution()
print s.searchInsert([1,3,5,7], 8)
print s.searchInsert([1,3,5,7], 5)
print s.searchInsert([1,3,5,7], 6)
print s.searchInsert([1,3,5,7], 0)
print s.searchInsert([1,3,5,7], 1)
print s.searchInsert([1,3,5,7], 7)


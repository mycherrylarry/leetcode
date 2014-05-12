#!/usr/bin/env python
class Solution:
    def searchRange(self, A, target):
        if len(A) == 0: return 0
        i, j = 0, len(A)
        while i < j:
            mid = (i+j)/2
            if A[mid] == target:
                l = mid
                while l > 0 and A[l-1] == target:
                    l -= 1
                r = mid
                while r < len(A)-1 and A[r+1] == target:
                    r += 1
                return [l, r]
            elif A[mid] < target:
                i = mid+1
            else:
                j = mid
        return [-1, -1]


s = Solution()
print s.searchRange([1,3,5,7], 8)
print s.searchRange([1,3,5,7], 5)
print s.searchRange([1,3,5,7], 6)
print s.searchRange([1,3,5,7], 0)
print s.searchRange([1,3,5,7], 1)
print s.searchRange([1,3,5,7,7,7,7], 7)


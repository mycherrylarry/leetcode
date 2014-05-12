#!/usr/bin/env python

class Solution:
    def removeDuplicates(self, A):
        if len(A) == 0 : return 0
        i = 1
        l = len(A)
        t = 0
        while i < l:
            if A[i] == A[i-1]:
                t += 1
            else:
                A[i-t] = A[i]
            i += 1
        return len(A) - t

s = Solution()
print s.removeDuplicates([1,1,1,1,2,2,3,3,4,4])
print s.removeDuplicates([1,1,2])


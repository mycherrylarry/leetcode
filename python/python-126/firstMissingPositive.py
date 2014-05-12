#!/usr/bin/env python
class Solution:
    def firstMissingPositive(self, A):
        for item in A:
            i = item
            while 0< i <= len(A) and A[i-1] != 'X':
                t = A[i-1]
                A[i-1] = 'X'
                i = t
        for i in range(len(A)):
            if A[i] != 'X':
                return i+1
        return len(A)+1


s = Solution()
print s.firstMissingPositive([-19,3,2,6,1,7,7,7,4,5])


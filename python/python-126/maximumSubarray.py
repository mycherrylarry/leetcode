#!/usr/bin/env python
class Solution:
    def maxSubArray(self, A):
        mx = A[0]
        tmp = A[0]
        for i in range(1, len(A)):
            if tmp < 0:
                tmp = A[i]
            else:
                tmp += A[i]
            if tmp > mx:
                mx = tmp
        return mx
s = Solution()
#print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print s.maxSubArray([1])

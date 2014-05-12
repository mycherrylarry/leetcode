#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
Resolution:
Time Complexity: O(N)
Space Complexity: O(N)
Result: AC
Note:
'''

class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0: return 0
        result = [0]*len(A)
        result[0] = A[0]
        for i in range(1, len(A)):
            if result[i-1] <= 0:
                result[i] = A[i]
            else:
                result[i] = A[i]+ result[i-1]
        return max(result)


s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

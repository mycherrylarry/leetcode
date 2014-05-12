#!/usr/bin/env python
from unittest import *

'''
Description:
    Simple
Time Complexity:
    O(N)
Result: AC
'''

class Solution:
    def removeDuplicates(self, A):
        if len(A) in (0, 1, 2): return len(A)
        tag = [A[0], 1]
        i = 1
        while i < len(A):
            if A[i] == tag[0]:
                if tag[1] == 2:
                    del(A[i])
                else:
                    tag[1] = 2
                    i += 1
            else:
                tag = [A[i], 1]
                i += 1
        return len(A)


s = Solution()
print s.removeDuplicates([1,1,1,2,2,3,3,3,3]) 




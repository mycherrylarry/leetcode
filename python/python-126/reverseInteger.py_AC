#!/usr/bin/env python
from unittest import *

'''
Description:
    1. Just like the problem of judging wether an integer is permutation
Time Complexity: O(len(x))
Result: AC
'''

class Solution:
    def reversePos(self, x):
        result = 0
        p = 1
        while x/(p*10) != 0: p*=10
        q = 1
        while p != 0:
            result += (x/p) * q
            x %= p
            p /= 10
            q *= 10
        return result
    
    def reverse(self, x):
        if x < 0:
            return -self.reversePos(-x)
        else:
            return self.reversePos(x)

s = Solution()
print s.reverse(-10002)


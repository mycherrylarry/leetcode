#!/usr/bin/env python
from unittest import *

'''
Description:
    1. judge minus
    2. caculate from front and end
Time Complexity: O(len(x))
Result: AC
Addition: x = abs(x) is OK!

'''

class Solution:
    def isPalindrome(self, x):
        x = abs(x)
        if x / 10 == 0: return True
        p, q = 10, 10
        while x / p != 0:
            p *= 10
        while p > q:
            # judge number
            if ((x%q)/(q/10)) != ((x%p)/(p/10)):
                return False
            p /= 10
            q *= 10
        return True

s = Solution()
print s.isPalindrome(10)



        



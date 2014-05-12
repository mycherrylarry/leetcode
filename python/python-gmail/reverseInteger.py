#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Reverse digits of an integer.

    Example1: x = 123, return 321
    Example2: x = -123, return -321
Description:
Time Complexity:
Space Complexity:
Result: AC
'''

class Solution:
    def reversePositive(self, x):
        if x == 0: return x
        result = []
        while x != 0:
            result.append(x%10)
            x /= 10
        return reduce(lambda x,y: x*10 +y, result)

    # @return an integer
    def reverse(self, x):
        if x<0: return -self.reversePositive(-x)
        return self.reversePositive(x)

s = Solution()
print s.reverse(-123)
print s.reverse(0)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

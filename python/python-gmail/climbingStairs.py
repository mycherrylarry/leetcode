#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        if n in (0, 1): return 1
        result = [1] * (n+1)
        for i in range(2, n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]

s = Solution()
print s.climbStairs(4)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

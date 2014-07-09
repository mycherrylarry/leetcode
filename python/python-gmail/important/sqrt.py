#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Implement int sqrt(int x).
    Compute and return the square root of x.

Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    def sqrt(self, x):
        assert(x > -1)
        if x in (0, 1): return x
        i, j = 0, x
        while i< j:
            mid = (i+j)/2
            if mid == (x/mid):
                return mid
            elif mid < (x/mid):
                i = mid + 1
            else:
                j = mid
        return i-1

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

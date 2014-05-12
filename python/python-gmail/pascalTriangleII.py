#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''
class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        result = [1]*(rowIndex+1)
        for i in range(rowIndex):
            # store previous values
            pre = 0
            for j in range(i+1):
                tmp = result[j]
                result[j] = result[j] + pre
                pre = tmp
        return result

s = Solution()
print s.getRow(4)
print s.getRow(5)
print s.getRow(6)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

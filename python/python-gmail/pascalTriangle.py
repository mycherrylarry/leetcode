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
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows <= 0: return []
        result = [[1]]
        for i in range(1, numRows):
            tmp = [0]*(i+1)
            for j in range(i+1):
                a, b = j-1, j
                if a>=0: tmp[j] += result[i-1][a]
                if b<i: tmp[j] += result[i-1][b]
            result.append(tmp)
        return result


s = Solution()
print s.generate(5)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

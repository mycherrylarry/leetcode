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
Note: read the question
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) in (0, 1): return 0
        mi = prices[0]
        result = 0
        for item in prices[1:]:
            if item < mi:
                mi = item
            else:
                result = max(result, item-mi)
        return result

s = Solution()
print s.maxProfit([1,2,3,1])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

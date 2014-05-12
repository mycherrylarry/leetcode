#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) in (0,1): return 0
        result = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i-1]
        return result

s = Solution()
print s.maxProfit([1,3,4,2])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

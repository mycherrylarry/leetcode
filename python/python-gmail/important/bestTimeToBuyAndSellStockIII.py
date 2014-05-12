#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Say you have an array for which the ith element is the price of a given stock on day i.

    Design an algorithm to find the maximum profit. You may complete at most two transactions.
Description:
    * reserve two arrays: sumS and sumE
    * sumS[i] = (max(prices[:i+1]) - min(prices[:i+1]))
    * sumE[i] = (max(prices[i:]) - min(prices[i:]))
    * result = max(map(lambda (x,y): x+y, zip(sumS, sumE)))
Time Complexity: O(N)
Space Complexity: O(N)
Result: AC
'''

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        n = len(prices)
        if n in (0, 1): return 0
        # calculate sumS
        sumS = [0]*n
        low = prices[0]
        mx = 0
        for i in xrange(n):
            if prices[i] <low:
                low = prices[i]
            mx = max(prices[i] - low, mx)
            sumS[i] = mx
        # calculate sumE
        sumE = [0]*n
        high = prices[n-1]
        mx = 0
        for i in range(n)[::-1]:
            if prices[i] >high:
                high = prices[i]
            mx = max(high - prices[i], mx)
            sumE[i] = mx
        result = 0
        for i in xrange(n):
            if sumS[i] + sumE[i] >result:
                result = sumS[i] + sumE[i]
        return result



s = Solution()
print s.maxProfit([1,2,3,1])
print s.maxProfit([2,1,2,0,1])
print s.maxProfit([1,2,4,2,5,7,2,4,9,0])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

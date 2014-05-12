#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
    1. DP, two routes
       f(i) = [0, i]'s max profit
       g(i) = [i, n-1]'s max profit
Time Complexity: O(N)
Result: AC
important
'''

class Solution:
    def maxProfit(self, prices):
        if len(prices) in (0, 1): return 0
        f = [0]*len(prices)
        g = [0]*len(prices)
        i = 1
        mi = prices[0]
        mi_mx = 0
        while i < len(prices):
            if prices[i] <= mi:
                mi = prices[i]
            else:
                mi_mx = max(prices[i] - mi, mi_mx)
            f[i] = mi_mx
            i += 1
        mx = prices[-1]
        i = len(prices)-2
        mx_mx = 0
        while i >= 0:
            if prices[i] >= mx:
                mx = prices[i]
            else:
                mx_mx = max(mx - prices[i], mx_mx)
            g[i] = mx_mx
            i -= 1
        result = 0
        for i in range(len(prices)):
            result = max(result, f[i]+g[i])
        return result



s = Solution()
    
print s.maxProfit([1,2,4,2,5,7,2,4,9,0])



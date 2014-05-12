#!/usr/bin/env python
class Solution:
    def maxProfit(self, prices):
        if len(prices) in (0, 1): return 0
        j = 1
        total = 0
        while j < len(prices):
            while j < len(prices) and prices[j] <= prices[j-1]:
                j += 1
            tag = j-1
            while j < len(prices) and prices[j] > prices[j-1]:
                j += 1
            total += prices[j-1] - prices[tag]
        return total
s = Solution()
    
print s.maxProfit([1,2,3,4,1,2,10,1,2,2,1])



#!/usr/bin/env python

class Solution:

    def merge(self, l, r):
        if len(l) == 0 or len(r) == 0:
            return 0
        return max(r) - min(l)
    
    def maxProfit(self, prices):
        if len(prices) in (0, 1):
            return 0
        mid = len(prices)/2
        l = self.maxProfit(prices[:mid])
        r = self.maxProfit(prices[mid:])
        x = self.merge(prices[:mid], prices[mid:])
        return max(l, r, x)

s = Solution()

print s.maxProfit([1,2])



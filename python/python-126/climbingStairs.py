#!/usr/bin/env python

class Solution:
    def climbStairs(self, n):
        if n < 0 : return 0
        if n in (0, 1): return 1
        route = [0] * (n+1)
        route[0], route[1] = 1, 1
        for i in range(2, n+1):
            route[i] = route[i-1] + route[i-2]
        return route[n]

s = Solution()
print s.climbStairs(11)
print s.climbStairs(1)
print s.climbStairs(2)
print s.climbStairs(3)
print s.climbStairs(4)

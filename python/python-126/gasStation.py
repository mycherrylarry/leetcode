#!/usr/bin/env python

class Solution:

    def canCompleteCircuit(self, gas, cost):
        def sub(x):
            a, b = x
            return a - b
        l = len(gas)
        route = map(sub, zip(gas, cost))*2
        index = 0
        p = 1
        result = route[0]
        while p < (2*l):
            if result < 0:
                result = route[p]
                index = p
                p += 1
                continue
            if (p - index) == l:
                return index
            result += route[p]
            p += 1
        return -1

s = Solution()
print s.canCompleteCircuit([3,2,1], [2,4,1])

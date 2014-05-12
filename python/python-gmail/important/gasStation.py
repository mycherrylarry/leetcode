#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Description:
    * For ith element, reserver an array to store the sub of cost[i] and gas[i]
    * route = [0]*2n and caculate
    * ...
Time Complexity: O(N)
Space Complexity: O(2*N)
Result: AC
'''

class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        if len(gas) == 0 or len(gas)!= len(cost): return -1
        n = len(gas)
        route = map(lambda (x,y): x-y, zip(gas, cost))*2
        i, j = 0, 1
        tmp_sum = route[0]
        while i < n:
            if tmp_sum < 0:
                tmp_sum = route[j]
                i = j
                j += 1
                continue
            if (j -i) == n:
                return i
            else:
                tmp_sum += route[j]
                j += 1
        return -1

s = Solution()
print s.canCompleteCircuit([4],[5])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

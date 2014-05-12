#!/usr/bin/env python
from unittest import *

'''
Description:
    1. find out the first element of kth permutation
    2. continue with recurtion
Time Complexity: O(N)
Result: AC
Addition: No check for invalid situations
'''
class Solution:

    # generate a list that contains the result of n! : pattern = [0, 1, 2!, 3!, 4! ... n!]
    def generatePattern(self, n):
        result = [0]*(n+1)
        result[1] = 1
        for i in range(2, n+1):
            result[i] = result[i-1]*i
        return result
    
    # store the first element of kth permutation to result
    def getList(self, li, k, pattern, result):
        if k == 0:
            result.extend(li)
            return
        l = len(li)
        next_c = k/(pattern[l-1])
        result.append(li[next_c])
        del(li[next_c])
        self.getList(li, k%(pattern[l-1]), pattern, result)
    
    def getPermutation(self, n, k):
        k -= 1
        pattern = self.generatePattern(n)
        result = []
        li = range(1, n+1)
        self.getList(li, k, pattern, result)
        return "".join([str(item) for item in result])

s = Solution()
print s.getPermutation(7, 10)
print s.getPermutation(1, 1)
print s.getPermutation(0, 0)

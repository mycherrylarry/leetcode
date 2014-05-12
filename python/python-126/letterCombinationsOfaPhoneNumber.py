#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    1. use hash
Time Complexity:
Result: AC
'''

class Solution:

    def combine(self, mp, digits, route):
        if len(digits) == 0: return route
        new_route = []
        for item in mp[digits[-1]]:
            for i in route:
                new_route.append(item + i)
        return self.combine(mp, digits[:-1], new_route)
    
    
    def letterCombinations(self, digits):
        mp = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        new_digits = []
        for item in digits:
            if mp.has_key(item):
                new_digits.append(item)
        route = self.combine(mp, new_digits, [''])
        return route

s = Solution()
print s.letterCombinations('123')


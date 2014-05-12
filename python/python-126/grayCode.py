#!/usr/bin/env python
from unittest import *

'''
Description:
    add 0 and reverse the list add 1
Result: AC
'''
class Solution:
    def generateFromN(self, n):
        if n == 0: return []
        if n == 1: return [[0], [1]]
        result = self.generateFromN(n-1)
        new_result = []
        for item in result:
            new_item = [0] + [sub_item for sub_item in item]
            new_result.append(new_item)
        for item in result[::-1]:
            new_item = [1] + [sub_item for sub_item in item]
            new_result.append(new_item)
        return new_result
    
    def grayCode(self, n):
        if n == 0: return [0]
        result = self.generateFromN(n)
        return [reduce(lambda x,y : x*2 +y, item) for item in result]

s = Solution()
print s.grayCode(2)
print s.grayCode(3)
print s.grayCode(4)
print s.grayCode(0)
print s.grayCode(1)



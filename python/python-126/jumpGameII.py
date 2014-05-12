#!/usr/bin/env python
from unittest import *

'''
Description:
Time Complexity:
Result:
'''

class Solution:
    def solve(self, A, route, result, i):
        if i >= (len(A) - 1):
            result.append([item for item in route])
            return
        for j in range(1, A[i]+1):
            route.append(i+j)
            self.solve(A, route, result, i + j)
            route.pop()
    
    
    def jump(self, A):
        route = []
        result = []
        self.solve(A, route, result, 0)
        return min([len(item) for item in result])

s = Solution()
print s.jump([2, 3, 1, 1, 4])
print s.jump([6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3])

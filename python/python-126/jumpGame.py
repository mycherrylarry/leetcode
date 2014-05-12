#!/usr/bin/env python
class Solution:
    def check(self, route, x):
        if 0<= x < len(route) and route[x]!= 1: return True
        return False
    
    def solve(self, A, route, n):
        if n >= (len(route)-1): return True
        if self.check(route, n):
            route[n] = 1
            l = self.solve(A, route, n-A[n])
            r = self.solve(A, route, n+A[n])
            if l or r: return True
            route[n] = 0
        return False
    
    def canJump(self, A):
        l = len(A)
        if l == 0: return True
        route = [0]* l
        return self.solve(A, route, 0)

s = Solution()
print s.canJump([3,2,1,0,4])
print s.canJump([2,3,1,1,4])

#!/usr/bin/env python

# Important!!!
class Solution:
    def solve(self, n, result, route, l, r):
        if (l+r) >= n*2 or l < r:
            if l == n and r == n:
                result.append([item for item in route])
            return 
        route.append("(")
        self.solve(n, result, route, l+1, r)
        route.pop()
        route.append(")")
        self.solve(n, result, route, l, r+1)
        route.pop()
        return
    
    
    def generateParenthesis(self, n):
        result = []
        route = []
        self.solve(n, result, route, 0, 0)
        return ["".join(item) for item in result]

s = Solution()
print s.generateParenthesis(8)


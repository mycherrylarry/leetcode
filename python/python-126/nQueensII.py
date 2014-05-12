#!/usr/bin/env python
# A common DFS solution

class Solution:
    
    def check(self, route, pos, n):
        x, y = pos
        for i in range(y):
            if route[x][i] == "Q": return False
        for j in range(x):
            if route[j][y] == "Q": return False
        t = min(x,y)
        for i in range(t+1):
            if route[x-i][y-i] == "Q": return False
        while (x >= 0 and y < n):
            if (route[x][y] == "Q"):
                return False
            x = x-1
            y = y+1
        return True
    
    def solve(self, route, n, j=0):
        if j == n:
            self.result.append(["".join([x for x in item]) for item in route])
            return
        for i in range(n):
            if self.check(route, (j, i), n):
                route[j][i] = "Q"
                self.solve(route, n, j+1)
                route[j][i] = "."
    
    def solveNQueens(self, n):
        self.result = []
        route = [["."]*n for i in range(n)]
        self.solve(route, n)
        return len(self.result)

s = Solution()
print s.solveNQueens(8)

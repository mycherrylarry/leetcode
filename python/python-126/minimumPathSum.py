#!/usr/bin/env python
class Solution:
    def minPathSum(self, grid):
        h = len(grid)
        if h == 0: return 0
        w = len(grid[0])
        if w == 0: return 0
        route = [[0]*(w+1) for i in range(h+1)]
        for i in range(h):
            route[i+1][1] = route[i][1] + grid[i][0]
        for j in range(w):
            route[1][j+1] = route[1][j] + grid[0][j]
        for i in range(1, h):
            for j in range(1, w):
                route[i+1][j+1] = min(route[i+1][j], route[i][j+1]) + grid[i][j]
        return route[h][w]

s = Solution()
print s.minPathSum([[1,2],[1,1]])
print s.minPathSum([[0]])

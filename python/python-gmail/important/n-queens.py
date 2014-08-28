#!/usr/bin/env python

# result:  AC
class Solution:
    def check(self, route, n, index, i):
        # left-top, top, right-top
        a, b = index, i
        while a >= 0 and b >= 0:
            if route[a][b]  == 'Q':
                return False
            a -= 1
            b -= 1
        a = index
        while a >= 0:
            if route[a][i] == 'Q':
                return False
            a -= 1
        a, b = index, i
        while a >=0 and b < n:
            if route[a][b] == 'Q':
                return False
            a -= 1
            b += 1
        return True

    def solve(self, route, result, n, index):
        if index == n:
            result.append([[cow for cow in rol] for rol in route])
            return
        for i in range(n):
            if self.check(route, n, index, i):
                route[index][i] = 'Q'
                self.solve(route, result, n, index+1)
                route[index][i] = '.'

    def solveNQueens(self, n):
        result = []
        route = [['.'] * n for i in range(n)]
        self.solve(route, result, n, 0)
        return [["".join(i) for i in j] for j in result]

s = Solution()
print s.solveNQueens(4)

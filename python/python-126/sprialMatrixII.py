#!/usr/bin/env python

'''
Description:
Time Complexity: O(N*N)
Result: AC
'''

class Solution:

    def generateMatrix(self, n):
        if n <=0 :return []
        result = [[0]*n for item in range(n)]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        i = 2
        tag = 0
        x, y = 0, 0
        result[0][0] = 1
        while i <= n*n:
            x1, y1 = direction[tag]
            x += x1
            y += y1
            result[x][y] = i
            if (not (0<=x+x1<n and 0<=y+y1<n)) or result[x+x1][y+y1] != 0:
                tag = (tag+1)%4
            i +=1
        return result

s = Solution()

for item in s.generateMatrix(10):
    print item







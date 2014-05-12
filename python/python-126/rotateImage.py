#!/usr/bin/env python
from unittest import *

'''
Description:
    1, 2, 3       7, 4, 1
    4, 5, 6   =>  8, 5, 2
    7, 8, 9       9, 6, 3
    
    1. tmp = i; i = j; j = (n-tmp-1)
Time Complexity: O(N^2)
Space Complexity: O(1)
Result: AC
'''

m = [list("11111"), list("22222"), list("33333"), list("44444"), list("55555")]
m = [list("1111"), list("2222"), list("3333"), list("4444")]

class Solution:
    # rotate from outside
    def rotateSub(self, matrix, i):
        n = len(matrix)
        if (i+1) > (n/2): return
        for j in range(i, n-i-1):
            x, y = i, j
            tmp = matrix[x][y]
            for k in range(0, 4):
                tmp_1 = matrix[y][n-x-1]
                matrix[y][n-x-1] = tmp
                tmp = tmp_1
                x, y = y, n-x-1
    
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(0, n/2):
            self.rotateSub(matrix, i)
        return matrix

m = [[]]
s = Solution()
print s.rotate(m)

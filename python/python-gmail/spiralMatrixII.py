#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        if n <= 0: return []
        result = [[0]*n for i in range(n)]
        position = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur = (0, 0)
        pos = 0
        index = 1
        while index <= n*n:
            x, y = cur
            result[x][y] = index
            index += 1
            offset_x, offset_y = position[pos]
            n_x, n_y = x+offset_x, y+offset_y
            if not(0<=n_x<n and 0<=n_y<n and result[n_x][n_y]== 0):
                pos = (pos+1)%4
                offset_x, offset_y = position[pos]
            cur = (x + offset_x, y + offset_y)
        return result
                
s = Solution()
print s.generateMatrix(30)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Resolution:
    * Gray tags
Time Complexity:
Space Complexity:
Result: AC
Note:
'''
class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0: return
        h, w = len(matrix), len(matrix[0])
        tag_w = [0]*w
        for i in range(h):
            for j in range(w):
                tag_h = 0
                if matrix[i][j] == 0:
                    if tag_h == 0:
                        tag_h = 1
                        for k in range(w):
                            if matrix[i][k] != 0:
                                matrix[i][k] = "G"
                    if tag_w[j] == 0:
                        tag_w[j] = 1
                        for k in range(h):
                            if matrix[k][j] != 0:
                                matrix[k][j] = "G"
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == "G":
                    matrix[i][j] = 0


matrix = [[1,0,0],[1,0,1],[1,1,1]]
s = Solution()
s.setZeroes(matrix)
print matrix
#List.prettyPrint(head)
#Tree.prettyPrint(root)

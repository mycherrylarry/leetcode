#!/usr/bin/env python

class Solution:
    def setZeroes(self, matrix):
        h = len(matrix)
        if h == 0: return matrix
        w = len(matrix[0])
        if w == 0: return matrix
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 0:
                    for t in range(w):
                        if matrix[i][t] in (0, 'W'):
                            matrix[i][t] = 'W'
                        else:
                            matrix[i][t] = 'X'
                    for t in range(h):
                        if matrix[t][j] in (0, 'H'):
                            matrix[t][j] = 'H'
                        else:
                            matrix[t][j] = 'X'
        for i in range(h):
            for j in range(w):
                if matrix[i][j] == 'X':
                    matrix[i][j] = 0
                elif matrix[i][j] == 'H':
                    for t in range(w):
                        matrix[i][t] = 0
                elif matrix[i][j] == 'W':
                    for t in range(h):
                        matrix[t][j] = 0
        return matrix


mx = [[0,2,3,4], [2,1,3,5], [2,1,0,2]]
s = Solution()
print s.setZeroes(mx)



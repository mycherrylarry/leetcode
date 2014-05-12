#!/usr/bin/env python
from unittest import *

'''
Description:
    1. direction is the key
Time Complexity: O(M*N)
Result: AC
'''

class Solution:
    def check(self, (pos), route, w, h):
        x, y = pos
        if x<0 or x>=h or y <0 or y>= w: return False
        if route[x][y] == 1: return False
        return True
    
    """solve every step
    # result: store the result
    # route: the route recording position that has been visited
    # cur_pos: current position
    # direction: [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # direction_i : current index of pos
    """
    def solve(self, result, matrix, cur_pos, route, direction, direction_i):
        h = len(matrix)
        w = len(matrix[0])
        if len(result) == h*w: return result
        x, y = cur_pos
        result.append(matrix[x][y])
        route[x][y] = 1
        d_x, d_y = direction[direction_i]
        if not self.check((x+d_x, y+d_y), route, w, h):
            direction_i = (direction_i+1)%4
            d_x, d_y = direction[direction_i]
        self.solve(result, matrix, (x+d_x, y+d_y), route, direction, direction_i)
    
    def spiralOrder(self, matrix):
        result = []
        h = len(matrix)
        if h == 0: return result
        w = len(matrix[0])
        if w == 0: return result
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        route = [[0]*w for item in range(h)]
        self.solve(result, matrix, (0, 0), route, direction, 0)
        return result


s = Solution()
print s.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])

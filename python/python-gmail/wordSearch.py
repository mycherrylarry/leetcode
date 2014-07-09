#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a 2D board and a word, find if the word exists in the grid.

    The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Method:
Solution:
    dfs
Time Complexity:
Space Complexity:
Result: Time Limit Exceeded
Note:
    * if there's no such a starting index, there's no need to do dfs
    * dfs costs a lot of time ! be careful and do pruning
'''

class Solution:
    def check(self, board, route, c, pos, h, w):
        x, y = pos
        if 0<= x< h and 0<= y < w:
            if board[x][y] == c:
                if route[x][y] == 0:
                    return True
        return False

    def solve(self, board, route, word, i_word, pos, h, w):
        if i_word == len(word): return True
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        if self.check(board, route, word[i_word], pos, h, w):
            x, y = pos
            route[x][y] = 1
            for direct in direction:
                d_x, d_y = direct
                if self.solve(board, route, word, i_word+1, (x+d_x, y+d_y), h, w):
                    return True
            route[x][y] = 0
        return False

    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if len(word) == 0: return True
        h = len(board)
        if h == 0: return False
        w = len(board[0])
        if w == 0: return False

        for i in range(h):
            for j in range(w):
                if board[i][j] == word[0]:
                    route = [[0]*w for k in range(h)]
                    if self.solve(board, route, word, 0, (i, j), h, w):
                        return True
        return False
                                
s = Solution()
board = [
          ["ABCE"],
            ["SFCS"],
              ["ADEE"]
              ]
print s.exist(board, 'SEE')
print s.exist(board, 'ABCCED')
print s.exist(board, 'ABCB')
#List.prettyPrint(head)
#Tree.prettyPrint(root)

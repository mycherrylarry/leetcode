#!/usr/bin/env python

board = [list("ABCE"),list("SFCS"),list("ADEE")]

class Solution:
    def __init__(self):
        self.position = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def createMp(self, board):
        h, w = self.h, self.w
        mp = {}
        for i in range(h):
            for j in range(w):
                if mp.has_key(board[i][j]):
                    mp[board[i][j]].append((i,j))
                else:
                    mp[board[i][j]] = [(i,j)]
        return mp
    
    def check(self, pos, c):
        x, y = pos
        h, w = self.h, self.w
        if 0 <= x < h and 0 <= y <w:
            if self.board[x][y] == c:
                if self.route[x][y] == 0:
                    return True
        return False
    
    def solve(self, pos, num, word):
        if num == len(word):
            return True
        x, y = pos
        if self.check(pos, word[num]):
            self.route[x][y] = 1
            for item in self.position:
                x1, y1 = item
                if self.solve((x+x1, y+y1), num+1, word):
                    return True
            self.route[x][y] = 0
        return False
    
    def exist(self, board, word):
        self.board = board
        self.word = word
        h = len(board)
        if h == 0: return False
        w = len(board[0])
        if w == 0: return False
        if len(word) == 0: return False
        self.h, self.w = h, w
        self.route = [[0]* w for item in range(h)]
        self.mp = self.createMp(board)
        s = word[0]
        if not self.mp.has_key(s): return False
        for item in self.mp[s]:
            if self.solve(item, 0, word):
                return True
        return False

s = Solution()
print s.exist(board, "CCSE")
print s.exist(board, "CCSEEDASFBA")
print s.exist(board, "F")


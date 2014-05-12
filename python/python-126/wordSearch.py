#!/usr/bin/env python
from unittest import *

position = [(-1, 0), (1, 0), (0, -1), (0, 1)]
board = [list("ABCE"),list("SFCS"),list("ADEE")]
h = len(board)
w = len(board[0])

mp = {}
for i in range(h):
    for j in range(w):
        if mp.has_key(board[i][j]):
            mp[board[i][j]].append((i,j))
        else:
            mp[board[i][j]] = [(i,j)]

route = [[0]* w for item in range(h)]

def check(pos, c):
    x, y = pos
    if 0 <= x < h and 0 <= y <w:
        if board[x][y] == c:
            if route[x][y] == 0:
                return True
    return False


def solve(pos, num, word):
    if num == len(word):
        return True
    x, y = pos
    if check(pos, word[num]):
        route[x][y] = 1
        for item in position:
            x1, y1 = item
            if solve((x+x1, y+y1), num+1, word):
                return True
        route[x][y] = 0
    return False


@unittest
def exist(word):
    s = word[0]
    if not mp.has_key(s): return False
    for item in mp[s]:
        if solve(item, 0, word):
            return True
    return False

exist("CCSE")
exist("CCSEEDASFBA")


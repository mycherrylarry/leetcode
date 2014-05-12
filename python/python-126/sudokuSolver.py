#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
    1. DFS
    2. prepare three array for sets:
       row = [set()...]
       col = [set()...]
       sub = [set()...]
Time Complexity:
Result: AC
'''

class Solution:
    def solve(self, board, sets, index):
        if index == 9*9:
            return True
        x, y = index/9, index%9
        z = (x/3)*3+(y/3)
        row, col, sub = sets
        interSection = row[x].intersection(col[y]).intersection(sub[z])
        if board[x][y] == ".":
            for item in interSection:
                board[x][y] = item
                row[x].remove(item)
                col[y].remove(item)
                sub[z].remove(item)
                result = self.solve(board, (row, col, sub), index+1)
                if result:
                    return True
                board[x][y] = "."
                row[x].add(item)
                col[y].add(item)
                sub[z].add(item)
        else:
            result = self.solve(board, sets, index+1)
            if result:
                return True
        return False
    
    
    def createSets(self, board):
        row = [set() for item in range(1, 10)]
        col = [set() for item in range(1, 10)]
        sub = [set() for item in range(1, 10)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    sub[(i/3)*3+(j/3)].add(board[i][j])
        cop = set([chr(ord("1")+item) for item in range(9)])
        for i in range(9):
            row[i] = row[i].symmetric_difference(cop)
            col[i] = col[i].symmetric_difference(cop)
            sub[i] = sub[i].symmetric_difference(cop)
        return (row, col, sub)
    
    def solveSudoku(self, board):
        sets = self.createSets(board)
        self.solve(board, sets, 0)
        return board

board = [list("53..7...."),
         list("6..195..."),
         list(".98....6."),
         list("8...6...3"),
         list("4..8.3..1"),
         list("7...2...6"),
         list(".6....28."),
         list("...419..5"),
         list("....8..79")
        ]
s = Solution()
s.solveSudoku(board)
for item in board:
    print item


#List.prettyPrint(head)
#Tree.prettyPrint(root)

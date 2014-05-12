#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
Time Complexity:
Result: AC
'''

class Solution:
    def check(self, li):
        new_li = filter(lambda x: x!= ".", li)
        if len(set(new_li)) == len(new_li):
            return True
        return False
    
    def isValidSudoku(self, board):
        for item in board:
            if not self.check(item):
                return False
        for i in range(9):
            li = []
            for j in range(9):
                li.append(board[j][i])
            if not self.check(li):
                return False
        for i in range(3):
            for j in range(3):
                li = []
                for z in range(3):
                    li.extend(board[i*3+z][j*3: j*3+3])
                if not self.check(li):
                    return False
        return True


s = Solution()
print s.isValidSudoku([".87654321","2........","3........","4........","5........","6........","7........","8........","9........"])
print s.isValidSudoku(["....5..1.",".4.3.....",".....3..1","8......2.","..2.7....",".15......",".....2...",".2.9.....","..4......"])

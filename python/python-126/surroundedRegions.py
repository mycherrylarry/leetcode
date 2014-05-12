#!/usr/bin/env python

'''
Description:
    1. Setting two token flags: G and B which stand for Gray and Black
    2. Set flag surrounded = True.
    3. Traverse the board, if current item "O", start BFS and set every
       element that is "O" as G. If certain "O" is not surrounded by "X",
       set surrounded = False.
    4. If surrounded == True, start BFS and set all the "G"s as "B".
    5. Re-tranverse the board, set "G" as "O", and "B" as "X"
Time Complexity: O(n*n)
Result: AC
'''

class Solution:
    def bfs(self, board, pos, sourceTag, targetTag):
        direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        h = len(board)
        w = len(board[0])
        surrounded = True
        queue = []
        queue.append(pos)
        while len(queue) != 0:
            pos = queue.pop()
            i, j = pos
            board[i][j] = targetTag
            # If "O" is not surrounded by "X", then "O" must at the edge of borders.
            # We can prove it.
            if (i in (0, h-1)) or (j in (0, w-1)):
                surrounded = False
            for x1, y1 in direction:
                if (0 <= (i+x1) < h) and (0 <= (j+y1) < w):
                    if board[i+x1][j+y1] == sourceTag:
                        queue.append([i+x1, j+y1])
        return surrounded
    
    def solve(self, board):
        h = len(board)
        if h == 0: return board
        w = len(board[0])
        if w == 0: return board
        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    # Set "O" to "G"
                    surrounded = self.bfs(board, (i, j), "O", "G")
                    if surrounded:
                        # If is surrounded by "X", set "G" to "B"
                        self.bfs(board, (i,j), "G", "B")
        # Set "G" to "O" and "B" to "X"
        for i in range(h):
            for j in range(w):
                if board[i][j] == "G":
                    board[i][j] = "O"
                elif board[i][j] == "B":
                    board[i][j] = "X"
        return board

    
board = [list('XXXX'), list('XOOX'), list('XXOX'), list('XOXX')]
board = [list('XXXXO'), list('XXOOX'), list('OXOOX'), list('OXOOX')]
s = Solution()
print s.solve(board)


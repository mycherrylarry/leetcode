#!/usr/bin/env python
from unittest import *

'''
needs practice
Description: DP
    pay attention to initiation:

  \ $ a b b a
  $ 1 1 1 1 1
  a 0 1 1 1 2
  b 0 0 1 2 2
  a 0 0 0 0 2

Result: AC
'''
class Solution:
    def numDistinct(self, S, T):
        w, h = len(S), len(T)
        if h == 0: return 1
        if w == 0: return 0
        route = [[0]*(w+1) for i in range(h+1)]
        for j in range(w+1):
            route[0][j] = 1
        for i in range(h):
            for j in range(w):
                if T[i] == S[j]:
                    route[i+1][j+1] = route[i][j] + route[i+1][j]
                else:
                    route[i+1][j+1] = route[i+1][j]
        return route[h][w]


print  numDistinct("rabbbit", "rabbit")


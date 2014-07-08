#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
    Dynamic Programming
Solution:
Time Complexity:
Space Complexity:
Result: Accepted
Note:
    Pay attention to edge cases! Very important
'''

class Solution:
    # @return an integer
    def minDistance(self, word1, word2):
        n1, n2 = len(word1), len(word2)
        route = [[0]*(n1+1) for i in range(n2+1)]
        for i in range(n1+1):
            route[0][i] = i
        for i in range(n2+1):
            route[i][0] = i
        for i in range(1, n2+1):
            for j in range(1, n1+1):
                temp = route[i-1][j-1]
                if word1[j-1] != word2[i-1]:
                    temp += 1
                route[i][j] = min(route[i-1][j] +1, route[i][j-1] + 1, temp)

        return route[n2][n1]

s = Solution()
print s.minDistance('abc', 'abd')
print s.minDistance('abc', 'abdcd')
#List.prettyPrint(head)
#Tree.prettyPrint(root)

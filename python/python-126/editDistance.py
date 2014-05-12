#!/usr/bin/env python

'''
Result: AC
'''
class Solution:
    def minDistance(self, word1, word2):
        l1 = len(word1)
        l2 = len(word2)
        route = [[0]* (l2+1) for item in range(l1+1)]
        for i in range(l1+1):
            route[i][0] = i
        for j in range(l2+1):
            route[0][j] = j
        for i in range(l1):
            for j in range(l2):
                tmp = route[i][j]
                if word1[i] != word2[j]:
                    tmp += 1
                route[i+1][j+1] = min(route[i+1][j]+1, route[i][j+1]+1, tmp)
        return route[l1][l2]

s = Solution()
print s.minDistance("abcd", "bcd")

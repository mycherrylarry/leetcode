#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

    For example,
    Given:
    s1 = "aabcc",
    s2 = "dbbca",

    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.
Method: Dynamic Programming
Resolution:
    * route[i][j] == True means the first ith elements of s1 and first jth elements of
      s2 can create the first (i+j)th elements of s3
    * thus: route[i][j] = (route[i-1][j] and s1[i] == s3[i+j]) or (route[i][j-1] and s2[j] == s3[i+j])
Time Complexity: O(N*M)
Space Complexity: O(N*M)
Result: AC
Note: needs practicing
'''

class Solution:
    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        l1, l2, l3 = len(s1), len(s2), len(s3)
        if (l1+l2) != l3: return False
        route = [[False]*(l2+1) for i in range(l1+1)]
        route[0][0] = True
        # setup initial values of s2:
        for i in range(l2):
            route[0][i+1] = route[0][i] and s2[i] == s3[i]
        # setup initial values of s1:
        for i in range(l1):
            route[i+1][0] = route[i][0] and s1[i] == s3[i]
        # setup route[i][j]
        for i in range(l1):
            for j in range(l2):
                route[i+1][j+1] = (route[i][j+1] and s1[i] == s3[i+j+1]) or (route[i+1][j] and s2[j] == s3[i+j+1])
        return route[l1][l2]

s = Solution()
s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s3 = "aadbbbaccc"
print s.isInterleave(s1, s2, s3)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

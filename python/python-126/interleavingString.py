#!/usr/bin/env python
class Solution:
    # DP
    def isInterleave(self, s1, s2, s3):
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l3 != (l1+l2):
            return False
        route = [[0]*(l1+1) for i in range(l2+1)]
        route[0][0] = True
        for i in range(l1):
            route[0][i+1] = route[0][i] and (s1[i] == s3[i])
        for i in range(l2):
            route[i+1][0] = route[i][0] and (s2[i] == s3[i])
        for i in range(l2):
            for j in range(l1):
                route[i+1][j+1] = (route[i][j+1] and (s2[i] == s3[i+j+1])) or (route[i+1][j] and (s1[j] == s3[i+j+1]))
        return route[l2][l1]

s = Solution()
print s.isInterleave("abc", "dd", "abdcd")




#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a string S and a string T, count the number of distinct subsequences of T in S.
Method: DP
Resolution: route[i][j] = 
                if S[i] == T[j]: 
                    route[i-1][j-1] + route[i-1][j]
Time Complexity:
Space Complexity:
Result:
Note:
'''

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

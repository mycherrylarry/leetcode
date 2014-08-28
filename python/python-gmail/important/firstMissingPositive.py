#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    def firstMissingPositive(self, A):
        for i in range(len(A)):
            if A[i] != i + 1:
                tmp = A[i]
                while 0 < tmp <= len(A) and A[tmp-1] != tmp:
                    t = A[tmp-1]
                    A[tmp-1] = tmp
                    tmp = t
        for i in range(len(A)):
            if A[i] != i + 1:
                return i + 1
        return len(A) + 1



#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

    For example,
    Given n = 3, there are a total of 5 unique BST's.

Resolution:
    f(0) = 1
    f(1) = 1
    f(2) = f(0)*f(1) + f(1)*f(0)
    f(3) = f(0)*f(2) + f(1)*f(1) + f(2)*f(0)
    f(4) = f(0)*f(3) + ....
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @return an integer
    def numTrees(self, n):
        if n in (0,1): return 1
        result = [1]*(n+1)
        for i in range(2, n+1):
            tmp = 0
            for j in range(i):
                tmp += result[j]*result[i-j-1]
            result[i] = tmp
        return result[n]



s = Solution()
print s.numTrees(3)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

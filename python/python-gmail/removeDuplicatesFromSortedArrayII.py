#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Follow up for "Remove Duplicates":
    What if duplicates are allowed at most twice?

    For example,
    Given sorted array A = [1,1,1,2,2,3],

    Your function should return length = 5, and A is now [1,1,2,2,3].
Method:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
    * pay attention to details
'''

class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) in (0, 1, 2): return len(A)
        offset = 0
        flag = A[0]
        tag = False
        for i in range(1, len(A)):
            A[i-offset] = A[i]
            if A[i] == flag:
                if tag:
                    offset += 1
                tag = True
            else:
                flag = A[i]
                tag = False
        return len(A) - offset


s = Solution()
A = [1,1,1,2,2,3]
A = [1,1,1,1,3,3]
A = [1,1,1,2]
print s.removeDuplicates(A)
print A
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given two sorted integer arrays A and B, merge B into A as one sorted array.

    Note:
    You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
Method:
Resolution:
    * A's size is greater than m, so we can move A's elements to the end of A, and
      use two pointers a and b to store the elements into A
Time Complexity: O(2*M+N)
Space Complexity: O(1)
Result: AC
Note:
    * pay attention to the edge cases. don't consider this
    * there's a better solution with O(M+N): hint merge from the end of A
'''

class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        # what about m == 0?
        if n == 0: return
        # move A's elements to end
        for i in range(m)[::-1]:
            A[i+n] = A[i]
        # a is current position of A, b is current position of B, and k is the merged array
        a, b, k = n, 0, 0
        while a< (m+n) and b< n:
            if A[a] < B[b]:
                A[k] = A[a]
                a += 1
            else:
                A[k] = B[b]
                b += 1
            k += 1
        if a== (m+n):
            while b <n:
                A[k] = B[b]
                b += 1
                k += 1
        return A

#s = Solution()
A = [2,4,6,9,0,0,0]
B = [1,3,10]
s = Solution()
print s.merge(A, 4, B, 3)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

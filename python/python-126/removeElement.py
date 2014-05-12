#!/usr/bin/env python
class Solution:

    def removeElement(self, A, elem):
        index = 0
        while index < len(A):
            if A[index] == elem:
                del(A[index])
            else:
                index += 1
        return len(A)

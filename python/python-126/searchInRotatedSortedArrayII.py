#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    1. Duplication allowed
Time Complexity:
Result: AC
'''

def binarySearch(A, target, i, j):
    if i >= j: return False
    mid = (i+j)/2
    if A[mid] == target:
        return True
    elif A[mid] < target:
        if A[j-1] < target and A[i] >= A[mid]:
            return binarySearch(A, target, i, mid) or binarySearch(A, target, mid+1, j)
        else:
            return binarySearch(A, target, mid+1, j)
    else:
        if A[i] > target and A[j-1] <= A[mid]:
            return binarySearch(A, target, i, mid) or binarySearch(A, target, mid+1, j)
        else:
            return binarySearch(A, target, i, mid)




class Solution:

    def binarySearch(self, A, target, i, j):
        if i >= j: return False
        mid = (i+j)/2
        if A[mid] == target:
            return True
        elif A[mid] < target:
            if A[j-1] < target and A[i] >= A[mid]:
                return self.binarySearch(A, target, i, mid) or self.binarySearch(A, target, mid+1, j)
            else:
                return self.binarySearch(A, target, mid+1, j)
        else:
            if A[i] > target and A[j-1] <= A[mid]:
                return self.binarySearch(A, target, i, mid) or self.binarySearch(A, target, mid+1, j)
            else:
                return self.binarySearch(A, target, i, mid)

    def search(self, A, target):
        return self.binarySearch(A, target, 0, len(A))

s = Solution()
A = [3,3,3,4,1,1,2,3]
print s.search(A, 2)
print s.search([1,3,1,1,1], 3)
print s.search([1,1,1,3,1], 3)

#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    Binary search
Time Complexity:
Result: AC
'''

class Solution:
    def binarySearch(self, li, target):
        i, j = 0, len(li)
        while i < j:
            mid = (i+j)/2
            if li[mid] == target:
                return True
            elif li[mid] < target:
                i = mid + 1
            else:
                j = mid
        return False
    
    def searchMatrix(self, matrix, target):
        h = len(matrix)
        if h == 0: return False
        w = len(matrix[0])
        if w == 0: return False
        i = 0
        while i< (h-1) and matrix[i+1][0] <= target:
            i += 1
        return self.binarySearch(matrix[i], target)

s = Solution()
print s.searchMatrix([
      [1,   3,  5,  7],
        [10, 11, 16, 20],
          [23, 30, 34, 50]
          ], 20)




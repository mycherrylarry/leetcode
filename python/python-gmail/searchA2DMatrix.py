#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties.
Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # return search col
    def binarySearchCol(self, li, target):
        i, j = 0, len(li)
        while(i < j):
            mid = (i+j)/2
            if li[mid] == target:
                return mid
            elif li[mid] < target:
                i = mid + 1
            else:
                j = mid
        if i == len(li):
            i = len(li)-1
        return i

    # return existance
    def binarySearchRow(self, li, target):
        i, j = 0, len(li)
        while(i < j):
            mid = (i+j)/2
            if li[mid] == target:
                return True
            elif li[mid] < target:
                i = mid + 1
            else:
                j = mid
        return False

    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        height = len(matrix)
        if height == 0: return False
        width  = len(matrix[0])
        if width == 0: return False
        row = self.binarySearchCol(map(lambda x: x[-1], matrix), target)
        return self.binarySearchRow(matrix[row], target)

s = Solution()
matrix = [
          [1,   3,  5,  7],
            [10, 11, 16, 20],
              [23, 30, 34, 50]
              ]
print s.searchMatrix(matrix, 3)
print s.searchMatrix(matrix, 20)
print s.searchMatrix(matrix, 7)
print s.searchMatrix(matrix, 50)
print s.searchMatrix(matrix, 51)
print s.searchMatrix(matrix, 0)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

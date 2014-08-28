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
    def spiralOrder(self, matrix):
        result = []
        h = len(matrix)
        if h == 0: return result
        w = len(matrix[0])
        if w == 0: return result

        top, bottom, left, right = 0, h-1, 0, w-1
        while top < bottom and left < right:
            for i in range(left, right):
                result.append(matrix[top][i])
            for i in range(top, bottom):
                result.append(matrix[i][right])
            for i in range(left+1, right+1)[::-1]:
                result.append(matrix[bottom][i])
            for i in range(top+1, bottom+1)[::-1]:
                result.append(matrix[i][left])
            top += 1
            bottom -= 1
            left += 1
            right -= 1

        if left == right and top == bottom:
            result.append(matrix[top][left])
        elif left == right:
            for i in range(top, bottom+1):
                result.append(matrix[i][left])
        elif top == bottom:
            for i in range(left, right+1):
                result.append(matrix[top][i])

        return result
                

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given an array of integers, every element appears three times except for one.
    Find that single one.

    Note:
    Your algorithm should have a linear runtime complexity.
    Could you implement it without using extra memory?
Description:
Time Complexity:
Space Complexity:
Result: AC
'''
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        result = [0]*65
        for item in A:
            if item < 0:
                result[0] = (result[0] + 1)%3
                item = -item
            i = 64
            while item != 0:
                result[i] = (result[i] + item%2)%3
                item = item >> 1
                i -= 1
        number = reduce(lambda x,y: x*2+y, result[1:])
        return result[0] != 0 and -number or number

                            

s = Solution()
print s.singleNumber([1,1,-1112,1,2,2,2,-1112,-1112, 21])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

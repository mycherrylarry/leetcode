#!/usr/bin/env python
from unittest import *

'''
Description:
    1. Tranverse the list
    2. Do twoSum with the rest of list
    3. Skip duplications
Time Complexity:
Result: Time limit exceed
'''

class Solution:
    def twoSum(self, li, target):
        result = []
        n = len(li)
        if n in (0, 1): return result
        i, j = 0, n-1
        while i < j:
            if li[i] + li[j] == target:
                result.append([li[i], li[j]])
                # skip duplicates
                while i+1 < n and li[i+1] == li[i]: i += 1
                i += 1
                while j>0 and li[j-1] == li[j]: j -= 1
                j -= 1
            elif li[i] + li[j] < target:
                i += 1
            else:
                j -= 1
        return result
    
    def threeSum(self, num):
        num.sort()
        result = []
        for i in range(len(num)):
            # skip duplicates
            if i>0 and  num[i] == num[i-1]: continue
            subResult = self.twoSum(num[i:], 0-num[i])
            subResult = [[num[i]] + item for item in subResult]
            if subResult != []:
                result += subResult
        return result


s = Solution()
#print s.threeSum([-1,0,1,2,-1,-4])
print s.threeSum([7,-1,14,-12,-8,7,2,-15,8,8,-8,-14,-4,-5,7,9,11,-4,-15,-6,1,-14,4,3,10,-5,2,1,6,11,2,-2,-5,-7,-6,2,-15,11,-6,8,-4,2,1,-1,4,-6,-15,1,5,-15,10,14,9,-8,-6,4,-6,11,12,-15,7,-1,-9,9,-1,0,-4,-1,-12,-2,14,-9,7,0,-3,-4,1,-2,12,14,-10,0,5,14,-1,14,3,8,10,-8,8,-5,-2,6,-11,12,13,-7,-12,8,6,-13,14,-2,-5,-11,1,3,-6])

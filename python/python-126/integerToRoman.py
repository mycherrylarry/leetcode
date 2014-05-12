#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
Time Complexity:
Result: AC
'''

class Solution:

    def intToRoman(self, num):
        result = []
        mp = {1:"I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        index = 10
        n = num
        while n!= 0:
            remainder = n%10
            n = n/10
            if remainder == 0:
                index *= 10
                continue
            # remainder 
            elif remainder in range(1, 4):
                for i in range(remainder):
                    result.insert(0, mp[index/10])
            elif remainder == 4:
                result.insert(0, mp[index/2])
                result.insert(0, mp[index/10])
            elif remainder == 5:
                result.insert(0, mp[index/2])
            elif remainder in range(6, 9):
                for i in range(remainder%5):
                    result.insert(0, mp[index/10])
                result.insert(0, mp[index/2])
            else:
                result.insert(0, mp[index])
                result.insert(0, mp[index/10])
            index *= 10
        return "".join(result)
        
    
s = Solution()
#print s.intToRoman(2016)
print s.intToRoman(4)
print s.intToRoman(40)



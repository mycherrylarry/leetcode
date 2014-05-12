#!/usr/bin/env python
from unittest import *
#print root

'''
Description: simple
Time Complexity:
Result: AC
'''

class Solution:

    def romanToInt(self, s):
        if len(s) == 0: return 0
        s = s.upper()
        mp = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        pre = {"V": "I", "X": "I", "L": "X", "C":"X", "D":"C", "M":"C"}
        result = 0
        i = len(s)-1
        while i>=0:
            if pre.has_key(s[i]):
                if i >0 and s[i-1] == pre[s[i]]:
                    result += mp[s[i]]
                    result -= mp[s[i-1]]
                    i -= 2
                    continue
            result += mp[s[i]]
            i -= 1
        return result

 
s = Solution()
print s.romanToInt("MCMXCII")
print s.romanToInt("MCMXCVIII")
print s.romanToInt("MMXVI")




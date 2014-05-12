#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    Complex!!!!!
Time Complexity:
Result: AC
'''

class Solution:

    def convert(self, li):
        if len(li) == 0: return 0
        result = []
        for item in li:
            if ord(item)-ord("0") < 0 or ord(item)-ord("0") > 9:
                break
            result.append(ord(item)-ord("0"))
        if len(result) == 0:
            return 0
        result = reduce(lambda x, y: x*10 + y, result)
        return result
    
    def atoi(self, str):
        li = str.strip()
        if len(li) == 0: return 0
        if li[0] == "-":
            result = self.convert(li[1:])
            if result != 0:
                if result > 2147483648:
                    return -2147483648
                else:
                    return -self.convert(li[1:])
            else:
                return result
        if li[0] == "+":
            result = self.convert(li[1:])
            if result > 2147483647:
                return 2147483647
            else:
                return result
        result = self.convert(li)
        if result > 2147483647:
            return 2147483647
        else:
            return result


s = Solution()

print s.atoi("123")
print s.atoi("")
print s.atoi("-123")
print s.atoi("123")
print s.atoi("+123")
print s.atoi("-1")
print s.atoi("   -0012a42")
print s.atoi("2147483648")


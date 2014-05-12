#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
"9876" * "987654321" = 
"0000" * "00000" =
"0" * "1" = 
Description:
    1. keep result reversed
Time Complexity:
Result: AC
'''

class Solution:

    def multiply(self, num1, num2):
        if num1 == "" or num2 == "": return ""
        result = [0]*(len(num1)+len(num2))
        li1 = [ord(item)-ord('0') for item in num1[::-1]]
        li2 = [ord(item)-ord('0') for item in num2[::-1]]
        for i in range(len(li1)):
            for j in range(len(li2)):
                result[i+j] += li1[i]*li2[j]
        remainder = 0
        i = 0
        while i < len(result):
            tmp = remainder + result[i]
            remainder = tmp/10
            result[i] = tmp%10
            i += 1
        while len(result) > 0 and result[-1] == 0:
            result.pop()
        if len(result) == 0: return "0"
        else: return "".join(map(lambda x: chr(x+ord("0")), result[::-1]))

            
s = Solution()
print s.multiply("123", "45555")
print s.multiply("000", "00")
print s.multiply("111", "00")
print s.multiply("111", "11")
print s.multiply("9999999", "99")


#List.prettyPrint(head)
#Tree.prettyPrint(root)

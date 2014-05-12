#!/usr/bin/env python
from unittest import *

'''
Description:
    a = "11"
    b = "1"
    return "100"
Time Complexity:
Result: AC
'''

class Solution:
    def addBinary(self, a, b):
        na = reduce(lambda x,y: x*2 + y, [int(i) for i in list(a)])
        nb = reduce(lambda x,y: x*2 + y, [int(i) for i in list(b)])
        nc = na + nb
        result = []
        if nc == 0: return "0"
        while nc != 0:
            result.insert(0, nc%2)
            nc /= 2
        return "".join([str(item) for item in result])

print addBinary("0", "0")




#!/usr/bin/env python
class Solution:
    def plusOne(self, digits):
        x = reduce(lambda x,y: x*10+y, digits)
        x += 1
        return [int(i) for i in list(str(x))]
    


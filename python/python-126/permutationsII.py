#!/usr/bin/env python

class Solution:
    def permute(self, num):
        l = len(num)
        if l == 0: return num
        if l == 1: return [num]
        x = num[0]
        tmp = self.permute(num[1:])
        result = set()
        for item in tmp:
            for i in range(len(item)+1):
                s = [y for y in item]
                s.insert(i,x)
                result.add(tuple(s))
        return [list(item) for item in list(result)]
    
s = Solution()
print s.permute([1,1,2])

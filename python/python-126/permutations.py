#!/usr/bin/env python

class Solution:
    def permute(self, num):
        l = len(num)
        if l == 0: return num
        if l == 1: return [num]
        x = num[0]
        tmp = self.permute(num[1:])
        result = []
        for item in tmp:
            for i in range(len(item)+1):
                s = [y for y in item]
                s.insert(i,x)
                result.append(s)
        return result
    
s = Solution()
print s.permute(range(4))

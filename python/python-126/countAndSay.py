#!/usr/bin/env python
'''
result : AC
'''
class Solution:
    def genNext(self, s):
        if len(s) == 1:
            return '1'+s
        result = []
        pre = 0
        p = 1
        while p != len(s):
            while p != len(s) and s[p] == s[pre]:
                p += 1
            result.append(str(p-pre))
            result.append(s[pre])
            pre = p
        return ''.join(result)
    
    def countAndSay(self, n):
        if n == 1: return "1"
        route =['1']
        for i in range(n-1):
            x = self.genNext(route[i])
            route.append(x)
        return route[-1]

s = Solution()
print s.countAndSay(7)

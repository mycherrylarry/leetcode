#!/usr/bin/env python
class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        t = []
        for item in s:
            if (ord(item) in range(ord('a'), ord('z')+1)) or (ord(item) in range(ord('0'), ord('9')+1)):
                t.append(item)
        return t == t[::-1]

s = Solution()
print s.isPalindrome("adfbf,dA,a")


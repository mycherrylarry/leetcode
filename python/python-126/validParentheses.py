#!/usr/bin/env python

class Solution:
    def isValid(self, s):
        t = ['(', '{', '[']
        mp = {')':'(', '}':'{', ']':'['}
        stack = []
        for item in s:
            if item in t:
                stack.append(item)
            else:
                if len(stack) == 0 or stack[-1] != mp[item]:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
s = Solution()
print s.isValid("(())")
print s.isValid("([)]")
print s.isValid("{([])}")
print s.isValid("{{{")
print s.isValid("{{{}}}")



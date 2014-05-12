#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
    1. check from back
Time Complexity:
Result:
'''

class Solution:
    def isMatch(self, s, p):
        if len(s) == 0 and len(p) == 0: return True
        if len(p) == 0: return False
        if len(s) == 0:
            if len(p) < 2 or p[-1]!= "*":
                return False
            return self.isMatch(s, p[:-2])
        if p[-1] != "*" and p[-1] != ".":
            if s[-1] != p[-1]:
                return False
            else:
                return self.isMatch(s[:-1], p[:-1])
        if p[-1] == ".":
            return self.isMatch(s[:-1], p[:-1])
        if p[-1] == "*":
            if len(p) < 2: return False
            if p[-2] == ".":
                # todo
                return True
            i = len(s)-1
            while i >= 0 and s[i] == p[-2]:
                i -= 1
                print i, s, p
            return self.isMatch(s[:i+1], p[:-2])
s = Solution()
print s.isMatch("aaa", "ab*a*c*a")


#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
    1. recursion
Time Complexity:
Result: AC
with out line 21 to 28: Time limit exceeded
'''

class Solution:
    def isScramble(self, s1, s2):
        if len(s1) != len(s2): return False
        n = len(s1)
        if n == 0: return True
        if n == 1 and s1 == s2: return True
        A = [0]*26
        for item in s1:
            A[ord(item)-ord("a")] += 1
        for item in s2:
            A[ord(item)-ord("a")] -=1
        for item in range(26):
            if A[item] != 0:
                return False
        for i in range(1, n):
            left_a = self.isScramble(s1[:i], s2[:i])
            right_a = self.isScramble(s1[i:], s2[i:])
            if left_a and right_a:
                return True
            left_b = self.isScramble(s1[:i], s2[-i:])
            right_b = self.isScramble(s1[i:], s2[:-i])
            if left_b and right_b:
                return True
        return False

s = Solution()
print s.isScramble("rgtae", "great")
print s.isScramble("abcdefghij", "efghijcadb")


#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem: KMP
    Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
Method: KMP
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
    * there's problem in the question's description
    * this problem means to return the left string from the hit point
'''

class Solution:
    def createKmpTable(self, needle):
        n = len(needle)
        if n == 0: return []
        table = [0]*n
        table[0] = -1
        j = 0
        for i in range(2, n):
            if needle[i-1] == needle[j]:
                table[i] = table[i-1] + 1
                j += 1
            else:
                j = 0
                if needle[i-1] == needle[j]:
                    table[i] = 1
                    j += 1
                else:
                    table[i] = 0
        return table

    def check(self, haystack, needle):
        table = self.createKmpTable(needle)
        i, j = 0, 0
        while i < len(haystack):
            if j == -1:
                i += 1
                j = 0
                continue
            if j == len(needle):
                return i-j
            if haystack[i] == needle[j]:
                j += 1
                i += 1
            else:
                j = table[j]
        if j == len(needle):
            return i-j
        return -1

    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        index = self.check(haystack, needle)
        if index != -1:
            return haystack[index:]
        return None
                                

s = Solution()
print s.strStr("babbcabdaaa","abcabdaa")
print s.strStr("mississippi", "a")
print s.strStr("a", "")
print s.strStr("aaa", "a")
#List.prettyPrint(head)
#Tree.prettyPrint(root)

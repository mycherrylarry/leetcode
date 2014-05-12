#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    s = "leetcode",
    dict = ["leet", "code"].

    Return true because "leetcode" can be segmented as "leet code".
Description:
Time Complexity:
Space Complexity:
Result:
'''
class Solution:

    def wordPart(self, s, i, j, dict, cache):
        if (i, j) in cache:
            return cache[(i, j)]
        if s[i:j] in dict:
            cache[(i, j)] = True
            return True
        for k in xrange(i+1, j):
            left = self.wordPart(s, i, k, dict, cache)
            right = self.wordPart(s, k, j, dict, cache)
            if left and right:
                cache[(i,j)] = True
                return True
        cache[(i, j)] = False
        return False
    
    def wordBreak(self, s, dict):
        return self.wordPart(s, 0, len(s), dict, {})

s = Solution()
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print s.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", ["a"])
print s.wordBreak("aaaaaaaaaaaaaaaaaaa", ["a", "aa"])

#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from unittest import *

'''
Description:
    1. Create SuffixTree of s
    2. Find the longest prefixes of s[::-1]'s substrings
Time Complexity: O(N*N)
Result: Memory limit exceeded
'''

class TrieNode:
    def __init__(self, c, val = None):
        self.c = c
        self.val = val
        self.children = {}

class SuffixTree:
    def __init__(self):
        self.root = TrieNode(None)

    # insert word to a suffixtree
    def insert(self, word):
        p = self.root
        if len(word) == 0:
            p.children['$'] = TrieNode('$')
        for i in range(len(word)):
            if not p.children.has_key(word[i]):
                p.children[word[i]] = TrieNode(word[i])
            p = p.children[word[i]]
            p.val = word[:i+1]

    def create(self, s):
        for i in range(len(s)+1):
            self.insert(s[i:])

class Solution:
    def findLongestPrefix(self, root, s):
        '''find the longest prefix length of s in a given suffix tree
        '''
        p = root
        i = 0
        while i < len(s) and p.children.has_key(s[i]):
            p = p.children[s[i]]
            i += 1
        return i
    
    
    def longestPalindrome(self, s):
        if len(s) in (0, 1): return len(s)
        suffixTree = SuffixTree()
        suffixTree.create(s)
        root = suffixTree.root
        r_s = s[::-1] # reversed string
        result = 0
        for i in range(len(r_s)+1):
            result = max(self.findLongestPrefix(root, r_s[i:]), result)
        return result



s = Solution()
print s.longestPalindrome("abcbca")
print s.longestPalindrome("abba")
print s.longestPalindrome("abb")
print s.longestPalindrome("ab")
print s.longestPalindrome("")

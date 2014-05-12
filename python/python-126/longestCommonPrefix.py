#!/usr/bin/env python

# Tire

class TireNode:
    def __init__(self, c, val = None):
        self.c = c
        self.val = val
        self.children = {}

class Solution:

    def addNode(self, root, s):
        i = 0
        p = root
        while i < len(s):
            if p.children.has_key(s[i]):
                p = p.children[s[i]]
                i += 1
            else:
                break
        while i < len(s):
            tmp = TireNode(s[i])
            p.children[s[i]] = tmp
            p = tmp
            i += 1
        p.val = s
    
    
    def longestCommonPrefix(self, strs):
        root = TireNode(None)
        for item in strs:
            self.addNode(root, item)
        result = []
        p = root
        while len(p.children) == 1 and p.val == None:
            p = p.children.values()[0]
            result.append(p.c)
        return "".join(result)

s = Solution()
print s.longestCommonPrefix(["abcd","abcd","abcdefg"])



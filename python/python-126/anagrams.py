#!/usr/bin/env python
from unittest import *

'''
Description:
    Simple Question
    1. sort each word
    2. use hash
Time Complexity:
Result: AC
'''

class Solution:
    def anagrams(self, strs):
        mp = {}
        for i in range(len(strs)):
            new_word = "".join(sorted(strs[i]))
            if not mp.has_key(new_word):
                mp[new_word] = [i]
            else:
                mp[new_word].append(i)
        result = []
        for value in mp.values():
            if len(value) > 1:
                result.extend([strs[item] for item in value])
        return result

s = Solution()
print s.anagrams(["abc", "cdb", "cab", "cba", "de", "ed", "a"])




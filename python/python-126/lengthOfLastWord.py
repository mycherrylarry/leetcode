#!/usr/bin/env python
class Solution:
    def lengthOfLastWord(self, s):
        li = s.plit()
        if len(li) == 0:
            return 0
        return len(li[-1])

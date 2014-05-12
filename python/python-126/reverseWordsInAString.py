#!/usr/bin/env python
from unittest import *

'''
Description:
    Given s = "the sky is blue",
    return "blue is sky the".
Time Complexity:
Result:
'''
class Solution:
    def reverseWords(self, s):
        result = []
        tmp = []
        for item in s:
            if item == ' ':
                result.extend(tmp)
                tmp = []
                result.append(item)
            else:
                tmp.insert(0, item)
        result.extend(tmp)
        return "".join(result[::-1])

s = Solution()
print s.reverseWords("a    abcde fg  ")
print s.reverseWords("blue is sky the")


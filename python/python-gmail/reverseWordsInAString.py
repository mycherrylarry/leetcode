#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note: Ask requirements as detailed as possible
'''

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        li = s[::-1].split()
        for i in range(len(li)):
            li[i] = li[i][::-1]
        return " ".join(li)

s = Solution()
print s.reverseWords(" the sky is  bule ")
#List.prettyPrint(head)
#Tree.prettyPrint(root)

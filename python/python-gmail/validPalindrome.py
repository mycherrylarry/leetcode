#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    For example,
    "A man, a plan, a canal: Panama" is a palindrome.
    "race a car" is not a palindrome.

    Note:
    Have you consider that the string might be empty? This is a good question to ask during an interview.

    For the purpose of this problem, we define empty string as valid palindrome.

Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
    * empty array
    * what are alphanumeric characters?
    * ask questions
'''

class Solution:
    def check(self, c):
        if (0<= ord(c) - ord("a") <26) or (0<= ord(c) - ord("A") < 26) or (0<= ord(c) - ord("0") <10):
            return True
        return False

    def preprocess(self, s):
        return [item.lower() for item in filter(self.check, str(s))]

    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        if len(s) == 0: return True
        route = self.preprocess(s)
        if len(route) == 0: return True
        i, j = 0, len(route)-1
        while i <=j:
            if route[i] == route[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

s = Solution()
print s.isPalindrome("A man, a plan, a canal: Panama")
print s.isPalindrome("1a2")
#List.prettyPrint(head)
#Tree.prettyPrint(root)

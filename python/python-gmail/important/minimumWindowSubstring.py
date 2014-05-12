#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

    For example,
    S = "ADOBECODEBANC"
    T = "ABC"
    Minimum window is "BANC"
Solution:
    * This problem has a one-pass solution. To find out the solution, first, we must guarantee
      that len(T) is not bigger than len(S). Second, we provide two pointers: 'front' and 'end'
      to indicate the enclosing interval of S that contains T. 
    * We need a calculator named 'length' to calculate the length of characters we have already
      found in S
    * We need two HashMaps: 'need_to_find' and 'already_found' to represent the items that
      we need to find and already found
    * After the condition of 'length' is fullfilled , which means that we've already found all
      characters of T in S, we should shrink the interval of 'front' and 'end' to find the 
      satisfaction with minimum length of interval.
Time Complexity: O(N)
Space Complexity: O(N)
Result: AC
Note:
    * needs practise
'''

class Solution:
    def createNeedToFind(self, T, mp):
        for c in T:
            if mp.has_key(c):
                mp[c] += 1
            else:
                mp[c] = 1

    # @return a string
    def minWindow(self, S, T):
        if len(S) < len(T) or len(T) == 0: return ""
        need_to_find = {}
        self.createNeedToFind(T, need_to_find)
        already_found = {}
        for key in need_to_find.keys():
            already_found[key] = 0
        length = 0
        front, end = 0, 0
        result = None
        for i in range(len(S)):
            if need_to_find.has_key(S[i]):
                already_found[S[i]] += 1
                if already_found[S[i]] <= need_to_find[S[i]]:
                    length += 1
                end = i
                if length == len(T):
                    # shrink
                    while front <= end:
                        if need_to_find.has_key(S[front]):
                            if already_found[S[front]] > need_to_find[S[front]]:
                                already_found[S[front]] -= 1
                                front += 1
                            else:
                                break
                        else:
                            front += 1
                    if result == None:
                        result = (front, end)
                    else:
                        f, e = result
                        if (end-front) < (e-f):
                            result = (front, end)
        if result == None:
            return ""
        f, e = result
        return S[f:e+1]

s = Solution()
print s.minWindow("ADOBECODEBANC", "ABC")
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Method: HashMap
Resolution:
    1. Initially create a map storing all elements of the array
    2. Delete elements of the map and calculate maximal
Time Complexity:
Space Complexity:
Result:
Note:
'''

class Solution:
    # @param num, a list of integer
    # @return a HashMap storing every element of num
    def createMap(self, num):
        mp = {}
        for item in num:
            mp[item] = 1
        return mp

    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        # edge case
        if len(num) in (0, 1): return len(num)
        mp = self.createMap(num)
        mx = 0
        for item in num:
            if mp.has_key(item):
                counter = 1
                del(mp[item])
                p = item-1
                while mp.has_key(p):
                    del(mp[p])
                    p -= 1
                    counter += 1
                p = item+1
                while mp.has_key(p):
                    del(mp[p])
                    p += 1
                    counter += 1
                mx = max(mx, counter)
        return mx

s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from unittest import *
#print root

'''
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).

Description:
    1. create a hashmap to store L (there may be duplicates)
    2. tranverse from the begining of S
Time Complexity: O(M*N)
Result: Time Limit Exceeded
'''

class Solution:

    def check(self, mp, route, S, L, item):
        if not mp.has_key(item): return False
        if not route.has_key(item):
            route[item] = 1
            return True
        if route[item] < mp[item]:
            route[item] += 1
            return True
        return False
    
    # @param result: the result
    # @param mp: hashmap to store origin L
    # @param route: hashmap to store current status
    # @param index: S's indexes index = [0...len(S)], start from 0
    # @param length: the length of current status
    
    def solve(self, result, mp, route, S, L, index, length, count=0):
        w = len(L[0])
        if length == len(L):
            result.append(index-(length*w))
            return
        if index + w >= len(S):
            return
        if self.check(mp, route, S, L, S[index:index+w]): 
            self.solve(result, mp, route, S, L, index+w, length+1, count+1)
    
    def createMap(self, L):
        mp = {}
        for item in L:
            if mp.has_key(item):
                mp[item] += 1
            else:
                mp[item] = 1
        return mp
    
    def findSubstring(self, S, L):
        result = []
        if len(L) == 0 or len(S) == 0: return result
        if len(L[0]) == 0: return result
        w = len(L[0])
        mp = self.createMap(L)
        for index in range(len(S) - len(L)*w + 1):
            route = {}
            self.solve(result, mp, route, S, L, index, 0)
        return result


s = Solution()
print s.findSubstring("barfoothefoobarman", ["foo", "bar"])
print s.findSubstring("ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababa", ["ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba","ab","ba"])

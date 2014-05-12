#!/usr/bin/env python

class Solution:
    def longestConsecutive(self, num):
        mp = {}
        maxlen = 0
        for item in num:
            mp[item] = 1
        while len(mp.keys()) != 0:
            l = 1
            tmp = mp.popitem()[0]
            p = tmp + 1
            while mp.has_key(p):
                mp.pop(p)
                l += 1
                p += 1
            p = tmp -1
            while mp.has_key(p):
                mp.pop(p)
                l += 1
                p -= 1
            maxlen = max(maxlen, l)
        return maxlen


s = Solution()
#print s.longestConsecutive([1,3,6,2,7,8,9,10,5,10,9])
#print s.longestConsecutive([0,0])
#print s.longestConsecutive([-3,2,8,5,1,7,-8,2,-8,-4,-1,6,-6,9,6,0,-7,4,5,-4,8,2,0,-2,-6,9,-4,-1])
#print s.longestConsecutive([0,0,0,1,1,1,2])
#print sorted([-3,2,8,5,1,7,-8,2,-8,-4,-1,6,-6,9,6,0,-7,4,5,-4,8,2,0,-2,-6,9,-4,-1])
#print s.longestConsecutive([-1,-2,0])
#print s.longestConsecutive([0, 1,2,3, -2, -8, -7, -6, -4, -3, -1])
print s.longestConsecutive([-9,-4,9,-7,0,7,3,-1,6,2,-2,8,-2,0,2,-7,-5,-2,6,-5,0,-8,8,1,0,6,8,-8,-1])
             

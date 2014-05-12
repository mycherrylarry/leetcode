#!/usr/bin/env python
class Solution:
    def twoSum(self, num, target):
        mp = {}
        for i in range(len(num)):
            y = num[i]
            if mp.has_key(y):
                mp[y] = mp[y]+[i]
            else:
                mp[y] = [i]
        for item in mp.keys():
            if mp.has_key(target-item):
                if target-item == item:
                    return (mp[item][0]+1, mp[item][1]+1)
                a = min(mp[item][0], mp[target-item][0])
                b = max(mp[item][0], mp[target-item][0])
                return (a+1, b+1)
    
s = Solution()
print s.twoSum([2, 7, 11, 15], 9)

print s.twoSum([0,4,3,0], 0)

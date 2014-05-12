#!/usr/bin/env python
class Solution:
    def quickSort(self, li):
        if len(li) in (0, 1): return li
        lesser = self.quickSort(filter(lambda x: x[0]<= li[-1][0], li[:-1]))
        bigger = self.quickSort(filter(lambda x: x[0]> li[-1][0], li[:-1]))
        return lesser + [li[-1]] + bigger
    
    def twoSum(self, num, target):
        li = []
        for i in range(len(num)):
            li.append((num[i], i+1))
        li = self.quickSort(li)
        i, j = 0, len(li)-1
        while i < j:
            if li[i][0] + li[j][0] == target:
                return (li[i][1], li[j][1])
            if li[i][0] + li[j][0] > target:
                j -= 1
            else:
                i += 1
        return (-1, -1)
    
s = Solution()
print s.twoSum([2, 7, 11, 15], 9)
print s.twoSum()


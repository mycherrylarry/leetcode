#!/usr/bin/env python
'''
Time Complexity: O(N)
Result:
'''
class Solution:

    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        if rowIndex == 1: return [1, 1]
        result = [1, 1]
        for item in range(1, rowIndex):
            i, j = 0, 1
            tmp = [1]
            while j < len(result):
                tmp.append(result[i] + result[j])
                i += 1
                j += 1
            tmp.append(1)
            result = tmp
        return result

s = Solution()

print s.getRow(0)
print s.getRow(1)
print s.getRow(2)
print s.getRow(3)
print s.getRow(4)

        


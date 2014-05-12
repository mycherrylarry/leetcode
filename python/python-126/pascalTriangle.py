#!/usr/bin/env python
class Solution:
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1,1]]
        result = [[1], [1,1]]
        for i in range(3, numRows+1):
            tmp = [1]
            for j in range(1, i-1):
                tmp.append(result[i-2][j-1]+result[i-2][j])
            tmp.append(1)
            result.append(tmp)
        return result

s = Solution()
print s.generate(5)


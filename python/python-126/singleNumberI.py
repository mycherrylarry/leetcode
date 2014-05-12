#!/usr/bin/env python
'''
Solution1. Hashmap
Solution2. convert each number to binary representation, and sum every bit and mod 3(or k)
'''

class Solution:
    def singleNumber(self, A):
        return reduce(lambda x, y: x^y, A)


s = Solution()
print s.singleNumber([1,1,3,3,4,6,4])



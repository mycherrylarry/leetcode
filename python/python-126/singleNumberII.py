#!/usr/bin/env python
'''
Solution1. Hashmap
Solution2. convert each number to binary representation, and sum every bit and mod 3(or k)
Result: AC
'''

class Solution:
    def singleNumber(self, A):
        v = [self.convertToBinary(item) for item in A]
        t = [sum(item)%3 for item in zip(*v)]
        x = reduce(lambda x,y: x*2 + y, t[1:])
        if t[0] == 1:
            return -x
        return x

    def convertToBinary(self, n):
        li = [0]*64
        if n < 0:
            li[0] = 1
        n = abs(n)
        i = 63
        while n!= 0:
            li[i] = n%2
            n = n>>1
            i -= 1
        return li

s = Solution()

print s.singleNumber([1,1,1,2,2,2,3,3,3,4])
print s.singleNumber([-401451,-177656,-2147483646,-473874,-814645,-2147483646,-852036,-457533,-401451,-473874,-401451,-216555,-917279,-457533,-852036,-457533,-177656,-2147483646,-177656,-917279,-473874,-852036,-917279,-216555,-814645,2147483645,-2147483648,2147483645,-814645,2147483645,-216555])

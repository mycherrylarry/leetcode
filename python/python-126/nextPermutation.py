#!/usr/bin/env python

'''1. Find the first non-increasing index j backword
2. Find the biggest number of the non-increasing array that is bigger than A[j-1] which marked as i
3. Switch A[i] and A[j-1]
4. Resort A[j:]
5. Append the new A[:j-1] + [A[j-1]] + A[j:]
exp1:
    1234567
    1234576
    1234657
    1234675
    ...
    1234765
    1235467
    ...
exp2:
    6754321
    7123456
'''
class Solution:
    def nextPermutation(self, num):
        if len(num) in range(0, 1): return num
        j = len(num)-1
        while j > 0 and num[j] <= num[j-1]:
            j -= 1
        if j == 0:
            return num[::-1]
        else:
            for i in range(len(num) - j)[::-1]:
                if num[j+i] > num[j-1]:
                    break
            x = num[j:]
            del(x[i])
            x.insert(i, num[j-1])
            return num[:j-1] + [num[j+i]] + x[::-1]

s = Solution()
print s.nextPermutation([1,2,3,4,7,6,5])
print s.nextPermutation([1,2,3])
print s.nextPermutation([3,2,1])
print s.nextPermutation([1,1,1,5])
print s.nextPermutation([2,3,1])
print s.nextPermutation([5,1,1])



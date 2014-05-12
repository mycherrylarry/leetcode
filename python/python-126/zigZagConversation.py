#!/usr/bin/env python
from unittest import *
#print root

'''
Description:

solution :

    |     |     |
    |   / |   / |
    | /   | /   |
    |     |

    1. first row: i*[(m-2)+m]
    2. last row: i*[(m-2)+m]+(m-1)
    3. middle: j+i*[(m-2)+m], (i+1)*[(m-2)+m]-j


solution 2:

    |     |     |
    | \   | \   |
    |   \ |   \ |
    |     |

    1. first row: i*[(m-2)+m]
    2. last row: i*[(m-2)+m]+(m-1)
    3. middle: j+i*[(m-2)+m], j+i*[(m-2)+m]+(m-1)
Time Complexity:
Result:
    solution: AC
'''
class Solution:
    def convert(self, s, m):
        if m<= 1: return s
        result = []
        # start 
        i = 0
        while i*(m*2-2) < len(s):
            result.append(s[i*(m*2-2)])
            i += 1
        # middle
        for j in range(1, m-1):
            i = 0
            while j+i*(m*2-2) < len(s):
                tmp = j+i*(m*2-2)
                result.append(s[tmp])
                tmp1 = (i+1)*(m*2-2)-j
                if tmp1 < len(s):
                    result.append(s[tmp1])
                i += 1
        # end
        i = 0
        while i*(m*2-2)+m-1 < len(s):
            result.append(s[i*(m*2-2)+m-1])
            i += 1
        return "".join(result)

class Solution2:
    def convert(self, s, m):
        if m<= 1: return s
        result = []
        # start 
        i = 0
        while i*(m*2-2) < len(s):
            result.append(s[i*(m*2-2)])
            i += 1
        # middle
        for j in range(1, m-1):
            i = 0
            while j+i*(m*2-2) < len(s):
                tmp = j+i*(m*2-2)
                result.append(s[tmp])
                if tmp+m-1 < len(s):
                    result.append(s[tmp+m-1])
                i += 1
        # end
        i = 0
        while i*(m*2-2)+m-1 < len(s):
            result.append(s[i*(m*2-2)+m-1])
            i += 1
        return "".join(result)

s = Solution()
print s.convert("PAYPALISHIRING", 3)
print s.convert("ABCDE", 4)







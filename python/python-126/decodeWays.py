#!/usr/bin/env python

'''
Description:
    Find different ways of dividing digital numbers by range(1, 27)
    1. DP
    2. case1 = route[i-1] {if i-1>=0 and s[i] in range(1, 10)} or 0 {others}
    3. case2 = route[i-2] {if i-2>=0 and (s[i-2]*10 + s[i-1]) in range(10, 27) or 0 {others}
    4. route[i] = case1 + case2
Time Complexity: O(N)
Space Complexity: O(N)
Result: AC
'''

class Solution:

    def numDecodings(self, s):
        if len(s) == 0: return 0
        route = [0]*(len(s)+1)
        route[0] = 1
        for i in range(1, len(s)+1):
            case1 = 0
            # Check case1
            if i-1>=0 and int(s[i-1]) in range(1, 10):
                case1 = route[i-1]
            case2 = 0
            # Check case2
            if i-2>=0 and (int(s[i-2])*10+int(s[i-1])) in range(10, 27):
                case2 = route[i-2]
            # Route i will be the sum of case1 and case2
            route[i] = case1 + case2
        return route[len(s)]

s = Solution()
print s.numDecodings("10")

        



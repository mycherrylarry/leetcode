#!/usr/bin/env python

'''
Description:
Time Complexity:
Result: Time Limit Exceeded
'''

class Solution:
    def check(self, s):
        i, j = 0, len(s)-1
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def innerPartition(self, s, route):
        if s == "":
            print route
            return
        for i in range(1, len(s)+1):
            if self.check(s[:i]):
                newRoute= [item for item in route]
                newRoute.append(s[:i])
                self.innerPartition(s[i:], newRoute)

    def partition(self, s):
        route = []
        self.innerPartition(s, [])

#partition("abc", [])
s = Solution()
s.partition("ltsqjodzeriqdtyewsrpfscozbyrpidadvsmlylqrviuqiynbscgmhulkvdzdicgdwvquigoepiwxjlydogpxdahyfhdnljshgjeprsvgctgnfgqtnfsqizonirdtcvblehcwbzedsmrxtjsipkyxk")


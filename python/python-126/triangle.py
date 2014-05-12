#!/usr/bin/env python

'''
Description: DP
Time Complexity: O(N)
Space Complexity: O(log(N))
Result: AC
Addition: needs improvement
'''
class Solution:
    def minimumTotal(self, triangle):
        h = len(triangle)
        if h == 1: return triangle[0][0]
        route = []
        for li in triangle:
            tmp = []
            for i in range(len(li)):
                if i == 0:
                    if len(route) != 0:
                        tmp.append(li[0] + route[0])
                    else:
                        tmp.append(li[0])
                elif i == len(li) -1:
                    tmp.append(li[i] + route[i-1])
                else:
                    tmp.append(li[i] + min(route[i], route[i-1]))
            route = tmp
        return min(route)

s = Solution()
print s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])

print s.minimumTotal([[2]])





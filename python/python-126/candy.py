#!/usr/bin/env python
class Solution:

    def candy(self, ratings):
        l = len(ratings)
        route = [1]*l
        i = 1
        while i != l:
            if ratings[i] > ratings[i-1]:
                route[i] = route[i-1] + 1
            i += 1
        j = l-2
        while j >= 0:
            if ratings[j] > ratings[j+1]:
                route[j] = max(route[j+1]+1, route[j])
            j -= 1
        return sum(route)

s = Solution()
print s.candy([1,2,2,2,1])




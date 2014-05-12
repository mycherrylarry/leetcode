#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
Time Complexity:
Result: AC
important
'''

class Solution:

    def justify(self, result, route, L, l):
        if len(route) == 0:
            return
        if len(route) == 1:
            result.append(route[0] + ' '*(L-l))
            return
        spaces = (L-l)/(len(route) - 1)
        remainder = (L-l)%(len(route)-1)
        while remainder != 0:
            route[remainder-1] += ' '
            remainder -= 1
        result.append((' '*spaces).join(route))
    
    def fullJustify(self, words, L):
        result = []
        i = 0
        route = []
        l = 0
        while i < len(words):
            if l+len(route)+len(words[i]) <= L:
                route.append(words[i])
                l += len(words[i])
                i += 1
            else:
                self.justify(result, route, L, l)
                route = []
                l = 0
        result.append(' '.join(route) + ' '*(L-l-len(route)+1))
        return result

s = Solution()
print s.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print s.fullJustify(["What","must","be","shall","be."], 12)
print s.fullJustify([''], 0)
print s.fullJustify(["Don't","go","around","saying","the","world","owes","you","a","living;","the","world","owes","you","nothing;","it","was","here","first."], 30)





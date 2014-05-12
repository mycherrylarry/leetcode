#!/usr/bin/env python
class Solution:
    def simplifyPath(self, path):
        li = path.split('/')
        s = []
        for item in li:
            if item != '' and item != '.':
                if item == '..' :
                    if len(s) > 0:
                        s.pop()
                else:
                    s.append(item)
        return '/'+'/'.join(s)
    
s = Solution()    
print s.simplifyPath("/a/./b/../../c/")
print s.simplifyPath("/home/../../..")
print s.simplifyPath("/..")

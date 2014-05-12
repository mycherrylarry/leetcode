#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
 a b c a b c a b d a a
-1 0 0 0 1 2 3 4 5 0 1 
Description:
Time Complexity:
Result:
'''

def createTable(s):
    n = len(s)
    if n == 0: return []
    if n == 1: return [-1]
    if n == 2: return [-1, 0]
    result = [0]*n
    result[0] = -1
    i, j, k = 0, 1, 2
    while k < n:
        if s[i] == s[j]:
            result[k] = result[j] + 1
            k += 1
            i += 1
            j += 1
        else:
            i = 0
            if s[i] == s[j]:
                result[k] = 1
                k += 1
                i += 1
                j += 1
            else:
                result[k] = 0
                k += 1
                j += 1
    return result

def kmp(s, t):
    table = createTable(t)
    #if len(s) == 0 and len(t) == 0: return 

print createTable("abcabcabdaa")


#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

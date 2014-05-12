#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].

    | c a t s a n d d o g
  --| -------------------
  c | 0 0 1 1 0 0 0 0 0 0                   
  a |   0 0 0 0 0 0 0 0 0                  
  t |     0 0 0 0 0 0 0 0                
  s |       0 0 0 1 0 0 0             
  a |         0 0 1 0 0 0         
  n |           0 0 0 0 0
  d |             0 0 0 0      
  d |               0 0 1    
  o |                 0 0 
  g |                   0
                
Description:
    1. DFS
Time Complexity:
Result:
'''

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

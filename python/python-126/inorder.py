#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
Time Complexity:
Result:
'''

def inorder(root, route, index=1):
    if root == None: return 
    inorder(root.left, route, index+1)
    route.append(root.val)
    print index,
    inorder(root.right, route, index+1)

route = []
inorder(root,route)

Tree.prettyPrint(root)
print route

#s = Solution()
#List.prettyPrint(head)

#!/usr/bin/env python
from unittest import *
from util.Tree import *
#print root

'''
Description: Simple
Time Complexity:
Result: AC
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # lenght of the list
    def convert(self, head, l):
        if l == 0: return None
        mid = l/2
        p_head = ListNode(-1)
        p_head.next = head
        pre = p_head
        p = head
        while mid > 0:
            pre = p
            p = p.next
            mid -= 1
        pre.next = None
        root = TreeNode(p.val)
        root.left = self.convert(head, l/2)
        root.right = self.convert(p.next, l - l/2 -1)
        return root
        
    
    
    def sortedListToBST(self, head):
        if head == None: return None
        l = 0
        p = head
        while p != None:
            l += 1
            p = p.next
        return self.convert(head, l)
    

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

s = Solution()
root = s.sortedListToBST(a)
Tree.prettryPrint(root)



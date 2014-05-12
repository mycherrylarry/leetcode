#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description:
    1. find a node in the cycle
    2. divide the cycle from the node into two lists
    3. find the connection of the lists
Time Complexity:
Result: AC
'''

class Solution:
    def findShareNode(self, head):
        p = head
        q = head.next
        while q!= None and q.next != None:
            if p == q:
                return p
            q = q.next.next
            p = p.next
        return None
    
    def detectCycle(self, head):
        if head == None: return head
        node = self.findShareNode(head)
        if node == None: return None
        head_a = node.next
        node.next = None
        l, la = 0, 0
        p, pa = head, head_a
        while p!= None:
            l += 1
            p = p.next
        while pa!= None:
            la += 1
            pa = pa.next
        if la > l:
            p = head_a
            q = head
        else:
            p = head
            q = head_a
        for item in range(abs(l -la)):
            p = p.next
        while p != q:
            p = p.next
            q = q.next
        return p

s = Solution()
print s.detectCycle(head)



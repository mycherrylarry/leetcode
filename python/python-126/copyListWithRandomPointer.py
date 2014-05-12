#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    1. create the new list inside the origin one
    2. split
Time Complexity: O(N)
Result: AC
'''

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def splitList(self, head):
        head_2 = head.next
        p = head
        while p!= None:
            q = p.next
            p.next = p.next.next
            if q.next != None:
                q.next = q.next.next
            p = p.next
        return (head, head_2)
    
    
    def copyRandomList(self, head):
        if head == None: return None
        p = head
        while p != None:
            new_node = RandomListNode(p.label)
            new_node.next = p.next
            p.next = new_node
            p = p.next.next
        p = head
        while p != None:
            if p.random != None:
                p.next.random = p.random.next
            p = p.next.next
        (head, h2) = self.splitList(head)
        return h2

h1 = RandomListNode(0)
n1 = RandomListNode(1)
n2 = RandomListNode(2)
h1.next = n1
n1.next = n2
h1.random = n2

s = Solution()
h2 = s.copyRandomList(h1)
print h1.random.label
print h2.random.label



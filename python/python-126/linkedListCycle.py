#!/usr/bin/env python
from unittest import *
#print root
from util.List import *

'''
Description:
    1. two pointers
Time Complexity:
Result: AC
'''

class Solution:
    def hasCycle(self, head):
        if head == None: return False
        p, q = head, head.next
        while q != None and q.next != None:
            if p == q:
                return True
            p = p.next
            q = q.next.next
        return False


head = ListNode(1)
a = ListNode(2)
b = ListNode(2)
c = ListNode(2)
head.next = a
a.next = b
b.next = None
s = Solution()
print s.hasCycle(head)

#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description:
Time Complexity:
Result: AC
'''

class Solution:

    def swapPairs(self, head):
        if head == None or head.next == None: return head
        p_head = ListNode(-1)
        p_head.next = head
        pre = p_head
        p = p_head.next
        q = p_head.next.next
        while p != None and q != None:
            pre.next = q
            tmp = q.next
            q.next = p
            p.next = tmp
            pre = pre.next.next
            p = pre.next
            if p == None: break
            q = p.next
        return p_head.next

s = Solution()
List.prettyPrint(head)
head = s.swapPairs(head)
List.prettyPrint(head)


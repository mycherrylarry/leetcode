#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description:
Time Complexity:
Result: Time Limit Exceeded
'''

class Solution:
    def insertionSortList(self, head):
        if head == None or head.next == None: return head
        p_head = ListNode(-1)
        p_head.next = head
        p = head
        pre_p = p_head
        while p != None:
            # insert p to p_head
            pre = p_head
            q = p_head.next
            while q != p and q.val < p.val:
                pre = q
                q = q.next
            if q == p:
                pre_p = p
                p = p.next
            else:
                pre_p.next = p.next
                p.next = q
                pre.next = p
                p = pre_p.next

        return p_head.next

s = Solution()
head = ListNode(9)
head.next = ListNode(8)
head.next.next = ListNode(9)
head.next.next.next = ListNode(1)
List.prettyPrint(head)
#List.prettyPrint(head)
head = s.insertionSortList(head)
List.prettyPrint(head)


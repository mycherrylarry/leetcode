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

    def partition(self, head, x):
        if head == None or head.next == None: return head
        p = ListNode(x)
        p_head = ListNode(-1)
        p_head.next = p
        p.next = head
        pre = p_head
        q = head
        pre_q = p_head.next
        while q!= None:
            if q.val < p.val:
                #insert before p
                pre.next = q
                tmp = q.next
                q.next = p
                pre = q
                q = tmp
                pre_q.next = q
            else:
                pre_q = q
                q = q.next
        # delete p
        pre.next = p.next
        return p_head.next

s = Solution()
head = ListNode(9)
head.next = ListNode(7)
head.next.next = ListNode(1)
List.prettyPrint(head)
head = s.partition(head, 3)
List.prettyPrint(head)
    


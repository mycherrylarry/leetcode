#!/usr/bin/env python
from unittest import *
#print root
from util.List import *

'''
Description:
    needs practice
Time Complexity:
Result: AC
'''

class Solution:

    # merge l2 to l1
    def mergeTwoLists(self, l1, l2):
        p_head = ListNode(-1)
        p_head.next = l1
        q_head = ListNode(-1)
        q_head.next = l2
        pre = p_head
        p = p_head.next
        q = q_head.next
        while p!= None and q!=None:
            if p.val > q.val:
                pre.next = q
                pre = q
                tmp = q.next
                q.next = p
                q = tmp
            else:
                while p != None and p.val <= q.val:
                    pre = p
                    p = p.next
        if p == None:
            pre.next = q
        return p_head.next

li = ListNode(1)
li.next = ListNode(2)
li.next.next = ListNode(3)

li = None

l2 = ListNode(1)
#l2.next = ListNode(2)
#l2.next.next = ListNode(3)


s = Solution()
l = s.mergeTwoLists(li, l2)
List.prettyPrint(l)




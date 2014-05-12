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

    def reverse(self, head, end):
        p_head = ListNode(-1)
        tx = end.next
        p_head.next = tx
        p = head
        while p != tx:
            tmp = p.next
            p.next = p_head.next
            p_head.next = p
            p = tmp
        return p_head.next
    
    
    # 1 <= m <= n <= length
    def reverseBetween(self, head, m, n):
        p_head = ListNode(-1)
        p_head.next = head
        pre = p_head
        p, q = head, head
        i, j = 1, 1
        while i < m:
            pre = p
            p = p.next
            q = q.next
            i += 1
            j += 1
        while j < n:
            q = q.next
            j += 1
        pre.next = self.reverse(p, q)
        return p_head.next

s = Solution()
List.prettyPrint(head)
head = s.reverseBetween(head, 1, 3)
List.prettyPrint(head)




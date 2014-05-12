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
        head_p = ListNode(-1)
        pivox = end.next
        head_p.next = pivox
        p = head
        while p != pivox:
            tmp = p.next
            p.next = head_p.next
            head_p.next = p
            p = tmp
        return (end, head)
    
    def reverseKGroup(self, head, k):
        if head == None or head.next == None: return head
        if k < 2: return head
        i = 0
        head_p = ListNode(-1)
        head_p.next = head
        p = head_p
        while i < k and p.next != None:
            i += 1
            p = p.next
        if i != k:
            return head
        (head, end) = self.reverse(head, p)
        end.next = self.reverseKGroup(end.next, k)
        return head

s = Solution()
List.prettyPrint(head)
head = s.reverseKGroup(head, 4)
List.prettyPrint(head)




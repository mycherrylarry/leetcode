#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description:
    could be shorter
Time Complexity: O(N)
Result: AC
'''

class Solution:

    def rotateRight(self, head, k):
        if head == None or head.next == None: return head
        head_p = ListNode(-1)
        head_p.next = head
        # length of the list
        l = 0
        p = head_p
        while p.next != None:
            l += 1
            p = p.next
        # the end pointer of the list
        end = p
        k = k%l
        if k == 0: return head
        i = 0
        p = head_p
        while i < k:
            p = p.next
            i += 1
        pre = head_p
        while p.next != None:
            pre = pre.next
            p = p.next
        head_p.next = pre.next
        pre.next = None
        p.next = head
        return head_p.next

s = Solution()
head = ListNode(1)
head.next = ListNode(2)
List.prettyPrint(head)
head = s.rotateRight(head, 100)
List.prettyPrint(head)



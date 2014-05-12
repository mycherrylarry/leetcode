#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description:
Time Complexity:
Result: Time limit exceeded
'''

class Solution:
    def quickSort(self, head):
        if head == None or head.next == None: return (head, head)
        pivot = head
        head_left = ListNode(-1)
        head_right = ListNode(-1)
        p = head.next
        while p != None:
            tmp = p.next
            if p.val <= pivot.val:
                p.next = head_left.next
                head_left.next = p
            else:
                p.next = head_right.next
                head_right.next = p
            p = tmp
        (lesser, tail_lesser) = self.quickSort(head_left.next)
        (bigger, tail_bigger) = self.quickSort(head_right.next)
        head_p = ListNode(-1)
        head_p.next = lesser
        if tail_lesser == None:
            head_p.next = pivot
        else:
            tail_lesser.next = pivot
        pivot.next = bigger
        if tail_bigger == None:
            tail_bigger = pivot
        return (head_p.next, tail_bigger)

    def sortList(self, head):
        head, tail = self.quickSort(head)
        return head
    



s = Solution()
head = ListNode(9)
head.next = ListNode(8)
head.next.next = ListNode(9)
head.next.next.next = ListNode(1)
List.prettyPrint(head)
head = s.sortList(head)
List.prettyPrint(head)

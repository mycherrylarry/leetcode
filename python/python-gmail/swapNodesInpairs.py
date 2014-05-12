#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a linked list, swap every two adjacent nodes and return its head.

    For example,
    Given 1->2->3->4, you should return the list as 2->1->4->3.

    Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        if head == None or head.next == None: return head
        p_head = ListNode(-1)
        p_head.next = head
        p = p_head
        while p.next != None and p.next.next != None:
            a = p.next
            b = a.next
            c = b.next
            b.next = a
            a.next = c
            p.next = b
            p = a
        return p_head.next

s = Solution()
List.prettyPrint(head)
head = s.swapPairs(head)
List.prettyPrint(head)
#Tree.prettyPrint(root)

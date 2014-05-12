#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Description:
Time Complexity: O(N)
Space Complexity: O(1)
Result: AC
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def split(self, head):
        p, q = head, head
        while q.next != None and q.next.next != None:
            p = p.next
            q = q.next.next
        q = p.next
        p.next = None
        return (head, q)

    def reverse(self, head):
        head_p = ListNode(-1)
        p = head
        while p!= None:
            tmp = p.next
            p.next = head_p.next
            head_p.next = p
            p = tmp
        return head_p.next

    # merge b to a
    def merge(self, head_a, head_b):
        p, q = head_a, head_b
        while q != None:
            tmp = q.next
            q.next = p.next
            p.next = q
            p = q.next
            q = tmp
        return head_a

    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        if head == None or head.next == None: return head
        head_a, head_b = self.split(head)
        head_b = self.reverse(head_b)
        return self.merge(head_a, head_b)
                            

List.prettyPrint(head)
s = Solution()
s.reorderList(head)
List.prettyPrint(head)

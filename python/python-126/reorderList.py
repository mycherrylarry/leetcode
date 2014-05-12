#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.

*******
Description:
Time Complexity:
Result: AC
'''

def splitAndMerge(head):
    head_p = ListNode(-1)
    head_q = ListNode(-1)
    p = head
    pre_p = head_p
    q = head.next
    while p!=None and q!=None:
        pre_p.next = p
        pre_p = p
        if p.next == None:
            p = None
        else:
            p = p.next.next
        if q.next == None:
            tmp = None
        else:
            tmp = q.next.next
        q.next = head_q.next
        head_q.next = q
        q = tmp
    if p != None:
        pre_p.next = p
    if q != None:
        q.next = head_q.next
        head_q.next = q
    return head_p.next, head_q.next


def reorderList(head):
    if head == None or head.next == None: return head
    return splitAndMerge(head)

List.prettyPrint(head)
h1, h2 = reorderList(head)
List.prettyPrint(h1)
List.prettyPrint(h2)

class Solution:

    def split(self, head):
        count = 0
        head_p = ListNode(-1)
        head_p.next = head
        p = head
        while p!= None:
            count += 1
            p = p.next
        helf = count/2
        if count%2 == 1:
            helf += 1
        i = 0
        pre = head_p
        while i != helf:
            pre = pre.next
            i += 1
        q = pre.next
        pre.next = None
        return (head, q)
    
    def reverse(self, head):
        p = head
        head_p = ListNode(-1)
        while p!= None:
            tmp = p.next
            p.next = head_p.next
            head_p.next = p
            p = tmp
        return head_p.next
    
    # merge h2 to h1
    def merge(self, h1, h2):
        p, q = h1, h2
        while q != None:
            tmp = q.next
            q.next = p.next
            p.next = q
            p = p.next.next
            q = tmp
        return h1
    
    def reorderList(self, head):
        if head == None or head.next == None: return head
        h1, h2 = self.split(head)
        h2 = self.reverse(h2)
        h1 = self.merge(h1, h2)
        return h1

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

List.prettyPrint(head)

s = Solution()
head = s.reorderList(head)

List.prettyPrint(head)




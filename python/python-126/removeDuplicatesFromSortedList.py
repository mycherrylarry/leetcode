#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description: Simple
Time Complexity:
Result: AC
'''

class Solution:
    def deleteDuplicates(self, head):
        if head == None or head.next == None: return head
        pre = head
        p = head.next
        while p != None:
            if p.val == pre.val:
                pre.next = p.next
            else:
                pre = p
            p = p.next
        return head

head = ListNode(1)
head.next = ListNode(1)
s = Solution()
List.prettyPrint(head)
s.deleteDuplicates(head)
List.prettyPrint(head)


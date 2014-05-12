#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a sorted linked list, delete all duplicates such that each element appear only once.

    For example,
    Given 1->1->2, return 1->2.
    Given 1->1->2->3->3, return 1->2->3.

Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if head == None: return None
        p = head
        while p != None:
            if p.next != None and p.next.val == p.val:
                p.next = p.next.next
            else:
                p = p.next
        return head

s = Solution()
List.prettyPrint(head)
print s.deleteDuplicates(head)
List.prettyPrint(head)
#Tree.prettyPrint(root)

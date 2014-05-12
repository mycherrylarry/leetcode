#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Resolution:
Time Complexity:
Space Complexity:
Result: AC
Note: mistake pro
'''

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        if l2 == None: return l1
        if l1 == None: return self.mergeTwoLists(l2, l1)
        if l1.val > l2.val:
            return self.mergeTwoLists(l2, l1)
        if l1.next != None and l1.next.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        # merge l2 to l1
        p, q = l1, l2
        tmp = q.next
        q.next = p.next
        p.next = q
        l1.next.next = self.mergeTwoLists(l1.next.next, tmp)
        return l1

s = Solution()
List.prettyPrint(head)
h1 = ListNode(-1)
head = s.mergeTwoLists(head, h1)
List.prettyPrint(head)
#Tree.prettyPrint(root)

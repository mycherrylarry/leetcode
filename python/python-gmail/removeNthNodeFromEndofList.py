#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a linked list, remove the nth node from the end of list and return its head.

Method:
Resolution:
    * find the nth's pre node
Time Complexity:
Space Complexity:
Result: AC
Note:
    * pay attention to the return
'''

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        p_head = ListNode(-1)
        p_head.next = head
        q = p_head
        p = head
        i = 0
        while i< n:
            p = p.next
            i += 1
        while p!= None:
            p = p.next
            q = q.next
        q.next = q.next.next
        return p_head.next
List.prettyPrint(head)
s = Solution()
s.removeNthFromEnd(head, 2)
List.prettyPrint(head)

#Tree.prettyPrint(root)

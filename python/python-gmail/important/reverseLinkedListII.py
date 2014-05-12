#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Reverse a linked list from position m to n. Do it in-place and in one-pass.

    For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,

    return 1->4->3->2->5->NULL.
Method:
Resolution:
    * 
Time Complexity:
Space Complexity:
Result: AC
Note:
    * pay attention to the requirement of "one-pass"
    * put down the calculation process on paper
'''

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        # 1 <= m <= n <= length
        p_head = ListNode(-1)
        p_head.next = head
        pre = p_head
        i, j = 1, 1
        while i < m:
            pre = pre.next
            i += 1
            j += 1
        p = pre.next
        tail = p
        while j <= n:
            q = p.next
            p.next = pre.next
            pre.next = p
            p = q
            j += 1
        tail.next = p
        return p_head.next

s = Solution()
List.prettyPrint(head)
head = s.reverseBetween(head, 1,2)
List.prettyPrint(head)
#Tree.prettyPrint(root)

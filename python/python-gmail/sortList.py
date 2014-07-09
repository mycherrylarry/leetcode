#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Sort a linked list in O(nlogn) time using constant space complexity.
Method:
Solution:
    Merge sort
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # split the list into two equal size sublists
    def splitList(self, head, size):
        pre = ListNode(-1)
        pre.next = head
        q = head
        for i in range(size/2):
            pre = pre.next
            q = q.next
        pre.next = None
        return head, size/2, q, size - size/2

    def merge(self, head1, head2):
        pre = ListNode(-1)
        p = pre
        p1 = head1
        p2 = head2
        while p1 != None and p2 != None:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        if p1 != None:
            p.next = p1
        if p2 != None:
            p.next = p2
        return pre.next

    def divide(self, head, size):
        if(size == 0 or size == 1):
            return head
        l_head, l_size, r_head, r_size = self.splitList(head, size)
        left = self.divide(l_head, l_size)
        right = self.divide(r_head, r_size)
        return self.merge(left, right)

    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        size = 0
        p = head
        while(p != None):
            p = p.next
            size += 1
        return self.divide(head, size)


s = Solution()
List.prettyPrint(head)
head = s.sortList(head)
List.prettyPrint(head)
#Tree.prettyPrint(root)

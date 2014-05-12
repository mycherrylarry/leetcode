#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description:
    1. Divid and conqure
Time Complexity: O(log(K)*N)
Result: AC
'''

class Solution:

    # merge 2 lists, merge l2 to l1
    def merge(self, head1, head2):
        if head1 == None: return head2
        if head2 == None: return head1
        head_p = ListNode(-1)
        head_p.next = head1
        pre = head_p
        p, q = head1, head2
        while p!= None and q!= None:
            if p.val <= q.val:
                pre = p
                p = p.next
            else:
                # insert q before p
                tmp = q.next
                q.next = p
                pre.next = q
                pre = q
                q = tmp
        if p == None:
            pre.next = q
        return head_p.next
    
    
    def mergeKLists(self, lists):
        if len(lists) == 0: return None
        if len(lists) == 1: return lists[0]
        mid = len(lists)/2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.merge(left, right)

head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(10)

head2 = ListNode(3)
head2.next = ListNode(5)
head2.next.next = ListNode(6)

head3 = ListNode(3)
head3.next = ListNode(10)
head3.next.next = ListNode(17)

s = [head1, head2, head3]

s = Solution()
List.prettyPrint(head1)
List.prettyPrint(head2)
h = s.mergeKLists([head1])
List.prettyPrint(h)


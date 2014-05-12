#!/usr/bin/env python
from unittest import *
from util.List import *
#print root

'''
Description:
    head ->1->2->3->4->None
Time Complexity:
Result: AC
error check
'''

class Solution:

    def removeNthFromEnd(self, head, n):
        if n <=0: return head
        pre_head = ListNode(-1)
        pre_head.next = head
        i = 1
        p = head
        while i < n:
            p = p.next
            i += 1
        pre = pre_head
        while p.next!= None:
            pre = pre.next
            p = p.next
        pre.next = pre.next.next
        return pre_head.next

List.prettyPrint(head)
head = removeNthFromEnd(head, 10)
List.prettyPrint(head)



    


#s = Solution()

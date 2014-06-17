#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method: 
    tree pointers:
    1. pre
    2. pre_target
    3. pre_p
    one template node
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        if head == None or head.next == None:
            return head
        pre = ListNode(-1)
        target = ListNode(x)
        target.next = head
        pre.next = target
        pre_p = target
        pre_target = pre
        while pre_p.next != None:
            if pre_p.next.val < x:
                p = pre_p.next
                pre_p.next = p.next
                p.next = pre_target.next
                pre_target.next = p
                pre_target = p
            else:
                pre_p = pre_p.next
        # delete target
        pre_target.next = pre_target.next.next
        return pre.next
            
s = Solution()
List.prettyPrint(head)
head = s.partition(head, 3)
List.prettyPrint(head)
#Tree.prettyPrint(root)

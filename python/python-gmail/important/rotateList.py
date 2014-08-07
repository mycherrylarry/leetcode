#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result: AC
Note:
    pay attention to edge cases
'''

class Solution:
    def rotate(self, head, l, k):
        if k == 0: return head
        if k >= l: return self.rotate(head, l, k%l)
        pre = ListNode(-1)
        pre.next = head
        p = pre
        for i in range(l - k):
            p = p.next
        pre.next = p.next
        p.next = None
        p = pre.next
        while p.next != None:
            p = p.next
        p.next = head
        return pre.next

    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if head == None: return head
        p = head
        l = 0
        while p != None:
            p = p.next
            l += 1
        return self.rotate(head, l, k)

s = Solution()
List.prettyPrint(head)
head = s.rotateRight(head, 2)
List.prettyPrint(head)

#Tree.prettyPrint(root)

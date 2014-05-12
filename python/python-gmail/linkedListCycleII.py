#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

    Follow up:
    Can you solve it without using extra space?
Description:
    1. Following the previous question. First judge whether a cycle exists.
    2. If there is a cycle, return the pointer at where p and q meet each other.
    3. Split the link, and find out the first common node of the two lists.

Time Complexity:
Space Complexity:
Result: AC
'''

class Solution:
    def hasCycle(self, head):
        p, q = head, head.next
        while q != None and q.next != None:
            if p == q:
                return p
            p = p.next
            q = q.next.next
        return None

    # find the first common node of two lists
    def findFirstCommonNode(self, head_a, head_b):
        l_a, l_b = 0, 0
        p, q = head_a, head_b
        while p != None:
            l_a += 1
            p = p.next
        while q != None:
            l_b += 1
            q = q.next
        p, q = head_a, head_b
        # make sure that l_a is bigger than l_b
        if l_a < l_b :
            l_a, l_b = l_b, l_a
            p, q = q, p
        for i in range(l_a - l_b):
            p = p.next
        while p != None:
            if p == q:
                return p
            p = p.next
            q = q.next
        return None

    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head == None: return None
        tag = self.hasCycle(head)
        if tag == None: return None
        h = tag.next
        tag.next = None
        return self.findFirstCommonNode(head, h)


s = Solution()
print s.detectCycle(head).val
#List.prettyPrint(head)
#Tree.prettyPrint(root)

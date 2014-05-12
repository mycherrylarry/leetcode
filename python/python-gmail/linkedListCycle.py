#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a linked list, determine if it has a cycle in it.

    Follow up:
    Can you solve it without using extra space?

Description:
    1. Given two pointers which both start from the begining of the list, pointer p move one
       step at a time, and pointer q move two steps at a time. If p and q finally meet each
       other, it means that there's a cycle in the given list.
Time Complexity:
Space Complexity: O(1)
Result: AC
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head == None: return False
        p, q = head, head.next
        while q != None and q.next != None:
            if p == q: return True
            p = p.next
            q = q.next.next
        return False

s = Solution()
print s.hasCycle(head)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

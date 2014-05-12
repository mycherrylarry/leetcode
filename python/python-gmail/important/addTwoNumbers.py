#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
Description:
Time Complexity:
Space Complexity:
Result: AC
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def adds(self, l1, l2, remainder, pre=None):
        if l1 == None and l2 == None:
            if remainder == 0: return
            pre.next = ListNode(remainder)
            return
        if l1 == None:
            pre.next = l2
            self.adds(l2, l1, remainder, l2)
            return
        if l2 == None:
            tmp = l1.val + remainder
            l1.val = tmp%10
            self.adds(l1.next, None, tmp/10, l1)
            return
        tmp = l1.val + l2.val + remainder
        l1.val = tmp%10
        self.adds(l1.next, l2.next, tmp/10, l1)

    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        self.adds(l1,l2,0,l1)
        return l1

#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

s = Solution()
l1 = ListNode(0)
l2 = ListNode(7)
l2.next = ListNode(3)
h = s.addTwoNumbers(l2,l1)
List.prettyPrint(h)

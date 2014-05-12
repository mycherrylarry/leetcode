#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
   - A linked list is given such that each node contains an additional random pointer which
     could point to any node in the list or null.
   - Return a deep copy of the list.
Description:
   * Create a new list inside the origin one
   * Split the new list
Time Complexity:
Space Complexity:
Result: AC
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    def createNewList(self, head):
        p = head
        while p != None:
            new_node = RandomListNode(p.label)
            new_node.next = p.next
            p.next = new_node
            p = p.next.next
        p = head
        while p != None:
            if p.random != None:
                p.next.random = p.random.next
            p = p.next.next
        return head

    def splitNewList(self, head):
        head_new = head.next
        p, q = head, head_new
        while p != None:
            p.next = p.next.next
            p = p.next
            if q.next != None:
                q.next = q.next.next
                q = q.next
        return head_new

    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None: return None
        head = self.createNewList(head)
        return self.splitNewList(head)


head = RandomListNode(1)
head.next = RandomListNode(2)
head.next.next = RandomListNode(3)
head.next.random = head

s = Solution()
h = s.copyRandomList(head)
print h.next.random.label

#List.prettyPrint(head)
#Tree.prettyPrint(root)

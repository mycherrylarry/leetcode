#!/usr/bin/env python

class ListNode:
    def __init__(self, v):
        self.val = v
        self.next = None

class List:
    def __init__(self, li):
        self.li = li
        self.head = ListNode(-1000000)
        self.head.next = self.genList(li)

    # Generate a linked-list from a given array
    def genList(self, li):
        pre = ListNode(li[0])
        head = pre
        for item in li[1:]:
            tmp = ListNode(item)
            pre.next = tmp
            pre = tmp
        return head

    # Convert the linked-list to an array
    @staticmethod
    def list(head):
        p = head
        while p!= None:
            yield p.val
            p = p.next

    @staticmethod
    def reverse(head):
        p = head.next
        head.next = None
        while p != None:
            tmp = p.next
            p.next = head.next
            head.next = p
            p = tmp
        return head

    @staticmethod
    def prettyPrint(head):
        print "->".join([str(item) for item in List.list(head)])


def prettyPrint(f, *args):
    def new_f(*args):
        li = f(*args)
        return [item for item in List.list(li)]
    return new_f

if __name__ == "__main__":
    head = List(range(10)).head
    List.prettyPrint(head)
    List.prettyPrint(List.reverse(head))

#!/usr/bin/env python


class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # add node to the front of list
    def add_front(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            node.prev = node.next = None
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        node.prev = None

    def remove_end(self):
        self.remove(self.tail)

    def remove(self, node):
        if self.head == self.tail:
            self.head = self.tail = None
            return
        if node == self.head:
            node.next.prev = None
            self.head = node.next
            return
        if node == self.tail:
            node.prev.next = None
            self.tail = node.prev
            return
        node.next.prev = node.prev
        node.prev.next = node.next

    def pretty_print(self):
        p = self.head
        while p != None:
            print p.value, "<->",
            p = p.next
        print


doubly_linked_list = DoublyLinkedList()
for item in range(10):
    doubly_linked_list.add_front(Node(item))

doubly_linked_list.remove_end()
doubly_linked_list.pretty_print()

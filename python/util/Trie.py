#!/usr/bin/env python

class Trie:
    def __init__(self, c, val = None):
        self.c = c
        self.val = val
        #self.count = 0
        self.children = {}

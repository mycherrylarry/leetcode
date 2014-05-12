#!/usr/bin/env python

# Based on Trie
# No compression
class TrieNode:
    def __init__(self, c, val = None):
        self.c = c
        self.val = val
        self.count = 1
        self.children = {}

class Trie:
    @staticmethod
    def prettyPrint(root, i= 0):
        print " "*i, root.c
        for item in root.children.values():
            Trie.prettyPrint(item, i+1)

    @staticmethod
    def find(root, target):
        p = root
        for i in range(len(target)):
            if not p.children.has_key(target[i]):
                return 0
            p = p.children[target[i]]
        if p.val != target:
            return 0
        return p.count

class SuffixTree:
    # Empty is also valid in suffixTree
    @staticmethod
    def insert(root, s):
        if len(s) == 0:
            root.children[s] = TrieNode("$", s)
            return root
        p = root
        for i in range(len(s)):
            if not p.children.has_key(s[i]):
                # Store c and val into TrieNode
                p.children[s[i]] = TrieNode(s[i], "".join(s[:i+1]))
            else:
                p.children[s[i]].count += 1
            p = p.children[s[i]]
        return root

    # if found, return occrance, else return 0
    @staticmethod
    def find(root, target):
        if len(target) == 0:
            return 0
        else:
            return Trie.find(root, target)

    # Create a SuffixTree for a string
    @staticmethod
    def create(s):
        root = TrieNode(None)
        for i in range(len(s) + 1):
            SuffixTree.insert(root, s[i:])
        return root

    @staticmethod
    def prettyPrint(root, i= 0):
        Trie.prettyPrint(root, i)

    # Count total different substrings in s, which actually is the number of  nodes in a SuffixTree
    @staticmethod
    def differentSubStrings(root):
        if len(root.children) == 0:
            return 0
        subSum = 0
        for item in root.children.values():
            subSum += SuffixTree.differentSubStrings(item)
        return subSum + len(root.children)


root = SuffixTree.create("abc")
#root = SuffixTree.create("abcd")
#print SuffixTree.find(root, "ab")
#print SuffixTree.find(root, "ba")
SuffixTree.prettyPrint(root)
print SuffixTree.differentSubStrings(root)







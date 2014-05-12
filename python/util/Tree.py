#!/usr/bin/env python
'''TreeNode and Tree data structures for
leetcode on-line judgement
'''
class TreeNode:
    def __init__(self, v):
        self.val = v
        self.left = None
        self.right = None

class Tree:
    # Calculate the height of a tree
    @staticmethod
    def height(root):
        if root == None:
            return 0
        return max(Tree.height(root.left), Tree.height(root.right)) + 1

    # Create a balanced tree
    def createTree(self, li):
        if len(li) == 0: return None
        if len(li) == 1: return TreeNode(li[0])
        mid = len(li)/2
        root = TreeNode(li[mid])
        root.left = self.createTree(li[:mid])
        root.right = self.createTree(li[mid+1:])
        return root

    # Print the contents of a tree
    @staticmethod
    def prettyPrint(root, height = 0):
        if root == None:
            return
        Tree.prettyPrint(root.right, height+1)
        for item in range(height):
            print "  ",
        print root.val
        Tree.prettyPrint(root.left, height+1)

    # Pre-print of a tree
    @staticmethod
    def preprint(root):
        if root == None:
            return
        print root.val
        Tree.preprint(root.left)
        Tree.preprint(root.right)


if __name__ == "__main__":
    s = Tree()
    Tree.prettyPrint(s.createTree(range(100)))

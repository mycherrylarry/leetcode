#!/usr/bin/env python
from unittest import *
from util.Tree import *


'''
Problem:
    Print arbitrary binary tree by vertical levels / columns from left to right
    example tree
          a
         / \
        b   c
       / \   \
      d   g   z
      \      /
       e    i
           /
          q
         /
        x
       /
      x1
    /
   x2
    
    sample output
    x2
    d x1
    b e x
    a g q
    c i

Description:
    1. set (key, value) = (node, (row, col))
    2. BFS
Time Complexity:
Result: ACC
'''

# sort li like [((1, 2), 1), ((1, 3), 2), ((2, 1), 3)] 
def quickSort(li):
    if len(li) in (0, 1): return li
    value, key = li[-1]
    lesserA = quickSort(filter(lambda x: x[0][1] < value[1], li[:-1]))
    lesserB = quickSort(filter(lambda x: x[0][1] == value[1] and x[0][0] <= value[0], li[:-1]))
    biggerA = quickSort(filter(lambda x: x[0][1] > value[1], li[:-1]))
    biggerB = quickSort(filter(lambda x: x[0][1] == value[1] and x[0][0] > value[0], li[:-1]))
    return lesserA + lesserB + [li[-1]] + biggerB + biggerA

def bfs(root):
    '''
    create the map like {node: (row, col)}
    '''
    mp = {}
    queue = []
    queue.append(root)
    # set root's value as row = 0 and col = 0
    mp[root] = (0, 0)
    while len(queue) != 0:
        cur_node = queue[0]
        del(queue[0])
        cur_row, cur_col = mp[cur_node]
        if cur_node.left != None:
            mp[cur_node.left] = (cur_row + 1, cur_col - 1)
            queue.append(cur_node.left)
        if cur_node.right != None:
            mp[cur_node.right] = (cur_row + 1, cur_col + 1)
            queue.append(cur_node.right)
    return mp

def printTreeByVerticalLevel(root):
    mp = bfs(root)
    for key, value in mp.iteritems():
        print key.val, value
    # mp = {<util.Tree.TreeNode instance at 0x103ac7e18>: (3, -1)}
    li = quickSort(zip(mp.values(), mp.keys()))
    # li = [((3, -3), <util.Tree.TreeNode instance at 0x11017dd40>)]
    tag = li[0][0][1]
    tmp = [li[0]]
    for i in range(1, len(li)):
        if tag == li[i][0][1]:
            tmp.append(li[i])
        else:
            for item in tmp:
                print item[1].val, 
            print
            tmp = [li[i]]
            tag = li[i][0][1]
    for item in tmp:
        print item[1].val,
        print

tree = Tree()
root = tree.createTree(range(10))
Tree.prettryPrint(root)


printTreeByVerticalLevel(root)

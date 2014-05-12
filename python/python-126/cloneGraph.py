#!/usr/bin/env python
from unittest import *
#print root

'''
Description:
    1. BFS: create node' and add them to the end of neighbors
    2. BFS: create links of node's
    3. BFS: delete node' of the origin nodes
Time Complexity: O(N)
Result: Time limit
'''

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # deep clone of the graph
    def cloneGraph(self, node):
        if node == None: return node
        # step 1
        queue = [node]
        route = {}
        while len(queue) != 0:
            item = queue[0]
            route[item] = 1
            del(queue[0])
            for node in item.neighbors:
                if not route.has_key(node):
                    queue.append(node)
            item.neighbors.append(UndirectedGraphNode(item.label))
            
        # step 2
        queue = [node]
        route = {}
        while len(queue) != 0:
            item = queue[0]
            route[item] = 1
            del(queue[0])
            neighbors = []
            for node in item.neighbors[:-1]:
                if not route.has_key(node):
                    queue.append(node)
                item.neighbors[-1].neighbors.append(node.neighbors[-1])
        result = node.neighbors[-1]
        # step 3
        queue = [node]
        route = {}
        while len(queue) != 0:
            item = queue[0]
            route[item] = 1
            del(queue[0])
            for node in item.neighbors[:-1]:
                if not route.has_key(node):
                    queue.append(node)
            item.neighbors.pop()
        return result
    

a = UndirectedGraphNode(1)
b = UndirectedGraphNode(2)

a.neighbors = [a,b]
b.neighbors = [a]


s = Solution()
print s.cloneGraph(a).neighbors
print a.neighbors







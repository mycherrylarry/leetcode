#!/usr/bin/env python

class UnionFind:
    def __init__(self):
        self.leaders = {}   # map members to leader
        self.groups = {}    # map leader to group

    # make a new group of list li
    def makeGroup(self, li):
        leader = li[0]
        group = set(li)
        self.groups[leader] = group
        for item in li:
            self.leaders[item] = leader

    # return the leader of group
    def find(self, item):
        return self.leaders[item]

    # union the groups of item1 and item2
    def union(self, item1, item2):
        leader1 = self.find(item1)
        leader2 = self.find(item2)
        # the same group
        if leader1 == leader2:
            return
        group1 = self.groups[leader1]
        group2 = self.groups[leader2]

        # merge group2 to group1
        group1 |= group2
        del[self.groups[leader2]]
        for item in group2:
            self.leaders[item] = leader1

class Edge:
    def __init__(self, a, b, val):
        self.a = a
        self.b = b
        self.val = val

class Graph:
    def __init__(self, n, edges):
        self.nodes = range(n)
        self.edges = edges

    # Sort edges by value
    def quickSort(self, li):
        if len(li) in range(0, 1): return li
        lesser = self.quickSort(filter(lambda x: x.val <= li[-1].val, li[:-1]))
        bigger = self.quickSort(filter(lambda x: x.val >  li[-1].val, li[:-1]))
        return lesser + [li[-1]] + bigger

    def minSpanTree(self):
        edges = self.quickSort(self.edges)
        result = []
        unionFind = UnionFind()
        # make groups of each node
        for item in self.nodes:
            unionFind.makeGroup([item])
        for item in edges:
            a, b = item.a, item.b
            if unionFind.find(a) == unionFind.find(b):
                continue
            result.append(item)
            unionFind.union(a, b)
        return result

edges = [
    Edge(0, 1, 3),
    Edge(0, 3, 2),
    Edge(0, 5, 1),
    Edge(1, 2, 1),
    Edge(1, 3, 1),
    Edge(2, 3, 10),
    Edge(3, 4, 2),
    Edge(3, 5, 1),
    Edge(4, 5, 5)
    ]

graph = Graph(6, edges)

for item in graph.minSpanTree():
    print item.a, item.b, item.val

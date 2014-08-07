#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result:
Note:
'''
class Graph:
    def __init__(self, n):
        self.n = n
        nodes = {}
        for i in range(n):
            nodes[i+1] = {}
        self.nodes = nodes

    def make(self, i, j, time):
        if self.nodes[i].has_key(j):
            self.nodes[i][j] = max(time, self.nodes[i][j])
            self.nodes[j][i] = max(time, self.nodes[j][i])
        else:
            self.nodes[i][j] = time
            self.nodes[j][i] = time

    def check(self, a, b, time):
        route = [0 for i in range(self.n+1)]
        queue = [a]
        nodes = self.nodes
        while len(queue) != 0:
            item = queue[0]
            del(queue[0])
            route[item] = 1
            avaliable_keys = filter(lambda x: nodes[item][x] >= time and route[x] == 0, nodes[item].keys())
            if b in avaliable_keys:
                print 'YES'
                return 
            queue.extend(avaliable_keys)
        print 'NO'
        return


def solve():
    n, q = map(int, raw_input().strip().split())
    g = Graph(n)
    for i in range(q):
        tag, a, b, time = raw_input().strip().split()
        if tag == 'make':
            g.make(int(a), int(b), int(time))
        else:
            g.check(int(a), int(b), int(time))

solve()


#List.prettyPrint(head)
#Tree.prettyPrint(root)

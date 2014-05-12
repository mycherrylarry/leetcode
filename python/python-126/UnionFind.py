#!/usr/bin/env python
from unittest import *

'''
Description: Union-Find Data Structure
'''

class UnionFind(object):
    def __init__(self):
        self.leaders = {}   # maps member to group leader
        self.groups = {}    # maps group leader to set of members

    def makeGroup(self, elements):
        ''' Insert elements as new group. '''
        assert type(elements) is list
        assert len(elements) != 0

        group = set(elements)
        leader = elements[0]
        self.groups[leader] = group
        for item in group:
            self.leaders[item] = leader

    def find(self, element):
        ''' Return the group leader of the element.'''
        return self.leaders[element]

    def union(self, element1, element2):
        ''' Merge the groups containing two different elements. '''
        leader1 = self.find(element1)
        leader2 = self.find(element2)
        if leader1 == leader2:
            return
        group1 = self.groups[leader1]
        group2 = self.groups[leader2]

        # mearge group2 to group1, and delete group2
        group1 |= group2
        del self.groups[leader2]
        # change leader of group2
        for item in group2:
            self.leaders[item] = leader1

unionFind = UnionFind()
unionFind.makeGroup(range(3))
unionFind.makeGroup(([4,6,7])
unionFind.union(2, 7)
print unionFind.groups
print unionFind.leaders


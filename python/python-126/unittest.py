#!/usr/bin/env python
def unittest0(testCase):
    def inner_f0(f, *args):
        def inner_f(*args):
            result = f(*args)
            print "Expected:", testCase
            print "Result  :", result
            print 
            return f
        return inner_f
    return inner_f0

def unittest(f, *args):
    def inner_f(*args):
        result = f(*args)
        print "Result  :", result
        print 
        return f
    return inner_f

from util.Tree import Tree

t = Tree()
#root = t.createTree([1,4,3,2,5])
root = t.createTree(range(10))

from util.List import *
h = List([0,0,1,1,1,2,2,3,3,4])
h = List(range(10))
head = h.head.next

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
root = t.createTree([1,2,3,4,5,6])

from util.List import *
h = List([1,4,3,2,5,2])
head = h.head.next

if __name__ == "__main__":
    Tree.prettyPrint(root)

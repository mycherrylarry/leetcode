#!/usr/bin/env python
from unittest import *
from util.Tree import *
from util.List import *
#print root

'''
Description:
    1. use HashMap to store info: mp = {(a, b): set()}
       a = (y1-y2)/(x1-x2)
       a = "." if y1-y2 == 0
       a = "*" if x1-x2 == 0
       a = "s" if y1-y2 == 0 and x1-x2 == 0

       b = y1 - x1*a
       b = x1 if x1 - x2 == 0
       b = y1 if y1 - y2 == 0
       b = (x, y) if x1-x2 ==0 and y1-y2==0

       set() stores the points

Time Complexity:
Result:
'''

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        if len(points) in (0, 1, 2): return len(points)
        mp = {}
        for i in range(len(points))[:-1]:
            for j in range(len(points))[i+1:]:
                x1, y1 = points[i].x, points[i].y
                x2, y2 = points[j].x, points[j].y
                if y1 == y2 and x1 == x2:
                    a = "s"
                elif y1 == y2:
                    a = "."
                elif x1 == x2:
                    a = "*"
                else:
                    a = float(y1-y2)/(x1-x2)
                if y1 == y2 and x1 == x2:
                    b = (x1, y1)
                elif y1 == y2:
                    b = y1
                elif x1 == x2:
                    b = x1
                else:
                    b = y1 - x1*a
                key = (a,b)
                if mp.has_key(key):
                    mp[key].add(points[i])
                    mp[key].add(points[j])
                else:
                    mp[key] = set([points[i], points[j]])
        result = 0
        print mp
        for value in mp.values():
            result = max(len(value), result)
        return result

li = []
li.append(Point(1,2))
li.append(Point(1,2))
li.append(Point(0,2))
li.append(Point(0,2))
li.append(Point(5,2))
li.append(Point(11,7))
#li.append(Point(4,2))
#li.append(Point(2,4))
#li.append(Point(0,2))
#li.append(Point(2,6))
#li.append(Point(4,8))

s = Solution()
print s.maxPoints(li)







#List.prettyPrint(head)
#Tree.prettyPrint(root)

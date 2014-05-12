#!/usr/bin/env python
from unittest import *

'''
Description: None

Result: Not Commit
#Important@@@
'''

def insert(intervals, newInterval):
    nx, ny = newInterval
    i = 0
    # The insert location
    loc = 0 
    while i < len(intervals):
        x, y = intervals[i]
        # Check if intervals[i] and newInterval overlap each other
        if x> ny or nx > y :
            i += 1
            if nx > y:
                loc = i
        # Merge overlaps
        else:
            nx = min(x, nx)
            ny = max(y, ny)
            del(intervals[i])
            loc = i
    intervals.insert(loc, (nx, ny))
    return intervals

print insert([(1,2), (3,5), (6,7), (8, 10), (12,16)], [4,9])
print insert([(1,2), (3,5), (6,7), (8, 10), (12,16)], [-2,-1])
print insert([(1,2), (3,5), (6,7), (8, 10), (12,16)], [22,23])
print insert([(1,2), (3,5), (6,7), (8, 10), (12,16)], [2,3])
print insert([[22,24]], [25,25])





#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Solution:
Time Complexity:
Space Complexity:
Result: AC
'''

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        i = 0
        while i < len(intervals):
            item = intervals[i]
            if item.end < newInterval.start:
                i += 1
            elif item.start > newInterval.end:
                intervals.insert(i, newInterval)
                break
            else:
                newInterval.start = min(newInterval.start, intervals[i].start)
                newInterval.end = max(newInterval.end, intervals[i].end)
                del(intervals[i])
        if i == len(intervals):
            intervals.append(newInterval)
        return intervals

s = Solution()
intervals = [Interval(1,3), Interval(6,9)]
interval = Interval(2,6)
i = s.insert(intervals, interval)
for item in i:
    print item.start, item.end
#List.prettyPrint(head)
#Tree.prettyPrint(root)

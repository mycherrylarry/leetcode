#!/usr/bin/env python

def quickSort(li):
    if len(li) in (0, 1): return li
    lesser = quickSort(filter(lambda x: x[0] <= li[-1][0], li[:-1]))
    bigger = quickSort(filter(lambda x: x[0] > li[-1][0], li[:-1]))
    return lesser + [li[-1]] + bigger

def merge(intervals):
    if len(intervals) in (0, 1): return intervals
    li = quickSort(intervals)
    i = 1
    while i != len(li):
        if li[i-1][1] >= li[i][0]:
            if li[i-1][1] >= li[i][1]:
                del(li[i])
            else:
                li[i-1][1] = li[i][1]
                del(li[i])
        else:
            i += 1
    return li

print merge([[1,3],[2,6],[8,10],[15,18]])
print merge([[1,3],[2,6],[8,10],[15,18],[9, 27],[7,7]])



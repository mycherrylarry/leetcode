#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a collection of numbers that contain duplicates, return all possible unique permutations.
Method:
Solution: DFS
Time Complexity:
Space Complexity:
Result: AC
Note:
'''

class Solution:
    def dfs(self, li, route, result):
        if len(li) == 0:
            result.append([item for item in route])
            return
        for i in range(len(li)):
            if i > 0 and li[i] == li[i-1]:
                continue
            route.append(li[i])
            del(li[i])
            self.dfs(li, route, result)
            li.insert(i, route.pop())

    def permuteUnique(self, num):
        num.sort()
        result = []
        route = []
        self.dfs(num, route, result)
        return result

s = Solution()
print s.permuteUnique([1,2,2])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

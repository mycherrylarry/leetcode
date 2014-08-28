#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a collection of numbers, return all possible permutations.
Method:
Solution: DFS
Time Complexity:
Space Complexity:
Result: AC
Note:
    * Are there duplicates?(don't consider)
'''

class Solution:
    def dfs(self, li, route, result):
        if len(li) == 0:
            result.append([item for item in route])
            return
        for i in range(len(li)):
            route.append(li[i])
            del(li[i])
            self.dfs(li, route, result)
            li.insert(i, route.pop())

    # given a list of numbers
    def permute(self, li):
        route = []
        result = []
        self.dfs(li, route, result)
        return result

s = Solution()
print s.permute(range(3))
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    Given a string s, partition s such that every substring of the partition is a palindrome.

    Return all possible palindrome partitioning of s.

    For example, given s = "aab",
    Return
    [
      ["aa","b"],
      ["a","a","b"]
    ]
Description:
    * Create a two dimensional array called route. 
        route[i+1][j-1] = 1 {if route[i][j] == 1}
    * DFS search the 2 dimensional array and find out the result.
    
Example:
    | a a b a b
  --| ---------
  a | 1 1 0 0 0
  a | * 1 0 1 0
  b | * * 1 0 1
  a | * * * 1 0
  b | * * * * 1
Time Complexity: O(N*N)?? maybe bigger, because of DFS
Space Complexity: O(N*N)
Result: AC
'''

class Solution:
    def createRoute(self, s):
        n = len(s)
        route = [['*']*n for i in range(n)]
        # inner function for calculating route.
        def setRoute(a, b, route):
            while a >=0 and b <n:
                if s[a] == s[b]:
                    if route[a+1][b-1] == 1:
                        route[a][b] = 1
                    else:
                        route[a][b] = 0
                else:
                    route[a][b] = 0
                a -= 1
                b += 1
        # for odd
        for i in range(n):
            route[i][i] = 1
            a, b = i-1, i+1
            setRoute(a, b, route)
        # for even
        for i in range(n-1):
            if s[i] == s[i+1]:
                route[i][i+1] = 1
            else:
                route[i][i+1] = 0
            a, b = i-1, i+2
            setRoute(a, b, route)
        return route

    def solve(self, s, route, result, part, index):
        if index == len(s):
            result.append([item for item in part])
            return
        for i in range(index, len(s)):
            if route[index][i] == 1:
                part.append(s[index:i+1])
                self.solve(s, route, result, part, i+1)
                part.pop()

    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        result = []
        if len(s) == 0: return []
        route = self.createRoute(s)
        result = []
        self.solve(s, route, result, [], 0)
        return result

s = Solution()
print s.partition("aabab")
print s.partition("aab")


#s = Solution()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
    There are N children standing in a line. Each child is assigned a rating value.

    You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?

Solution:
    * Solve this problem by greedy
    * First, scan the list from left to right, set the first element to 1,
      if the next element is bigger than current one, the next elemnt's value
      is set as current's+1
    * Second, scan the list from right to left, set the element as bigger
Time Complexity: O(N)
Space Complexity: O(1)
Result: AC
'''

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        if len(ratings) == 0: return 0
        result = [0]*len(ratings)
        result[0] = 1
        for i in range(len(ratings)-1):
            if ratings[i+1] > ratings[i]:
                result[i+1] = result[i] + 1
            else:
                result[i+1] = 1
        for j in range(len(ratings)-1)[::-1]:
            if ratings[j] > ratings[j+1]:
                result[j] = max(result[j+1]+1, result[j])
        return sum(result)


s = Solution()
print s.candy([2,3,5,5,5,1,2,1])
print s.candy([2,3,2])
#List.prettyPrint(head)
#Tree.prettyPrint(root)

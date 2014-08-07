#!/usr/bin/env python
from util.List import *
from util.Tree import *
from unittest import *

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result:
Note:
'''


#A, B, X1, K, M = 3, 2, 5, 1, 7

A, B, X1, K, M = 1234, 5678, 123, 12345, 9876

class Solution:
    def solve(self, A, B, X1, K, M):
        current_value = X1
        def gen(v): return (v * A + B) % M
        log = []
        for i in range(K):
            log.append(current_value)
            current_value = gen(current_value)
            if current_value == X1:
                break
        current_value = log[(K-1)%len(log)]
        for i in range(5):
            print current_value
            current_value = gen(current_value)

    def calculate(self):
        A, B, X1, K, M = map(int, raw_input().strip().split())
        self.solve(A, B, X1, K, M)


s = Solution()
s.calculate()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

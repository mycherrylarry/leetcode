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
Reference: https://github.com/Linzertorte/LeetCode-in-Python/blob/master/WordLadder.py

very import,
needs practise
'''
import Queue

class Solution:
    characters = map(chr, range(97, 123))
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dic):
        def find_next(word, dic):
            for i in range(len(word)):
                for c in self.characters:
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in dic and c != word[i]:
                        yield new_word
        dic.append(end)
        dist = {}
        dist[start] = 1
        queue = Queue.deque()
        queue.append(start)
        while len(queue) != 0:
            head = queue.popleft()
            if head == end:
                return dist[head]
            for w in find_next(head, dic):
                if w not in dist:
                    dist[w] = dist[head] + 1
                    queue.append(w)
        return 0

                                    

s = Solution()
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
print s.ladderLength(start, end, dict)
#List.prettyPrint(head)
#Tree.prettyPrint(root)

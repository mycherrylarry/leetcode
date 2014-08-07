#!/usr/bin/env python

'''
Problem:
Method:
Solution:
Time Complexity:
Space Complexity:
Result:
Note:
'''

class Solution:
    def solve(self, input_str):
        if len(input_str) == 0: return []
        mp = {}
        for c in input_str:
            if mp.has_key(c):
                mp[c] += 1
            else:
                mp[c] = 1
        # sort map by value
        sorted_map = sorted(mp.items(), key=lambda x: x[1])[::-1]
        tag = sorted_map[0][1]
        result = []
        temp = [sorted_map[0][0]]
        # resort keys with the same value
        for i in range(1, len(sorted_map)):
            if tag == sorted_map[i][1]:
                temp.append(sorted_map[i][0])
            else:
                result.extend(sorted(temp))
                temp = [sorted_map[i][0]]
                tag = sorted_map[i][1]
        result.extend(sorted(temp))
        return result

    def frequency(self):
        s = raw_input()
        result = self.solve(s)
        for item in result:
            print item

s = Solution()
s.frequency()
#List.prettyPrint(head)
#Tree.prettyPrint(root)

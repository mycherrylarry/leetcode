#!/usr/bin/env python

'''Find the longest substring of a given string s which has no repeating characters.
Strategy: Greedy
TimeComplexity: O(n)
Result: AC
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) in (0, 1): return len(s)
        p, q = 0, 1 # pre-index p, post-index q
        result = 0
        mp = {s[0]:0} # mapping the value to position
        while q < len(s):
            # If the element exists, it means that there is a duplication in the subarray.
            # Compare the result with the current substring length, and restart counting
            # from the next index of duplication item.
            if mp.has_key(s[q]):
                result = max(result, len(mp))
                p = mp[s[q]] + 1 # p starts from the next index of the duplicated item.
                mp = {s[p]:p} # reset map
                q = p+1 # reset q
            else:
                mp[s[q]] = q
                q += 1
        if q == len(s):
            result = max(result, len(mp))
        return result

s = Solution()
print s.lengthOfLongestSubstring("bbbbbbbbbbba")
print s.lengthOfLongestSubstring("abcabcabcdef")
print s.lengthOfLongestSubstring("abcdefghabcabcdef")
print s.lengthOfLongestSubstring("wlrbbmqbhcdarzowkkyhiddqscdxrjmowfrxsjybldbefsarcbynecdyggxxpklorellnmpapqfwkhopkmco")




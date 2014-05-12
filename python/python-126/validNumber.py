#!/usr/bin/env python
'''
Conditions:
    0. Trim s
    1. valid characters: {0..9}, ., e, +, -
    2. "." and "e" can only exist once
    3. "e" cannot at the beginning or ending of the string
    4. if there are "." and "e", "e"'s position must behind that of "."
    5. - and + can exist at the beginning of s
    6. .e123 is not allowed
    7. "-" and "+" must following e and not at the end of s
Result: AC

'''
class Solution:
    def isNumber(self, s):
        validChars = [str(item) for item in range(10)] + [".", "e"] + ["+", "-"]
        s = s.strip()
        if len(s) == 0: return False
        # case 5
        if s[0] in ["-", "+"]:
            s = s[1:]
        if len(s) == 1: return (s[0] in [str(item) for item in range(10)])
        # case 0
        tagDot = False
        tagE = False
        for i in range(len(s)):
            # case 1
            if s[i] not in validChars:
                return False
            if s[i] == ".":
                # case 2 and case 4
                if tagDot or tagE:
                    return False
                tagDot = True
            if s[i] == "e":
                # case 3
                if i in (0, len(s)-1):
                    return False
                # case 2
                if tagE:
                    return False
                # case 6
                if tagDot and i == 1:
                    return False
                tagE = True
            # case 7
            if s[i] in ["+", "-"]:
                if not tagE:
                    return False
                if s[i-1] != "e":
                    return False
                if i == len(s)-1:
                    return False
        return True

s = Solution()
print s.isNumber("0")
print s.isNumber(" 0.1 ")
print s.isNumber("abc")
print s.isNumber("1 a")
print s.isNumber("2e10")
print s.isNumber("2e.10")
print s.isNumber(".23e1")
print s.isNumber(".")
print s.isNumber("e")
print s.isNumber("")
print s.isNumber("     e ")
print s.isNumber(".e1")
print s.isNumber("-1.22e1")
print s.isNumber("-e221")
print s.isNumber(" -.")
print s.isNumber(".")
print s.isNumber("005047e+6")
print s.isNumber("005047e+-5")
print s.isNumber("005047e-5")


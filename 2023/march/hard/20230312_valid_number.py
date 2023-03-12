'''
65. Valid Number

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], 
while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.
'''
# This is a true Frankenstein; Brute force solution
from collections import Counter
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        if len(s) == 1 and s[0] in 'abcdefghijklmnopqrstuvwxyz.+-':
            return False

        sides = None
        if 'e' in s:
            sides = s.split('e')
            right_side = sides[1]
            if ('-' in right_side and right_side.index('-') > 0) or ('+' in right_side and right_side.index('+') > 0):
                return False

        c = Counter(s)
        if c['.'] > 1 or c['e'] > 1 or c['-'] > 1 or c['+'] > 1:
            if s[0] in '+-':
                if c[s[0]] > 2:
                    return False
            else:
                return False

        if ('.e' in s or '-e' in s or '+e' in s) and s.index('e') == 1:
            return False

        if ('+.' in s or '-.' in s) and 'e' in s and s.index('e') == 2:
            return False

        for i in range(len(s)):
            if s[i] not in '0123456789e.+-':
                return False
            else:
                if (s[i] == 'e' and ((i > 0 and s[i-1] not in '0123456789+-.') or i == 0 or i == len(s)-1)) or \
                (s[i] in '+-' and (('e' not in s and i > 0) or i == len(s)-1 or (i > 0 and 'e' in s and s.index('e') > i))) or \
                    (s[i] == '.' and ((i > 0 and s[i-1] not in '0123456789+-') or \
                    (i > 0 and i == len(s)-1 and s[i-1] not in '0123456789') or \
                    ('e' in s and s.index('e') < i))):
                    return False
        return True
    
print(Solution().isNumber('.1')) # True
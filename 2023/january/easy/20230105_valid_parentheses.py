'''
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:
1 <= s.length <= 10**4
s consists of parentheses only '()[]{}'.
'''

class Solution:
    def isValid(self, s: str) -> bool:
        def reverse_char(c):
            if c == ')':
                return '('
            elif c == '}':
                return '{'
            return '['

        opened = []
        for c in s:
            if c in ['(', '{', '[']:
                opened.append(c)
            else:
                if len(opened) == 0:
                    return False
                else:
                    if opened[-1] == reverse_char(c):
                        opened.pop()
                    else:
                        return False

        return True if len(opened) == 0 else False
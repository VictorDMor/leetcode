"""
224. Basic Calculator

Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

Constraints:
1 <= s.length <= 3 * 10**5
s consists of digits, '+', '-', '(', ')', and ' '.
s represents a valid expression.
'+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
'-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
There will be no two consecutive operators in the input.
Every number and running calculation will fit in a signed 32-bit integer.
"""

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        signal = 1
        result = 0
        s = s.replace(' ', '')

        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            elif s[i] in ['+', '-']:
                result += num * signal
                num = 0
                signal = 1 if s[i] == '+' else -1
            elif s[i] == '(':
                stack.append((result, signal))
                result = 0
                signal = 1
            else:
                result += num * signal
                num = 0
                if stack:
                    prev_result, prev_signal = stack.pop()
                    result = prev_result + prev_signal * result

        result += num * signal
        return result

    

if __name__ == '__main__':
    s = Solution()
    print(s.calculate("1 + 1"))
    print(s.calculate("(1+(4+5+2)-3)+(6+8)"))
    # print(s.calculate("2-(5-6)"))
    # print(s.calculate("2-4-(8+2-6+(8+4-(1)+8-10))"))
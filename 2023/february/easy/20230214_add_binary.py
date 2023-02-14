'''
67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"

Constraints:
1 <= a.length, b.length <= 10**4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # I could use bin but it would be like cheating...
        int_a = sum([int(a[::-1][i]) * 2 ** i for i in range(len(a))])
        int_b = sum([int(b[::-1][i]) * 2 ** i for i in range(len(b))])

        add = int_a + int_b
        if add == 0: return '0'
        bin_add = ''
        while add > 0:
            carry = int(add % 2)
            add = int(add // 2)
            bin_add += str(carry)

        return bin_add[::-1]
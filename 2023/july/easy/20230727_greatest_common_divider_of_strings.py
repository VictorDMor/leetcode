"""
1071. Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:
1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if f'{str1}{str2}' != f'{str2}{str1}':
            return ''
        
        str1_length = len(str1)
        str2_length = len(str2)

        def calculate_gcd(x, y):
            while y != 0:
                x, y = y, x % y
            return x

        gcd = calculate_gcd(str1_length, str2_length)
        return str1[:gcd]
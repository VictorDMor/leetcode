'''
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1:
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input: s1 = "ab", s2 = "eidboaoo"
Output: false

Constraints:
1 <= s1.length, s2.length <= 10**4
s1 and s2 consist of lowercase English letters.
'''
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False
        if s1 in s2: return True
        c_s1 = Counter(s1)
        for i in range(len(s2)):
            c_ss2 = Counter(s2[i:i+len(s1)])
            if c_ss2 == c_s1:
                return True
        return False
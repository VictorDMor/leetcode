'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
1 <= s.length <= 3 * 10**5
s consist of printable ASCII characters.
'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        word_vowels = []
        for w in s:
            if w.lower() in 'aeiou':
                word_vowels.append(w)

        new_word = []
        for w in s:
            if w.lower() in 'aeiou':
                new_word.append(word_vowels.pop())
            else:
                new_word.append(w)

        return ''.join(new_word)

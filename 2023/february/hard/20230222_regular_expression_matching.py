'''
10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
 
Constraints:
1 <= s.length <= 20
1 <= p.length <= 20
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if '*' not in p and '.' not in p:
            return True if p == s else False

        if p == '.*': return True

        if '.' in p and '*' not in p and len(p) != len(s): return False

        if len(p) == 2 and p[1] == '*' and ''.join(list(set(s))) == p[0]: return True

        temp_p = p
        for j in range(len(p)-1):
            if p[j] not in ['*', '.'] and p[j] not in s and p[j+1] == '*':
                temp_p = p.replace(f'{p[j]}*', '')
        p = temp_p

        temp_p = p.replace('*', '')
        if temp_p == s:
            return True

        i = 0
        s_length = len(s)
        while True:
            if i == len(s):
                return True
            if '*' not in p and '.' not in p:
                return True if p == s else False
            if p[i] != s[i]:
                if p[i] == '*':
                    original_len = len(p)
                    p = p.replace(f'{p[i-1]}*', '', 1)
                    diff = original_len - len(p)
                    if list(set(p)) == list(set(s)) and len(p) == len(s):
                        return True
                    s = s.replace(f'{s[i-1]*diff}', '', 1)
                    s_length = len(s)
                    i = 0
                elif p[i] != '.':
                    try:
                        if p[i+1] != '*':
                            return False
                        i += 1
                    except IndexError:
                        return False
                else:
                    if i+1 < len(p):
                        if p[i+1] == '*':
                            letter_count = 0
                            letter = s[i]
                            for l in s:
                                if l != letter:
                                    break
                                letter_count += 1
                            s = s.replace(f'{s[i] * letter_count}', '', 1)
                            p = p.replace('.*', '', 1)
                            i = 0
                        else:
                            i += 1
                    else:
                        i += 1
            else:
                if i == s_length-1:
                    return True
                i += 1
            
solution = Solution()
print(solution.isMatch('aa', 'a')) # False
print(solution.isMatch('aa', 'a*')) # True
print(solution.isMatch('ab', '.*')) # True
print(solution.isMatch('aab', 'c*a*b')) # True
print(solution.isMatch('mississippi', 'mis*is*p*.')) # False
print(solution.isMatch('ab', '.*c')) # False
print(solution.isMatch('churros', 'chur*')) # False
print(solution.isMatch('chuabo', 'chuac*bo')) # True
print(solution.isMatch('mississippi', 'mis*is*ip*.')) # True
print(solution.isMatch('aaa', '.a')) # False
print(solution.isMatch('aaa', 'ab*a')) # False
print(solution.isMatch('aaca', 'ab*a*c*a')) # True
print(solution.isMatch('bbbbaa', '.*a*a')) # True
print(solution.isMatch('bbbba', '.*a*a')) # True
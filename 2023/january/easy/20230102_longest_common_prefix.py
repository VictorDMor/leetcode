'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 
Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''
class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 1: return strs[0]
        min_word_length = min([len(w) for w in strs])
        
        has_prefix = False
        for i in range(min_word_length, 0, -1):
            words = [w[:i] for w in strs]
            has_prefix = all(w == words[0] for w in words)
            if has_prefix:
                break
        
        return words[0] if has_prefix else ''
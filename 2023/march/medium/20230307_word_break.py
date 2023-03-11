'''
139. Word Break

Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or 
more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
'''
class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        if ''.join(wordDict) == s:
            return True

        i = 1
        while True:
            if s[:i] in wordDict:
                s = s.replace(s[:i], '')
                i = 1
                if s == '':
                    return True
            else:
                if i >= len(s):
                    if s != '':
                        for word in wordDict:
                            if s + word in wordDict:
                                return True
                    return False
                i += 1

    
# print(Solution().wordBreak("leetcode", ["leet","code"])) # True
# print(Solution().wordBreak("applepenapple", ["apple","pen"])) # True
# print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"])) # False
# print(Solution().wordBreak("cars", ["car","ca","rs"])) # True
# print(Solution().wordBreak("bb", ["a","b", "bbb", "bbbb"])) # True
# print(Solution().wordBreak("aaaaaaa", ["aaaa","aa"])) # False
print(Solution().wordBreak("goalspecial", ["go","goal", "goals", "special"])) # True
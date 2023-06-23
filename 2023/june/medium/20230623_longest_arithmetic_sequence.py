"""
1027. Longest Arithmetic Subsequence

Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.

Note that:

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).

Example 1:
Input: nums = [3,6,9,12]
Output: 4
Explanation:  The whole array is an arithmetic sequence with steps of length = 3.

Example 2:
Input: nums = [9,4,7,2,10]
Output: 3
Explanation:  The longest arithmetic subsequence is [4,7,10].

Example 3:
Input: nums = [20,1,15,3,10,5,8]
Output: 4
Explanation:  The longest arithmetic subsequence is [20,15,10,5].
 

Constraints:

2 <= nums.length <= 1000
0 <= nums[i] <= 500
"""

from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        # This is a dynamic programming problem
        # Let's start by filling the DP list
        dp = []
        nums_length = len(nums)
        for i in range(nums_length):
            dp.append({})
        
        # Let's compare each element from the nums list
        for i in range(nums_length):
            for j in range(i+1, nums_length):
                diff = nums[j] - nums[i]
                if diff in dp[i]:
                    dp[j][diff] = dp[i][diff] + 1
                else:
                    dp[j][diff] = 2

        return max(max(dp[i].values()) for i in range(len(dp)) if dp[i])
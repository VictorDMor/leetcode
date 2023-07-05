
"""
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.

Constraints:
1 <= nums.length <= 105
nums[i] is either 0 or 1.
"""

from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        def count_subarray(l: List[int]) -> int:
            longest = 0
            curr = 0
            for n in range(len(l)):
                if l[n] == 1 and n+1 < len(l):
                    curr += 1
                elif l[n] == 1 and n+1 == len(l):
                    if curr+1 > longest:
                        longest = curr+1
                else:
                    if curr > longest: longest = curr
                    curr = 0
            return longest

        zero_indexes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_indexes.append(i)

        if len(zero_indexes) == 0:
            return len(nums)-1

        original_nums = nums.copy()
        max_length = 0
        for idx in zero_indexes:
            nums.pop(idx)
            subarray_length = count_subarray(nums)
            if subarray_length > max_length:
                max_length = subarray_length
            nums = original_nums.copy()
        
        return max_length
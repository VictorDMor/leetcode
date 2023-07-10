"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:
Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-10**4 <= target <= 10**4
"""
# ChatGPT helped me here too
from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        target_diff = float('inf')
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums)-1
            while left < right:
                sum_triplet = sum([nums[i], nums[left], nums[right]])
                if abs(sum_triplet-target) < abs(target_diff-target):
                    target_diff = sum_triplet

                if sum_triplet > target:
                    right -= 1
                else:
                    left += 1
        return target_diff
            
s = Solution()

# Examples
print(s.threeSumClosest(nums = [-1,2,1,-4], target = 1))
print(s.threeSumClosest(nums = [0,0,0], target = 1))
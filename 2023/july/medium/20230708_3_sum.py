
'''
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0. 

Constraints:
3 <= nums.length <= 3000
-10**5 <= nums[i] <= 10**5
'''
# This code is not mine, it's ChatGPT's, but I wanted to understand it and write it out myself.
from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        triplets = set()

        for i in range(len(nums) - 2):
            # Skip duplicates of the first number
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                triplet_sum = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]

                if triplet_sum == 0:
                    triplets.add((sorted_nums[i], sorted_nums[left], sorted_nums[right]))
                    # Skip duplicates of the second and third numbers
                    while left < right and sorted_nums[left] == sorted_nums[left+1]:
                        left += 1
                    while left < right and sorted_nums[right] == sorted_nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif triplet_sum < 0:
                    left += 1
                else:
                    right -= 1

        return list(triplets)